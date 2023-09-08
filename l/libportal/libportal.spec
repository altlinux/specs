%def_disable snapshot

%define ver_major 0.7
%define api_ver_major 1
%define api_ver %api_ver_major.0
%define soname 0
%define xdg_name org.gnome.Portal

%def_enable introspection
%def_enable vala
%def_enable docs
%def_enable test
%def_enable check

Name: libportal
Version: %ver_major
Release: alt1
Epoch: 1

Summary: Flatpak portal library
Group: System/Libraries
License: LGPL-3.0
Url: https://github.com/flatpak/libportal

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.58

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel gir(Gtk) = 3.0 gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_test:BuildRequires: libgtk+3-devel libgjs-devel pkgconfig(gstreamer-audio-1.0)}
%{?_enable_check:BuildRequires: xvfb-run}

%description
%name provides GIO-style async APIs for most Flatpak portals.

%package gtk3
Summary: Portal API wrappers (GTK3)
Group: System/Libraries
Requires: %name = %EVR

%description gtk3
%name-gtk3 provides Portal API wrapper library for GTK3.

%package gtk4
Summary: Portal API wrappers (GTK4)
Group: System/Libraries
Requires: %name = %EVR

%description gtk4
%name-gtk4 provides Portal API wrapper library for GTK4.

%package qt5
Summary: Portal API wrappers (QT5)
Group: System/Libraries
Requires: %name = %EVR

%description qt5
%name-qt5 provides Portal API wrapper library for QT5.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%name provides GIO-style async APIs for most Flatpak portals.
This package provides files for development with %name.

%package gtk3-devel
Summary: Development files and libraries for %name-gtk3
Group: Development/C
Requires: %name-gtk3 = %EVR
Requires: %name-devel = %EVR

%description gtk3-devel
This package provides files for development with %name-gtk3.

%package gtk4-devel
Summary: Development files and libraries for %name-gtk4
Group: Development/C
Requires: %name-gtk4 = %EVR
Requires: %name-devel = %EVR

%description gtk4-devel
This package provides files for development with %name-gtk4.

%package qt5-devel
Summary: Development files and libraries for %name-qt5
Group: Development/C++
Requires: %name-qt5 = %EVR
Requires: %name-devel = %EVR

%description qt5-devel
This package provides files for development with %name-qt5.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Flatpak portal library

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the Flatpak portal library

%package gtk3-gir
Summary: GObject introspection data for %name-gtk3
Group: System/Libraries
Requires: %name-gir = %EVR

%description gtk3-gir
GObject introspection data for the GTK3 portal wrapper library.

%package gtk3-gir-devel
Summary: GObject introspection devel data for %name-gtk3
Group: Development/Other
BuildArch: noarch
Requires: %name-gtk3-devel = %EVR
Requires: %name-gtk3-gir = %EVR

%description gtk3-gir-devel
GObject introspection devel data for the GTK3 portal wrapper library.

%package gtk4-gir
Summary: GObject introspection data for %name-gtk4
Group: System/Libraries
Requires: %name-gir = %EVR

%description gtk4-gir
GObject introspection data for the GTK4 portal wrapper library.

%package gtk4-gir-devel
Summary: GObject introspection devel data for %name-gtk4
Group: Development/Other
BuildArch: noarch
Requires: %name-gtk4-devel = %EVR
Requires: %name-gtk4-gir = %EVR

%description gtk4-gir-devel
GObject introspection devel data for the GTK4 portal wrapper library.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
%name provides GIO-style async APIs for most Flatpak portals.

This package provides development documentations for %name.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR
Requires: %name-gtk3 = %EVR
Requires: %name-gtk4 = %EVR
Requires: %name-qt5 = %EVR
Requires: gst-plugins-base1.0

%description tests
This package provides portal-test application for checking functionality
of the installed %name.


%prep
%setup

%build
%meson \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_disable_vala:-Dvapi=false} \
    %{?_enable_test:-Dportal-tests=true}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_libdir/%name.so.*
%doc README*

%files gtk3
%_libdir/%name-gtk3.so.*

%files gtk4
%_libdir/%name-gtk4.so.*

%files qt5
%_libdir/%name-qt5.so.*

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%{?_enable_vala:%_vapidir/%name.deps
%_vapidir/%name.vapi}

%files gtk3-devel
%_includedir/%name-gtk3
%_libdir/%name-gtk3.so
%_pkgconfigdir/%name-gtk3.pc
%{?_enable_vala:%_vapidir/%name-gtk3.deps
%_vapidir/%name-gtk3.vapi}

%files gtk4-devel
%_includedir/%name-gtk4
%_libdir/%name-gtk4.so
%_pkgconfigdir/%name-gtk4.pc
%{?_enable_vala:%_vapidir/%name-gtk4.deps
%_vapidir/%name-gtk4.vapi}

%files qt5-devel
%_includedir/%name-qt5
%_libdir/%name-qt5.so
%_pkgconfigdir/%name-qt5.pc

%if_enabled introspection
%files gir
%_typelibdir/Xdp-%api_ver.typelib

%files gir-devel
%_girdir/Xdp-%api_ver.gir

%files gtk3-gir
%_typelibdir/XdpGtk3-%api_ver.typelib

%files gtk3-gir-devel
%_girdir/XdpGtk3-%api_ver.gir

%files gtk4-gir
%_typelibdir/XdpGtk4-%api_ver.typelib

%files gtk4-gir-devel
%_girdir/XdpGtk4-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/%name-%api_ver_major
%endif

%if_enabled test
%files tests
%_bindir/portal-test-gtk3
%_bindir/portal-test-qt
%_bindir/%{xdg_name}Test.Gtk4
%_desktopdir/%{xdg_name}Test.Gtk3.desktop
%_desktopdir/%{xdg_name}Test.Gtk4.desktop
%_datadir/dbus-1/services/org.gnome.PortalTest.Gtk3.service
%_datadir/dbus-1/services/org.gnome.PortalTest.Gtk4.service
%_datadir/%{xdg_name}Test.Gtk3/
%_datadir/%{xdg_name}Test.Gtk4/
%_datadir/portal-test-gtk4
%endif

%changelog
* Fri Sep 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.7-alt1
- 0.7

* Wed Mar 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1:0.6-alt1
- 0.6

* Wed Dec 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1:0.5-alt1
- 0.5
- new gtk{3,4},qt5 subpackages

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1:0.4-alt1
- 0.4

* Sat Dec 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.3-alt1
- 0.3

* Fri Dec 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.2-alt1
- 0.2
- new -tests subpackage

* Thu Nov 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.1-alt1
- 0.1

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.2-alt1
- first build for Sisyphus

