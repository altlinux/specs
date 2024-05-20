%define _name gupnp-dlna
%define ver_major 0.12
%define namespace GUPnPDLNA
%define api_ver 2.0

%def_enable introspection
%def_enable vala
%def_enable gtk_doc

Name: libgupnp-dlna
Version: %ver_major.0
Release: alt2
Summary: GUPnP DLNA library

Group: System/Libraries
License: LGPL-2.0-or-later
Url: http://www.gupnp.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio-devel >= 2.58 pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires: pkgconfig(gstreamer-1.0) >= 1.0 pkgconfig(gstreamer-pbutils-1.0) >= 1.0
%{?_enable_introspection:
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.36.0 /usr/bin/g-ir-scanner
BuildRequires: gir(GObject) = 2.0 gir(Gst) = 1.0 gir(GstPbutils) = 1.0}
%{?_enable_vala:
BuildRequires: vala-tools >= 0.18 rpm-build-vala libvala-devel
BuildRequires: vapi(libxml-2.0) vapi(gstreamer-pbutils-1.0)
BuildRequires: vapi(gstreamer-1.0) vapi(gstreamer-base-1.0) vapi(gstreamer-video-1.0)}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP DLNA is a collection of helpers for building DLNA (Digital
Living Network Alliance) compliant applications using GUPnP.

%package devel
Summary: Development package for %_name
Group: Development/Other
Requires: %name = %EVR

%description devel
Contains libraries and header files for developing applications that
use %_name.

%package gir
Summary: GObject introspection data for the %_name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name

%package gir-devel
Summary: GObject introspection devel data for the %_name
Group: System/Libraries
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %_name

%package devel-doc
Summary: Development package for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %_name.

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/*
%_libdir/lib*.so.*
%_datadir/%{_name}*
%_libdir/%_name/*.so
%doc AUTHORS NEWS README TODO

%files devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/*
%{?_enable_vala:
%_vapidir/*.deps
%_vapidir/*.vapi}

%if_enabled introspection
%files gir
%_typelibdir/%{namespace}*-%api_ver.typelib

%files gir-devel
%_girdir/%{namespace}*-%api_ver.gir
%endif

%{?_enable_gtk_doc:%files devel-doc
%_datadir/gtk-doc/html/*}

%changelog
* Mon May 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt2
- switched to Meson build system

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Thu Jul 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sun Apr 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt2
- fixed buildreqs

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.3-alt1
- 0.10.3

* Thu Jun 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Fri Mar 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed Dec 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- upstream snapshot (990d1bec2d39f42dfef04527464b784f57120837)
- add GObject packages

* Tue May 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
