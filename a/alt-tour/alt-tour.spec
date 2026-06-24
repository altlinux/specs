%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tour

Name: alt-tour
Version: 1.2.1
Release: alt1

Summary: ALT Tour and Greeter
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/alt-tour
Vcs: https://altlinux.space/alt-gnome/alt-tour
Source: %name-%version.tar

Requires: alt-panelmoded

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)

%description
A guided tour and greeter for Alt with GNOME DE.

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
%_datadir/metainfo/%app_id.metainfo.xml
%_sysconfdir/xdg/autostart/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%doc README.md

%changelog
* Wed Jun 24 2026 Alexander Davydzik <paladindev@altlinux.org> 1.2.1-alt1
- fixed title bar settings

* Wed Mar 11 2026 Alexander Davydzik <paladindev@altlinux.org> 1.2.0-alt1
- updated app icon
- updated links

* Tue Jun 24 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.9-alt1
- remove changelog from metadata

* Wed Jun 04 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.8-alt1
- added about dialog to last page
- updated slides images

* Mon Jun 02 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.7-alt1
- added metadata
- updated app icon
- changed system style preview icons
- updated translations

* Mon Apr 07 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.6-alt1
- fixed autostart

* Fri Mar 28 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.5-alt1
- updated translations

* Fri Mar 28 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.4-alt1
- added new tour pages

* Tue Mar 18 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.3-alt1
- fixed autostart path

* Tue Mar 18 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.2-alt1
- updated autostart logic

* Mon Mar 17 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.1-alt1
- added window title
- added video support
- added wallpaper button
- removed gnome tour conflict and desktop file
- updated russian translations
- added autoremove from startup apps

* Thu Mar 06 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1-alt1
- Added settings page with color scheme selector and topbar buttons.
- Added tour pages for each system style.

* Tue Mar 04 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0-alt1
- initial build
