# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-session-alt
Version: 47.0
Release: alt3
Summary: Session GNOME Shell for Alt distributions
License: GPL-2.0-or-later
Group:  Graphical desktop/GNOME
Url: https://git.altlinux.org/gears/g/gnome-session-alt.git
Vcs: https://git.altlinux.org/gears/g/gnome-session-alt.git
Source: %name-%version.tar

BuildArch: noarch

Requires: gnome-shell >= %version
Requires: gnome-session >= %version
Requires: gnome-console >= %version
Requires: gnome-text-editor >= %version
Requires: nautilus >= %version
Requires: gnome-shell-extensions >= %version
Requires: gnome-shell-extension-dash-to-panel
Requires: gnome-shell-extension-arcmenu
Requires: gnome-shell-extension-gtk4-desktop-icons-ng
Requires: gnome-shell-extension-clipboard-indicator
Requires: gnome-shell-extension-appindicator

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gnome-shell/modes
install -m644 alt.json \
	%buildroot%_datadir/gnome-shell/modes/alt.json

mkdir -p %buildroot%_datadir/glib-2.0/schemas
install -m644 25_org.gnome.shell.extensions.gschema.override \
	%buildroot%_datadir/glib-2.0/schemas/25_org.gnome.shell.extensions.gschema.override

mkdir -p %buildroot%_datadir/wayland-sessions
install -m644 alt-gnome-wayland.desktop \
	%buildroot%_datadir/wayland-sessions/alt-gnome-wayland.desktop

mkdir -p %buildroot%_datadir/xsessions
install -m644 alt-gnome-xorg.desktop \
	%buildroot%_datadir/xsessions/alt-gnome-xorg.desktop

%files
%_datadir/gnome-shell/modes/alt.json
%_datadir/glib-2.0/schemas/25_org.gnome.shell.extensions.gschema.override
%_datadir/wayland-sessions/alt-gnome-wayland.desktop
%_datadir/xsessions/alt-gnome-xorg.desktop

%changelog
* Sun Dec 22 2024 Anton Midyukov <antohami@altlinux.org> 47.0-alt3
- alt-gnome-wayland.desktop: remove wayland from Name
- alt-gnome-*.desktop: fix description and categories
- alt.json: Enable extension "appindicatorsupport@rgcjonas.gmail.com" on startup
- gschema.override: make the panel wider and increase the margins in tray
- gschema.override: add org.gnome.Software.desktop to favorite-apps

* Sat Dec 21 2024 Anton Midyukov <antohami@altlinux.org> 47.0-alt2
- Fix Url and Vcs

* Sat Dec 21 2024 Anton Midyukov <antohami@altlinux.org> 47.0-alt1
- Initial build
