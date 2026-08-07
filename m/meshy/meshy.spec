%define _unpackaged_files_terminate_build 1
%define app_id page.codeberg.sesivany.Meshy

%def_enable qr

Name: meshy
Version: 26.08
Release: alt1
Summary: A GTK4/libadwaita client for MeshCore
License: GPL-3.0-or-later
Group: Communications
Url: https://codeberg.org/sesivany/meshy
VCS: https://codeberg.org/sesivany/meshy.git

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: /usr/bin/gtk4-update-icon-cache
BuildRequires: /usr/bin/update-desktop-database
BuildRequires: blueprint-compiler

Requires: python3(Crypto)
Requires: python3(pyzbar)
Requires: python3(segno)
Requires: python3(serial)

%description
A GTK4/libadwaita application for reading (and eventually writing) NFC tags
via the **neard** daemon's D-Bus interface. Designed for mobile phones and
tablets running GNOME/Phosh, but works on any Linux desktop.

%prep
%setup
%autopatch -p 1

%build
%meson \
    -Dshortcuts_dialog=true \
    %{subst_enable_meson_bool qr qr_scanner}
%meson_build -v

%install
%meson_install
%find_lang %name --all-name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name
%_datadir/metainfo/*.xml
%_datadir/glib-2.0/schemas/%app_id.*
%python3_sitelibdir/%name

%changelog
* Wed Aug 05 2026 Vasiliy Doylov <neko@altlinux.org> 26.08-alt1
- Initial build for ALT.
