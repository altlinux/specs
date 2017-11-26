%define _name mypaint
%define ver_major 1.3
%define api_ver %ver_major

%def_disable gegl

Name: lib%_name
Version: %ver_major.0
Release: alt3

Summary: The brush library used by MyPaint
Group: System/Libraries
License: BSD
Url: https://github.com/%_name/%name

Source: %url/archive/%name-%version.tar.gz

BuildRequires: intltool libjson-c-devel
BuildRequires: gobject-introspection-devel
%{?_enable_gegl:BuildRequires: libgegl0.3-devel libgegl0.3-gir-devel}

%description
%name, a.k.a. "brushlib", is a library for making brushstrokes which
is used by MyPaint and other projects.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
%name, a.k.a. "brushlib", is a library for making brushstrokes which
is used by MyPaint and other projects.

This package provides development files for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
%name, a.k.a. "brushlib", is a library for making brushstrokes which
is used by MyPaint and other projects.

This package provides GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
%name, a.k.a. "brushlib", is a library for making brushstrokes which
is used by MyPaint and other projects.

This package provides GObject introspection devel data for %name.


%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{subst_enable gegl}

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%{?_enable_gegl:%_libdir/%name-gegl.so.*}

%files devel
%_includedir/%name/
%{?_enable_gegl:%_includedir/%name-gegl/}
%_libdir/*.so
%_pkgconfigdir/%name.pc
%{?_enable_gegl:%_pkgconfigdir/%name-gegl.pc}

%files gir
%_typelibdir/MyPaint-%api_ver.typelib
%{?_enable_gegl:%_typelibdir/MyPaintGegl-%api_ver.typelib}

%files gir-devel
%_girdir/MyPaint-%api_ver.gir
%{?_enable_gegl:%_girdir/MyPaintGegl-%api_ver.gir}

%changelog
* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt3
- fixed buildreqs

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt2
- rebuilt against libjson-c.so.2

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus

