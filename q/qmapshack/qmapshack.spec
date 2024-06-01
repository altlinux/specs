Name: qmapshack
Version: 1.17.1
Release: alt1.1
Summary: GPS mapping and management tool
Group: Sciences/Geosciences

License: GPL-3.0-or-later and BSD
Url: https://github.com/Maproom/qmapshack/wiki
# Repacked https://github.com/Maproom/qmapshack/archive/V_%version/qmapshack-%version.tar.gz
Source: qmapshack-%version.tar
Patch1: qmapshack-1.14.1-alt-fix-HTML_INSTALL_DIR.patch

#Recommends: routino
#Recommends: qmaptool

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5-webengine
# Automatically added by buildreq on Sun Jul 30 2023
# optimized out: cmake-modules freexl gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libcairo-gobject libcrypt-devel libcurl-devel libdouble-conversion3 libgdk-pixbuf libglvnd-devel libgpg-error libhdf5-103 libhdf5-hl-100 libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-help libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-xml libquazip1-qt5_1.0.0 librabbitmq-c4 libsasl2-3 libssl-devel libstdc++-devel libudev-devel libunixODBC-devel libx265-199 libxerces-c ocl-icd pkg-config python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel routino-data sh4 zlib-devel
BuildRequires: cmake libalglib-devel libgdal-devel libjpeg-devel libproj-devel libroutino-devel libtiff-devel qt5-tools-devel qt5-webengine-devel quazip-qt5-devel libsqlite3-devel

ExclusiveArch: %qt5_qtwebengine_arches

%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop

%package -n qmaptool
Summary: Create raster maps from paper map scans
Url: https://bitbucket.org/maproom/qmaptool/wiki/Home
Group: Sciences/Geosciences

%description -n qmaptool
This is a tool to create raster maps from paper map scans. QMapTool can be
considered as a front-end to the well-known GDAL package. It complements
QMapShack.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	#
%cmake_build

%install
%cmakeinstall_std

%define _unpackaged_files_terminate_build 1

%files
%doc changelog.txt LICENSE
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/QMapShack.*
%_datadir/pixmaps/QMapShack.png
%_datadir/%name/
%_mandir/man1/%name.*

%files -n qmaptool
%_bindir/qmaptool
%_bindir/qmt_*
%_datadir/applications/qmaptool.desktop
%_datadir/icons/hicolor/*/apps/QMapTool.*
%_datadir/pixmaps/QMapTool.png
%_datadir/qmaptool/
%_datadir/qmt_*/
%_mandir/man1/qmaptool.*
%_mandir/man1/qmt_*.*

%changelog
* Sat Jun 01 2024 Andrey Cherepanov <cas@altlinux.org> 1.17.1-alt1.1
- NMU: FTBFS: built with libsqlite3-devel.

* Wed Jan 24 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.17.1-alt1
- Updated to 1.17.1.

* Sun Jul 30 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.17.0-alt1
- Updated to 1.17.0.

* Tue Nov 16 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.16.0-alt1
- Updated to 1.16.0 (ALT#44114).

* Sat Mar 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.15.2-alt1
- Updated to 1.15.2.

* Mon Oct 26 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.15.0-alt1
- Updated to 1.15.0.
- Fixed ftbfs with qt 5.15.

* Mon Apr 13 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.14.1-alt1
- Initial build.
