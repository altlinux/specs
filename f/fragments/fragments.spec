%def_enable snapshot
%define optflags_lto %nil

%define ver_major 2.1
%define rdn_name de.haeckerfelix.Fragments

%def_disable bootstrap

Name: fragments
Version: %ver_major.1
Release: alt1

Summary: A BitTorrent Client for GNOME
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://apps.gnome.org/Fragments

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Fragments/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Fragments.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10.1
%define adwaita_ver 1.4

Requires: transmission-daemon

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo git
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)

BuildRequires: pkgconfig(libcurl)

%description
Fragments is an easy to use BitTorrent client. It can be used to
transfer files via the BitTorrent protocol, such as videos, music or
installation images for Linux distributions.

Note: Fragments requires running transmission daemon.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
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
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Mon Oct 09 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus (v0.2.0-6-gff8c151)


