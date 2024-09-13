%define _unpackaged_files_terminate_build 1
# WARNING: Rebuild QGIS whenever a new version of GRASS is shipped! Even though the soname might stay the same, it won't work anymore.
# http://hub.qgis.org/issues/5274
%define grass_version 8.4.0
%def_enable grass
%def_enable python
%def_enable devel
%def_enable server

%ifarch %qt5_qtwebengine_arches
%def_enable qt5_qtwebengine
%else
%def_disable qt5_qtwebengine
%endif

Name:    qgis
Version: 3.38.3
Release: alt1

Summary: A user friendly Open Source Geographic Information System
License: GPL-3.0+ with exceptions
Group:   Sciences/Geosciences
Url:     http://qgis.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source3: qgis-server-httpd.conf
Source4: qgis-server-README
Source5: qgis.xml

Patch1: qgis-serverprefix.patch
Patch2: qgis-no-politics.patch
Patch3: qgis-alt-python3-libpath.patch
Patch2000: qgis-e2k.patch

# Fix unresolved symbols in grass based libs
%set_verify_elf_method unresolved=relaxed

# Set proper libexec directory
%define _libexecdir %prefix/libexec

Conflicts: qgis

ExcludeArch: armh ppc64le

# TODO: Pyspatialite is included if you use the bundled libspatialite.
# Some plug-ins need it.
# The license is not totally clear, see:
# http://code.google.com/p/pyspatialite/issues/detail?id=3
# It also is sort of a fork of pysqlite, which is not elegant.

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: flex bison
%if_enabled grass
BuildRequires: grass-devel = %grass_version
%endif
BuildRequires: gzip
BuildRequires: libexpat-devel
BuildRequires: libfcgi-devel
BuildRequires: libgdal-devel
BuildRequires: libgeos-devel
BuildRequires: libgsl-devel
BuildRequires: libproj-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libqscintilla2-qt5-devel
BuildRequires: libspatialite-devel
BuildRequires: libsqlite3-devel
BuildRequires: libzip-devel
BuildRequires: postgresql-devel
%if_enabled python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-PyQt5-devel
BuildRequires: python3-module-PyQt-builder
BuildRequires: python3-module-nose2
BuildRequires: python3-module-qscintilla2-qt5-devel
BuildRequires: python3-module-sip6
BuildRequires: python3-module-OWSLib
%endif
BuildRequires: qt5-base-devel
BuildRequires: qt5-3d-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-webkit-devel
%if_enabled qt5_qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-serialport-devel
BuildRequires: spatialindex-devel
BuildRequires: libexiv2-devel
BuildRequires: txt2tags
BuildRequires: libqwt6-qt5-devel
BuildRequires: libprotobuf-devel
BuildRequires: libprotobuf-lite-devel
BuildRequires: protobuf-compiler
BuildRequires: ocl-icd-devel
BuildRequires: libhdf5-devel
BuildRequires: libnetcdf-devel
BuildRequires: libxml2-devel
BuildRequires: /proc
BuildRequires: libzstd-devel
BuildRequires: libpdal-devel
BuildRequires: pdal
BuildRequires: libdraco-devel
BuildRequires: libtiff-devel

#Requires: libqt4-sql-sqlite
Requires: qca-qt5-ossl
Requires: gpsbabel
Requires: libqwt6-qt5

Provides: qgis3 = %EVR
Obsoletes: qgis3 < %EVR

# We don't want to provide private Python extension libs
%add_findprov_skiplist %%python_sitelibdir/qgis/*.so 
%add_python3_path %_datadir/qgis/python
%filter_from_requires /^python3(processing.core.GeoAlgorithm)/d
%add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets

%description
Geographic Information System (GIS) manages, analyzes, and displays
databases of geographic information. Quantum GIS (QGIS) supports shape
file viewing and editing, spatial data storage with PostgreSQL/PostGIS,
projection on-the-fly, map composition, and a number of other features
via a plugin interface. QGIS also supports display of various
geo-referenced raster and Digital Elevation Model (DEM) formats
including GeoTIFF, Arc/Info ASCII Grid, and USGS ASCII DEM.

%package devel
Summary: Development Libraries for the Quantum GIS
Group: Development/C
Requires: %name = %version-%release
Provides: qgis3-devel = %EVR
Obsoletes: qgis3-devel < %EVR

%description devel
Development packages for Quantum GIS including the C header files.

%package grass 
Summary: GRASS Support Libraries for Quantum GIS
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: grass
Provides: qgis3-grass = %EVR
Obsoletes: qgis3-grass < %EVR
  
%description grass
GRASS plugin for Quantum GIS required to interface with the GRASS
system.

%package python 
Summary: Python integration and plug-ins for Quantum GIS
Group: Sciences/Geosciences
Requires: %name = %version-%release
Requires: python3-module-gdal
Requires: python3-module-qscintilla2-qt5
Provides: qgis3-python = %EVR
Obsoletes: qgis3-python < %EVR

%description python
Python integration and plug-ins for Quantum GIS.

%package server 
Summary: FCGI based OGC web map server
Group: Sciences/Geosciences
Provides:  %name-mapserver = %version-%release
Obsoletes: %name-mapserver < %version-%release
Requires: %name = %version-%release
Requires: libfcgi
Provides: qgis3-server = %EVR
Obsoletes: qgis3-server < %EVR

%description server
This FastCGI OGC web map server implements OGC WMS 1.3.0 and 1.1.1.
The services are prepared as regular projects in QGIS. They're rendered
using the QGIS libraries. The server also supports SLD (Styled Layer
Descriptor) for styling. Sample configurations for Httpd and Lighttpd
are included.

Please refer to %name-server-README for details!

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch %e2k
%patch2000 -p1
%endif

# Delete bundled libs
rm -rf src/core/gps/qextserialport
rm -rf "python/ext-libs/!(CMakeLists.txt|tests)"
rm -rf src/plugins/dxf2shp_converter/
sed -i '/dxf2shp_converter/d' src/plugins/CMakeLists.txt

gzip ChangeLog

%build
%ifarch %e2k
# "error: cpio archive too big"
%define optflags_debug -g0
%endif
%add_optflags -Wno-error=return-type
CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
CXXFLAGS="${CXXFLAGS:-%optflags}"; export CXXFLAGS;
export LD_LIBRARY_PATH=`pwd`/output/%_lib
%cmake_insource -GNinja \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DQGIS_LIB_SUBDIR:PATH=%_lib \
    -DQGIS_MANUAL_SUBDIR:PATH=/share/man \
    -DQGIS_PLUGIN_SUBDIR:PATH=%_lib/%name \
    -DQGIS_CGIBIN_SUBDIR:PATH=%_libexecdir/%name \
    -DWITH_BINDINGS:BOOL=%{?_enable_python:ON}%{?!_enable_python:OFF} \
    -DWITH_SERVER:BOOL=%{?_enable_server:ON}%{?!_enable_server:OFF} \
%if_enabled grass
    -DWITH_GRASS=TRUE \
    -DGRASS_PREFIX8=%_libdir/grass \
%endif
%if_enabled qt5_qtwebengine
    -DWITH_QTWEBENGINE:BOOL=ON \
%else
    -DWITH_QTWEBENGINE:BOOL=OFF \
%endif
    -DBINDINGS_GLOBAL_INSTALL:BOOL=TRUE \
    -DWITH_CUSTOM_WIDGETS:BOOL=TRUE \
    -DGDAL_INCLUDE_DIR:PATH=%_includedir/gdal \
    -DGDAL_LIBRARY:PATH=%_libdir/libgdal.so \
    -DGEOS_LIBRARY:PATH=%_libdir/libgeos_c.so \
    -DQWT_INCLUDE_DIR=%_includedir/qt5/qwt \
    -DQWT_LIBRARY=%_libdir/libqwt-qt5.so \
    -DENABLE_TESTS:BOOL=FALSE \
    -DWITH_QTMOBILITY:BOOL=FALSE \
    -DLIBZIP_INCLUDE_DIR:PATH=%_includedir/libzip \
    -DLIBZIP_CONF_INCLUDE_DIR:PATH=%_libdir/libzip/include \
    -DQCA_INCLUDE_DIR:PATH=%_includedir/qt5/Qca-qt5/QtCrypto \
    -DWITH_OAUTH2_PLUGIN=OFF \
    .
%ifarch %ix86
export NPROCS=8
%endif
%ninja_build

%install
%ninja_install

# Install MIME type definitions
install -pd %buildroot%_datadir/mime/packages
install -pm0644 %SOURCE5 %buildroot%_datadir/mime/packages/%name.xml

# Install application and MIME icons
install -pd %buildroot%_datadir/pixmaps
install -pd %buildroot%_datadir/icons/hicolor/16x16/apps
install -pd %buildroot%_datadir/icons/hicolor/scalable/apps
install -pd %buildroot%_datadir/icons/hicolor/128x128/mimetypes
install -pm0644 \
        images/icons/qgis-icon-60x60.png \
	%buildroot%_datadir/pixmaps/%name.png
install -pm0644 \
	images/icons/%name-icon-16x16.png \
	%buildroot%_datadir/icons/hicolor/16x16/apps/%name.png
install -pm0644 \
	images/icons/%{name}_icon.svg \
	%buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg
install -pm0644 \
	%buildroot%_datadir/%name/images/icons/%name-mime-icon.png \
	%buildroot%_datadir/icons/hicolor/128x128/mimetypes/application-x-qgis-layer-settings.png
install -pm0644 \
	%buildroot%_datadir/%name/images/icons/%name-mime-icon.png \
	%buildroot%_datadir/icons/hicolor/128x128/mimetypes/application-x-qgis-project.png

# Install basic QGIS Mapserver configuration for Apache
install -pd %buildroot%_sysconfdir/httpd/conf.d
install -pm0644 %SOURCE3 %buildroot%_sysconfdir/httpd/conf.d/qgis-server.conf

# Remove files packaged by doc
pushd %buildroot%_datadir/%name/doc
rm -f BUGS \
	CHANGELOG \
	CODING \
	COPYING \
	INSTALL \
	PROVENANCE \
	README
popd

# Install server docs
mkdir -p %buildroot%_datadir/doc/%name-server-%version
cp %SOURCE4 %SOURCE3 \
   %buildroot%_datadir/doc/%name-server-%version

%if_enabled python
# Copy test utilities form tests to plugins/processing/tests
cp tests/src/python/utilities.py %buildroot%_datadir/qgis/python/plugins/processing/tests/
%endif

%find_lang %name --with-qt
# Add missing localization
echo "%%lang(zh) /usr/share/qgis/i18n/qgis_zh-Hans.qm" >> %name.lang
echo "%%lang(zh) /usr/share/qgis/i18n/qgis_zh-Hant.qm" >> %name.lang

%if_disabled devel
rm -rf %buildroot%_datadir/%name/FindQGIS.cmake \
       %buildroot%_includedir/%name \
       %buildroot%_libdir/lib%{name}*.so \
       %buildroot%_libdir/qt5/plugins/designer/libqgis_customwidgets.so* \
       %buildroot%_datadir/doc/%name-server-%version \
       %buildroot%_sysconfdir/httpd/conf.d/%{name}-server.conf \
       %buildroot%_libexecdir/%name
%endif

%if_disabled qt5_qtwebengine
rm -rvf %buildroot%python3_sitelibdir/%name/PyQt/QtWebEngine*
sed -i '/QtWebEngine/d' %buildroot%_datadir/%name/python/qsci_apis/PyQt5.api
%endif


%files -f %name.lang
%doc BUGS COPYING Exception_to_GPL_for_Qt.txt PROVENANCE *.md ChangeLog.gz
# QGIS shows these files in the GUI
%_datadir/%name/doc
%dir %_datadir/%name/i18n/
%_libdir/lib%{name}_analysis.so.*
%_libdir/lib%{name}_app.so.*
%_libdir/lib%{name}_core.so.*
%_libdir/lib%{name}_gui.so.*
%_libdir/lib%{name}_native.so.*
%_libdir/lib%{name}_3d.so.*
%_libdir/%name
%_bindir/%name
%_bindir/%{name}_process
%doc %_man1dir/*
%dir %_datadir/%name/
%_datadir/mime/packages/%name.xml
%_datadir/pixmaps/%name.png
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/128x128/mimetypes/application-x-%name-project.png
%_datadir/icons/hicolor/128x128/mimetypes/application-x-%name-layer-settings.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/*x*/mimetypes/%{name}-*.png
%_iconsdir/hicolor/scalable/mimetypes/%{name}*.svg
%_datadir/applications/*.desktop
%_datadir/%name/images
%_datadir/%name/resources
%_datadir/%name/svg
%if_enabled server
%_libdir/lib%{name}_server.so.*
%endif
%if_enabled grass
%exclude %_libdir/libqgisgrass*.so.*
%exclude %_libdir/%name/libprovider_grass*.so
%exclude %_libdir/%name/libprovider_grassraster*.so
%exclude %_libdir/%name/grass
%endif
%_datadir/metainfo/org.qgis.qgis.appdata.xml

%if_enabled devel
%files devel
%_datadir/%name/FindQGIS.cmake
%_includedir/%name
%_libdir/lib%{name}*.so
%_libdir/qt5/plugins/designer/libqgis_customwidgets.so*
%endif

%if_enabled grass
%files grass
%_libdir/libqgisgrass*.so.*
%_libdir/%name/libprovider_grass*.so
%_libdir/%name/grass
%_datadir/%name/grass
%endif

%if_enabled python
%files python
%_libdir/libqgispython.so.*
%_datadir/%name/python
%python3_sitelibdir/%name
%python3_sitelibdir/PyQt5/uic/widget-plugins/
%endif

%if_enabled server
%files server
%doc %_datadir/doc/%name-server-%version
%config(noreplace) %_sysconfdir/httpd/conf.d/%{name}-server.conf
%_bindir/qgis_mapserver
%_libexecdir/%name
%endif

%changelog
* Fri Sep 13 2024 Andrey Cherepanov <cas@altlinux.org> 3.38.3-alt1
- New version.

* Sat Aug 17 2024 Andrey Cherepanov <cas@altlinux.org> 3.38.2-alt1
- New version.

* Sun Jul 28 2024 Andrey Cherepanov <cas@altlinux.org> 3.38.1-alt2
- Rebuilt with GRASS 8.4.0.

* Sat Jul 20 2024 Andrey Cherepanov <cas@altlinux.org> 3.38.1-alt1
- New version.

* Wed Jul 17 2024 Ivan A. Melnikov <iv@altlinux.org> 3.38.0-alt2
- enable building with QtWebEngine on architectures where
  it's available;
- fix FTBFS on architectures where QtWebEngine is not available.

* Mon Jun 24 2024 Andrey Cherepanov <cas@altlinux.org> 3.38.0-alt1
- New version.

* Sat May 18 2024 Andrey Cherepanov <cas@altlinux.org> 3.36.3-alt1
- New version.

* Thu May 09 2024 Andrey Cherepanov <cas@altlinux.org> 3.36.2-alt1
- New version.

* Sat Mar 09 2024 Andrey Cherepanov <cas@altlinux.org> 3.36.0-alt3
- Rebuilt with grass 8.3.2.

* Fri Mar 01 2024 Michael Shigorin <mike@altlinux.org> 3.36.0-alt2
- E2K: fix build (ilyakurdyukov@).

* Sat Feb 24 2024 Andrey Cherepanov <cas@altlinux.org> 3.36.0-alt1
- New version.
- Renamed ro qgis.

* Sun Jan 21 2024 Andrey Cherepanov <cas@altlinux.org> 3.34.3-alt1
- New version.

* Sat Dec 23 2023 Andrey Cherepanov <cas@altlinux.org> 3.34.2-alt1
- New version.

* Sat Nov 25 2023 Andrey Cherepanov <cas@altlinux.org> 3.34.1-alt1
- New version.

* Sun Oct 29 2023 Andrey Cherepanov <cas@altlinux.org> 3.34.0-alt1
- New version.

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.3-alt3
- Rebuilt with GRASS 8.3.1.

* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.3-alt2
- Fixed build with PDAL 2.6.x.

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.3-alt1
- New version.

* Sat Aug 19 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.2-alt1
- New version.

* Sat Jul 22 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.1-alt1
- New version.

* Sat Jun 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.32.0-alt1
- New version.

* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 3.30.3-alt1
- New version.

* Mon May 15 2023 Andrey Cherepanov <cas@altlinux.org> 3.30.2-alt1
- New version.

* Sun Apr 30 2023 Andrey Cherepanov <cas@altlinux.org> 3.30.1-alt1
- New version.
- No politics on News pane.

* Tue Jan 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.24.3-alt1
- New version.

* Wed Oct 19 2022 Andrey Cherepanov <cas@altlinux.org> 3.24.0-alt3
- Rebuilt with grass-8.2.0.

* Mon Feb 28 2022 Andrey Cherepanov <cas@altlinux.org> 3.24.0-alt2
- Rebuilt with grass-8.0.1.

* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 3.24.0-alt1
- New version.

* Fri Jan 28 2022 Andrey Cherepanov <cas@altlinux.org> 3.22.3-alt2
- Rebuild with grass-8.0.0.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 3.22.3-alt1
- New version.

* Tue Jan 04 2022 Andrey Cherepanov <cas@altlinux.org> 3.22.2-alt1
- New version.

* Mon Nov 29 2021 Andrey Cherepanov <cas@altlinux.org> 3.22.1-alt1
- New version.

* Fri Oct 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.22.0-alt1
- New version.

* Thu Oct 21 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.3-alt3
- Remove desktop files absent in upstream.

* Mon Oct 11 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.3-alt2
- Rebuild with grass 7.8.6.

* Fri Sep 10 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.3-alt1
- New version.

* Fri Aug 13 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.2-alt1
- New version.

* Mon Jul 19 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.1-alt1
- New version.

* Thu Jul 15 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.0-alt1
- New version.

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.18.3-alt2
- NMU: fix build with sip5

* Sat May 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.18.3-alt1
- New version.

* Tue Apr 20 2021 Andrey Cherepanov <cas@altlinux.org> 3.18.2-alt1
- New version.
- Enable GRASS support.

* Sat Mar 20 2021 Andrey Cherepanov <cas@altlinux.org> 3.18.1-alt1
- New version.

* Mon Feb 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.18.0-alt1
- New version.

* Fri Jan 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.16.3-alt1
- New version.

* Thu Dec 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.16.2-alt1
- New version.

* Wed Dec 16 2020 Andrey Cherepanov <cas@altlinux.org> 3.16.1-alt1
- New version.

* Mon Nov 02 2020 Andrey Cherepanov <cas@altlinux.org> 3.16.0-alt1
- New version.

* Mon Aug 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.14.15-alt1
- New version.
- Skip python3 requires: PyQt5.QtWebKit, PyQt5.QtWebKitWidgets.
- Exclude armh from build architectures.
- Build in 8 threads on i586.

* Tue Jul 21 2020 Andrey Cherepanov <cas@altlinux.org> 3.14.1-alt1
- New version.

* Fri Jun 19 2020 Andrey Cherepanov <cas@altlinux.org> 3.14.0-alt1
- New version.
- Build using ninja-build.
- Remove obsoleted and unnecessary CMake flags.

* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 3.12.3-alt1
- New version.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 3.12.2-alt1
- New version.

* Sat Mar 21 2020 Andrey Cherepanov <cas@altlinux.org> 3.12.1-alt1
- New version.

* Thu Mar 19 2020 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.
- Fixed license tag according to SPDX.

* Thu Dec 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.10.1-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- New version.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Mon Aug 12 2019 Anton Midyukov <antohami@altlinux.org> 3.8.1-alt2
- fix PATHs for libqwt6-qt5

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Sat Jun 22 2019 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt2
- Add qca-qt5-ossl as authentication plugin.

* Tue Jun 11 2019 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- New version.

* Fri Mar 22 2019 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version with name qgis3
- Build without Python and Grass bindings.

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.18.16-alt3
- Rebuild with grass 7.4.1.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.18.16-alt2
- Rebuild with new version of spatialite and grass.

* Sun Jan 21 2018 Andrey Cherepanov <cas@altlinux.org> 2.18.16-alt1
- New version.

* Mon Dec 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.15-alt0.M80P.1
- Backport new version to p8 branch

* Mon Dec 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.15-alt1
- New version.

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.18.14-alt1.1
- rebuild with new spatialindex

* Mon Oct 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.14-alt0.M80P.1
- Backport new version to p8 branch

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.14-alt1
- New version

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.18.13-alt2
- Rebuilt with qscintilla2 2.10.1.

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.13-alt0.M80P.1
- Backport new version to p8 branch

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.13-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.12-alt0.M80P.1
- Backport new version to p8 branch

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.12-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.11-alt2
- Rebuild with geos 3.6.2

* Wed Aug 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.11-alt0.M80P.1
- Backport new version to p8 branch

* Sun Jul 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.11-alt1
- New version

* Sat Jun 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.10-alt1
- New version

* Fri May 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.9-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.8-alt0.M80P.1
- Backport new version to p8 branch

* Sat May 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.8-alt1
- New version

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.7-alt0.M80P.1
- Backport new version to p8 branch

* Sat Apr 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.7-alt1
- New version

* Sun Apr 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.6-alt0.M80P.1
- Backport new version to p8 branch

* Sat Apr 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.6-alt1
- New version

* Fri Mar 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.5-alt0.M80P.1
- Backport new version to p8 branch

* Fri Mar 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.5-alt1
- New version

* Tue Mar 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.4-alt0.M80P.1
- Backport new version to p8 branch

* Tue Mar 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.4-alt1
- New version
- Fix GRASS default path
- Add qca2-ossl to enable auth plugin for qgis

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.3-alt1
- new version 2.18.3

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt0.M80P.1
- Backport new version to p8 branch

* Fri Oct 28 2016 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- New version

* Sun Aug 14 2016 Andrey Cherepanov <cas@altlinux.org> 2.16.1-alt1
- New version

* Sun Jan 31 2016 Andrey Cherepanov <cas@altlinux.org> 2.12.3-alt1
- New version

* Sat Jan 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.12.2-alt1
- New version

* Fri Dec 11 2015 Andrey Cherepanov <cas@altlinux.org> 2.12.1-alt1
- New version

* Tue Nov 03 2015 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- New version

* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.10.1-alt1
- New version
- Add libqt4-sql-sqlite to requirements for work with bookmarks

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt2.git4dce5ec
- rebuilt with qwt-6.1.2/qwtpolar-1.1.1

* Tue Aug 26 2014 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.git4dce5ec
- New version 2.4.0 with update source to Git commit 4dce5ec
- Merge patchset with Fedora

* Mon Feb 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version

* Mon Jan 27 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version (ALT #27790)
- Fix Grass version to make breakage more visible

* Fri Dec 06 2013 Andrey Kolotov <qwest@altlinux.org> 1.8.0-alt1.1
- build fixed

* Fri Jun 07 2013 Ivan Ovcherenko <asdus@altlinux.org> 1.8.0-alt1
- New upstream release

* Fri Oct 19 2012 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt2
- fix build 

* Thu Feb 23 2012 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.1
- Rebuilt with libqwt6 instead of libqwt

* Sun Dec 18 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Tue Dec 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jun 22 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qgis

* Thu May 12 2011 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt2
- fix build (Patch3)

* Wed Dec 22 2010 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0
- without grass

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt2
- fix build on x86_64
- cleanup spec, move libqgisgrass to qgis-grass package

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 28 2008 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-2
- defining lib path in build
- installing python bindings globally
- adding patch to determine python site packages dir correctly

* Mon Dec 17 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.1-1
- update to 0.9.1
- removing lib64 and man instal path patches (included upstream)
- enabling python integration

* Fri Oct 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-2
- enabling build for PPC64 (bug#247152)

* Wed Sep 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.9.0-1
- update to 0.9.0
- remove settings-include-workdir.patch
- updated man-install-share.patch to man-install-share-0.9.0.patch
- updated lib64-suffix.patch to lib64-suffix-0.9.0.patch
- enabled python to support msexport tool
- added Requires: grass to grass subpackage

* Tue Aug 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-13
- bump for expat 2.0 rebuild bug#195888

* Thu Aug 02 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-12
- updated License from GPL to GPLv2+

* Tue Jul 10 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-11
- allowing docs to be installed by qgis so they can be referenced by internal
  help system (bug#241403)
- updated lib64 patch (bug#247549) to try to get plugins found on x86_64

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-10
- updated lib64 patch for core and grass libraries

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-9
- updated lib64 patch

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-8
- adding ExcludeArch: ppc64 for bug#247152 (lrelease segfault)

* Thu Jul 05 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-7
- adding patch for lib64 support through lib_suffix

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-6
- fixed date of changelog entry for 0.8.1-5 from Wed Jun 27 2007 to
  Thu Jun 28 2007
- linking icon to included png instead of packaging it again

* Thu Jun 28 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-5
- adding comment on why grass is required in addition to grass-devel for BR
- fixing typo

* Wed Jun 27 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-4
- adding contributors to doc
- adding desktop file and icon

* Mon Jun 25 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-3
- updating detection of grass libraries to not use RPM call
- disabling building of -devel package due to shared libraries not being
  versioned and having no other packages that compile against qgis
  (see bug #241403)
- removing chmod of test_export.py due to lack of python requirement
- removing msexport and share/python directory due to removal of python

* Fri Jun 22 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-2
- added BuildRequires: cmake
- updated build to use cmake macro and make verbose

* Tue Jun 19 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.1-1
- updating version
- removed BuildRequires: python-devel due to lack of PyQt4 bindings
- updated build for use of cmake instead of autotools
- added patch for setting WORKDIR in settings.pro file
- added patch for fixing install path of man pages
- updated library names

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-6
- adding BuildRequires bison, flex

* Tue May 29 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-5
- fixing more directory owernship (themes, themes-default)
- fixing qt4 hardcoded lib path
- removing Requires ldconfig
- adding BuildRequires sqlite-devel
- adding patch for supporting python 2.5 in configure script

* Sat May 26 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-4
- moving all BuildRequires to main section
- dropping use of makeinstall macro
- making sure directories are owned by this package
- removing *.a and *.la files
- disabled stripping of libraries and binaries to allow debuginfo package
  to be built
- fixing macros in changelog
- removing executable bits on source files

* Wed May 16 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-3
- fixing Requires statements for sub-packages

* Tue May 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-2
- added devel dependancy on qgis
- moved qgis-config to devel package
- moving doc directory
- removed zero-length NEWS doc
- added postin/postun ldconfig calls
- split packages up to reduce package size and split out dependancies
  grass, theme-nkids

* Mon May 14 2007 Douglas E. Warner <silfreed@silfreed.net> 0.8.0-1
- Initial RPM release.

