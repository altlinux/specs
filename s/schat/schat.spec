%define privuser  schatd
%define privgroup schatd
%define privpath  /var/empty

Name: schat
Version: 2.4.0
Release: alt1.cf35e54

Summary: IMPOMEZIA Simple Chat

License: GPLv3+
Group: Networking/Chat
Url: https://schat.me/

Epoch: 1

# Source0-url: https://github.com/impomezia/schat/archive/refs/heads/master.zip
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Source2: %name.desktop
Source4: %name.conf
Source6: schatd.service
Source7: schat-authd.service

Patch1: %name.patch

BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5WebKit) pkgconfig(Qt5Multimedia) pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xscrnsaver) pkgconfig(hunspell)
BuildRequires: libGeoIP-devel zlib-devel qt5-tools
BuildRequires: gcc-c++

%package -n schatd
Summary: Simple Chat server
Group: Networking/Chat

%description
Simple and powerful cross-platform chat for local networks and the Internet.

%description -n schatd
Simple and powerful cross-platform server for local networks and the Internet.

%package -n %name-server
Summary: Server for IMPOMEZIA Simple Chat (%name)
Group: System/Servers

%description -n %name-server
Server for IMPOMEZIA Simple Chat (%name)

%prep
%setup
%patch1 -p2
rm -rv src/3rdparty/zlib/
rm -rv src/common/plugins/SpellChecker/3rdparty

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" \
          "CONFIG+=debug" \
          PREFIX=%prefix LIBDIR=%_libdir GEOIP=1 schat2.pro
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot
rm -f %buildroot/%_libdir/lib*.so

install -D -p -m 0644 %SOURCE6 %buildroot%_unitdir/schatd.service
install -D -p -m 0644 %SOURCE7 %buildroot%_unitdir/schat-authd.service

install -Dp -m 0644 %SOURCE2 %buildroot/%_desktopdir/%name.desktop
rm -v %buildroot%_desktopdir/schat2.desktop

mkdir -p %buildroot%_sysconfdir/schatd2
mkdir -p %buildroot%_var/lib/schatd2
mkdir -p %buildroot%_logdir/schatd2

install -Dp -m 0644 %SOURCE4 %buildroot%_sysconfdir/schatd2/schat2.conf

%pre -n schatd
%_sbindir/groupadd -r -f %privgroup
%_sbindir/useradd -r -s /dev/null -g %privgroup -d %privpath >/dev/null -c 'schat daemon' %privuser >/dev/null 2>&1 ||:

%post -n schatd
%post_service %{name}d

%preun -n schatd
%preun_service %{name}d

%files
%doc README.md LICENSE
%_bindir/schat2
%_libdir/libschat-client.so.*
%_libdir/libschat.so.*
%_libdir/schat2/
%_datadir/schat2/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/schat2.png

%files -n schatd
%_sbindir/schatd2
%_sbindir/schat-authd
%_libdir/libschat-rest.so.*
%_libdir/libschat-tufao.so.*
%_libdir/libschatd.so.*
%_libdir/schatd2/
%_datadir/schatd2/
%_unitdir/schatd.service
%_unitdir/schat-authd.service
%attr(0750, schatd, schatd) %dir %_sysconfdir/schatd2
%config(noreplace) %attr(0640, schatd, schatd) %_sysconfdir/schatd2/schat2.conf
%attr(0750, schatd, schatd) %_var/lib/schatd2
%attr(0750, schatd, schatd) %_logdir/schatd2

%changelog
* Sat Mar 11 2023 Vitaly Lipatov <lav@altlinux.ru> 1:2.4.0-alt1.cf35e54
- fix version (ALT bug 45012)

* Mon Jan 09 2023 Vitaly Lipatov <lav@altlinux.ru> 1:2.3.4-alt1.cf35e54
- new version (2.3.4) with rpmgs script
- switch to Qt5

* Wed Aug 15 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.6-alt1.svn3549.1
- add systemd support

* Sun Mar 03 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3549
- 0.8.6.3549

* Fri Mar 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3539
- 0.8.6.3539

* Wed Feb 27 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.6-alt1.svn3531
- 0.8.6.3531

* Wed Nov 07 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.5-alt1.svn3271
- 0.8.5.3271

* Fri Feb 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1.svn2311
- 0.8.4.2311

* Mon Feb 13 2012 Motsyo Gennadi <drool@altlinux.ru> 0.8.4-alt1.svn2297
- 0.8.4.2297

* Sat Aug 27 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.3-alt1.svn1675
- 0.8.3.1675

* Thu Aug 25 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.3-alt1.svn1668
- 0.8.3.1668 (add Ukrainian translation)

* Mon Aug 15 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1.svn1637
- 0.8.2.1637 released (fixed build with Qt-4.4)

* Sat Aug 13 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.2-alt1.svn1629
- 0.8.2.1629 released

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.1-alt1.svn1452.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for schat
  * postclean-03-private-rpm-macros for the spec file

* Wed Apr 20 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.1-alt1.svn1452
- 0.8.1.1452 released

* Sun Feb 13 2011 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn1438
- 0.8.0.1438 released

* Fri Feb 04 2011 Motsyo Gennadi <drool@altlinux.ru> 0.7.5-alt0.1.svn1428
- svn 1428

* Tue Nov 23 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt1.svn1350
- release 0.7.4

* Fri Nov 12 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1347
- svn 1347

* Fri Aug 27 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1339
- svn 1339
- change license tag from GPLv3 to GPLv3+
- moved ChangeLog.html for search path

* Thu Aug 26 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1333
- svn 1333

* Wed Aug 25 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1329
- svn 1329

* Tue Aug 24 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt2.svn1325
- svn 1325
- release 0.7.3

* Thu Jul 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1320.1
- fix repocop wanings (remove svn subdir, add condstop to init-script)

* Fri Jul 09 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1320
- svn 1320

* Tue Jul 06 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1317
- svn 1317
- create subpackage for schat-server

* Sun Jul 04 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1313
- svn 1313

* Mon Jun 21 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.1.svn1296
- initial build for ALT Linux
