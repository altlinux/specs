%define _name gupnp-igd
%define ver_major 0.2
%define api_ver 1.0
%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable python

Name: libgupnp-igd
Version: %ver_major.5
Release: alt1

Summary: A library to handle UPnP IGD port mapping
Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildPreReq: libgupnp-devel >= 0.13.2
BuildRequires: glib2-devel >= 2.14 gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgupnp-gir-devel}
%{?_enable_python:BuildRequires: python-module-pygobject-devel python-module-pygtk-devel}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%name is a library to handle UPnP IGD port mapping.

%package devel
Summary: Development files and libraries for gUPnP-IGD
Group: Development/C
Requires: %name = %version-%release

%description devel
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%name is a library to handle UPnP IGD port mapping.
This package provides files for development with gUPnP-IGD.

%package devel-doc
Summary: Development documentaion for gUPnP-IGD
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%name is a library to handle UPnP IGD port mapping.
This package provides development documentations for gUPnP-IGD.

%package gir
Summary: GObject introspection data for the gUPnP-IGD library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the gUPnP-IGD library

%package gir-devel
Summary: GObject introspection devel data for the gUPnP-IGD library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the gUPnP-IGD library

%package -n python-module-%name
Summary: Python bindings for gUPnP-IGD
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%name is a library to handle UPnP IGD port mapping.
This package provides Python bindings for gUPnP-IGD

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable python}

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/*.so.*
%doc AUTHORS README ChangeLog

%files devel
%_libdir/pkgconfig/*
%_libdir/*.so
%_includedir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GUPnPIgd-%api_ver.typelib

%files gir-devel
%_girdir/GUPnPIgd-%api_ver.gir
%endif

%files -n python-module-%name
%python_sitelibdir/gupnp/*

%exclude %python_sitelibdir/gupnp/*.la

%changelog
* Mon Nov 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Wed Oct 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Mon Dec 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Sat Nov 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.11-alt2.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt2
- rebuild against newest gssdp and gupnp

* Tue May 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt1
- 0.1.11

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt3
- rebuild for debuginfo

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt2
- rebuild for set-version

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7
- %%check section

* Tue Jan 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6
- python bindings packaged

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- new version

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

