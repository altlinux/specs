%define _unpackaged_files_terminate_build 1
%define app_id app.devsuite.Manuals

Name: manuals
Version: 48.0
Release: alt1

Summary: Install, Browse, and Search developer documentation
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://devsuite.app/manuals
Vcs: https://gitlab.gnome.org/chergert/manuals
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(gom-1.0)
BuildRequires: pkgconfig(libdex-1)
BuildRequires: pkgconfig(libpanel-1)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(webkitgtk-6.0)

%description
Manuals is an extraction of the Documentation component of GNOME Builder
into a standalone application.

%prep
%setup

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
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/dbus-1/services/%app_id.service
%doc README.md

%changelog
* Mon Apr 07 2025 Alexander Davydzik <paladindev@altlinux.org> 48.0-alt1
- initial build
