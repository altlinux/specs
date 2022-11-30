%def_disable snapshot
%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%define _libexecdir %_prefix/libexec

Name: xdg-desktop-portal-gtk
Version: 1.14.1
Release: alt1

Summary: Backend implementation for xdg-desktop-portal using GTK+
Group: Graphical desktop/GNOME
License: LGPL-2.0
Url: https://github.com/flatpak/%name

%if_disabled snapshot
Source: %url/releases/download/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define xdg_desktop_portal_ver %version
%define gtk_ver 3.22

Requires: xdg-desktop-portal >= %xdg_desktop_portal_ver

BuildRequires: libgtk+3-devel >= %gtk_ver gsettings-desktop-schemas-devel
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: libdbus-devel pkgconfig(systemd)

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
* Wed Nov 30 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt2
- updated to 1.14.0-14-g30ef5f8

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Dec 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt2
- rebuilt against libgnome-desktop-so.19

* Sat Dec 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Dec 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

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

