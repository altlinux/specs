%define _name textpieces
%define ver_major 4.0
%define rdn_name io.gitlab.liferooter.TextPieces

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.6
Release: alt1

Summary: Developer's scratchpad
License: GPL-3.0-or-later
Group: Text tools
Url: https://apps.gnome.org/Textpieces

Vcs: https://gitlab.com/liferooter/textpieces.git
Source: %name-%version.tar
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5) gir(GtkSource) = 5
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Powerful scratchpad with ability to perform a lot of text transformations, such as:

Calculate hashes
Encode text
Decode text
Remove trailing spaces and lines
Count lines, symbols and words
Format JSON and XML
Escape and unescape strings
Convert JSON to YAML and vice versa
Filter lines
Replace substrings and regular expressions
...and so on.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

sed -i 's|nonet|no-net|' data/meson.build

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
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README.*

%changelog
* Wed Jun 05 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0.6-alt1
- v4.0.6-8-g5acecd7 (ported to rust)

* Tue Apr 30 2024 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- prepared for Sisyphus

* Sun Apr 28 2024 Semen Fomchenkov <armatik@altlinux.org> 3.4.1-alt1
- First Build
