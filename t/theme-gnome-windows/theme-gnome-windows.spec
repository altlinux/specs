%define gnome_version 47

Name:     theme-gnome-windows
Version:  1.0
Release:  alt8

Summary:  GNOME theme for Windows-like layout
License:  GPL-3.0-or-later
Group:    Graphical desktop/GNOME
Url:      https://altlinux.space/antohami/theme-gnome-windows
VCS:	  https://altlinux.space/antohami/theme-gnome-windows.git

Source:   %name-%version.tar

ExcludeArch: %ix86

Requires: dconf
Requires: gnome-shell >= %gnome_version
Requires: icon-theme-morewaita
Requires: nautilus >= %gnome_version
Requires: gnome-shell-extensions >= %gnome_version
Requires: gnome-shell-extension-dash-to-panel
Requires: gnome-shell-extension-arcmenu
Requires: gnome-shell-extension-gtk4-desktop-icons-ng
Requires: gnome-shell-extension-clipboard-indicator
Requires: gnome-shell-extension-appindicator
Requires: gnome-shell-extension-add-to-desktop
Requires: gnome-shell-extension-session-keeper
Requires: gnome-shell-extension-caffeine
Requires: gnome-shell-extension-no-overview-at-startup

Conflicts: alt-panelmoded

%description
GNOME theme for Windows-like layout: taskbar at bottom with menu button.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/glib-2.0/schemas
install -pm644 *.gschema.override \
        %buildroot%_datadir/glib-2.0/schemas/

%files
%_datadir/glib-2.0/schemas/*.gschema.override

%changelog
* Sun Mar 22 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt8
- Enable extension 'no-overview-at-startup'.

* Tue Feb 24 2026 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt7
- Enable extension 'caffeine'.

* Thu Dec 04 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt6
- Enable extensions 'session-keeper', 'add-to-desktop'.
- ExcludeArch: %%ix86.

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt5
- Remove 40-alt-specyfic.gschema.override

* Mon Mar 17 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt4
- 60-windows-like.gschema.override: revert 'primary-monitor=0'
- update URL tag
- add VCS tag

* Fri Mar 14 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt3
- add maximize, minimize window buttons
- add conflict with alt-panelmoded
- Separate settings into those that should override branding and
  those that should be overridden by branding

* Fri Mar 14 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- remove sets of monitor for dash-to-panel extension (Closes: 53434)

* Sun Feb 23 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- initial build
