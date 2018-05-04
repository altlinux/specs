%define _name nice
%define ver_major 0.1
%define api_ver %ver_major
%define gst_api_ver 1.0
%define old_gst_api_ver 0.10

%def_disable static
%def_disable gtk_doc
%def_without old_gstreamer

Name: libnice
Version: %ver_major.14
Release: alt1.1

Summary: Connectivity Establishment standard (ICE) library
Group: System/Libraries
License: LGPLv2+/MPL
URL: http://nice.freedesktop.org

Source: http://nice.freedesktop.org/releases/%name-%version.tar.gz

%define glib_ver 2.44
%define tls_ver 2.12

BuildRequires: glib2-devel >= %glib_ver gtk-doc libgupnp-igd-devel
%{?_with_old_gstreamer:BuildRequires: gst-plugins-devel}
BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgnutls-devel

%description
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains files needed to develop applications using Nice

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for the Nice library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Nice library.

%package gir-devel
Summary: GObject introspection devel data for the Nice library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Nice library.

%package devel-static
Summary: Static library for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains a statically-linked variant of %name

%package -n gst-plugins-nice
Summary: UDP connectivity establishment plugin for Gstreamer based on libnice
Group: System/Libraries
Requires: %name = %version-%release

%description -n gst-plugins-nice
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package provides Interactive UDP connectivity establishment plugin
for Gstreamer

%package -n gst-plugins-nice%gst_api_ver
Summary: UDP connectivity establishment plugin for Gstreamer (1.0) based on libnice
Group: System/Libraries
Requires: %name = %version-%release

%description -n gst-plugins-nice%gst_api_ver
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package provides Interactive UDP connectivity establishment plugin
for Gstreamer (1.0 API version)

%prep
%setup

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_without_old_gstreamer:--without-gstreamer-0.10}

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README

%files devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files gir
%_typelibdir/Nice-%api_ver.typelib

%files gir-devel
%_girdir/Nice-%api_ver.gir

%if_with old_gstreamer
%files -n gst-plugins-nice
%_libdir/gstreamer-%old_gst_api_ver/libgstnice010.so
%endif

%files -n gst-plugins-nice%gst_api_ver
%_libdir/gstreamer-%gst_api_ver/libgstnice.so

%exclude %_libdir/gstreamer-*/*.la

# don't package tools
%exclude %_bindir/stun*
# and example progs
%exclude %_bindir/*example


%changelog
* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.14-alt1.1
- NMU: Rebuilt for e2k.

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- 0.1.14

* Wed Nov 18 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt2
- disabled build of GStreamer-0.10 plugin

* Wed May 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt1
- 0.1.13

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt1
- 0.1.11

* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8
- new gir{,-devel} subpackages

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3
- new gst-plugins-nice1.0 subpackage for GStreamer-1.0

* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0
- dropped obsolete libnice-Compatibility-with-OC2007-R2.patch

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt2
- rebuild for debuginfo

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1
- 0.0.13

* Tue May 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.12-alt1
- 0.0.12
- applied patch for compatibility with OC2007-R2 (shaba@)

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- 0.0.6

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.4-alt1
- 0.0.4

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- first build for Sisyphus

