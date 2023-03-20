%define ver_major 1.6
%define api_ver 1
%define _name d-spy
%define xdg_name org.gnome.dspy

%def_enable tests
%def_disable check

Name: dspy
Version: %ver_major.0
Release: alt1

Summary: A tool to discover and explore D-Bus services
Group: Development/Tools
License: GPL-3.0
Url: https://wiki.gnome.org/Apps/Builder

Vcs: https://gitlab.gnome.org/GNOME/d-spy.git
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Requires: lib%name = %EVR
Requires: dbus-tools-gui

%define glib_ver 2.68
%define gtk4_ver 4.6
%define libadwaita_ver 1.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %libadwaita_ver
#%{?_enable_tests:BuildRequires:}

%description
D-Spy is a tool to explore and test end-points and interfaces on the
System or Session D-Bus. You can also connect to D-Bus peers by address.
D-Spy was originally part of GNOME Builder.

%package -n lib%name
Summary: Library for the %name project
License: LGPL-3.0
Group: System/Libraries

%description -n lib%name
D-Spy is a tool to explore and test end-points and interfaces on the
System or Session D-Bus.

This package provides shared library for D-Spy.

%package -n lib%name-devel
Summary: Development files for D-Spy
License: LGPL-3.0
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
D-Spy is a tool to explore and test end-points and interfaces on the
System or Session D-Bus.

This package provides development files for D-Spy library.


%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%xdg_name.appdata.xml

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Jul 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- first build for Sisyphus


