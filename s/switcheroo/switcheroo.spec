%def_enable snapshot
%define _name Switcheroo
%define ver_major 2.0
%define xdg_name io.gitlab.adhami3310.Converter

%def_disable bootstrap

Name: switcheroo
Version: %ver_major.1
Release: alt1

Summary: Simple App to Convert Photo Images
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Converter

Vcs: https://apps.gnome.org/Converter.git
Source: %name-%version.tar
Source1: %name-%version-cargo.tar

%define gtk_ver 4.6
%define adwaita_ver 1.2.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1

%description
Convert between different image filetypes and resize them easily.

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

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_iconsdir/hicolor/*/actions/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- updated to v2.0.1-5-g698957d

* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus (v2.0.0-4-g2ac1c4c)



