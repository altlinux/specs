%def_disable snapshot
%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%define _libexecdir %_prefix/libexec
%def_disable docs
# test-portals-openuri -- timeout
%def_disable check
%def_enable installed_tests

Name: xdg-desktop-portal
Version: 1.16.0
Release: alt1

Summary: Portal frontend service to Flatpak
Group: Graphical desktop/GNOME
License: LGPL-2.0
Url: https://github.com/flatpak/%name

%if_disabled snapshot
Source: %url/releases/download/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%{?_enable_installed_tests:%add_python3_path %_libexecdir/installed-tests/%name}

%define meson_ver 0.56.2
%define glib_ver 2.60
%define geoclue_ver 2.5.2
%define portal_ver 0.2.90
%define fuse3_ver 3.10.0

Requires: dbus
Requires: flatpak >= 1.6.0
Requires: /usr/bin/fusermount
Requires: pipewire
Requires: geoclue2 >= %geoclue_ver

BuildRequires(pre): rpm-macros-meson rpm-build-systemd %{?_enable_installed_tests:rpm-build-python3}
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(flatpak) flatpak
BuildRequires: pkgconfig(fuse3) >= %fuse3_ver
BuildRequires: pkgconfig(gio-unix-2.0) >= %glib_ver
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libgeoclue-2.0) >= %geoclue_ver
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(json-glib-1.0)
# since 1.5
BuildRequires: pkgconfig(libportal) >= %portal_ver
%{?_enable_docs:BuildRequires: xmlto docbook-dtds docbook-style-xsl}
%{?_enable_installed_tests:BuildRequires: /proc fuse3 pipewire
BuildRequires: python3-module-pytest python3-module-pygobject3
BuildRequires: python3-module-dbus python3-module-dbusmock}

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces known as
portals under a well-known name (org.freedesktop.portal.Desktop) and object
path (/org/freedesktop/portal/desktop). The portal interfaces include APIs for
file access, opening URIs, printing and others.

%package devel
Summary: Development files for %name
Group: Development/C
BuildArch: noarch
Requires: %name = %EVR

%description devel
The pkg-config file for %name.

%package tests
Summary: Tests for the %name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name.

%prep
%setup
sed -i 's/pytest-3/py.test-3/' tests/meson.build

%build
%meson \
    %{?_disable_docs:-Ddocbook-docs=disabled} \
    %{?_enable_installed_tests:-Dinstalled-tests=true}
%nil
%meson_build

%install
%meson_install
# directory for portals such as xdg-desktop-portal-gtk
install -d -m755 %buildroot/%_datadir/%name/portals
%find_lang %name

%check
%__meson_test -t 4

%files -f %name.lang
%_libexecdir/%name
%_libexecdir/xdg-document-portal
%_libexecdir/xdg-permission-store
%_libexecdir/%name-validate-icon
%_libexecdir/%name-rewrite-launchers
%_datadir/dbus-1/interfaces/org.freedesktop.portal.*.xml
%_datadir/dbus-1/interfaces/org.freedesktop.impl.portal.*.xml
%_datadir/dbus-1/services/org.freedesktop.portal.Desktop.service
%_datadir/dbus-1/services/org.freedesktop.portal.Documents.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%_datadir/%name/
%_userunitdir/%name.service
%_userunitdir/xdg-document-portal.service
%_userunitdir/xdg-permission-store.service
%_userunitdir/%name-rewrite-launchers.service
%doc README.md NEWS
%{?_enable_docs:%doc %_docdir/%name}

%files devel
%_datadir/pkgconfig/%name.pc

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif

%changelog
* Tue Dec 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0 (ported to Meson build system)
- new -tests subpackage

* Sun Sep 04 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Wed Aug 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.6-alt1
- 1.14.6

* Tue Jul 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.5-alt1
- 1.14.5

* Thu May 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Fri Apr 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Wed Mar 30 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Dec 23 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Wed Dec 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Sep 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Jul 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt2.1
- disabled check

* Sun Apr 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt2
- updated to 1.8.1-3-g89d2197

* Thu Feb 18 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2
- enabled %%check

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt2
- updated to 1.6.0-18-g552a4f3
- built against pipewire-0.3

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

