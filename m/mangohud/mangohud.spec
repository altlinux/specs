%define uname   MangoHud
%define srcname %uname-v%version-Source
%define srcpath %uname-v%version

Name: mangohud
Version: 0.7.0
Release: alt1

Summary: A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more
License: MIT
Group: Games/Arcade

Url: https://github.com/flightlessmango/%uname
Source: https://github.com/flightlessmango/%uname/releases/download/v%version/%srcname.tar.xz

Patch0: %name-python3.patch

BuildRequires: appstream
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: glslang
BuildRequires: libGLEW-devel
BuildRequires: libXrandr-devel
BuildRequires: libdbus-devel
BuildRequires: libglfw3-devel
BuildRequires: libspdlog-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libwayland-client-devel
BuildRequires: meson
BuildRequires: nlohmann-json-devel
BuildRequires: nvidia-settings-devel
BuildRequires: python3-dev
BuildRequires: python3-module-mako

%description
A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more.

To enable the MangoHud Vulkan overlay layer, set `MANGOHUD=1` in the shell,
or use the `mangohud` command to launch programs.
See '%_docdir/%name' for configuration details.
%ifarch %ix86 x86_64

The `goverlay` package provides a third-party GUI frontend for MangoHud.
%endif

%package -n mangoapp
Summary: A transparent background application with a built-in %uname for gamescope
Group: Games/Arcade
Requires: %name

%description -n mangoapp
A transparent background OpenGL application with a built-in %uname designed to be run inside a gamescope instance.

%prep
%setup -n %srcpath
%patch0 -p1

%build
%meson \
  -Duse_system_spdlog=enabled \
  -Dwith_wayland=enabled \
  -Dmangoapp=true \
  -Dmangohudctl=true \
  -Dmangoapp_layer=true

%meson_build

%install
%meson_install

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_bindir/%{name}ctl
%_bindir/mangoplot
%_libdir/%name/
%_man1dir/%name.1*
%_datadir/icons/hicolor/scalable/*/*.svg
%_datadir/vulkan/implicit_layer.d/*Mango*.json
%_docdir/%name/%uname.conf.example
%_datadir/metainfo/*.metainfo.xml

%files -n mangoapp
%_bindir/mangoapp
%_man1dir/mangoapp.1*

%changelog
* Wed Sep 27 2023 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Jul 07 2023 Nazarov Denis <nenderus@altlinux.org> 0.6.9-alt1
- 0.6.9-1

* Wed Aug 03 2022 Ilya Mashkin <oddity@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Wed Oct 27 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.6-alt2
- 0.6.6-1

* Wed Oct 20 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sat Aug 28 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Wed Apr 21 2021 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- initial build for ALT Sisyphus (thx Mageia)

* Wed Dec 30 2020 akien <akien> 0.6.1-1.mga8
+ Revision: 1665672
- Version 0.6.1

* Fri Oct 23 2020 akien <akien> 0.5.1-1.mga8
+ Revision: 1638865
- Version 0.5.1
- Require vulkan-loader lib explicitly

* Thu Jun 11 2020 akien <akien> 0.4.1-1.mga8
+ Revision: 1592504
- Version 0.4.1

* Fri Feb 14 2020 akien <akien> 0.2.0-1.mga8
+ Revision: 1519991
- imported package mangohud

