%def_enable snapshot

%define _name gupnp-av
%define ver_major 0.14
%define api_ver 1.0

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable check

Name: libgupnp-av
Version: %ver_major.1
Release: alt2

Summary: A library to handle UPnP A/V profiles
Group: System/Libraries
License: LGPL-2.1
Url: http://www.gupnp.org/

Vcs: https://gitlab.gnome.org/GNOME/gupnp-av.git
%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson glib2-devel >= 2.58 libxml2-devel
%{?_enable_introspection:
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel}
%{?_enable_vala:
BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
gUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The gUPnP API is intended to be easy to use, efficient and flexible.

GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles

%package devel
Summary: Development files and libraries for gUPnP-IGD
Group: Development/C
Requires: %name = %EVR

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
Requires: %name = %EVR

%description gir
GObject introspection data for the GUPnP A/V library

%package gir-devel
Summary: GObject introspection devel data for the GUPnP A/V library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the GUPnP A/V library


%prep
%setup -n %_name-%version

%build
%ifarch %e2k
%add_optflags -Wno-error=deprecated-declarations
%endif
%meson \
%{?_disable_introspection:-Dintrospection=false} \
%{?_disable_vala:-Dvapi=false} \
%{?_enable_gtk_doc:-Dgtk_doc=true}
%nil
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/*.so.*
%doc AUTHORS README* NEWS
%_datadir/%_name

%files devel
%_pkgconfigdir/*
%_libdir/*.so
%_includedir/*
%{?_enable_vala:%_vapidir/*.deps
%_vapidir/*.vapi}

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GUPnPAV-%api_ver.typelib

%files gir-devel
%_girdir/GUPnPAV-%api_ver.gir
%endif


%changelog
* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt2
- updated to 0.14.1-9-g1e10a41 (fixed build with libxml2-2.12.x)

* Fri Jun 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Mon Aug 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1
- fixed build for %%e2k

* Thu Jul 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0 (ported to Meson build system)

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.12.11-alt1
- 0.12.11

* Sat Oct 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt1
- 0.12.10

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12.9-alt1
- 0.12.9
- updated buildreqs

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- 0.12.8

* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Mon Feb 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Sun Jun 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.11.5-alt1
- 0.11.5

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

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

