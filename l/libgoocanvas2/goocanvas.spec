%define ver_major 2.0
%define api_ver 2.0
%define _name goocanvas
%def_disable static
%def_enable python
%def_enable introspection

Name: lib%{_name}2
Version: %ver_major.1
Release: alt1
Summary: A canvas widget for GTK+3 that uses cairo for drawing

Group: System/Libraries
License: LGPLv2+
Url: http://live.gnome.org/GooCanvas
Source: %_name-%version.tar.xz

BuildPreReq: rpm-build-gnome
# From configure.in
BuildPreReq: libgtk+3-devel >= 3.2.0
BuildPreReq: glib2-devel >= 2.28.0
BuildPreReq: libcairo-devel >= 1.10.0
BuildRequires: gtk-doc
%{?_enable_python:BuildRequires: python-module-pygobject-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%package devel
Group: Development/C
Summary: A new canvas widget for GTK+3 that uses cairo for drawing
Requires: %name = %version-%release

%description devel
GooCanvas is a canvas widget for GTK+3 that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

These are the files used for development.

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %name.

%package gir
Summary: GObject introspection data for the GooCanvas library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
This package provides GObject introspection data for the GooCanvas
library.

%package gir-devel
Summary: GObject introspection devel data for the GooCanvas library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
This package provides GObject introspection devel data for the GooCanvas
library.

%package -n python-module-%{_name}2
Summary: Python module for %name
Group: Development/Python

%description -n python-module-%{_name}2
GooCanvas is a canvas widget for GTK+3 that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

This package provides Python language bindings for for the GooCanvas library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure %{subst_enable static} \
	--enable-gtk-doc
%make_build


%install
%make_install DESTDIR=%buildroot install

%find_lang %{_name}2

%files -f %{_name}2.lang
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README TODO

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GooCanvas-%api_ver.typelib

%files gir-devel
%_girdir/GooCanvas-%api_ver.gir
%endif

%if_enabled python
%files -n python-module-%{_name}2
%python_sitelibdir/gi/overrides/*
%endif


%changelog
* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus

