%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# See https://github.com/rinigus/pure-maps/pull/595
%define revname io.github.rinigus.PureMaps

# Due to libs2geometry
ExcludeArch: armh ppc64le i586

Name: pure-maps
Version: 3.5.0
Release: alt1

Summary: Maps and navigation
License: GPL-3.0-or-later
Group: Sciences/Geosciences
URL: https://github.com/rinigus/pure-maps
VCS: https://github.com/rinigus/pure-maps.git

Requires: kf5-kirigami
Requires: libqt5-multimedia
Requires: libqt5-sensors
Requires: libqt5-quickcontrols2
Requires: geoclue2
Requires: nemo-qml-plugin-dbus
Requires: mapbox-gl-qml
Requires: pyotherside
# Debundled submodule
%py3_requires geomag

# The pyotherside is not a python module,
# to avoid python3(pyotherside) dependency
%add_python3_req_skip pyotherside

Source0: %name-%version.tar
Source1: pure-maps-16.png
Source2: pure-maps-32.png
Source3: pure-maps-48.png

Patch0: pure-maps-3.4.1-alt-debundle-flexpolyline.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libs2geometry-devel
BuildRequires: python3-module-setuptools
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-quickcontrols2-devel

%add_python3_path %_datadir/pure-maps

AutoProv: nopython3

%description
Pure Maps is an application for Sailfish OS and Linux to display
vector and raster maps, places, routes, and provide navigation
instructions with a flexible selection of data and service providers.

%prep
%setup
%patch0 -p1

%build
%cmake \
    -DUSE_BUNDLED_GEOMAG=OFF \
    -DUSE_BUNDLED_GPXPY=OFF \
    -DUSE_BUNDLED_FLEXPOLYLINE=OFF \
    -DFLAVOR=kirigami\
    %nil
%cmake_build

%install
%cmake_install
%find_lang --with-qt %name

install -pD -m644 %SOURCE1 %buildroot/%_miconsdir/%revname.png
install -pD -m644 %SOURCE2 %buildroot/%_niconsdir/%revname.png
install -pD -m644 %SOURCE3 %buildroot/%_liconsdir/%revname.png
# Remove icons with a strange resolution
rm -rf %buildroot/%_iconsdir/hicolor/86x86/
rm -rf %buildroot/%_iconsdir/hicolor/108x108/

%files -f %name.lang
%_bindir/pure-maps
%_desktopdir/*.desktop
%_datadir/pure-maps/geocoders/
%_datadir/pure-maps/guides/
%_datadir/pure-maps/maps/
%_datadir/pure-maps/poor/
%_datadir/pure-maps/qml/
%_datadir/pure-maps/routers/
%_datadir/metainfo/%revname.appdata.xml
%_iconsdir/hicolor/128x128/apps/%revname.png
%_iconsdir/hicolor/256x256/apps/%revname.png
%_miconsdir/%revname.png
%_niconsdir/%revname.png
%_liconsdir/%revname.png

%changelog
* Mon May 04 2026 Egor Shestakov <ved@altlinux.org> 3.5.0-alt1
- Add support for HERE v3 API maps.
- Update MapTiler maps (from 3.4.2).
- Fix Stadia API (from 3.4.2).

* Fri Oct 17 2025 Egor Shestakov <ved@altlinux.org> 3.4.1-alt1
- Initial build.
