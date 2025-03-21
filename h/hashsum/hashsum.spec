%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Hashsum
%define nautilus_extdir %_datadir/nautilus-python/extensions
%def_enable check

Name: hashsum
Version: 4.0.4
Release: alt1

Summary: Check hashes for your files
License: GPL-3.0-or-later
Group: Other

Url: https://altlinux.space/alt-gnome/Hashsum
Vcs: https://altlinux.space/alt-gnome/Hashsum
Source: %name-%version.tar
Source1: 100_%app_id.gschema.override

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libblake3)
BuildRequires: pkgconfig(gee-0.8)
%{?_enable_check:BuildRequires: desktop-file-utils %_bindir/appstream-util}

%description
Check hashes for your files - A GUI tool to generate, compare and verify MD5,
SHA-1, SHA-256, SHA-512, Blake3, CRC32, Adler32 STRIBOG256 & STRIBOG512 hashes.

%package nautilus
Summary: Nautilus extension for Hashsum
Group: Other
Requires: %name = %EVR
Requires: nautilus-python

%description nautilus
An extension for Nautilus that allows you to quickly check the hash of file.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
install -m644 %SOURCE1 %buildroot%_datadir/glib-2.0/schemas
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/100_%app_id.gschema.override
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc LICENSE README.md

%files nautilus
%nautilus_extdir/%name-extension.py

%changelog
* Fri Mar 21 2025 Alexander Davydzik <paladindev@altlinux.org> 4.0.4-alt1
- initial build
