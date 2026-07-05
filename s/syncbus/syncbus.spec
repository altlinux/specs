%define _libexecdir %_prefix/libexec

%define _name syncbus
%define __name phosh-session-services
%define ver_major 0.2
%define rdn_name mobi.phosh.syncbus

%def_disable demo
%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Phosh Session Services
Group: Networking/Other
License: GPL-3.0-only
Url: https://gitlab.gnome.org/World/Phosh/syncbus

Vcs: https://gitlab.gnome.org/World/Phosh/syncbus.git

Source: %name-%version.tar
Source1: %name-%version-cargo.tar

%define adw_ver 1.8
%define systemd_ver 242

Provides: %__name = %EVR
Requires: syncthing >= 2.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo desktop-file-utils
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(systemd) >= %systemd_ver

%description
A set of services to run in Phosh's session.

Syncbus is a D-Bus server for [Syncthing](https://syncthing.net/).
It exposes few functionalities of Syncthing through D-Bus properties and
methods.

phosh-os-updater indicates when new OS updates are available. It uses
org.freedesktop.sysupdate1 for that.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
export GETTEXT_SYSTEM=1
%meson \
    %{subst_enable_meson_bool demo demo}
%nil
%meson_build

%install
export GETTEXT_SYSTEM=1
%meson_install
%find_lang %__name

%check
export GETTEXT_SYSTEM=1
%__meson_test

%files -f %__name.lang
# syncbus
%_libexecdir/phosh-%_name
%_userunitdir/phosh-%_name.service
%_datadir/dbus-1/interfaces/%rdn_name.Folder.xml
%_datadir/dbus-1/interfaces/%rdn_name.Manager.xml
%_datadir/dbus-1/services/%rdn_name.service
# os-updater
%_libexecdir/phosh-os-updater
%_userunitdir/phosh-os-updater.service
%_desktopdir/mobi.phosh.OsUpdater.desktop
%_iconsdir/hicolor/symbolic/apps/mobi.phosh.OsUpdater-symbolic.svg
%doc README* NEWS

%{?_enable_demo:
%files demo
%_libexecdir/phosh-%name-demo}

%changelog
* Sun Jul 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- updated to v0.2.0-8-g07444dd

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus


