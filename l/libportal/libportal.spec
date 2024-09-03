%def_disable snapshot

%define ver_major 0.8
%define api_ver_major 1
%define api_ver %api_ver_major.0
%define soname 0
%define namespace Xdp
%define xdg_name org.gnome.Portal

%def_enable introspection
%def_enable vala
%def_enable docs
%def_enable test
%def_enable check

Name: libportal
Version: %ver_major.0
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

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir} %{?_enable_vala:rpm-build-vala}
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools
BuildRequires: pkgconfig(Qt6Core) pkgconfig(Qt6Gui) pkgconfig(Qt6Widgets)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Gtk) = 3.0 gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_test:BuildRequires: libgtk+3-devel libgjs-devel pkgconfig(gstreamer-audio-1.0)}
%{?_enable_check:BuildRequires: xvfb-run
BuildRequires: pkgconfig(Qt5Test) pkgconfig(Qt6Test)
#BuildRequires: python3(pytest) python3(dbus) python3(dbusmock)
}

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

%package qt6
Summary: Portal API wrappers (QT6)
Group: System/Libraries
Requires: %name = %EVR

%description qt6
%name-qt6 provides Portal API wrapper library for QT6.

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

%package qt6-devel
Summary: Development files and libraries for %name-qt6
Group: Development/C++
Requires: %name-qt6 = %EVR
Requires: %name-devel = %EVR

%description qt6-devel
This package provides files for development with %name-qt6.

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
sed -i 's|pytest-3|py.test3|' tests/meson.build

%ifarch %e2k
# workaround for EDG frontend
sed -E -i 's/g_autofree ([ a-z]*) \*/g_autofree_edg(\1) /' \
    libportal/portal-qt{5,6}.cpp
%endif

%build
%meson \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool vala vapi} \
    %{subst_enable_meson_bool test portal-tests}
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

%files qt6
%_libdir/%name-qt6.so.*

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

%files qt6-devel
%_includedir/%name-qt6
%_libdir/%name-qt6.so
%_pkgconfigdir/%name-qt6.pc


%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%files gtk3-gir
%_typelibdir/%{namespace}Gtk3-%api_ver.typelib

%files gtk3-gir-devel
%_girdir/%{namespace}Gtk3-%api_ver.gir

%files gtk4-gir
%_typelibdir/%{namespace}Gtk4-%api_ver.typelib

%files gtk4-gir-devel
%_girdir/%{namespace}Gtk4-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/%name-%api_ver_major
%endif

%if_enabled test
%files tests
%_bindir/portal-test-gtk3
%_bindir/portal-test-qt5
%_bindir/portal-test-qt6
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
* Tue Sep 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.8.0-alt1
- 0.8.0
- new -qt6{,-devel} subpackages

* Thu Mar 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.7.1-alt1.1
- fixed build for %%e2k (ilyakurdyukov@)

* Sun Sep 10 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.7.1-alt1
- 0.7.1

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

