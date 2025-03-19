%def_disable snapshot

%define _name lptk
%define ver_major 0.5
%define rdn_name me.ogarcia.%_name

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Stateless password manager
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.com/ogarcia/lptk

Vcs: https://gitlab.com/ogarcia/lptk.git

%if_disabled snapshot
Source: https://gitlab.com/ogarcia/lptk/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-macros-meson rpm-macros-rust
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1)
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
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed Mar 19 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

