# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-arcmenu
Epoch: 1
Version: 69.0
Release: alt1
Summary: Application menu for GNOME Shell
License: GPL-2.0-or-later
Group:  Graphical desktop/GNOME
Url: https://gitlab.com/arcmenu/ArcMenu
Vcs: https://gitlab.com/arcmenu/ArcMenu
Source: %name-%version.tar
Source1: 00_arcmenu-disable-notification.gschema.override
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 47.0
# https://bugzilla.altlinux.org/53075
Requires: typelib(GMenu) = 3.0
Requires: altlinux-freedesktop-menu-gnome3
BuildRequires: %_bindir/glib-compile-schemas

%description
ArcMenu is an application menu for GNOME Shell, designed to provide a more
familiar user experience and workflow. This extension has many features,
including various menu layout styles, GNOME search, quick access to system
shortcuts, and much more!

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std
%find_lang arcmenu

install -Dm644 %SOURCE1 \
	%buildroot%_datadir/glib-2.0/schemas/00_arcmenu-disable-notification.gschema.override

%files -f arcmenu.lang
%_datadir/gnome-shell/extensions/arcmenu@arcmenu.com
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.arcmenu.gschema.xml
%_datadir/glib-2.0/schemas/00_arcmenu-disable-notification.gschema.override
%doc README.md

%changelog
* Wed Mar 18 2026 Anton Midyukov <antohami@altlinux.org> 1:69.0-alt1
- New version 69.0.

* Wed Jan 14 2026 Dmitry Udalov <udalov@altlinux.org> 1:68.0-alt3
- New snapshot.
- Improved duplicate items handling in icon grid.
- Add option to show generic application names.

* Sun Dec 14 2025 Anton Midyukov <antohami@altlinux.org> 1:68.0-alt2
- src/extension.js: remove undefined this._updateNotification.

* Sat Dec 13 2025 Anton Midyukov <antohami@altlinux.org> 1:68.0-alt1
- New version 68.0.

* Thu Nov 20 2025 Anton Midyukov <antohami@altlinux.org> 1:67.2-alt2
- src/iconGrid.js: remove empty item.

* Thu Nov 20 2025 Anton Midyukov <antohami@altlinux.org> 1:67.2-alt1
- new version 67.2.

* Sun Oct 19 2025 Anton Midyukov <antohami@altlinux.org> 1:67.1-alt2
- Fix version to 67.1, bump epoch.
- Add runtime dependency on altlinux-freedesktop-menu-gnome3.

* Mon Sep 15 2025 Anton Midyukov <antohami@altlinux.org> v67.1-alt1
- New version v67.1.

* Mon Sep 08 2025 Anton Midyukov <antohami@altlinux.org> 67.0-alt1
- New version 67.0.

* Sat Jul 19 2025 Anton Midyukov <antohami@altlinux.org> 66.0-alt1
- New snapshot, bump version to 66.0

* Sun Jun 01 2025 Anton Midyukov <antohami@altlinux.org> 66-alt1
- New version 66.

* Sun Apr 20 2025 Anton Midyukov <antohami@altlinux.org> 65-alt5
- Hide category menu item if it contains no apps
- Fix bug where apps assigned to multiple categories only appeared
  in the first category loaded

* Fri Apr 18 2025 Anton Midyukov <antohami@altlinux.org> 65-alt4
- Set 'metadata::trusted: true' when creating desktop shortcuts

* Sun Apr 13 2025 Anton Midyukov <antohami@altlinux.org> 65-alt3
- extension.js: drop UpdateNotifications for fix extension disabling

* Sun Mar 16 2025 Anton Midyukov <antohami@altlinux.org> 65-alt2
- prefs.js: Remove donate page
- add gsettings override for disable update notification

* Mon Mar 10 2025 Anton Midyukov <antohami@altlinux.org> 65-alt1
- New version 65.

* Wed Feb 19 2025 Anton Midyukov <antohami@altlinux.org> 64-alt4
- iconGrid.js: Don't throw an error when the icon has already been added before
  (Closes: 53135)

* Fri Feb 14 2025 Anton Midyukov <antohami@altlinux.org> 64-alt3
- add dependency on libgnome-menus-gir (Closes: 53075)

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 64-alt2
- extension.js: Remove UpdateNotifier

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 64-alt1
- New version 64.

* Thu Dec 19 2024 Anton Midyukov <antohami@altlinux.org> 63-alt1
- initial build
