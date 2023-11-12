%def_enable snapshot
%define _name decoder
%define ver_major 0.4
%define xdg_name com.belmoussaoui.Decoder

%define optflags_lto %nil

%def_disable bootstrap

Name: gnome-qr-%_name
Version: %ver_major.1
Release: alt1

Summary: Scan and Generate QR Codes
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.gnome.org/World/decoder

Vcs: https://gitlab.gnome.org/World/decoder.git
Source: %_name-%version.tar
Source1: %_name-%version-cargo.tar
# update zbar-rust to last commit
Patch: decoder-0.3.3-alt-cargo.toml-zbar.patch
#Patch1: decoder-0.3.3-alt-cargo.lock-zbar.patch

%define glib_ver 2.76
%define gtk_ver 4.11.0
%define adwaita_ver 1.4
%define zbar_ver 0.20
%define gst_api_ver 1.0
%define gst_ver 1.20
%define pipewire_ver 0.3

Requires: gst-plugins-bad%gst_api_ver >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: /usr/bin/appstreamcli /usr/bin/appstream-util desktop-file-utils
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

%description
Decoder is a program for scan and generate QR codes.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
#%patch1 -b .zbar
%{?_enable_bootstrap:
%patch -b .zbar
# see build-aux/dist-vendor.sh
mkdir .cargo
cargo update -p zbar-rust && cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
#cat > .cargo/config << _EOF_
#[source.crates-io]
#replace-with = "vendored-sources"

#[source.vendored-sources]
#directory = "vendor"
#_EOF_

tar -cf %_sourcedir/%_name-%version-cargo.tar Cargo.lock .cargo/ vendor/}

# remove broken build.rs from zbar-rust
rm -f vendor/zbar-rust/build.rs
sed -i 's|"build.rs":"894b33392971ba9dad1dd4e45869478198f86e911e0b29f7e0d9fbf1342672c2",||' vendor/zbar-rust/.cargo-checksum.json

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
* Sun Nov 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- updated to 0.4.1-22-gd494532

* Fri Sep 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Jul 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- first build for Sisyphus

