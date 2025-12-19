%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: watchflower
Version: 5.4
Release: alt1

Summary: plant monitoring application that reads and plots data from compatible Bluetooth sensors
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/emericg/WatchFlower

Source: %name-%version.tar

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Bluetooth)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Sql)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Charts)
BuildRequires: qt6-tools

Requires: libqt6-chartsqml
Requires: libqt6-core5compat

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
- Name your plants and set your own limits for optimal care
- Plant database with over 3400 plants
- Background updates and notifications (excluding iOS)
- Synchronize sensors history (FlowerCare, RoPot and ThermoBeacon
  ONLY for now)
- Configurable update intervals
- Clickable two-week graphs
- Monthly/weekly/daily data histograms
- 90 days CSV data export
- Scalable UI: 4.6" to 34" screens, landscape or portrait

%prep
%setup
sed -i "s/Categories=.*/Categories=Network;Monitor;Qt;/" assets/linux/watchflower.desktop
sed -i "s|assets/android/res/drawable-xxxhdpi/||" README.md
sed -i "s|\`assets/android/gradle.properties\`|[gradle.properties](gradle.properties)|" README.md
sed -i "s|assets/COPYING|COPYING|g" README.md

%build
lrelease-qt6 WatchFlower.pro
qmake-qt6 \
          -config release \
          PREFIX=%_prefix

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc LICENSE README.md docs
%doc assets/android/res/drawable-xxxhdpi/splashicon.png assets/android/gradle.properties assets/COPYING
%_bindir/watchflower
%_datadir/appdata/watchflower.appdata.xml
%_desktopdir/watchflower.desktop
%_iconsdir/hicolor/scalable/apps/watchflower.svg
%_pixmapsdir/watchflower.svg

%changelog
* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 5.4-alt1
- Initial build for Sisyphus
