%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%define _libexecdir %_prefix/libexec
%def_disable docs
# ERROR: test-portals - Bail out! xdg-desktop-portal:ERROR:tests/camera.c:72:camera_cb: 'ret' should be FALSE
%def_disable check

Name: xdg-desktop-portal
Version: 1.6.0
Release: alt1

Summary: Portal frontend service to Flatpak
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: https://github.com/flatpak/%name

Source: %url/releases/download/%version/%name-%version.tar.xz

%define geoclue_ver 2.5.2
%define portal_ver 0.2

Requires: dbus
Requires: flatpak >= 1.6.0
Requires: /usr/bin/fusermount
Requires: pipewire
Requires: geoclue2 >= %geoclue_ver

BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libpipewire-0.2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libgeoclue-2.0) >= %geoclue_ver
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(json-glib-1.0)
# since 1.5
BuildRequires: pkgconfig(libportal) >= %portal_ver
%{?_enable_docs:BuildRequires: xmlto docbook-dtds docbook-style-xsl}

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces known as
portals under a well-known name (org.freedesktop.portal.Desktop) and object
path (/org/freedesktop/portal/desktop). The portal interfaces include APIs for
file access, opening URIs, printing and others.

%package devel
Summary: Development files for %name
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description devel
The pkg-config file for %name.

%prep
%setup

%build
%autoreconf
%configure %{?_disable_docs:--disable-docbook-docs}
%make_build

%install
%makeinstall_std
# directory for portals such as xdg-desktop-portal-gtk
install -d -m755 %buildroot/%_datadir/%name/portals
%find_lang %name

%check
%make check

%files -f %name.lang
%_libexecdir/%name
%_libexecdir/xdg-document-portal
%_libexecdir/xdg-permission-store
%_datadir/dbus-1/interfaces/org.freedesktop.portal.*.xml
%_datadir/dbus-1/interfaces/org.freedesktop.impl.portal.*.xml
%_datadir/dbus-1/services/org.freedesktop.portal.Desktop.service
%_datadir/dbus-1/services/org.freedesktop.portal.Documents.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%_datadir/%name/
%_userunitdir/%name.service
%_userunitdir/xdg-document-portal.service
%_userunitdir/xdg-permission-store.service
%doc README.md NEWS
%{?_enable_docs:%doc %_docdir/%name}

%files devel
%_datadir/pkgconfig/%name.pc


%changelog
* Sat Dec 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Dec 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Thu Nov 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Thu May 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Jan 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- first build for Sisyphus

