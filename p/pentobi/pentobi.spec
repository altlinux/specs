Name: pentobi
Version: 21.0
Release: alt1.1

Summary: A computer program that plays the board game Blokus

License: GPLv3
Group: Games/Boards
Url: https://pentobi.sourceforge.io

# Source-url: https://github.com/enz/pentobi/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5-webengine

# Automatically added by buildreq on Wed Jun 15 2022
# optimized out: cmake-modules dconf fontconfig gcc-c++ glib-networking glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libcairo-gobject libgdk-pixbuf libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libsasl2-3 libssl-devel libstdc++-devel python3 python3-base python3-module-libxml2 qt5-base-devel qt5-declarative-devel qt5-tools sh4 shared-mime-info xml-common
BuildRequires: cmake docbook-style-xsl itstool libGConf libappstream-glib-devel libgtk+3-devel libpolkit-devel librsvg-utils qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel xsltproc

%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%endif

%description
Pentobi is a computer program that plays the board game Blokus.

- Supports the game variants Classic, Classic Two-Player, and Duo
- Different levels of playing strength
- Save and load games in Smart Game Format including comments and move variations
- Board display with optional move numbers and coordinate labels
- Export images of board positions
- Source code is available under the GNU General Public License

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_sysconfdir

%files
%_bindir/pentobi
%_bindir/pentobi-thumbnailer
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/mime/packages/*.xml
%_datadir/thumbnailers/*
%_datadir/metainfo/*
%_man6dir/*
%_mandir/*/man6/*

%changelog
* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 21.0-alt1.1
- NMU: Use rpm-macros-qt5-webengine (fixes build on loongarch64)

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 21.0-alt1
- Autobuild version bump to 21.0
- Fix ppc build

* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 19.0-alt1
- NMU: build new version, build with Qt5

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 9.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 9.0-alt1
- Autobuild version bump to 9.0

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 8.2-alt1
- Autobuild version bump to 8.2

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 8.0-alt1
- Autobuild version bump to 8.0

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 7.2-alt1
- Autobuild version bump to 7.2

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 7.1-alt1
- Autobuild version bump to 7.1

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 6.0-alt1
- Autobuild version bump to 6.0
- Remove gconf bindings

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 5.0-alt1
- Autobuild version bump to 5.0

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1.1
- Rebuilt with Boost 1.52.0

* Mon Nov 12 2012 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Autobuild version bump to 4.3

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Autobuild version bump to 4.2

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.1
- Rebuilt with Boost 1.51.0

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with Boost 1.49.0

* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Autobuild version bump to 1.0
- Catch upstream's relocation to gamesbindir/gamesdatadir

* Wed Dec 07 2011 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Autobuild version bump to 0.2
- Thumbnailer and books added

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with Boost 1.47.0

* Fri Jul 22 2011 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Autobuild version bump to 0.1

