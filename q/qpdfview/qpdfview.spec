Name: qpdfview
Version: 0.5
Release: alt3
Summary: Tabbed PDF viewer using the poppler library
License: GPL-2.0-or-later
Group: Office
Url: https://launchpad.net/qpdfview

Source: %name-%version.tar
Patch: qpdfview-0.4.18-fix-build-with-qt5-5.15.patch
Patch1: qpdfview-desktop.patch
# std::optional requires std=c++17 or later. Fixes:
# /usr/include/poppler/qt5/poppler-form.h:888:6: error: ‘optional’ in namespace ‘std’ does not name a template type
Patch2: qpdfview-stdc++17.patch

BuildRequires: qt6-tools
BuildRequires: pkgconfig(poppler-qt6)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(zlib)
BuildRequires: cups-devel
BuildRequires: desktop-file-utils

Requires: qt6-sql-sqlite
Requires: qt6-svg

%description
qpdfview is a tabbed PDF viewer using the poppler library.

%prep
%setup
%autopatch -p2

%build
lrelease-qt6 qpdfview.pro
%qmake_qt6 qpdfview.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

install -d %buildroot%_liconsdir
install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir

ln -s %_iconsdir/hicolor/scalable/apps/%name.svg \
	%buildroot%_liconsdir
ln -s %_iconsdir/hicolor/scalable/apps/%name.svg \
	%buildroot%_miconsdir
ln -s %_iconsdir/hicolor/scalable/apps/%name.svg \
	%buildroot%_niconsdir

%files
%doc CHANGES CONTRIBUTORS README TODO
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*
%_libexecdir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%name.appdata.xml

%changelog
* Thu Jul 11 2024 Anton Midyukov <antohami@altlinux.org> 0.5-alt3
- rebuild with qt6

* Sun Jan 21 2024 Anton Midyukov <antohami@altlinux.org> 0.5-alt2
- fix build with poppler 23.08.0

* Tue Jul 25 2023 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- new version (0.5) with rpmgs script

* Tue Jul 25 2023 Anton Midyukov <antohami@altlinux.org> 0.4.18-alt4
- add russian translation to desktop file

* Sat Aug 15 2020 Anton Midyukov <antohami@altlinux.org> 0.4.18-alt3
- Fix build with qt5 5.15
- Fix License Tag

* Tue Sep 10 2019 Anton Midyukov <antohami@altlinux.org> 0.4.18-alt2
- Version 0.4.18

* Wed Mar 06 2019 Anton Midyukov <antohami@altlinux.org> 0.4.18-alt1.beta1
- Version 0.4.18beta1

* Sun Jan 14 2018 Anton Midyukov <antohami@altlinux.org> 0.4.17-alt3.beta1.S1
- Build translations
- Update buildrequires

* Fri Oct 27 2017 Sergey V Turchin <zerg@altlinux.org> 0.4.17-alt3.beta1
- Fix requires

* Thu Oct 26 2017 Sergey V Turchin <zerg@altlinux.org> 0.4.17-alt2.beta1
- Build with Qt5

* Sat Dec 10 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.17-alt1.beta1
- Version 0.4.17beta1 (ALT #32876)

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1
- Version 0.4.10

* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1
- Version 0.4.7 (ALT #29618)

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1
- Version 0.4.6

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1
- Version 0.4.5

* Thu Jun 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- Version 0.4.3 (ALT #29090)

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Version 0.4.1 (ALT #28781)

* Sun Feb 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4 (ALT #28589)

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt2
- Added requirement on libqt4-sql-sqlite (ALT #28519)

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Version 0.3.7 (ALT #28294)

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6 (ALT #28153)

* Fri Oct 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus (ALT #27871)

