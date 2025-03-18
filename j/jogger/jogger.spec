%def_enable snapshot

%define _name jogger
%define __name Jogger
%define ver_major 1.3
%define rdn_name xyz.slothlife.%__name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: An app for Gnome Mobile to Track running and other workouts
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://codeberg.org/baarkerlounger/jogger.git

Vcs: https://codeberg.org/baarkerlounger/jogger.git

%if_disabled snapshot
Source: https://codeberg.org/baarkerlounger/jogger/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.14
%define adwaita_ver 1.5

Requires: dconf geoclue2 espeak-ng

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: gir(Adw) = 1
BuildRequires: pkgconfig(shumate-1.0) gir(Shumate) = 1.0
BuildRequires: pkgconfig(sqlite3)
BuildRequires: clang-devel
BuildRequires: libalsa-devel pkgconfig(espeak-ng)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils espeak-ng clippy}

%description
Track and view your runs, walks, cycles, swims, and other workouts on
mobile Linux.


%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
# required for "ring"
%define optflags_lto %nil

%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %__name

%check
%__meson_test -t 2

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Tue Mar 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat Jan 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- first build for Sisyphus (1.2.8-2-ga4cad10)


