# spec file for package openvpn (Version 2.1)
#

Name: openvpn
Version: 2.2.2
Release: alt1

Summary: a full-featured SSL VPN solution
Summary(ru_RU.UTF-8): полнофункциональное решение VPN на базе SSL

License: %gpl2only
Group: System/Servers
Url: http://www.openvpn.net

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.init
Source2: %name-startup
Source3: %name.sysconfig
Source4: %name.chroot.lib
Source5: %name.chroot.conf
Source6: %name.chroot.all
Source7: %name-README.ALT.utf-8
Source8: %name-server.conf
Source9: %name-client.conf

Patch1: %name-2.1_rc18-alt-make_COPYRIGHT.patch

# Because of /etc/syslog.d/ feature
Conflicts: syslogd < 1.4.1-alt11

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Nov 30 2010
BuildRequires: liblzo2-devel libpam-devel libssl-devel net-tools


%description
OpenVPN is a full-featured SSL VPN solution which can accomodate
a wide range  of configurations,  including road warrior access,
home/office/campus  telecommuting,  WiFi security, secure branch
office  linking,  and enterprise-scale  remote access  solutions
with load balancing, failover, and fine-grained access-controls.

%description -l ru_RU.UTF-8
OpenVPN  -  полнофункциональное решение для VPN с использованием
SSL, с помощью которого можно решить широкий круг задач, включая
подключения  для удалённых  пользователей,  телекоммуникации для
дома и офиса,  безопасные  подключения  для  беспроводных сетей,
безопасную связь  с удалёнными офисами,  решения  для удалённого
доступа масштаба предприятий с поддержкой балансировки нагрузки,
отказоустойчивости и четко разграниченным контролем доступа.

%package plugins
Summary: external plugins for OpenVPN
Summary(ru_RU.UTF-8): внешние расширения для OpenVPN
Group: System/Servers
Requires: %name = %version-%release

%description plugins
OpenVPN is a full-featured SSL VPN solution.
This package contains OpenVPN plugins for user authentication
via PAM and to allow run a down script with root privileges.

%description plugins -l ru_RU.UTF-8
OpenVPN - полнофункциональное решение для VPN на базе SSL.
Данный пакет содержит расширения (plugins) для авторизации
пользователей через  PAM и  запуска при разрыве соединений
скрипта с привилегиями root.

%package docs
Summary: OpenVPN documentation
Summary(ru_RU.UTF-8): документация к OpenVPN
Group: System/Servers
Requires: %name = %version-%release

%description docs
OpenVPN is a full-featured SSL VPN solution.
This package contains OpenVPN documentation,
sample configs and scripts.

%description docs -l ru_RU.UTF-8
OpenVPN - полнофункциональное решение для VPN на базе SSL.
Данный пакет содержит документацию, примеры конфигурации и
скриптов для OpenVPN.

%define openvpn_root   %_localstatedir/%name
%define openvpn_cache  %openvpn_root/cache
%define ovpn_user      openvpn
%define ovpn_group     openvpn

%prep
%setup -n %name-%version
%patch0 -p1

%patch1

cp -- %SOURCE7 README.ALT.utf-8
cp -- %SOURCE8 server.conf
cp -- %SOURCE9 client.conf

mv -f -- COPYRIGHT.GPL COPYRIGHT.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYRIGHT.GPL) COPYRIGHT.GPL

%build
%autoreconf
%configure \
    --enable-iproute2 \
    --with-iproute-path=/sbin/ip \
    --enable-password-save \
    --enable-x509-alt-username \
    %nil

%make_build
subst 's|nobody|%ovpn_user|' sample-config-files/*

make -C plugin/down-root/
make -C plugin/auth-pam/

# Building 'simple' plugin
pushd plugin/examples
./build simple
mv -- simple.so %name-examples.so
popd

# Building 'defer' plugin
pushd plugin/defer
./build simple
mv -- simple.so %name-defer.so
popd

%ifndef __BTE
   # make check hangs inside hasher
   make check
%endif

%install
%make_install DESTDIR=%buildroot install

mkdir -p -- %buildroot/%_initdir
mkdir -p -- %buildroot/%_sysconfdir/sysconfig
install -m 0750 -d -- %buildroot%_sysconfdir/%name
install -m 0750 -d -- %buildroot%_sysconfdir/%name/keys
install -m 0755 -d -- %buildroot%openvpn_root
install -m 0755 -d -- %buildroot%openvpn_root/etc
install -m 0755 -d -- %buildroot%openvpn_root/%_lib
install -m 0755 -d -- %buildroot%openvpn_root/etc/openvpn
install -m 0755 -d -- %buildroot%openvpn_cache
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name
install -m 0750 -- %SOURCE2 %buildroot%_sysconfdir/%name
install -m 0640 -- %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -p -m 0750 -D -- %SOURCE4 %buildroot%_sysconfdir/chroot.d/%name.lib
install -p -m 0750 -D -- %SOURCE5 %buildroot%_sysconfdir/chroot.d/%name.conf
install -p -m 0750 -D -- %SOURCE6 %buildroot%_sysconfdir/chroot.d/%name.all

# Install plugins
install -m 0750 -d -- %buildroot%_libdir/%name/plugin

for pi in auth-pam down-root defer examples; do
    mv -f -- plugin/$pi/README plugin/README.$pi
    if [ -x plugin/$pi/%name-$pi.so ]; then
	install -c -m 0755 -- plugin/$pi/%name-$pi.so %buildroot%_libdir/%name/plugin/%name-$pi.so
    fi
done

mkdir -- plugins
mv -f -- plugin/README plugin/README.plugins
mv -f -- plugin/README* plugins/

# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
mkdir -p -- %buildroot%openvpn_root/dev
/usr/bin/mksock %buildroot%openvpn_root/dev/log
mkdir -p -m700 -- %buildroot%_sysconfdir/syslog.d
ln -s -- %openvpn_root/dev/log %buildroot%_sysconfdir/syslog.d/%name

# Moving management-notes.txt from %%buildroot/usr/share/doc/openvpn/
mv -f -- %buildroot/%_docdir/%name/management-notes.txt .

%pre
# Add the "openvpn" user
%_sbindir/groupadd -r -f %ovpn_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %ovpn_group -c 'OpenVPN daemon' \
        -s /dev/null -d /dev/null %ovpn_user 2>/dev/null ||:

%post
%_sysconfdir/chroot.d/%name.all
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS ChangeLog NEWS PORTS README COPYING
%doc --no-dereference COPYRIGHT.GPL
%doc README.ALT.utf-8 server.conf client.conf

%_sbindir/%name
%_mandir/man?/*

%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name
%attr(0750,root,%ovpn_group) %dir %_sysconfdir/%name/keys
%attr(0750,root,%ovpn_group) %dir %openvpn_root
				%dir %openvpn_root/etc
%attr(0710,root,%ovpn_group)	%dir %openvpn_root/dev
%ghost %attr(0666,root,root)     %openvpn_root/dev/log
			    %dir %openvpn_root/etc/openvpn
			    %dir %openvpn_root/%_lib
%attr(0750,%ovpn_user,%ovpn_group) %dir %openvpn_cache

%config(noreplace)	    %_sysconfdir/%name/%name-startup
%config(noreplace)	    %_sysconfdir/sysconfig/%name
%config 		    %_sysconfdir/chroot.d/%name.*
%config			    %_initdir/%name

%_sysconfdir/syslog.d/%name

%files plugins
%doc plugins*
%dir %_libdir/%name
%dir %_libdir/%name/plugin
     %_libdir/%name/plugin/%name-*.so

%files docs
%doc INSTALL-win32.txt INSTALL
%doc management-notes.txt
%doc easy-rsa*
%doc sample-config-files*
%doc sample-keys*
%doc sample-scripts*

%changelog
* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.2.2-alt1
- New version 2.2.2

* Thu Jun 23 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.2.0-alt1
- New version 2.2.0

* Mon Nov 29 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.4-alt1
- New version 2.1.4

* Sat Oct 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.3-alt1
- New version 2.1.3
- Removing bashisms from the init.d script

* Thu Dec 31 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.1-alt1
- New version 2.1.1 (Closes: 19934)
- Disabling service by default (Closes: 17218)
- Building with liblzo2
- Fixing Requies/Obsoletes

* Thu Jun 04 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.9-alt2
- Adding 'lladdr' support (thanks Mykola S. Grechukh, (gns@))
- Adding LSB header into init.d script

* Wed Apr 18 2007 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.9-alt1
- New version 2.0.9
-- Fix some issues in Windows-related code
- Adding lib64/ in chroot environment (#10164)
- Adding note to README.ALT about #11016
- Spec file cleanup

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.8-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.8-alt1
- New version 2.0.8
-- Fix in Windows installer, no changes into source code
- Fix small mistakes in README.ALT

* Fri Sep 01 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.7-alt1
- New version 2.0.7
-- small bugfixes
- Fix typos in openvpn.init (#9870)
- Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature (#9945)
- Move documentation to separate package openvpn-docs
- Sample config files with ALT Linux specific comments added (#9367)

* Sat Apr 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.6-alt2
- Fix init.d script for run openvpn-startup/openvpn-shutdown scripts
- Plugins packed to separate package openvpn-plugins.

* Tue Apr 06 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.6-alt1
- New version 2.0.6
-- Security fixes for CVE-2005-3393, CVE-2005-3409, CVE-2006-1629
-- several minor bug fixes and improvements, see ChangeLog for details
- Adding README.ALT
- Updating init.d script
- Building and packaging plugins

* Thu Aug 25 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.2-alt1
- New version 2.0.2:
  -- Security fix for several DoS attacks: CAN-2005-2531; CAN-2005-2532;
     CAN-2005-2533; CAN-2005-2534.
  -- Several minor bug fixes and improvements, see ChangeLog for details
- Run in chroot by default

* Wed Apr 27 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt1
- First build for Sisyphus

* Fri Apr 22 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt0
- First build of 2.0 release

* Mon Jan 10 2005 - Nikolay A. Fetisov <naf@nat.net.ru> 1.0.3-naf1.rc6
- Updating to version 2.0_rc6

* Sun Dec 26 2004 - Nikolay A. Fetisov <naf@nat.net.ru> 1.0.3-naf1
- Initial build
