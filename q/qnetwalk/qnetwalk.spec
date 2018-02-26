Name: qnetwalk
Version: 1.3
Release: alt3

Group: Games/Puzzles
Summary: Qt-version of the popular NetWalk game
License: GPL
URL: http://qt.osdn.org.ua/qnetwalk.html

Source0: http://qt.osdn.org.ua/%name-%version.tar

Patch1: %name-1.1-paths.patch
Patch2: %name-1.3-gcc45.patch

Packager: Evgenii Terechkov <evg@altlinux.ru>

# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: ImageMagick gcc-c++ libqt4-devel

%description
Qt-version of the popular NetWalk game.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

subst "s|\(target.path.*=\).*|\1 %_gamesbindir/|" %name.pro
subst "s|\(share.path.*=\).*|\1 %_gamesdatadir/%name/|" %name.pro
subst "s|/usr/local/man|%_mandir|" %name.pro
subst "s|/usr/local/share|%_gamesdatadir|g" %name.pro

export QTDIR=%_qt4dir PATH=%_qt4dir/bin:$PATH
qmake -unix
%make clean

%build
export QTDIR=%_qt4dir PATH=%_qt4dir/bin:$PATH
%make_build

%install
make install INSTALL_ROOT=%buildroot

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps/
install -m 0644 pics/%name.png %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 0644 pics/computer2.png %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
convert -resize 48x48 pics/computer2.png %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

%files
%_gamesbindir/*
%_datadir/%name
%_desktopdir/*
%_iconsdir/*/*/*/%name.png
%_man6dir/%name.6.*
%doc ChangeLog README

%changelog
* Sun Nov  7 2010 Terechkov Evgenii <evg@altlinux.org> 1.3-alt3
- Fix build with gcc4.5

* Sun Nov 16 2008 Terechkov Evgenii <evg@altlinux.ru> 1.3-alt2
- Update spec to new filetriggers system

* Thu Apr  3 2008 Terechkov Evgenii <evg@altlinux.ru> 1.3-alt1
- 1.3
- Patch1 updated
- Migrate to vanila "make install"
- Vanila .desktop file used
- Spec cleanup

* Sat Jun 23 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2-alt4
- Spec cleanup

* Wed Jan 10 2007 Terechkov Evgenii <evg@altlinux.ru> 1.2-alt3
- Debian menu replaced by .desktop
- Spec cleanups
- man page added

* Tue Oct 10 2006 Igor Zubkov <icesik@altlinux.ru> 1.2-alt2
- buildreq (must fix build)

* Thu Jul 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.2-alt1
- new version
- don't use soundwrapper

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- new version

* Fri Oct 29 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- fix %%install

* Wed Oct 27 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec

