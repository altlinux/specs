%define _name gfbgraph
%define ver_major 0.2
%define api_ver 0.2
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major.3
Release: alt0.1

Summary: A GObject library for Facebook Graph API
License: %lgpl2plus
Group: System/Libraries
Url: http://developer.gnome.org/

#Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Source: %name-%version.tar

%define glib_ver 2.31.2

BuildPreReq: rpm-build-gnome rpm-build-licenses gnome-common gtk-doc
BuildPreReq: glib2-devel >= %glib_ver
BuildRequires: libjson-glib-devel librest-devel libsoup-devel
BuildRequires: libgnome-online-accounts-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 1.30 librest-gir-devel libjson-glib-gir-devel libsoup-gir-devel}

%description
LibGFBGraph is a GObject library for Facebook Graph API.

%package devel
Summary: Development environment for LibGFBGraph
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop with
LibGFBGraph library.


%package devel-doc
Summary: Development documentation for LibGFBGraph
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for LibGFBGraph library.

%package gir
Summary: GObject introspection data for the LibGFBGraph library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the LibGFBGraph library

%package gir-devel
Summary: GObject introspection devel data for the LibGFBGraph library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the LibGFBGraph library.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang %name

%check
#%make check

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GFBGraph-%api_ver.typelib

%files gir-devel
%_girdir/GFBGraph-%api_ver.gir
%endif

%changelog
* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt0.1
- first build for Sisyphus


