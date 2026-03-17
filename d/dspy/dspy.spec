%define ver_major 50
%define api_ver 1
%define _name d-spy
%define xdg_name org.gnome.dspy

%def_enable tests
%def_enable check

Name: dspy
Version: %ver_major.0
Release: alt1

Summary: A tool to discover and explore D-Bus services
Group: Development/Tools
License: GPL-3.0-or-later
Url: https://wiki.gnome.org/Apps/Builder

Vcs: https://gitlab.gnome.org/GNOME/d-spy.git

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Requires: dbus-tools-gui

%define glib_ver 2.80
%define gtk4_ver 4.16
%define libadwaita_ver 1.7
%define dex_ver 0.11

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %libadwaita_ver
BuildRequires: pkgconfig(libdex-1) >= %dex_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
D-Spy is a tool to explore and test end-points and interfaces on the
System or Session D-Bus. You can also connect to D-Bus peers by address.
D-Spy was originally part of GNOME Builder.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Tue Mar 17 2026 Yuri N. Sedunov <aris@altlinux.org> 50.0-alt1
- 50.0

* Wed Oct 29 2025 Yuri N. Sedunov <aris@altlinux.org> 49.2-alt1
- 49.2

* Wed Sep 17 2025 Yuri N. Sedunov <aris@altlinux.org> 49.1-alt1
- 49.1

* Sun Mar 16 2025 Yuri N. Sedunov <aris@altlinux.org> 48.0-alt1
- 48.0

* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Sat Mar 16 2024 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Jul 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- first build for Sisyphus


