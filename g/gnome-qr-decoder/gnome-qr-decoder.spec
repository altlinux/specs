%def_enable snapshot
%define _name decoder
%define ver_major 0.8
%define xdg_name com.belmoussaoui.Decoder

%define optflags_lto %nil

%def_enable check
%def_disable bootstrap

Name: gnome-qr-%_name
Version: %ver_major.0
Release: alt1

Summary: Scan and Generate QR Codes
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Decoder

Vcs: https://gitlab.gnome.org/World/decoder.git

Source: %_name-%version.tar
Source1: %_name-%version-cargo.tar

%define glib_ver 2.80
%define gtk_ver 4.16.0
%define adwaita_ver 1.8
%define gst_api_ver 1.0
%define gst_ver 1.20
%define pipewire_ver 0.3

Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
Requires: gst-plugin-gtk4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-plugins-bad-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(libpipewire-0.3) >= %pipewire_ver
BuildRequires: pkgconfig(sqlite3) pkgconfig(sqlcipher)
BuildRequires: pkgconfig(openssl)
BuildRequires: clang-devel
BuildRequires: /usr/bin/appstreamcli desktop-file-utils

%description
Decoder is a program for scan and generate QR codes.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/%_name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Fri Oct 10 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Tue Apr 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Mon Sep 23 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0-5-g3732c7d

* Thu Mar 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Sun Nov 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- updated to 0.4.1-22-gd494532

* Fri Sep 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Jul 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- first build for Sisyphus

