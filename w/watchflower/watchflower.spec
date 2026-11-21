%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: watchflower
Version: 6.0
Release: alt1

Summary: plant monitoring application that reads and plots data from compatible Bluetooth sensors
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/emericg/WatchFlower

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-qml6

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Graphs)
BuildRequires: pkgconfig(Qt6Bluetooth)
BuildRequires: pkgconfig(Qt6Positioning)
BuildRequires: qt6-tools-devel

Requires: libqt6-positioning

%description
A plant monitoring application for Bluetooth Low Energy sensors and
thermometers like Xiaomi 'Flower Care' or Parrot 'Flower Power'

WatchFlower is a plant monitoring application that reads and plots data
from compatible Bluetooth Low Energy sensors like Xiaomi "Flower Care"
and "Ropot" or Parrot "Flower Power" and "Parrot Pot", as well as many
thermometers and air quality sensors!

It works with international and Chinese Xiaomi devices, doesn't require
an account creation, your GPS location, nor any other personal data from
you!

Features:

- Support many different plant sensors and thermometers
- Support a couple of environmental and air quality sensors
- Plant database with over 3400 plants
- Name your plants and set your own limits for optimal care
- Background updates and notifications (excluding iOS)
- Synchronize sensors history (FlowerCare, RoPot and ThermoBeacon ONLY for now)
- Configurable update intervals
- Clickable 4/2/1 week graphs
- Monthly/weekly/daily data histograms
- 180 days CSV data export
- Scalable UI: 5" to 34" screens, landscape or portrait

%prep
%setup
sed -i "s/Categories=.*/Categories=Network;Monitor;Qt;/" platforms/linux/WatchFlower.desktop
sed -i "s|platforms/android/res/drawable-xxxhdpi/||" README.md

sed -i "s|assets/COPYING|COPYING|g" README.md

mv -v thirdparty/IconLibrary/COPYING thirdparty/IconLibrary-COPYING
sed -i "s|thirdparty/IconLibrary/COPYING|IconLibrary-COPYING|" README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md docs
%doc platforms/android/res/drawable-xxxhdpi/splashicon.png assets/COPYING thirdparty/IconLibrary-COPYING
%_bindir/WatchFlower
%_datadir/appdata/WatchFlower.appdata.xml
%_desktopdir/WatchFlower.desktop
%_iconsdir/hicolor/scalable/apps/WatchFlower.svg
%exclude %_datadir/licenses/WatchFlower/LICENSE.md
%_pixmapsdir/WatchFlower.svg

%changelog
* Sat Nov 21 2026 Nikolay Strelkov <snk@altlinux.org> 6.0-alt1
- New version 6.0.

* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 5.4-alt1
- Initial build for Sisyphus
