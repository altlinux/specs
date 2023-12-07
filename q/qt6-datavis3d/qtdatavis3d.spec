%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtdatavis3d

Name: qt6-datavis3d
Version: 6.1.1
Release: alt1

Group: System/Libraries
Summary: Qt6 - Data Visualization component
Url: http://www.qt.io/
License: GPL-3.0-only with Qt-GPL-exception-1.0

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-base-devel
BuildRequires: qt6-declarative-devel qt6-multimedia-devel

%description
Qt Data Visualization module provides multiple graph types to visualize data in 3D space
both with C++ and Qt Quick 2.

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

%package -n libqt6-datavisualization
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-datavisualization
%summary.

%package -n libqt6-datavisualizationqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-datavisualizationqml
%summary.

%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-qt6 -version %version

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
%_qt6_qmldir/QtDataVisualization/

%files -n libqt6-datavisualization
%_qt6_libdir/libQt?DataVisualization.so.*
%files -n libqt6-datavisualizationqml
%_qt6_libdir/libQt?DataVisualizationQml.so.*

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_libdir/pkgconfig/Qt*.pc
%_qt6_archdatadir/mkspecs/modules/*.pri
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build
