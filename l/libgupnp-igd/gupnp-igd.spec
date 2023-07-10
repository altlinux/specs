%def_disable snapshot

%define _name gupnp-igd
%define ver_major 1.6
%define api_ver 1.6
%define gupnp_api_ver 1.6
%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A library to handle UPnP IGD port mapping
Group: System/Libraries
License: LGPL-2.1
Url: http://www.gupnp.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define gupnp_ver 1.6.0
%define glib_ver 2.70

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson libgupnp%gupnp_api_ver-devel >= %gupnp_ver
BuildRequires: glib2-devel >= %glib_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgupnp%gupnp_api_ver-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

%name is a library to handle UPnP IGD port mapping.

%package devel
Summary: Development files and libraries for gUPnP-IGD
Group: Development/C
Requires: %name = %EVR

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
Requires: %name = %EVR

%description gir
GObject introspection data for the gUPnP-IGD library

%package gir-devel
Summary: GObject introspection devel data for the gUPnP-IGD library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the gUPnP-IGD library

%prep
%setup -n %_name-%version

%build
%meson \
	%{?_disable_introspection:-Dintrospection=false} \
	%{?_enable_gtk_doc:-Dgtk_doc=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test -v -t 2

%files
%_libdir/%name-%api_ver.so.*
%doc AUTHORS README NEWS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc

%{?_enable_gtk_doc:%files devel-doc
%_datadir/gtk-doc/html/*}

%if_enabled introspection
%files gir
%_typelibdir/GUPnPIgd-%api_ver.typelib

%files gir-devel
%_girdir/GUPnPIgd-%api_ver.gir
%endif


%changelog
* Thu Apr 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0 (ported to GUPnP-1.6)
- enabled %%check again

* Wed Jun 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1.2
- disabled %%check until
  https://gitlab.gnome.org/GNOME/gupnp/-/issues/12 will be fixed

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1.1
- made twice as much tests timeout 

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Mar 30 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt4
- updated to 0.2.5-21-g230402e (ported to Meson build system,
  removed python bindings)
- fixed buildreqs
- fixed license tag

* Mon Dec 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt3
- rebuilt aganst gupnp-1.2
- disabled python2 support
- enabled check

* Mon Jan 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt2
- updated to 0.2.5-3-gedd78a6 (fixed BGO #790165)

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

