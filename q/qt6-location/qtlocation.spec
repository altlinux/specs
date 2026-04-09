%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtlocation

Name: qt6-location
Version: 6.10.3
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtLocation component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake qt6-declarative-devel qt6-positioning-devel qt6-shadertools-devel qt6-tools

%description
The Qt Location module helps you create mapping solutions using data available
from popular location service providers, such as Open Street Map.

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

%package -n libqt6-location
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-location
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
%if %qdoc_found
%Q6make --target docs
%endif

%install
%Q6install_qt
%if %qdoc_found
#%make -C BUILD DESTDIR=%buildroot install_docs ||:
mkdir -p %buildroot/%_docdir/qt6/
cp -ar BUILD/share/doc/qt6/* %buildroot/%_docdir/qt6/
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
* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Thu Nov 27 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt2
- fix package description

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Thu Feb 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt2
- fix to build docs

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- initial build
