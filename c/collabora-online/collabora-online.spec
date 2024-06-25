%define _unpackaged_files_terminate_build 1

%define service_name coolwsd
%define service_user cool
%define default_loroot %_libdir/LibreOffice

%ifarch ppc64le
%define __nprocs 32
%endif

Name: collabora-online
Version: 23.05.10.1
Release: alt1
Summary: Collabora Online WebSocket Daemon
License: MPL-2.0
Group: Office
Url: https://www.collaboraoffice.com/collabora-online/
Vcs: https://github.com/CollaboraOnline/online.git

Source0: %name-%version.tar
Source1: node_modules-%version.tar
Source2: %name.conf.nginx
Source3: %name.conf.apache2
Source4: README.alt

Patch1: collabora-online-23.05.4-alt-systemd-service.patch
Patch2: collabora-online-23.05.10-alt-exclude_unused_states.patch
Patch3: collabora-online-23.05.10-alt-fix-cached-path.patch

ExcludeArch: %ix86 %arm

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libtool automake npm libcap-utils fontconfig rsync
BuildRequires: libpoco-devel libpng-devel libcap-devel cppunit-devel
BuildRequires: pam-devel libpcre-devel
BuildRequires: python3 python3-module-polib python3-module-lxml
BuildRequires: libreofficekit-devel libzstd-devel

Requires: LibreOffice python3 fonts-ttf-core vixie-cron
Requires: glibc-core libpoco-crypto
Requires(post): coreutils grep sed cpio /sbin/setcap

%description
This is Collabora Online, which provides basic collaborative editing of
documents in a browser by re-using the LibreOffice core.
Rendering fidelity should be excellent,
and interoperability match that of LibreOffice.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
ExcludeArch: %ix86 %arm
Requires: %name = %EVR
Requires: nginx

%description nginx
nginx web-server default configuration for %name.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
ExcludeArch: %ix86 %arm
Requires: %name = %EVR
Requires: apache2
Requires: apache2-mods
Requires: apache2-mod_ssl

%description apache2
Apache 2.x web-server default configuration for %name.

%prep
%setup -a1
%autopatch -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%ifarch ppc64le
# ppc64le misses following definition
%add_optflags -D__linux=1
%endif

%autoreconf
# Excluding unsupported functionality with loongarch64
%configure \
%ifarch loongarch64
	 --disable-seccomp \
%endif
	--enable-silent-rules \
	--with-lo-path=%default_loroot \
	--disable-setcap \
	--disable-werror \
	--localstatedir=%_var

env BUILDING_FROM_RPMBUILD=yes %make_build

%install
env BUILDING_FROM_RPMBUILD=yes %makeinstall_std

install -D -m 444 %service_name.service %buildroot%_unitdir/%service_name.service

install -d -m 755 %buildroot%_var/adm/fillup-templates
install -d -m 755 %buildroot%_cachedir/%name
install -d -m 755 %buildroot%_localstatedir/%service_user/child-roots
install -d -m 755 %buildroot%_localstatedir/%service_user/systemplate
install -d -m 755 %buildroot%_logdir/%service_name

mkdir -p %buildroot%_sysconfdir/cron.d
echo "#Remove old tiles once every 10 days at midnight" > %buildroot%_sysconfdir/cron.d/%service_name.cron
echo "0 0 */1 * * root find %_cachedir/%name -name \"*.png\" -a -atime +10 -exec rm {} \;" >> %buildroot%_sysconfdir/cron.d/%service_name.cron

mkdir -p %buildroot%_sysconfdir/pam.d
echo "auth       required     pam_unix.so" > %buildroot%_sysconfdir/pam.d/%service_name
echo "account    required     pam_unix.so" >>  %buildroot%_sysconfdir/pam.d/%service_name

install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf
mv %buildroot%_sysconfdir/apache2/conf-available  %buildroot%_sysconfdir/httpd2/conf/

install -pD -m0644 etc/*.pem %buildroot%_sysconfdir/%service_name/

ln -s dist %buildroot%_datadir/%service_name/browser/%version

cp etc/apache2/%service_name.conf %service_name.apache2.conf
cp etc/nginx/%service_name.conf %service_name.nginx.conf

mv %buildroot%_defaultdocdir/%service_name ./%{name}-doc

cp  %SOURCE4 README.alt

%pre
getent group %service_user >/dev/null \
    && echo "Warning: coolwsd uses 'cool' group as a service gruop, but it already exists." \
    || groupadd -r %service_user
getent passwd %service_user >/dev/null \
    && echo "Warning: coolwsd uses 'cool' user as a service user, but it already exists." \
    || useradd -g %service_user -r %service_user -d %_localstatedir/%service_user -s /bin/bash

%post
rm -rf %_cachedir/%name/*
rm -rf %_localstatedir/%service_user/child-roots/*

fc-cache ${lokitroot}/share/fonts/truetype
coolwsd-systemplate-setup %_localstatedir/%service_user/systemplate %default_loroot >/dev/null 2>&1
coolconfig generate-proof-key >/dev/null 2>&1

%post_service %service_name

cat %_defaultdocdir/%name-%version/README.alt

%ifarch loongarch64
cat << EOF
    WARNING: Collabora Online does not yet support seccomp filtering on loongarch64, so this installation is not as secured as it would be on other platforms.
EOF
%endif

%preun
%preun_service %service_name

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
a2enmod proxy

%preun apache2
a2dissite %name

%files
%doc README.alt AUTHORS ChangeLog NEWS PROBLEMS *.md
%doc %{name}-doc
%_bindir/*
%_datadir/%service_name
%_man1dir/*
%dir %_sysconfdir/%service_name/
%config(noreplace) %attr(640, %service_user, root) %_sysconfdir/%service_name/%service_name.xml
%config(noreplace) %_sysconfdir/%service_name/coolkitconfig.xcu
%config(noreplace) %attr(640,%service_user, root) %_sysconfdir/%service_name/*.pem
%config(noreplace) %_sysconfdir/cron.d/%service_name.cron
%config(noreplace) %_sysconfdir/pam.d/%service_name
%_unitdir/%service_name.service
%dir %attr(-,%service_user,%service_user) %_localstatedir/%service_user
%dir %attr(-,%service_user,%service_user) %_localstatedir/%service_user/child-roots
%dir %attr(-,%service_user,%service_user) %_localstatedir/%service_user/systemplate
%dir %attr(-,%service_user,%service_user) %_cachedir/%name
%dir %attr(-,%service_user,%service_user) %_logdir/%service_name

%files nginx
%doc %service_name.nginx.conf
%_sysconfdir/nginx/snippets/%service_name.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%files apache2
%doc %service_name.apache2.conf
%_sysconfdir/httpd2/conf/conf-available/%service_name.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%changelog
* Tue Jun 25 2024 Aleksei Kalinin <kaa@altlinux.org> 23.05.10.1-alt1
- Updated to new version.
- Added loongarch64 build support.
- Returned the native name for service user.
- Spec fix related new collabora version.
- Updated fix for cached path dropping out.
- Replaced excludes patch for libreofficekit compatibility.

* Fri Oct 13 2023 Aleksei Kalinin <kaa@altlinux.org> 23.05.4.2-alt1
- Fixed some cached path dropping out.
- Exclude unused states in libreofficekit-devel-7.6.2.1.
- Added alt-specific system configuration files.
- Node modules bundled.
- Initial build for Alt.
