%define _libexecdir %_prefix/libexec
%define ver_major 42
%define beta %nil

Name: xdg-desktop-portal-gnome
Version: %ver_major.1
Release: alt1%beta

Summary: GNOME Desktop Portal
Group: Graphical desktop/GNOME
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

%define xdg_desktop_portal_ver 1.14.0

Requires: xdg-desktop-portal-gtk >= %xdg_desktop_portal_ver
Conflicts: xdg-desktop-portal-gtk < 1.12.0

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson libgtk4-devel pkgconfig(libadwaita-1) pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: gsettings-desktop-schemas-devel

%description
XDG Desktop Portal implementation for GNOME. It uses GNOME-specific APIs
and components, such as GNOME Shell, Mutter, and GNOME Settings Daemon,
to provide various portal features.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
%_datadir/xdg-desktop-portal/portals/gnome.portal
%_userunitdir/%name.service
%doc NEWS README*


%changelog
* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0.1-alt1
- 42.0.1

* Thu Sep 23 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- first build for Sisyphus

