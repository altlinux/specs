%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: toolblex
Version: 0.17
Release: alt1

Summary: A multiplatform Bluetooth Low Energy (and Classic) device scanner and analyzer
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/emericg/toolBLEx

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Bluetooth)
BuildRequires: pkgconfig(Qt6Charts)
BuildRequires: pkgconfig(Qt6Graphs)
BuildRequires: qt6-tools-devel

Requires: bluez
Requires: libqt6-chartsqml
Requires: libqt6-quickcontrols2
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quickcontrols2fusion
Requires: libqt6-qmlcore
Requires: libqt6-quickcontrols2material
Requires: libqt6-quickeffects
Requires: libqt6-quicklayouts
Requires: libqt6-quickdialogs2

%description
A multiplatform Bluetooth Low Energy (and Classic) device scanner and analyzer.

Features:

- Bluetooth host adapters info
- RSSI graph / proximity graph (BLE and classic)
- Device scanner (BLE and classic)
- Device advertisement and services explorer (BLE)
- Read/write on device characteristics data (BLE)
- Export device info: advertisement packets, services and
  characteristics (with or without values)
- Frequency analyzer (ONLY if you have an Ubertooth One)

%prep
%setup
sed -i "s/Categories=.*/Categories=Network;Monitor;Qt;/" assets/linux/toolBLEx.desktop
sed -i "s|assets/gfx/||" README.md
sed -i "s|assets/COPYING|COPYING|g" README.md

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md assets/COPYING assets/gfx/banner.svg
%_bindir/toolBLEx
%_datadir/appdata/toolBLEx.appdata.xml
%_desktopdir/toolBLEx.desktop
%_iconsdir/hicolor/scalable/apps/toolBLEx.svg
%exclude %_datadir/licenses/toolBLEx/LICENSE.md
%_pixmapsdir/toolBLEx.svg

%changelog
* Tue Jun 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.17-alt1
- New version 0.17.

* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.16-alt1
- New version 0.16.

* Tue Feb 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.15-alt1
- New version 0.15.

* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 0.14.1-alt1
- Initial build for Sisyphus
