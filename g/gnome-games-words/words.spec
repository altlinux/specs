%def_enable snapshot

%define _name words
%define ver_major 0.1
%define rdn_name page.codeberg.petsoi.%_name

%def_enable check
%def_disable bootstrap

# conflicts with words-2-alt1
Name: gnome-games-%_name
Version: %ver_major.5
Release: alt1

Summary: Words!
License: GPL-3.0-or-later
Group: Games/Boards
Url: https://codeberg.org/petsoi/words

Vcs: https://codeberg.org/petsoi/words.git

%if_disabled snapshot
Source: https://codeberg.org/petsoi/words/archive/v%version/%name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define glib_ver 2.76
%define adwaita_ver 1.6

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Words! is similar to a popular word puzzle game where players try to
guess a hidden word within six attempts. It's simple yet addictive,
combining logic, vocabulary, and deduction. 

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    -Dprofile=default
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Sat Jan 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus (v0.1.5-4-g03fcc07)


