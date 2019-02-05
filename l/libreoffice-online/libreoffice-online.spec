%define service_name loolwsd
%define service_user lool
%define default_loroot %_libdir/LibreOffice
%define loolparent %_localstatedir

Name: libreoffice-online
Version: 6.0.2.3
Release: alt3

Summary: LibreOffice Online WebSocket Daemon

License: MPLv2
Group: Office
Url: https://gerrit.libreoffice.org/p/online.git

Source0: %name-%version.tar
Source1: %service_name.init
Source2: %name.conf.nginx
Source3: %name.conf.apache2
Source4: node-modules.tar

Patch0: remove-rpath.patch
Patch1: disable-setcap.patch
Patch2: disable-copying-libs.patch
Patch3: fix-conf-dir.patch
Patch4: log-to-file.patch
Patch5: i586-build.patch
Patch6: i586-lfs-support.patch
Patch7: ru-translation.patch
Patch8: npm-shrinkwrap.patch
Patch9: package.patch
Patch10: loleaflet-makefile.patch
Patch11: fix-printing-size-type.patch
Patch12: libreoffice-online-upstream-gcc8.patch

Requires: LibreOffice python3 fonts-ttf-core

BuildRequires(pre): rpm-build-python3
BuildRequires: libtool automake npm libcap-utils fontconfig
BuildRequires: libpoco-devel libpng-devel libcap-devel cppunit-devel
BuildRequires: pam-devel libpcre-devel
BuildRequires: python-module-polib python-module-lxml

%description
This is LibreOffice Online, which provides basic collaborative editing of
documents in a browser by re-using the LibreOffice core.
Rendering fidelity should be excellent,
and interoperability match that of LibreOffice.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name nginx

BuildArch: noarch

%description nginx
nginx web-server default configuration for %name.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name apache2

BuildArch: noarch

%description apache2
Apache 2.x web-server default configuration for %name.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if "%_lib" != "lib64"
%patch5 -p1
%patch6 -p1
%endif

tar -xf %SOURCE4 -C loleaflet/

%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
sh autogen.sh

%configure --enable-silent-rules \
           --with-lokit-path=bundled/include \
           --disable-setcap \
           --with-lo-path=%default_loroot \
           --localstatedir=%_var \
%ifnarch x86_64
           --disable-seccomp
%endif

mkdir -p bin && cd bin
ln -s ../loleaflet/node_modules/jake/bin/cli.js jake
cd -
export PATH="$PATH:$(pwd)/bin"

%make_build

%install
export PATH="$PATH:$(pwd)/bin"
%makeinstall_std

unit_file="%buildroot%_unitdir/%service_name.service"

mkdir -p %buildroot%_unitdir

cat > "$unit_file" << EOF
[Unit]
Description=LibreOffice Online WebSocket Daemon
After=network.target

[Service]
EnvironmentFile=-%_sysconfdir/sysconfig/%service_name
ExecStart=%_bindir/%service_name --version \
--o:sys_template_path=%loolparent/%service_user/systemplate \
--o:lo_template_path=%default_loroot \
--o:child_root_path=%loolparent/%service_user/child-roots \
--o:file_server_root_path=%_datadir/%name
User=%service_user
KillMode=control-group
Restart=always

[Install]
WantedBy=multi-user.target
EOF

install -D -m 755 %SOURCE1 %buildroot%_initdir/%service_name

install -d -m 755 %buildroot%_var/adm/fillup-templates
install -d -m 755 %buildroot%_cachedir/%name
install -d -m 755 %buildroot%loolparent/%service_user/child-roots 
install -d -m 755 %buildroot%loolparent/%service_user/systemplate
install -D -m 644 sysconfig.%service_name %buildroot%_sysconfdir/sysconfig/%service_name

mkdir -p %buildroot%_sysconfdir/cron.d
echo "#Remove old tiles once every 10 days at midnight" > %buildroot%_sysconfdir/cron.d/%service_name.cron
echo "0 0 */1 * * root find %_cachedir/%name -name \"*.png\" -a -atime +10 -exec rm {} \;" >> %buildroot%_sysconfdir/cron.d/%service_name.cron

mkdir -p %buildroot%_sysconfdir/pam.d
echo "auth       required     pam_unix.so" > %buildroot%_sysconfdir/pam.d/%service_name
echo "account    required     pam_unix.so" >>  %buildroot%_sysconfdir/pam.d/%service_name

install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/%service_name.log

install -pD -m0644 etc/*.pem %buildroot%_sysconfdir/%name

%pre
getent group %service_user >/dev/null || groupadd -r %service_user
getent passwd %service_user >/dev/null || useradd -g %service_user -r %service_user -d %loolparent/%service_user -s /bin/bash

%post
rm -rf %_cachedir/%name/*
rm -rf %loolparent/%service_user/child-roots/*

%post_service %service_name

%preun
%preun_service %service_name

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%_bindir/*
%_datadir/%name
%_defaultdocdir/%name
%dir %_sysconfdir/%name/
%attr(755,%service_user,%service_user) %_cachedir/%name
%dir %attr(755,%service_user,%service_user) %loolparent/%service_user
%attr(755,%service_user,%service_user) %loolparent/%service_user/child-roots
%attr(755,%service_user,%service_user) %loolparent/%service_user/systemplate
%attr(644,%service_user,%service_user) %_logdir/%service_name.log
%config(noreplace) %attr(640,%service_user, root) %_sysconfdir/%name/*.pem
%attr(755,root,root) %_initdir/%service_name
%config(noreplace) %_sysconfdir/sysconfig/%service_name
%config(noreplace) %_sysconfdir/cron.d/%service_name.cron
%config(noreplace) %_sysconfdir/pam.d/%service_name
%config(noreplace) %attr(640, %service_user, root) %_sysconfdir/%name/%service_name.xml
%config(noreplace) %_sysconfdir/%name/loolkitconfig.xcu
%config %attr(644, root, root) %_unitdir/%service_name.service

%doc AUTHORS ChangeLog README NEWS TODO

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%changelog
* Tue Feb 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2.3-alt3
- NMU: fixed build.

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2.3-alt2
- NMU: rebuilt with openssl 1.1.

* Wed Apr 18 2018 Maxim Voronov <mvoronov@altlinux.org> 6.0.2.3-alt1
- initial build for ALT

