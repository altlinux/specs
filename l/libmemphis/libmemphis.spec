%define _name memphis
%define ver_major 0.2
%define api_ver 0.2
%def_disable static

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: Map-rendering library for OpenStreetMap
License: LGPL2.1+
Group: System/Libraries
Url: http://trac.openstreetmap.ch/trac/memphis/

Source: http://wenner.ch/files/public/mirror/memphis/%_name/%_name-%version.tar.gz

BuildRequires: glib2-devel libexpat-devel libcairo-devel
BuildRequires: libvala-devel vala-tools gobject-introspection-devel
BuildRequires: gtk-doc

%description
Memphis is a map-rendering application and a library for OpenStreetMap
written in C using eXpat, Cairo and GLib.

%package devel
Group: Development/C
Summary: Development files of Memphis
Provides: %_name-devel = %version-%release
Requires: %name = %version-%release

%description devel
Memphis is a map-rendering application and a library for OpenStreetMap.

This package contains the C headers and libraries required for building
programs with Memphis shared library.

%package gir
Summary: GObject introspection data for the Memphis library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Memphis library.

%package gir-devel
Summary: GObject introspection devel data for the Memphis library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Memphis library.

%package devel-doc
Summary: Development documentation for Memphis
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for Memphis library.

%package devel-static
Group: Development/C
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description devel-static
Memphis is a map-rendering application and a library for OpenStreetMap.

This package contains the static library required for statically linking
applications with Memphis library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name-%api_ver.so.*
%_datadir/%_name/
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
#%_datadir/vala/vapi/%_name-%api_ver.vapi

%files gir
%_typelibdir/Memphis-%api_ver.typelib

%files gir-devel
%_girdir/Memphis-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%name/

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- first build for Sisyphus

