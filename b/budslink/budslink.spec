%define _unpackaged_files_terminate_build 1
%define app_id io.github.maniacx.BudsLink

Name: budslink
Version: 0.1.5
Release: alt1

Summary: Monitor and control Bluetooth earbuds
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://maniacx.github.io/BudsLink/
VCS: https://github.com/maniacx/BudsLink
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(libpulse)
BuildRequires: gobject-introspection-devel

%description
BudsLink is an application that provides battery monitoring and feature control
for supported Bluetooth wearable audio devices, including AirPods, Beats, Sony
Audio wearables, Samsung Galaxy Buds and Nothing/CMF buds.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %app_id

%files -f %app_id.lang
%_bindir/%name
%_libdir/%app_id/*
%_desktopdir/%app_id.desktop
%_datadir/%app_id/*
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/scalable/actions/bbm-*.svg
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Wed Jul 08 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.5-alt1
- Update to 0.1.5.

* Sat May 23 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.4-alt1
- Initial build.
