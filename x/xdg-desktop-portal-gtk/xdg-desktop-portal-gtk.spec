%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-gtk
Version: 1.5.1
Release: alt1

Summary: Backend implementation for xdg-desktop-portal using GTK+
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://github.com/flatpak/%name
Source: %url/releases/download/%version/%name-%version.tar.xz

%define xdg_desktop_portal_ver 1.5.0

Requires: xdg-desktop-portal >= %xdg_desktop_portal_ver

BuildRequires: libgtk+3-devel
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: libdbus-devel libsystemd-devel
# since 1.5.1
BuildRequires: pkgconfig(gnome-desktop-3.0)

%description
A backend implementation for xdg-desktop-portal that is using GTK+ and various
pieces of GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.

%prep
%setup

%build
%add_optflags -lX11
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%_datadir/xdg-desktop-portal/portals/gtk.portal
%_userunitdir/%name.service
%doc NEWS


%changelog
* Thu Nov 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu May 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- first build for Sisyphus

