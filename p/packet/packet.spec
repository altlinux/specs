%define _unpackaged_files_terminate_build 1
%define app_id io.github.nozwock.Packet

Name: packet
Version: 0.3.0
Release: alt1

# Fails to link under aarch64
ExcludeArch: aarch64

Summary: A Quick Share client for Linux
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/nozwock/packet
Vcs: https://github.com/nozwock/packet
Source: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo protobuf-compiler
BuildRequires: blueprint-compiler
BuildRequires: libdbus-devel
BuildRequires: pkgconfig(libadwaita-1)

%description
An implementation of the Google Quick Share protocol to send and receive files
to Android devices or another instance of Packet.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/packet/resources.gresource
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%changelog
* Fri May 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.0-alt1
- initial build
