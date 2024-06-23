%define _libexecdir %_prefix/libexec
%define ver_major 1.0

Name: xdg-desktop-portal-xapp
Version: %ver_major.7
Release: alt1

Summary: Xapp Desktop Portal
License: LGPL-2.1-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/xdg-desktop-portal-xapp/

# Source-url: https://github.com/linuxmint/xdg-desktop-portal-xapp/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

%define xdg_desktop_portal_ver 1.15.0

Requires: xdg-desktop-portal-gtk >= 1.14

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libxapps-devel
BuildRequires: libgtk+3-devel

%description
A backend implementation for xdg-desktop-portal that is using GTK
and various pieces of Cinnamon/MATE/Xfce4 infrastructure.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%_datadir/xdg-desktop-portal/portals/xapp.portal
%_userunitdir/%name.service
%doc README*


%changelog
* Sun Jun 23 2024 Anton Midyukov <antohami@altlinux.org> 1.0.7-alt1
- new version (1.0.7) with rpmgs script

* Fri Jun 14 2024 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1
- new version (1.0.6) with rpmgs script

* Sat Jun 08 2024 Anton Midyukov <antohami@altlinux.org> 1.0.5-alt1
- new version (1.0.5) with rpmgs script

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 1.0.4-alt1
- new version (1.0.4) with rpmgs script

* Mon Jul 10 2023 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- new version

* Mon Jun 19 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt2
- fix long start of GTK apps in non-Cinnamon DEs (closes: #46571)

* Thu Jun 8 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- first build for Sisyphus

