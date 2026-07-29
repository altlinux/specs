%define _unpackaged_files_terminate_build 1
%define app_id io.github.focustimerhq.FocusTimer

Name: focustimer
Version: 1.1.3
Release: alt1

Summary: Work with regular breaks
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://github.com/focustimerhq/FocusTimer
VCS: https://github.com/focustimerhq/FocusTimer.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: icon-theme-hicolor

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(glib-2.0) >= 2.50
BuildRequires: pkgconfig(gobject-2.0) >= 2.50
BuildRequires: pkgconfig(gio-2.0) >= 2.50
BuildRequires: pkgconfig(gtk4) >= 4.18
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.8.0
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires: pkgconfig(libpeas-2) >= 2.2.0
BuildRequires: pkgconfig(gom-1.0) >= 0.5.0
BuildRequires: pkgconfig(gstreamer-1.0) >= 1.0.10
BuildRequires: pkgconfig(gstreamer-controller-1.0)
BuildRequires: pkgconfig(json-glib-1.0) >= 1.6.2
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(pangocairo)

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang focus-timer

%files -f focus-timer.lang
%_bindir/focus-timer
%_desktopdir/%{app_id}.desktop
%_datadir/dbus-1/interfaces/%{app_id}*.xml
%_datadir/dbus-1/services/%{app_id}*.service
%_datadir/glib-2.0/schemas/%{app_id}*.gschema.xml
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/focus-timer
%dir %_datadir/focus-timer/sounds
%dir %_datadir/knotifications6
%_datadir/metainfo/%{app_id}.metainfo.xml
%_datadir/focus-timer/sounds/*
%_datadir/knotifications6/%{app_id}.notifyrc

%changelog
* Tue Jul 28 2026 Anton Osipov <radiolamp@altlinux.org> 1.1.3-alt1
- Initial build.
