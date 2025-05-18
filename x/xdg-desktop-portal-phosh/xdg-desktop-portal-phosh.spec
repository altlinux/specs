%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 0.47
%define beta %nil

%def_enable check

Name: xdg-desktop-portal-phosh
Version: %ver_major.0
Release: alt1%beta

Summary: Phosh Desktop Portal
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/guidog/xdg-desktop-portal-phosh

Vcs: https://gitlab.gnome.org/guidog/xdg-desktop-portal-phosh.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/guidog/xdg-desktop-portal-phosh/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

%define xdg_desktop_portal_ver 1.19.1
%define adw_ver 1.6
%define gsds_ver 47
%define pfs_ver 0.0.3

Requires: xdg-desktop-portal >= %xdg_desktop_portal_ver

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libpfs-0)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver

%description
A backend implementation for xdg-desktop-portal that is using
GTK/GNOME/Phosh to provide interfaces that aren't provided by the GTK
portal.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta 

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.phosh.service
%_datadir/xdg-desktop-portal/portals/phosh.portal
%_userunitdir/%name.service
%doc NEWS README*


%changelog
* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.47.0-alt1
- 0.47.0

* Tue Apr 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- first build for Sisyphus

