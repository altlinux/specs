%def_disable snapshot

%define ver_major 3.0
%define api_ver_major 3
%define api_ver 3.0
%define _name goocanvas
%def_disable static
%def_enable python
%def_enable introspection
%def_enable gtk_doc

Name: lib%_name%api_ver_major
Version: %ver_major.0
Release: alt1

Summary: A canvas widget for GTK+3 that uses cairo for drawing
Group: System/Libraries
License: LGPL-2.0
Url: http://live.gnome.org/GooCanvas

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/goocanvas.git
Source: %_name-%version.tar
%endif

BuildRequires: libgtk+3-devel >= 3.2.0
BuildRequires: glib2-devel >= 2.28.0
BuildRequires: libcairo-devel >= 1.10.0
BuildRequires: gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_python:
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pygobject3-devel}

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%package devel
Group: Development/C
Summary: A new canvas widget for GTK+3 that uses cairo for drawing
Requires: %name = %EVR

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
Requires: %name = %EVR

%description gir
This package provides GObject introspection data for the GooCanvas
library.

%package gir-devel
Summary: GObject introspection devel data for the GooCanvas library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
This package provides GObject introspection devel data for the GooCanvas
library.

%package -n python3-module-%_name%api_ver_major
Summary: Python module for %name
Group: Development/Python3

%description -n python3-module-%_name%api_ver_major
GooCanvas is a canvas widget for GTK+3 that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

This package provides Python3 language bindings for for the GooCanvas library.

%prep
%setup -n %_name-%version

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	PYTHON=%__python3
%nil
%make_build

%install
%makeinstall_std

%find_lang %_name%api_ver_major

%files -f %_name%api_ver_major.lang
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README TODO

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GooCanvas-%api_ver.typelib

%files gir-devel
%_girdir/GooCanvas-%api_ver.gir
%endif

%if_enabled python
%files -n python3-module-%_name%api_ver_major
%python3_sitelibdir/gi/overrides/*
%endif


%changelog
* Sat Jan 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- goocanvas-2.0 -> goocanvas-3.0

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Thu Aug 31 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sun Nov 03 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1.1
- updated from upstream git

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus

