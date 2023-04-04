%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtnetworkauth

Name: qt6-networkauth
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt Network Authenticators
Url: http://qt.io/
License: GPL-3.0-only WITH Qt-GPL-exception-1.0

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel
BuildRequires: qt6-base-devel qt6-tools

%description
Qt Network Authenticators; QtOAuth in particular.

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
Requires: qt6-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-networkauth
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-networkauth
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

%files -n libqt6-networkauth
%_qt6_libdir/libQt?NetworkAuth.so.*
#%_qt6_plugindir/networkauth/
#%_qt6_qmldir/QtNetworkAuth/

%files devel
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_headerdir/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pr*
%_libdir/cmake/Qt*/
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
