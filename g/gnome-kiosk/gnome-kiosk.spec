%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 50
%define beta %nil
%define xdg_name org.gnome.Kiosk

# disabled by default
%def_disable notification_daemon
%def_disable accessibility_panel
%def_enable check

Name: gnome-kiosk
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Kiosk
License: GPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/GNOME/gnome-kiosk/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

Vcs: https://gitlab.gnome.org/halfline/gnome-kiosk.git

%define glib_ver 2.68.0
%define gtk4_ver 4.0
%define mutter_api_ver 18
%define mutter_ver 50
%define ibus_ver 1.5.24

Requires: dconf gnome-settings-daemon

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson dconf desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(libmutter-%mutter_api_ver) >= %mutter_ver
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(ibus-1.0) >= %ibus_ver
BuildRequires: pkgconfig(systemd)

%description
GNOME Kiosk provides a desktop environment suitable for fixed purpose, or
single application deployments like wall displays and point-of-sale systems.

%package session-script
Summary: Basic session used for running kiosk application from shell script
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %EVR
Requires: gnome-session
Requires: gnome-text-editor

%description session-script
This package generates a shell script and the necessary scaffolding to
start that shell script within a kiosk session.

%package search-appliance
Summary: Sample Search Appliance Application for GNOME Kiosk
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %EVR
#Requires: firefox
Requires: gnome-session

%description search-appliance
This package provides a full screen firefox window pointed to Yandex.

%prep
%setup -n %name-%version%beta
# switch from google to yandex
sed -i 's|google\.com|ya.ru|' search-app/%xdg_name.SearchApp.desktop.in.in
# fix shebang
sed -i 's|/usr/\(bin/sh\)|/\1|' kiosk-script/%name-script

%build
%meson \
    %{subst_enable_meson_bool notification_daemon notification-daemon} \
    %{subst_enable_meson_bool accessibility_panel accessibility-panel}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dconf/profile/gnomekiosk
%dir %_datadir/%name
%_datadir/%name/gnomekiosk.dconf.compiled
%_datadir/%name/window-config.ini
%_userunitdir/%xdg_name.target
%_userunitdir/%{xdg_name}@wayland.service

%if_enabled notification_daemon
%_bindir/%name-notification-send
%_userunitdir/%name-notification-daemon.service
%_libexecdir/%name-notification-daemon
%_datadir/dbus-1/services/org.freedesktop.Notifications.service
%_datadir/dbus-1/services/org.gtk.Notifications.service
%_datadir/%name/notification-daemon.css
%endif

%if_enabled accessibility_panel
%_bindir/%name-accessibility-panel
%_desktopdir/%{xdg_name}.AccessibilityPanel.desktop
%endif

%doc NEWS README.md

%files session-script
%_bindir/%name-script
%_desktopdir/%xdg_name.Script.desktop
%_datadir/gnome-session/sessions/%name-script.session
%_datadir/wayland-sessions/%name-script-wayland.desktop
%_userunitdir/gnome-session@%name-script.target.d/session.conf
%_userunitdir/%xdg_name.Script.service

%files search-appliance
%_desktopdir/%xdg_name.SearchApp.desktop
%_datadir/gnome-session/sessions/%xdg_name.SearchApp.session
%_datadir/wayland-sessions/%xdg_name.SearchApp.Session.desktop
%_userunitdir/%xdg_name.SearchApp.service
%_userunitdir/gnome-session@%xdg_name.SearchApp.target.d/session.conf

%changelog
* Tue Mar 17 2026 Yuri N. Sedunov <aris@altlinux.org> 50.0-alt1
- 50.0

* Wed Sep 17 2025 Yuri N. Sedunov <aris@altlinux.org> 49.0-alt1
- 49.0

* Sun Jul 06 2025 Yuri N. Sedunov <aris@altlinux.org> 48.0-alt1.1
- gnome-kiosk-script: fix shebang again (ALT #55086)

* Mon Mar 17 2025 Yuri N. Sedunov <aris@altlinux.org> 48.0-alt1
- 48.0

* Thu Sep 19 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Mon Mar 18 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Thu Jun 22 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt0.1
- first preview for Sisyphus (44.0-2-g12a9674)



