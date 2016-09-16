Name: dwm
Version: 6.1
Release: alt1

Summary: Dynamic window manager for X

License: MIT
Group: Graphical desktop/Other
Url: http://dwm.suckless.org/

# Repacked http://www.suckless.org/download/%name-%version.tar.gz
Source: %name-%version.tar
Source1: dwm.wmsession
Source2: dwm-start
Source3: dwm-start.1

Patch0: dwm-user-notes.patch

# Automatically added by buildreq on Fri Sep 16 2016
# optimized out: fontconfig fontconfig-devel libX11-devel libXrender-devel libfreetype-devel python-base xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXft-devel libXinerama-devel

Requires: st

%description
dwm is a dynamic window manager for X.
It manages windows in tiling and floating modes.  Either mode can be
applied dynamically, optimizing the environment for the application in
use and the task performed. It is the little brother of wmii.

%prep
%setup
%patch -p1
# Nuke the silent build.
sed -i.backup -e 's|\t@|\t|' Makefile
cmp -s Makefile{,.backup} && false
# Insert optflags
sed -i.backup -e 's|-Os|%optflags -D_DEFAULT_SOURCE|' config.mk
cmp -s config.mk{,.backup} && false
# No strip for debuginfo, and insert ldflags to enhance the security.
sed -i.backup -e 's|-s ${LIBS}|${LIBS}|' config.mk
cmp -s config.mk{,.backup} && false
# X includedir path fix
sed -i.backup -e 's|X11INC = .*|X11INC = %_includedir|' config.mk
cmp -s config.mk{,.backup} && false
# libdir path fix
sed -i.backup -e 's|X11LIB = .*|X11LIB = %_libdir|' config.mk
cmp -s config.mk{,.backup} && false

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

install -pD -m 644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/14%name

install -m755 %SOURCE2 %buildroot%_bindir/dwm-start
install -m644 %SOURCE3 %buildroot%_man1dir/dwm-start.1
sed -i "s/VERSION/%version/;s/RELEASE/%release/" \
	%buildroot%_man1dir/dwm-start.1

%files
%_bindir/dwm
%_bindir/dwm-start
%_man1dir/dwm.1*
%_man1dir/dwm-start.1*
%doc README
%config %_sysconfdir/X11/wmsession.d/14%name

%changelog
* Fri Sep 16 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.1-alt1
- Updated to 6.1.
- Added dwm-start script to start user-built dwm.

* Mon Jan 02 2012 Ilya Mashkin <oddity@altlinux.ru> 6.0-alt1
- 6.0

* Sun Jul 10 2011 Ilya Mashkin <oddity@altlinux.ru> 5.9-alt1
- 5.9

* Fri Jul 23 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8.2-alt1
- 5.8.2

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 5.7.2-alt1
- 5.7.2

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6.1-alt1
- 5.6.1

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 5.5-alt1
- 5.5

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_wms for dwm

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1-alt1
- new version 4.1 (with rpmrb script)

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1.tar.gz-alt1
- new version 4.1.tar.gz (with rpmrb script)

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1-alt1
- new version 4.1 (with rpmrb script)

* Fri May 11 2007 Lunar Child <luch@altlinux.ru> 4.0-alt1
- new version

* Thu Jan 04 2007 Lunar Child <luch@altlinux.ru> 2.8-alt1
- new version

* Wed Nov 29 2006 Lunar Child <luch@altlinux.ru> 2.3-alt1
- new version

* Thu Nov 09 2006 Lunar Child <luch@altlinux.ru> 2.1-alt1
- new version

* Tue Oct 24 2006 Lunar Child <luch@altlinux.ru> 2.0-alt1
- First build for ALT Linux Sisyphus
