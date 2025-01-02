%def_disable snapshot
%define _name turnon
%define ver_major 2.1
%define rdn_name de.swsnr.%_name

%def_disable bootstrap

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Turn on devices in your network
License: MPL-2.0
Group: Networking/Other
Url: https://github.com/swsnr/turnon

Vcs: https://github.com/swsnr/turnon.git

%if_disabled snapshot
Source: https://github.com/swsnr/turnon/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adw_ver 1.6

Requires: dconf

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
A small GNOME application to send Wake On LAN (WoL) magic packets to
devices in a network.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%makeinstall_std DESTPREFIX=%buildroot%_prefix
%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Jan 03 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus

