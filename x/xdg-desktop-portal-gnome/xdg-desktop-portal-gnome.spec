%define _libexecdir %_prefix/libexec
%define ver_major 44
%define beta %nil

Name: xdg-desktop-portal-gnome
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Desktop Portal
Group: Graphical desktop/GNOME
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

%define xdg_desktop_portal_ver 1.15.0

Requires: xdg-desktop-portal-gtk >= 1.14
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
%_datadir/glib-2.0/schemas/%name.gschema.xml
%_userunitdir/%name.service
%doc NEWS README*


%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Tue Oct 18 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Sep 04 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.9.rc
- 43.rc

* Sun Jul 03 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0.1-alt1
- 42.0.1

* Thu Sep 23 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- first build for Sisyphus

