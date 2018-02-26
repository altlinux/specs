%define _name mash
%define ver_major 0.2
%def_enable introspection

Name: lib%_name
Version: %ver_major.0
Release: alt2

Summary: A library for using real 3D models within a Clutter scene
Group: System/Libraries
License: LGPLv2+
Url: http://wiki.clutter-project.org/wiki/Mash

Source: http://source.clutter-project.org/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires: glib2-devel >= 2.16 libclutter-devel librply-devel libmx-devel >= 1.1.0 libgdk-pixbuf-devel gtk-doc
%{?_enable_introspection:BuildRequires: libclutter-gir-devel}

%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development of programs using %name.

%package gir
Summary: GObject introspection data for the Mash library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Mash library

%package gir-devel
Summary: GObject introspection devel data for the Mash library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Mash library

%package devel-doc
Summary: Development documentation for Mash
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for Mash library.

%prep
%setup -n %_name-%version

%build
export CFLAGS="$CFLAGS `pkg-config --cflags gdk-pixbuf-2.0`"
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/libmash-%ver_major.so.*
%doc README NEWS AUTHORS

%files devel
%_includedir/%_name-%ver_major/
%_libdir/lib%_name-%ver_major.so
%_libdir/pkgconfig/%_name-%ver_major.pc

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- rebuild against new cogl

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

