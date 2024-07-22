%def_disable snapshot

%define _name Hieroglyphic
%define ver_major 1.1
%define rdn_name io.github.finefindus.%_name

%def_disable check
%def_disable bootstrap

Name: hieroglyphic
Version: %ver_major.0
Release: alt1

Summary: Find LaTeX symbols
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/FineFindus/Hieroglyphic

Vcs: https://github.com/FineFindus/Hieroglyphic.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define adw_ver 1.5

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
If you work with LaTeX, you know it's difficult to memorize the names of
all the symbols. Hieroglyphic allows you to search through over 1000
different LaTeX symbols by sketching.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

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
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Mon Jul 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus


