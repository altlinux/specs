%def_enable snapshot

%define _name blurble
%define __name Blurble
%define ver_major 0.4
%define rdn_name app.drey.%__name

# online screenshots
%def_disable check

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: Word guessing game
License: GPL-3.0-or-later
Group: Games/Boards
Url: https://gitlab.gnome.org/World/Blurble

Vcs: https://gitlab.gnome.org/World/Blurble.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Blurble/-/archive/v%version/%_name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif

%define glib_ver 2.76
%define adwaita_ver 1.6

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Solve the riddle until you run out of guesses!
The game is a clone of Wordle and made with localization in mind.

%prep
%setup -n %__name-%version

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
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Fri May 02 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus (v0.4.0-37-g1a0c47a)


