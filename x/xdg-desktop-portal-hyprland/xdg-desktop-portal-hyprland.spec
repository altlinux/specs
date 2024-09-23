%def_enable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 1.3

%def_enable check

Name: xdg-desktop-portal-hyprland
Version: %ver_major.5
Release: alt1

Summary: xdg-desktop-portal backend for Hyprland
Group: Graphical desktop/Other
License: BSD-3-Clause
Url: https://github.com/hyprwm/xdg-desktop-portal-hyprland

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/hyprwm/xdg-desktop-portal-hyprland.git
Source: %name-%version.tar
%endif

ExcludeArch: %ix86 armh

Requires: xdg-desktop-portal
Requires: qt6-wayland

BuildRequires(pre): rpm-macros-cmake rpm-build-systemd
BuildRequires: cmake gcc-c++ ctest
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(hyprland-protocols)
BuildRequires: hyprwayland-scanner >= 0.4.2
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(libpipewire-0.3) >= 1.2
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(sdbus-c++)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: qt6-tools pkgconfig(Qt6Widgets)

%description
XDG Desktop Portal implementation for Hyprland.

%prep
%setup -n %name-%version

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang %name

%check
%ctest

%files -f %name.lang
%_bindir/hyprland-share-picker
%_libexecdir/%name
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%_datadir/xdg-desktop-portal/portals/hyprland.portal
%_userunitdir/%name.service
%doc README*


%changelog
* Mon Sep 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- v1.3.5-1-g4adb6c4

* Mon Jul 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Fri Jul 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- updated to v1.3.2-2-gc5b3093

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue Dec 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Tue Nov 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Sat Nov 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Oct 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- first build for Sisyphus


