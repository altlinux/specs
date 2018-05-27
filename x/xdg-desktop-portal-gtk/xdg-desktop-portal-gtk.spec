%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-gtk
Version: 0.11
Release: alt1

Summary: Backend implementation for xdg-desktop-portal using GTK+
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://github.com/flatpak/%name
Source: %url/releases/download/%version/%name-%version.tar.xz

%define xdg_desktop_portal_ver 0.11

Requires: xdg-desktop-portal >= %xdg_desktop_portal_ver

BuildRequires: libgtk+3-devel
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: libsystemd-devel

%description
A backend implementation for xdg-desktop-portal that is using GTK+ and various
pieces of GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.

%prep
%setup

%build
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
* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- first build for Sisyphus

