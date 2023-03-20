%define ver_major 44
%define beta %nil
%define xdg_name org.gnome.Tour
%def_enable check

Name: gnome-tour
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Tour and Greeter
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://gitlab.gnome.org/GNOME/gnome-tour

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

Requires: /etc/os-release

%define glib_ver 2.64
%define gtk4_ver 4.4
%define adwaita_ver 1.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: /proc meson rust rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: desktop-file-utils %_bindir/appstream-util}

%description
A guided tour and greeter for GNOME.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/gnome-tour
%_datadir/applications/%xdg_name.desktop
%_datadir/icons/hicolor/scalable/apps/%xdg_name.svg
%_datadir/icons/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/%name
%doc NEWS README.md

%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0 (ported to GTK4)

* Sun Sep 05 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.9.rc
- 41.rc

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- first build for Sisyphus


