%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id com.cassidyjames.butler

Name: butler
Version: 1.3.0
Release: alt1

Summary: Companion for Home Assistant
License: GPL-3.0-or-later
Group: Other

Url: https://github.com/cassidyjames/butler
Vcs: https://github.com/cassidyjames/butler
Source: %name-%version.tar

%define webki_api_ver 6.0
%define webkit_ver 2.43.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(webkitgtk-%webki_api_ver) >= %webkit_ver
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
Access your Home Assistant dashboard from a native companion UI, integrating
better with your OS. Native features include:

* Icon in your App Grid, Applications Menu, Dash, Dock, etc.
* Native header bar
* Save and restore current view and size when closed and re-opened
* Two-finger swipe and mouse button support to go back/forward between views
* Cross-desktop light/dark style support (if supported by your Lovelace theme)
Butler is designed to make getting at your Home Assistant dashboard easier for
kiosks, your laptop/desktop, or your Linux phone. It does not support companion
app features from Android and iOS like location services, notifications, or
exposing device sensors.

Other features include:

* Pinch-to-zoom
* Set the scaling with Ctrl+Plus/Minus or Ctrl+0 to reset
* Fullscreen from the menu, a keyboard shortcut, or a GSetting to better support
kiosk use cases

Note WebRTC camera streams (i.e. used by some newer Nest cameras) are not
currently supported.

%prep
%setup

%build
%meson \
    -Dprofile=release
%meson_build

%install
%meson_install
%find_lang --with-gnome %app_id

%check
%meson_test

%files -f %app_id.lang
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Mon Feb 17 2025 Semen Fomchenkov <armatik@altlinux.org> 1.3.0-alt1
- Initial build
