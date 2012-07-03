Name: pentobi
Version: 2.0
Release: alt1
License: GPLv3
Summary: A computer program that plays the board game Blokus
Source: %name-%version.tar.gz
Group: Games/Boards
Url: http://pentobi.sourceforge.net/

# Automatically added by buildreq on Fri Jul 22 2011
# optimized out: boost-devel boost-devel-headers cmake-modules fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel
BuildRequires: boost-filesystem-devel boost-program_options-devel cmake gcc-c++ libqt4-opengl phonon-devel

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
(
cd BUILD
%make_build
)

%install
(
cd BUILD
%makeinstall DESTDIR=%buildroot
)
mkdir -p %buildroot%_sysconfdir
mv %buildroot/usr/etc/gconf %buildroot%_sysconfdir/

%files
%_gamesbindir/*
%_sysconfdir/gconf/schemas/%name.schemas
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/mime/packages/*.xml
%_datadir/thumbnailers/*
%_gamesdatadir/%name
%_man6dir/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with Boost 1.49.0

* Fri Jan 13 2012 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Autobuild version bump to 1.0
- Catch upstream's relocation to gamesbindir/gamesdatadir

* Mon Dec 07 2011 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Autobuild version bump to 0.2
- Thumbnailer and books added

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with Boost 1.47.0

* Fri Jul 22 2011 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Autobuild version bump to 0.1

