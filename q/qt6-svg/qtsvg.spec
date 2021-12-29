%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtsvg

Name: qt6-svg
Version: 6.2.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Support for rendering and displaying SVG
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: qt6-base-devel
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
Requires: %name-common = %EVR
Requires: qt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-svg
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
Provides: %name = %EVR
%description -n libqt6-svg
%summary

%package -n libqt6-svgwidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
Provides: %name = %EVR
%description -n libqt6-svgwidgets
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif


%files common
%files
%doc *LICENSE*
%_qt6_plugindir/iconengines/libqsvgicon.so
%_qt6_plugindir/imageformats/libqsvg.so

%files -n libqt6-svg
%doc *LICENSE*
%_qt6_libdir/libQt?Svg.so.*
%files -n libqt6-svgwidgets
%_qt6_libdir/libQt?SvgWidgets.so.*

%files devel
%_qt6_headerdir/QtSvg/
%_qt6_headerdir/QtSvgWidgets/
%_qt6_libdir/lib*.so
%_qt6_libdir/lib*.prl
%_qt6_libdatadir/lib*.so
%_qt6_libdatadir/lib*.prl
%_qt6_libdir/cmake/Qt?Svg/
%_qt6_libdir/cmake/Qt?SvgWidgets/
%_qt6_libdir/cmake/Qt?Gui/*Svg*.cmake
%_qt6_libdir/cmake/Qt?BuildInternals/
%_qt6_libdir/cmake/Qt6BuildInternals/StandaloneTests/*Svg*.cmake
%_qt6_archdatadir/mkspecs/modules/qt_lib_svg*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build
