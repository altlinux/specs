%def_disable snapshot

%define ver_major 45
%define beta %nil
%define xdg_name org.gnome.Kiosk

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

%define glib_ver 2.68.0
%define gtk4_ver 4.0
%define mutter_api_ver 13
%define mutter_ver 45
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
Requires: gedit

%description session-script
This package generates a shell script and the necessary scaffolding to
start that shell script within a kiosk session.

%package search-appliance
Summary: Sample Search Appliance Application for GNOME Kiosk
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %EVR
Requires: firefox
Requires: gnome-session

%description search-appliance
This package provides a full screen firefox window pointed to Yandex.

%prep
%setup -n %name-%version%beta
# switch from google to yandex
sed -i 's|google\.com|ya.ru|' search-app/%xdg_name.SearchApp.desktop.in.in
# fix shebang
sed -i 's|/usr/\(bin/sh\)|\1|' kiosk-script/%name-script

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dconf/profile/gnomekiosk
%_datadir/%name/gnomekiosk.dconf.compiled
%_userunitdir/%xdg_name.target
%_userunitdir/%{xdg_name}@wayland.service
%_userunitdir/%{xdg_name}@x11.service
%doc NEWS README.md

%files session-script
%_bindir/%name-script
%_desktopdir/%xdg_name.Script.desktop
%_datadir/gnome-session/sessions/%name-script.session
%_datadir/wayland-sessions/%name-script-wayland.desktop
%_datadir/xsessions/%name-script-xorg.desktop
%_userunitdir/gnome-session@%name-script.target.d/session.conf
%_userunitdir/%xdg_name.Script.service

%files search-appliance
%_desktopdir/%xdg_name.SearchApp.desktop
%_datadir/gnome-session/sessions/%xdg_name.SearchApp.session
%_datadir/xsessions/%xdg_name.SearchApp.Session.desktop
%_datadir/wayland-sessions/%xdg_name.SearchApp.Session.desktop

%changelog
* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Thu Jun 22 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt0.1
- first preview for Sisyphus (44.0-2-g12a9674)



