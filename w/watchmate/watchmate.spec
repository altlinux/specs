%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define xdg_name io.gitlab.azymohliad.WatchMate

Name: watchmate
Version: 0.5.3
Release: alt1

Summary: PineTime smart watch companion app for Linux phone and desktop
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.gnome.org/philippun1/snoop/
VCS: https://gitlab.gnome.org/philippun1/snoop/

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
Companion app for InfiniTime-powered PineTime smart watch.
Visually optimized for GNOME, adaptive for phone and desktop, Linux only.
Features:
* Current time service.
* Data reading: battery level, heart rate, steps count, firmware version.
* OTA firmware and external resources updates. Both, from manually specified
  DFU/resources files, or automatically downloaded from InfiniTime releases
  for selected version.
* Media-player control.
* Notifications forwarding.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
cargo build %_smp_mflags --release --offline

%install
install -vpD target/release/%name -t %buildroot%_bindir
install -vpD assets/icons/* -t %buildroot%_iconsdir/hicolor/scalable/apps
install -vpD assets/%xdg_name.desktop -t %buildroot%_desktopdir
install -vpD assets/%xdg_name.gschema.xml -t %buildroot%_datadir/glib-2.0/schemas
install -vpD assets/%xdg_name.metainfo.xml -t %buildroot%_datadir/metainfo

%files
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Wed May 21 2025 Alexey Volkov <qualimock@altlinux.org> 0.5.3-alt1
- Initial build for ALT
