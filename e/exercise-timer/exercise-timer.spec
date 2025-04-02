%def_enable snapshot

%define _name exercise-timer
%define __name hiit
%define ver_major 1.8
%define beta %nil
%define rdn_name xyz.safeworlds.%__name

%def_disable bootstrap
%def_enable check

Name: %_name
Version: %ver_major.1
Release: alt1%beta

Summary: Exercise Timer
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/ru/Hiit

Vcs: https://github.com/mfep/exercise-timer.git

%if_disabled snapshot
Source: https://github.com/mfep/exercise-timer/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.14
%define adwaita_ver 1.4

Provides: %__name = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(alsa)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Exercise Timer is a simple utility to conduct interval training. It is
built for the GNOME desktop using Libadwaita Relm4 (https://relm4.org/).

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    -Dprofile=default
%nil
%meson_build

%install
%meson_install
%find_lang %__name

%check
%__meson_test

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* CHANGELOG*


%changelog
* Wed Apr 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- first build for Sisyphus (v1.8.1-23-gefa1c7a)



