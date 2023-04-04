%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtpositioning

Name: qt6-positioning
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtPositioning component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel qt6-declarative-devel qt6-serialport-devel
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: libicu-devel zlib-devel libssl-devel
BuildRequires: libxkbcommon-devel

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

%package -n libqt6-positioningquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
#Requires: qt6-quickcontrols
%description -n libqt6-positioningquick
%summary

%package -n libqt6-positioning
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
#Requires: qt6-quickcontrols
%description -n libqt6-positioning
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%ifarch e2k
sed -i 's|-ftree-vectorize||' src/3rdparty/*/*.pro
%endif

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

%files -n libqt6-positioning
%_qt6_libdir/libQt?Positioning.so.*
%_qt6_qmldir/QtPositioning/
%_qt6_plugindir/position/

%files -n libqt6-positioningquick
%_qt6_libdir/libQt?PositioningQuick.so.*

%files devel
%_qt6_headerdir/QtPositioning/
%_qt6_headerdir/QtPositioningQuick/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
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

* Tue Jun 07 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
