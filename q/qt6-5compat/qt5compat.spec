%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qt5compat

Name: qt6-5compat
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Qt5 compatibility layer
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): qt6-tools
BuildRequires: cmake glibc-devel libxkbcommon-x11-devel libicu-devel
BuildRequires: qt6-base-devel  qt6-shadertools-devel qt6-declarative qt6-declarative-devel

%description
Porting support from Qt5 to Qt6.

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

%package -n libqt6-core5compat
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-core5compat
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
%_qt6_archdatadir/qml/Qt5Compat/

%files -n libqt6-core5compat
%_qt6_libdir/libQt?Core5Compat.so.*

%files devel
%_qt6_headerdir/QtCore5Compat/
%_qt6_libdir/lib*.so
%_qt6_libdatadir/lib*.so
%_qt6_libdir/lib*.prl
%_qt6_libdatadir/lib*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pri
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

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Mon Apr 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- initial build
