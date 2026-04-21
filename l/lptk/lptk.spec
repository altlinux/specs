%define optflags_lto %nil
%def_enable snapshot

%define _name lptk
# since 0.10 0 renamed as rotor
%define __name rotor
%define ver_major 0.11
%define rdn_name me.ogarcia.%__name
%def_enable check

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Stateless password manager
License: GPL-3.0-only
Group: Graphical desktop/GNOME
Url: https://gitlab.com/ogarcia/lptk

Vcs: https://gitlab.com/ogarcia/lptk.git

%if_disabled snapshot
Source: https://gitlab.com/ogarcia/lptk/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adw_ver 1.8

Provides: %__name = %EVR
Provides: %rdn_name = %EVR

BuildRequires(pre): rpm-macros-meson rpm-macros-rust
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(openssl)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Generate unique passwords for websites, email accounts or anything you
can think of based only on a master password and information you already
know.

By default this is a completely offline tool that does not store any
information and is based on the principle of "same input, same output"
so by simply entering the same parameters you will always get the same
password. It's that simple!

But you also have the possibility, if you want, to connect to a server
(e.g. Rockpass) so that you don't have to remember the options entered.
It's magic!

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%__name
%_desktopdir/%rdn_name.desktop
%_datadir/%__name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Apr 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Fri Jan 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Thu Nov 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0-2-g7255f61

* Tue Oct 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sun Aug 17 2025 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- updated to 0.7.0-2-g1c5f677

* Sun Jun 29 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Mar 19 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

