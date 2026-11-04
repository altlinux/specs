%def_enable snapshot

%define ver_major 1.7
%define git_commit 3d400164bcfb2616873be65e298df2df184a8971
%define _name waycheck
%define __name Waycheck
%define rdn_name dev.serebit.%__name

Name: %_name
Version: %ver_major.0
Release: alt2

Summary: Display information for Wayland compositors
License: Apache-2.0
Group: System/X11
Url: https://gitlab.freedesktop.org/serebit/waycheck

Vcs: https://gitlab.freedesktop.org/serebit/waycheck.git

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/serebit/waycheck/-/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

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
%setup -n %_name-%{?_disable_snapshot:v%version-%git_commit}%{?_enable_snapshot:%version}

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
* Wed Nov 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt2
- updated to v1.7.0-8-gd3147c0

* Sat Jun 28 2025 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Feb 19 2025 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- first build for Sisyphus

