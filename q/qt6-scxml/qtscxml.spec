%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtscxml

Name: qt6-scxml
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - SCXML (state machine notation) compiler and related tools
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel qt6-base-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: libxkbcommon-devel

%description
SCXML (state machine notation) compiler and related tools.

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

%package -n libqt6-scxml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-scxml
%summary

%package -n libqt6-scxmlqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-scxmlqml
%summary

%package -n libqt6-statemachine
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-statemachine
%summary

%package -n libqt6-statemachineqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-statemachineqml
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
%doc LICENSES/*

%files
%_qt6_libexecdir/qscxmlc
%_qt6_plugindir/scxmldatamodel/
%_qt6_qmldir/QtQml/StateMachine/
%_qt6_qmldir/QtScxml/

%files -n libqt6-scxml
%_qt6_libdir/libQt?Scxml.so.*
%files -n libqt6-scxmlqml
%_qt6_libdir/libQt6ScxmlQml.so.*
%files -n libqt6-statemachine
%_qt6_libdir/libQt6StateMachine.so.*
%files -n libqt6-statemachineqml
%_qt6_libdir/libQt6StateMachineQml.so.*

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdatadir/libQt*.so
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_archdatadir/mkspecs/features/*scxml*.prf
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
#%_qt6_examplesdir/*

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed Jun 08 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
