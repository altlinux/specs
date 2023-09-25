%define _name eyedropper

%def_enable snapshot
%define ver_major 0.6
%define rdn_name com.github.finefindus.%_name

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: GNOME Eyedropper
License: GPL-3.0
Group: Graphics
Url: https://apps.gnome.org/Eyedropper

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/FineFindus/eyedropper.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: blueprint-compiler gir(Adw)

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
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
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
#%_datadir/dbus-1/services/%rdn_name.service
#%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc CHANGELOG* README*

%changelog
* Mon Sep 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus


