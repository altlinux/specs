%def_enable snapshot
%define _name decoder
%define ver_major 0.6
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

%define glib_ver 2.76
%define gtk_ver 4.16.0
%define adwaita_ver 1.6
%define zbar_ver 0.20
%define gst_api_ver 1.0
%define gst_ver 1.20
%define pipewire_ver 0.3

Requires: gst-plugins-bad%gst_api_ver >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(zbar) >= %zbar_ver
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
cargo update -p zbar-rust && cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

# remove broken build.rs from zbar-rust
rm -f vendor/zbar-rust/build.rs
sed -i '/build.rs/d' vendor/zbar-rust/Cargo.toml
sed -i 's|"build.rs":"894b33392971ba9dad1dd4e45869478198f86e911e0b29f7e0d9fbf1342672c2",||
        s/"files":{[^}]*}/"files":{}/' \
    vendor/zbar-rust/.cargo-checksum.json

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
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
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

