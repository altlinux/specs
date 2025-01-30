%define ver_major 1.5
%define git_commit c41915bbbf9c5716c62f975ba379a968fa386ae2
%define _name waycheck
%define __name Waycheck
%define rdn_name dev.serebit.%__name

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Display information for Wayland compositors
License: Apache-2.0
Group: System/X11
Url: https://gitlab.freedesktop.org/serebit/waycheck

Vcs: https://gitlab.freedesktop.org/serebit/waycheck.git

Source: https://gitlab.freedesktop.org/serebit/waycheck/-/archive/v%version/%_name-%version.tar.gz

%define wayland_ver 1.17

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(wayland-client)
BuildRequires: qt6-base-devel qt6-tools
BuildRequires: pkgconfig(Qt6WaylandClient)

%description
Waycheck is a simple Qt6 application that displays all of the Wayland
protocols that your compositor supports, and all of the protocols that
it doesn't support.

It can be used to compare protocol support between compositors, or if
you're working on your own compositor, to keep track of which protocols
you still need to implement.

%prep
%setup -n %_name-v%version-%git_commit

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%doc README.md

%changelog
* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- first build for Sisyphus

