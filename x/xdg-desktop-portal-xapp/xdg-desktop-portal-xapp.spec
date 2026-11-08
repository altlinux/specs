# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec
%define ver_major 1.2

Name: xdg-desktop-portal-xapp
Version: %ver_major.0
Release: alt1

Summary: Xapp Desktop Portal
License: LGPL-2.1-or-later
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/xdg-desktop-portal-xapp/
VCS: https://github.com/linuxmint/xdg-desktop-portal-xapp/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define xdg_desktop_portal_ver 1.15.0

Requires: xdg-desktop-portal-gtk >= 1.14

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-systemd
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
%patch -p1

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
%_datadir/xdg-desktop-portal/portals/xapp-gnome-keyring.portal
%_userunitdir/%name.service
%doc README*

%changelog
* Sat Nov 07 2026 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Thu Nov 13 2025 Anton Midyukov <antohami@altlinux.org> 1.1.3-alt1
- New version 1.1.3.

* Tue Aug 12 2025 Anton Midyukov <antohami@altlinux.org> 1.1.2-alt1
- New version 1.1.2.

* Sun Jun 01 2025 Anton Midyukov <antohami@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Mon Dec 02 2024 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- New version 1.1.0.
- Build from git tag.

* Tue Aug 06 2024 Anton Midyukov <antohami@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Thu Jul 18 2024 Anton Midyukov <antohami@altlinux.org> 1.0.8-alt1
- New version 1.0.8.

* Sun Jun 23 2024 Anton Midyukov <antohami@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Fri Jun 14 2024 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1
- New version 1.0.6.

* Sat Jun 08 2024 Anton Midyukov <antohami@altlinux.org> 1.0.5-alt1
- New version 1.0.5.

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 1.0.4-alt1
- New version 1.0.4.

* Mon Jul 10 2023 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- New version.

* Mon Jun 19 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt2
- Fix long start of GTK apps in non-Cinnamon DEs (closes: #46571).

* Thu Jun 8 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- First build for Sisyphus.
