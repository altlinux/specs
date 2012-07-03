%define _name gupnp-av
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: libgupnp-av
Version: 0.10.2
Release: alt1

Summary: A library to handle UPnP A/V profiles
Group: System/Libraries
License: LGPLv2+
Url: http://www.gupnp.org/

Source: http://www.gupnp.org/sources/%_name/%_name-%version.tar.xz

BuildPreReq: libgupnp-devel >= 0.17.0
BuildRequires: glib2-devel >= 2.14 gtk-doc
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgupnp-gir-devel}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles

%package devel
Summary: Development files and libraries for gUPnP-IGD
Group: Development/C
Requires: %name = %version-%release

%description devel
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.
This package provides files for development with gUPnP-AV.

%package devel-doc
Summary: Development documentaion for gUPnP-AV
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.
This package provides development documentations for gUPnP-AV.

%package gir
Summary: GObject introspection data for the GUPnP A/V library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GUPnP A/V library

%package gir-devel
Summary: GObject introspection devel data for the GUPnP A/V library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GUPnP A/V library


%prep
%setup -q -n %_name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure --disable-static \
%{?_enable_gtk_doc:--enable-gtk-doc} \
%{subst_enable introspection}

%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

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
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Fri Apr 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Tue May 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Aug 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Tue Jul 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6
- %%check section

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5
- introspection support

* Wed Mar 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed Dec 16 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus

