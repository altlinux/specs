%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtmqtt

Name: qt6-mqtt
Version: 6.10.3
Release: alt1

Group: System/Libraries
Summary: Qt6 - MQTT protocol module
Url: http://qt.io/
VCS: https://github.com/qt/qtmqtt
License: GPL-3.0-only

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake glibc-devel qt6-base-devel qt6-tools-devel

%description
Qt MQTT provides an implementation of the MQTT protocol. It enables
applications to act as telemetry displays and devices to publish telemetry
data. The module supports MQTT protocol versions 3.1, 3.1.1, and 5.0.

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

%package -n libqt6-mqtt
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-mqtt
%summary

%prep
%setup

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
mkdir -p %buildroot/%_docdir/qt6/
cp -ar BUILD/share/doc/qt6/* %buildroot/%_docdir/qt6/
%endif

%files common
%doc LICENSES/*

%files -n libqt6-mqtt
%_qt6_libdir/libQt?Mqtt.so.*

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
* Fri May 22 2026 Anton Farygin <rider@altlinux.org> 6.10.3-alt1
- 6.10.2 -> 6.10.3

* Wed Feb 18 2026 Anton Farygin <rider@altlinux.org> 6.10.2-alt1
- 6.10.1 -> 6.10.2

* Sat Feb 08 2026 Anton Farygin <rider@altlinux.org> 6.10.1-alt1
- initial build for ALT Linux
