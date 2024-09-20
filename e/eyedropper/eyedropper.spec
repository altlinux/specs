%def_disable snapshot

%define _name eyedropper
%define ver_major 2.0
%define rdn_name com.github.finefindus.%_name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: GNOME Eyedropper
License: GPL-3.0
Group: Graphics
Url: https://apps.gnome.org/Eyedropper

Vcs: https://github.com/FineFindus/eyedropper.git

%if_disabled snapshot
Source: https://github.com/FineFindus/eyedropper/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.14
%define adwaita_ver 1.6

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: blueprint-compiler gir(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
An application to pick and format colors.

Features:
- Pick a Color
- Enter a color in Hex-Format
- Parse RGB/RGBA/ARGB Hex-Colors
- View colors in formats
- Customize which formats appear as well as their order
- Generate a palette of different shades

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc CHANGELOG* README*

%changelog
* Fri Sep 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sun Oct 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- v1.0.0-5-g2c52ba0

* Mon Sep 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus


