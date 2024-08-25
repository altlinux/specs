%define _name Iconic
%define binary_name folder_icon
%define ver_major 2024.8
%define rdn_name nl.emphisia.icon

%def_enable check
%def_disable bootstrap

Name: iconic
Version: %ver_major.1
Release: alt1

Summary: Easilly add icons on top of folders
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/youpie/Iconic

Vcs: https://github.com/youpie/Iconic.git

Source: %name-%version.tar
Source1: %name-%version-cargo.tar

Requires: dconf
Requires: icon-theme-adwaita

%define adw_ver 1.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libxml-2.0)
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
An application made for GNOME written in Rust to easilly add images on
top of folders.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
cat << _EOF_ > \
%buildroot%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
[%rdn_name]
folder-svg-path='%_iconsdir/Adwaita/scalable/places/folder.svg'
_EOF_


%find_lang --output=%name.lang %binary_name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%binary_name
%_datadir/%binary_name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.8.1-alt1
- first build for Sisyphus (v2024.8.1-4-gb103890)


