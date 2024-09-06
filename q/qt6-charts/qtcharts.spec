%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtcharts

Name: qt6-charts
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Charts component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-declarative-devel

%description
Qt Charts module provides a set of easy to use chart components. It uses
the Qt Graphics View Framework, therefore charts can be easily integrated
to modern user interfaces.

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

%package -n libqt6-charts
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-charts
%summary

%package -n libqt6-chartsqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libqt6-chartsqml
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

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files -n libqt6-charts
%_qt6_libdir/libQt?Charts.so.*

%files -n libqt6-chartsqml
%_qt6_libdir/libQ?6ChartsQml.so.*
%_qt6_qmldir/QtCharts/

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdatadir/libQt*.so
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_archdatadir/metatypes/qt6*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Mon Jul 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- relax depends on plugins files

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed Jun 08 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
