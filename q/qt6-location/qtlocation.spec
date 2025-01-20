%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtlocation

Name: qt6-location
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtLocation component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake qt6-declarative-devel qt6-positioning-devel qt6-shadertools-devel qt6-tools

%description
The Qt Positioning API gives developers the ability to determine a position
by using a variety of possible sources, including satellite, or wifi, or
 text file, and so on. That information can then be used to for example
determine a position on a map. In addition satellite information can be
retrieved and area based monitoring can be performed.

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

%package -n libqt6-location
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-location
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

%files -n libqt6-location
%_qt6_libdir/libQt?Location.so.*
%_qt6_plugindir/geoservices/
%_qt6_qmldir/QtLocation/

%files devel
%_qt6_headerdir/QtLocation/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_libdir/pkgconfig/Qt*.pc
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json


%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- initial build
