Name: qlandkartegt
Version: 1.8.1
Release: alt3
Summary: GPS mapping (GeoTiff and vector) and GPSr management

Group: Sciences/Geosciences
License: GPLv2+
Url: http://www.qlandkarte.org

Source: qlandkartegt-%version.tar
Patch0: 01_literal-suffix.patch
Patch1: 02_map2rmp_signedchar.patch

BuildRequires: cmake gcc-c++ gdal gpsbabel libXScrnSaver-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXft-devel libXmu-devel libXpm-devel
BuildRequires: libXres-devel libXxf86misc-devel libXxf86vm-devel libgdal-devel
BuildRequires: libjpeg-devel libproj-devel libqt4-sql-interbase libqt4-sql-mysql
BuildRequires: libqt4-sql-odbc libqt4-sql-sqlite2 libxkbfile-devel phonon-devel
BuildRequires: qt4-designer ruby ruby-stdlibs rpm-macros-cmake

%description
Quantum GIS (QGIS) is a user friendly Open Source Geographic Information
System (GIS) that runs on Linux, Unix, Mac OSX, and Windows. QGIS supports
vector, raster, and database formats. QGIS is licensed under the GNU
General Public License. QGIS lets you browse and create map data on your
computer. It supports many common spatial data formats (e.g. ESRI ShapeFile,
geotiff). QGIS supports plugins to do things like display tracks from your GPS.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1

%build
%add_optflags -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H=1
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc INSTALL changelog.txt
%dir %_datadir/%name
%_bindir/*
%_man1dir/*
%_pixmapsdir/*
%_desktopdir/*
%_datadir/%name/*

%changelog
* Sun Oct 06 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.8.1-alt3
- Rebuild with libproj 6.2.0 (use ACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.8.1-alt2
- Rebuild with libproj 5.2.0.
- Fix build of 3rdparty/map2rmp

* Wed Mar 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Thu Jun 06 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt2
- build fixes

* Wed Jun 05 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt1
- Initial build for ALT Linux
