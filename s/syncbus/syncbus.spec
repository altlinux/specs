%define _libexecdir %_prefix/libexec

%define ver_major 0.1
%define rdn_name mobi.phosh.syncbus

%def_disable demo
%def_enable check
%def_disable bootstrap

Name: syncbus
Version: %ver_major.0
Release: alt1

Summary: A D-Bus server for Syncthing
Group: Networking/Other
License: GPL-3.0-only
Url: https://gitlab.gnome.org/World/Phosh/syncbus

Vcs: https://gitlab.gnome.org/World/Phosh/syncbus.git

Source: %name-%version.tar
Source1: %name-%version-cargo.tar

%define adw_ver 1.8
%define systemd_ver 232

Requires: syncthing >= 2.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(systemd) >= %systemd_ver
%{?_enable_demo:BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver}

%description
Syncbus is a D-Bus server for [Syncthing](https://syncthing.net/).
It exposes few functionalities of Syncthing through D-Bus properties and
methods.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    %{subst_enable_meson_bool demo demo}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libexecdir/phosh-%name
%_userunitdir/phosh-%name.service
%_datadir/dbus-1/interfaces/%rdn_name.Folder.xml
%_datadir/dbus-1/interfaces/%rdn_name.Manager.xml
%_datadir/dbus-1/services/%rdn_name.service
%doc README* NEWS

%{?_enable_demo:
%files demo
%_libexecdir/phosh-%name-demo}

%changelog
* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus


