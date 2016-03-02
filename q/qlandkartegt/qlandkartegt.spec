Name: qlandkartegt
Version: 1.8.1
Release: alt1
Summary: GPS mapping (GeoTiff and vector) and GPSr management

Group: Sciences/Geosciences
License: GPLv2+
Url: http://www.qlandkarte.org

Source: qlandkartegt-%version.tar

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

%build
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
* Wed Mar 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Thu Jun 06 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt2
- build fixes

* Wed Jun 05 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt1
- Initial build for ALT Linux
