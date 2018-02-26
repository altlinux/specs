%define _name colord
%def_enable introspection
%def_enable vala

Name: lib%_name-gtk
Version: 0.1.22
Release: alt1

Summary: GTK+3 support library for colord daemon
License: GPLv2+
Group: System/Libraries

URL: http://www.freedesktop.org/software/%name/
Source: http://www.freedesktop.org/software/%name/releases/%_name-gtk-%version.tar.xz

%define glib_ver 2.31
%define lcms_ver 2.2
%define colord_ver 0.1.22

Requires: lib%_name >= %colord_ver

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: liblcms2-devel >= %lcms_ver
BuildRequires: lib%_name-devel >= %colord_ver libgtk+3-devel
BuildRequires: gtk-doc intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel lib%_name-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools lib%_name-vala}

%description
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides GTK+3 library for interaction with colord.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides development files for the %_name-gtk library.

%package gir
Summary: GObject introspection data for the %_name-gtk  library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name-gtk library.

%package gir-devel
Summary: GObject introspection devel data for the %_name-gtk library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name-gtk library.

%package vala
Summary: Vala Bindings for %_name-gtk
Group: Development/C
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for %_name-gtk library.

%prep
%setup -n %_name-gtk-%version

%build
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std

%find_lang %_name-gtk

%files  -f %_name-gtk.lang
%_libdir/%name.so.*

%files devel
%_includedir/%_name-1/%_name-gtk.h
%_includedir/%_name-1/%_name-gtk/
%_libdir/%name.so
%_libdir/pkgconfig/%_name-gtk.pc

%if_enabled introspection
%files gir
%_typelibdir/ColordGtk-1.0.typelib

%files gir-devel
%_girdir/ColordGtk-1.0.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/%_name-gtk.vapi
%endif


%changelog
* Sun Jul 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.22-alt1
- first build for Sisyphus

