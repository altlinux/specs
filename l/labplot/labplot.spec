ExcludeArch: %ix86
%define _unpackaged_files_terminate_build 1
%define soversion 2.12.0
Name: labplot
Version: 2.12.1
Release: alt3
Summary: Function and Data Plotter
License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://labplot.kde.org/
%K6init no_altplace

Conflicts: labplot1.6
Requires: ImageMagick-tools gsl pstoedit cantor

VCS: https://invent.kde.org/education/labplot.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake gcc-c++ extra-cmake-modules
BuildRequires: qt6-base-devel qt6-svg-devel
BuildRequires: qt6-declarative-devel
BuildRequires: libfftw3-devel
BuildRequires: liblz4-devel
BuildRequires: libcerf-devel
BuildRequires: libvulkan-devel
BuildRequires: libpoppler-qt6-devel
BuildRequires: eigen3-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-karchive-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-knewstuff-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: libXScrnSaver-devel libXau-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libgsl-devel libhdf5-devel libnetcdf-devel
BuildRequires: libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires: qt6-serialport-devel
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: cantor-devel
BuildRequires: libcfitsio-devel
BuildRequires: libmatio-devel
BuildRequires: libdiscount-devel
BuildRequires: liborcus-devel libixion-devel
BuildRequires: libzstd-devel

%description
This is a program for plotting of functions and data manipulation.

A versatile spreadsheet for data import and editing was added.
Also a better 3 dimensional plot with rotation and colormaps is available.
Newly supported are data set operations and image manipulations. One can now
import over 80 different images formats and export directly to ps, eps or pdf.
The plots now use double buffering and LabPlot supports scripting using QSA.

%package -n liblabplot-devel
Summary: Development files for labplot
Group: Development/KDE and QT

%description -n liblabplot-devel
This package contains the LabPlot Software Development Kit.

%package -n liblabplot%soversion
Summary: Library for LabPlot - data analysis and visualization
Group: Sciences/Mathematics

%description -n liblabplot%soversion
LabPlot is a free software data analysis and visualization tool.
This package provides the shared library for LabPlot.

%prep
%setup

# fix missing QElapsedTimer include (qt6 >= 6.10)
sed -i '/#include <QIcon>/a #include <QElapsedTimer>' \
    src/backend/worksheet/plots/cartesian/XYFourierFilterCurve.cpp

# fix Eigen3 detection with new cmake config (eigen3 >= 5.0):
# Eigen3Config.cmake sets Eigen3_FOUND/Eigen3_VERSION/Eigen3::Eigen,
# but not legacy EIGEN3_FOUND/EIGEN3_INCLUDE_DIR/EIGEN3_VERSION_STRING
sed -i '/find_package(Eigen3 QUIET)/a\    if(Eigen3_FOUND AND NOT DEFINED EIGEN3_FOUND)\n        set(EIGEN3_FOUND TRUE)\n        get_target_property(EIGEN3_INCLUDE_DIR Eigen3::Eigen INTERFACE_INCLUDE_DIRECTORIES)\n        set(EIGEN3_VERSION_STRING "${Eigen3_VERSION}")\n    endif()' CMakeLists.txt

# fix missing INTERFACE_INCLUDE_DIRECTORIES in cantor-devel cmake config:
# CantorTargets.cmake omits include dirs, so cantor/session.h is not found
sed -i 's|    return()|    if(TARGET Cantor::cantorlibs)\n        get_target_property(_ci Cantor::cantorlibs INTERFACE_INCLUDE_DIRECTORIES)\n        if(NOT _ci)\n            find_path(_ci cantor/session.h PATH_SUFFIXES KF6)\n            if(_ci)\n                set_target_properties(Cantor::cantorlibs PROPERTIES INTERFACE_INCLUDE_DIRECTORIES "${_ci}")\n            endif()\n        endif()\n    endif()\n    return()|' cmake/FindCantor.cmake

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%K6build \
    -DQT_VERSION_MAJOR=6 \
    -DQT_FIND_PRIVATE_MODULES=ON \
    -DENABLE_READSTAT:BOOL=OFF \
    -DENABLE_VECTOR_BLF:BOOL=OFF \
    -DENABLE_REPRODUCIBLE:BOOL=ON \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS README.md LICENSES/* ChangeLog
%_K6bin/*
%_datadir/%{name}/
%_K6xdgapp/*
%_K6icon/hicolor/*/apps/*
%_K6xdgmime/%{name}.xml
%_datadir/metainfo/*.xml

%files -n liblabplot%soversion
%_libdir/liblabplot.so.%soversion

%files -n liblabplot-devel
%_includedir/labplot
%_libdir/cmake/labplot
%_K6link/liblabplot.so

%changelog
* Wed Mar 18 2026 Sergey V Turchin <zerg@altlinux.org> 2.12.1-alt3
- fix requires (closes: 58267)

* Wed Feb 18 2026 Anton Farygin <rider@altlinux.org> 2.12.1-alt2
- fixed build with qt6 >= 6.10 (Qt6GuiPrivate no longer auto-loaded,
  missing QElapsedTimer include)
- fixed build with eigen3 >= 5.0 (cmake variable name change)
- enabled optional features: cantor, cfitsio, matio, discount,
  orcus (ODS import), zstd (MCAP compression)
- excluded %%ix86 because it's unusable

* Tue Sep 09 2025 Anton Farygin <rider@altlinux.com> 2.12.1-alt1
- 2.12.0 -> 2.12.1

* Sat May 03 2025 Anton Farygin <rider@altlinux.com> 2.12.0-alt1
- 2.11.1 -> 2.12.0
- built devel and shared libs packages

* Wed Feb 12 2025 Anton Farygin <rider@altlinux.ru> 2.11.1-alt1
- 2.10.1 -> 2.11.1
- built for QT/KDE6 with support fo vulkan, fftw3, cerf, poopler, lz4 and eigen3

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 2.10.1-alt1
- new veresion

* Tue Jul 04 2023 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt1
- new veresion

* Wed Jun 08 2022 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt1
- new veresion

* Thu Apr 28 2022 Sergey V Turchin <zerg@altlinux.org> 2.8.2-alt2
- Move to standart place

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.2-alt1
- Updated to upstream version 2.8.2.

* Mon Apr 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.0-alt1
- Updated to upstream version 2.7.0.

* Thu Jul 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Updated to upstream version 2.6.0.

* Thu May 23 2019 Michael Shigorin <mike@altlinux.org> 2.5.0-alt3
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Mon Oct 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt2
- Updated runtime dependencies.

* Wed Aug 29 2018 Pavel Moseev <mars@altlinux.org> 2.5.0-alt1
- Updated to upstream version 2.5.0.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.0-alt1
- Updated to upstream version 2.4.0.
- Rebuilt with qt5 and kde5.
- Cleaned up spec.

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.svn20140201
- Version 2.0.1

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.beta1.svn20131107
- Version 2.0.0.beta1

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt7.svn20090921
- Rebuilt with new libhdf5

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.svn20090921
- Rebuilt with libhdf5-7-seq 1.8.8-alt2

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt5.svn20090921
- Fixed build

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.8
- Rebuilt with libhdf5-7

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.7
- Rebuilt with libnetcdf7

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.6
- Rebuilt for debuginfo

* Mon Feb 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.5
- Fixed build

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.4
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.3
- Built without system liborigin

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.2
- Rebuilt with Qt 4.7

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.1
- Rebuilt with gsl 1.13-alt1

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921
- New snapshot
- Added SciDAvis (experimental Qt frontend)

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- rebuild with libnetcdf-4.0.1

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version (2.0.0)
- build with libnetcdf-4.0

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0.2-alt1
- new version (1.6.0.2)

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt0.4
- new version

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- release

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt0.1pre2.1
- Rebuilt with libtiff.so.4.

* Sat Jul 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1pre2
- new version
- add russian translation

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus

