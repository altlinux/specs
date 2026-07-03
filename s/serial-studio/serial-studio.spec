%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: serial-studio
Version: 4.0.2
Release: alt1

Summary: Cross-platform telemetry visualization application for real-time data monitoring and analysis from multiple sources
License: GPL-3.0-only
Group: Engineering
Url: https://github.com/Serial-Studio/Serial-Studio

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(mimalloc)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Graphs)
BuildRequires: pkgconfig(Qt6Bluetooth)
BuildRequires: pkgconfig(Qt6SerialPort)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6WebEngineQuick)

Requires: libqt6-core5compat
Requires: libqt6-qmlcore
Requires: libqtgraphs-qt6
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quickeffects
Requires: libqt6-quicklayouts
Requires: libqt6-quickshapes
Requires: libqt6-qml
Requires: libqt6-webenginequick

# no libqt6-webenginequick
ExcludeArch: %ix86 riscv64

%description
Serial Studio is an open-source tool that helps you see data from Arduino,
ESP32, Raspberry Pi, and other devices in real-time. It works with serial
ports (UART), Bluetooth Low Energy (BLE), MQTT, Modbus TCP/RTU, CAN Bus,
TCP/UDP networks, and audio devices. You can create dashboards to monitor
sensors and debug hardware without writing code.

%prep
%setup
%patch -p1
sed -i "s|doc/screenshot.png|screenshot.png|" README.md
sed -i "s|./doc/brand/||" README.md
sed -i "s|share/pixmaps|%_iconsdir/hicolor/scalable/apps|" app/CMakeLists.txt

sed -i "s|set(SS_MIMALLOC_PLATFORM TRUE)|set(SS_MIMALLOC_PLATFORM FALSE) # HACK|" cmake/MiMalloc.cmake

%build
%cmake \
       -DUSE_SYSTEM_ZLIB=ON \
       -DUSE_SYSTEM_EXPAT=ON \
       -DPRODUCTION_OPTIMIZATION=ON
%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%files -f %{name}.lang
%doc LICENSE.md README.md doc/brand/logo.svg doc/screenshot.png
%doc LICENSES CLAUDE.md examples
%_bindir/serial-studio-gpl3
%_desktopdir/serial-studio-gpl3.desktop
%_datadir/metainfo/serial-studio.metainfo.xml
%_datadir/mime/packages/serial-studio-ssproj.xml
%_iconsdir/hicolor/scalable/apps/serial-studio-gpl3.svg

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Fri Jun 19 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.1-alt1
- New version 4.0.1.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.0-alt1
- New version 4.0.0.

* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.7-alt1
- New version 3.2.7.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.6-alt1
- New version 3.2.6.

* Mon Feb 23 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.4-alt1
- Initial build for Sisyphus
