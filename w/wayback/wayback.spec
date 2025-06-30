%define _name wayback
%define ver_major 0.1
%define rdn_name io.github.fizzyizzy05.%_name

%def_enable check

Name: %_name
Version: %ver_major
Release: alt0.1

Summary: A way to run X DE using Wayland components
License: MIT
Group: System/Servers
Url: https://github.com/kaniini/wayback.git

Vcs: https://github.com/kaniini/wayback.git

Source: %name-%version.tar

%define wl_proto_ver 1.14
%define wlr_api_ver 0.19

Requires: xorg-xwayland

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= %wl_proto_ver
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wlroots-%wlr_api_ver)

#%{?_enable_check:BuildRequires:}

%description
Wayback is an experimental X compatibility layer which allows for
running full X desktop environments using Wayland components. It is
essentially a stub compositor which provides just enough Wayland
capabilities to host a rootful Xwayland server.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%doc README.*

%changelog
* Mon Jun 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.1
- first build for Sisyphus (3507471)
