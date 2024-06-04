%def_enable snapshot

%define optflags_lto %nil

%define _name paleta
%define ver_major 0.3
%define rdn_name io.github.nate_xyz.Paleta

%def_disable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Color palettes generator for GNOME
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/nate-xyz/paleta

Vcs: https://github.com/nate-xyz/paleta.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adwaita_ver 1.2

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

BuildRequires: pkgconfig(sqlite3)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Find the dominant color palette from any image and manage palettes with
Paleta. 
Paleta is An intuitive tool for designers, artists, or anyone looking to
streamline their color work.

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
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- first build for Sisyphus (v0.3.1-25-gf9d3dc9)


