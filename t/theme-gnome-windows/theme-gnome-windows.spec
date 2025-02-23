%define gnome_version 47

Name:     theme-gnome-windows
Version:  1.0
Release:  alt1

Summary:  GNOME theme for Windows-like layout
License:  GPL-3.0-or-later
Group:    Graphical desktop/GNOME
Url:      https://altlinux.org

Source:   %name-%version.tar

BuildArch: noarch

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
* Sun Feb 23 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- initial build
