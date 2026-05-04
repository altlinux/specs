Name: mapbox-gl-qml
Version: 3.2.1
Release: alt1

Summary: Mapbox GL Native QML plugin
License: LGPL-3.0-or-later
Group: Sciences/Geosciences
URL: https://github.com/rinigus/mapbox-gl-qml
VCS: https://github.com/rinigus/mapbox-gl-qml.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-svg-devel
BuildRequires: libmaplibre-native-qt-devel
BuildRequires: libcurl-devel

%description
QML plugin for Maplibre GL Native, Mapbox GL Native fork.

%prep
%setup

%build
%cmake \
    -DUSE_CURL_SSL=ON \
    %nil
%cmake_build

%install
%cmake_install

%files
%_qt5_qmldir/MapboxMap/

%changelog
* Wed Apr 29 2026 Egor Shestakov <ved@altlinux.org> 3.2.1-alt1
- New version.

* Wed Oct 15 2025 Egor Shestakov <ved@altlinux.org> 3.0.0-alt1
- Initial build.
