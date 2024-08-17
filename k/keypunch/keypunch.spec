%define _name Keypunch
%define ver_major 3.1
%define rdn_name dev.bragefuglseth.%_name

%def_enable check
%def_disable bootstrap

Name: keypunch
Version: %ver_major
Release: alt1

Summary: Keypunch is a typing tutor
License: GPL-3.0-or-later
Group: Games/Educational
Url: https://github.com/bragefuglseth/keypunch

Vcs: https://github.com/bragefuglseth/keypunch.git
Source: %name-%version.tar
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Practice your typing skills with Keypunch.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
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
%_desktopdir/%{rdn_name}*.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README.*

%changelog
* Sat Aug 17 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Thu Jul 18 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- updated to v3.0-3-g6380e9e

* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- updated to v2.0-7-geb167e7

* Sat Jun 08 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus (v1.0-15-g959968c)
