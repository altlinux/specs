Name:    hidviz
Version: 0.2.1
Release: alt1

Summary: A tool for in-depth analysis of USB HID devices communication
License: GPL-3.0-only
Group:   System/Configuration/Hardware
Url:     https://github.com/hidviz/hidviz

Source: %name-%version.tar
Patch0: %name-%version-asio.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel libprotobuf-devel git-core asio-devel libusb-devel

%description
Hidviz is a GUI application for in-depth analysis of USB HID class devices.
The 2 main usecases of this application are reverse-engineering existing
devices and developing new USB HID devices.

USB HID class consists of many possible devices, e.g. mice, keyboards,
joysticks and gamepads. But that's not all! There are more exotic HID devices,
e.g. weather stations, medical equipment (thermometers, blood pressure monitors)
or even simulation devices (think of flight sticks!).

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/hidviz
%_prefix/libexec/libhidx_server_daemon
%_desktopdir/hidviz.desktop
%_iconsdir/hicolor/128x128/apps/hidviz.png

%changelog
* Thu Jun 25 2026 Sergey Palcheh <minergenon@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus
