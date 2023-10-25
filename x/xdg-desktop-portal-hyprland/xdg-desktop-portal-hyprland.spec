%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 1.2

%def_enable check

Name: xdg-desktop-portal-hyprland
Version: %ver_major.3
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

Requires: qt6-wayland

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(hyprland-protocols)
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.62
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
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/hyprland-share-picker
%_libexecdir/%name
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%_datadir/xdg-desktop-portal/portals/hyprland.portal
%_userunitdir/%name.service
%doc README*


%changelog
* Wed Oct 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- first build for Sisyphus


