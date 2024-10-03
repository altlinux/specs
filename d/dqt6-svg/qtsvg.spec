%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module dqtsvg

Name: dqt6-svg
Version: 6.7.2
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - Support for rendering and displaying SVG
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar

# find librares
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools rpm-build-ninja
BuildRequires: dqt6-base-devel
BuildRequires: gcc-c++ glibc-devel
BuildRequires: cmake libxkbcommon-devel zlib-devel

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libdqt6-svg
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libdqt6-svg
%summary

%package -n libdqt6-svgwidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-svgwidgets
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%DQ6build -DCMAKE_MAKE_PROGRAM=ninja
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
mkdir -p %buildroot%_dqt6_docdir
cp -a BUILD/share/doc/dqt6/* %buildroot%_dqt6_docdir ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files -n libdqt6-svg
%doc *LICENSE*
%_dqt6_libdir/libQt?Svg.so.*
%_dqt6_plugindir/iconengines/libqsvgicon.so
%_dqt6_plugindir/imageformats/libqsvg.so
%files -n libdqt6-svgwidgets
%_dqt6_libdir/libQt?SvgWidgets.so.*

%files devel
%_dqt6_headerdir/QtSvg/
%_dqt6_headerdir/QtSvgWidgets/
%_dqt6_libdir/lib*.so
%_dqt6_libdir/lib*.prl
%_dqt6_libdatadir/lib*.so
%_dqt6_libdatadir/lib*.prl
%_dqt6_libdir/cmake/Qt?Svg/
%_dqt6_libdir/cmake/Qt?SvgWidgets/
%_dqt6_libdir/cmake/Qt?Gui/*Svg*.cmake
%_dqt6_libdir/cmake/Qt?BuildInternals/StandaloneTests/*Svg*.cmake
%_dqt6_archdatadir/mkspecs/modules/qt_lib_svg*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
#%_dqt6_examplesdir/*

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Fri Jan 12 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt3
- build docs verbose

* Wed Dec 06 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt2
- fix provides (closes: 47318)

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Fri Nov 17 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt2
- add upstream fixes

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build
