%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name ashpd
%define ver_major 0.13
%define rdn_name com.belmoussaoui.%_name.demo

%def_enable check

%def_disable bootstrap

Name: %_name-demo
Version: %ver_major.0
Release: alt1

Summary: ASHPD Demo
License: MIT
Group: System/Libraries
Url: https://github.com/bilelmoussaoui/ashpd

Vcs: https://github.com/bilelmoussaoui/ashpd.git

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define adw_ver 1.9
%define gst_ver 1.16

BuildRequires(pre): rpm-macros-rust rpm-macros-meson
BuildRequires: rust-cargo meson clang-devel
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-gl-1.0)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libusb-1.0)

%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli}

%description
ASHPD, acronym of Aperture Science Handheld Portal Device is a Rust &
[zbus](https://gitlab.freedesktop.org/dbus/zbus) wrapper of the XDG
portals DBus interfaces.

The library aims to provide an easy way to interact with the various
portals defined per the specifications (https://flatpak.github.io/xdg-desktop-portal/docs/).
It provides an alternative to the C library.

This package provides ASHPD demo program to play with portals.

%prep
%setup -n %_name-%version/demo %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
cd client
%meson
%meson_build

%install
cd client
%meson_install

%check
cd client
%meson_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc ../README*

%changelog
* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0-52-g3ee41bb02

* Sat Apr 26 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (0.5.0-demo-9-g51cc0b110)

