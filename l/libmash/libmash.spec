%define _name mash
%define ver_major 0.2
%def_enable introspection

Name: lib%_name
Version: %ver_major.1
Release: alt0.2

Summary: A library for using real 3D models within a Clutter scene
Group: System/Libraries
License: LGPLv2+
Url: https://github.com/clutter-project/mash

#VCS: git://github.com/clutter-project/mash.git
Source: %_name-%version.tar

BuildRequires: glib2-devel >= 2.16 libclutter-devel >= 1.2.0 librply-devel libgdk-pixbuf-devel gtk-doc
%{?_enable_introspection:BuildRequires: libclutter-gir-devel}
# for examples
BuildRequires: libmx-devel >= 1.1.0

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
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for Mash library.

%prep
%setup -n %_name-%version

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags gdk-pixbuf-2.0`"
%configure --disable-static --enable-gtk-doc
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
* Fri Sep 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt0.2
- rebuild against libcogl.so.15

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt0.1
- 0.2.1 snapshot

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- rebuild against new cogl

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

