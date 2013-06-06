Name: qlandkartegt
Version: 1.7.0
Release: alt2
Summary: GPS mapping (GeoTiff and vector) and GPSr management

Group: Sciences/Geosciences
License: GPLv2+
Url: http://www.qlandkarte.org

Source: qlandkartegt-%version.tar

# Automatically added by buildreq on Wed Jun 05 2013
# optimized out: cmake-modules fontconfig libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libgst-plugins libhdf5-7-seq libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
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
# make install DESTDIR=%buildroot

%files
%doc INSTALL changelog.txt
%dir %_datadir/%name
%_bindir/*
%_man1dir/*
%_pixmapsdir/*
%_desktopdir/*
%_datadir/%name/*

%changelog
* Thu Jun 06 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt2
- build fixes

* Wed Jun 05 2013 Grigory Milev <week@altlinux.ru> 1.7.0-alt1
- Initial build for ALT Linux
