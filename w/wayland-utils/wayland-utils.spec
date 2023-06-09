%define ver_major 1.2

Name: wayland-utils
Version: %ver_major.0
Release: alt1

Summary: Display information utility for Wayland
License: MIT
Group: System/X11
Url: https://wayland.freedesktop.org/

Vcs: https://gitlab.freedesktop.org/wayland/wayland-utils.git
Source: https://gitlab.freedesktop.org/wayland/wayland-utils/-/archive/%version/%name-%version.tar.gz

%define wayland_ver 1.17

BuildRequires(pre): meson
BuildRequires: libwayland-server-devel >= %wayland_ver
BuildRequires: libwayland-client-devel wayland-protocols libdrm-devel

%description
wayland-info is a utility for displaying information about the Wayland
protocols supported by a Wayland compositor.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/wayland-info
%_man1dir/wayland-info.1*
%doc README.md

%changelog
* Fri Jun 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0


* Sat Aug 1 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

