%def_enable snapshot
%define _name farstream
%define api_ver 0.2
%define gst_api_ver 1.0
%define gupnp_api_ver 1.2

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_disable check

Name: %_name%api_ver
Version: 0.2.9.1
Release: alt0.3

Summary: A audio/video conferencing framework (0.2)
Group: System/Libraries
License: LGPL-2.1-or-later
Url: http://www.freedesktop.org/wiki/Software/Farstream

%if_disabled snapshot
Source: http://freedesktop.org/software/%_name/releases/%_name/%_name-%version.tar.gz
%else
Vcs: https://gitlab.freedesktop.org/farstream/farstream.git
Source: %_name-%version.tar
%endif
#https://gitlab.freedesktop.org/farstream/farstream/-/merge_requests/7
Patch: farstream-0.2.9-up-drop_volatile_qualifiers.patch

%define nice_ver 0.1.8
%define gst_ver 1.4
%define glib_ver 2.32

#Obsoletes: farsight2
Conflicts: farsight2

Requires: lib%name = %version-%release
Requires: gst-plugins-nice%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver

BuildRequires(pre): rpm-build-python3
BuildRequires: libgio-devel >= %glib_ver libnice-devel >= %nice_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: libgupnp-igd-devel gtk-doc
BuildRequires: python3-dev python3-module-gst%gst_api_ver python3-module-pygobject3-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgstreamer%gst_api_ver-gir-devel}
%{?_enable_check:BuildRequires: libgupnp%gupnp_api_ver-devel}

%description
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

This package provides Farstream-0.2 for GStreamer-1.0

%package -n lib%name
Summary: Farstream libraries
Group: System/Libraries

%description -n lib%name
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

This package provides shared Farstream (0.2 API version) library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

The lib%name-devel package contains libraries and header files for
developing applications that use Farstream.

%package -n lib%name-gir
Summary: GObject introspection data for the Farstream
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Farstream library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Farstream
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Farstream library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description devel-doc
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

This package provides development documentation for the Farstream library.

%prep
%setup -n %_name-%version
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	PYTHON=%__python3
%nil
#SMP-incomaptible build
%make

%install
%makeinstall_std

%check
%make check

%files
%_libdir/gstreamer-%gst_api_ver/libfsrawconference.so
%_libdir/gstreamer-%gst_api_ver/libfsrtpxdata.so
%_libdir/gstreamer-%gst_api_ver/libfsrtpconference.so
%_libdir/gstreamer-%gst_api_ver/libfsvideoanyrate.so
%_datadir/%_name/%api_ver/
%doc AUTHORS NEWS

%files -n lib%name
%_libdir/lib%_name-%api_ver.so.*
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/libmulticast-transmitter.so
%_libdir/%_name-%api_ver/libnice-transmitter.so
%_libdir/%_name-%api_ver/librawudp-transmitter.so
%_libdir/%_name-%api_ver/libshm-transmitter.so

%files -n lib%name-devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-gir
%_typelibdir/Farstream-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Farstream-%api_ver.gir

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%exclude %_libdir/%_name-%api_ver/*.la
%exclude %_libdir/gstreamer-%gst_api_ver/*.la


%changelog
* Sat Oct 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.9.1-alt0.3
- fixed build with GCC11

* Thu Apr 22 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.9.1-alt0.2
- updated to 0.2.9-5-ge70dcd0a (ported to gupnp-1.2)

* Sat Aug 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.9.1-alt0.1
- updated to 0.2.9-4-g46d7b108 (fixed build with GNU Make-4.3)

* Sun Mar 15 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Sat Jun 04 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8

* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Tue May 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Thu Nov 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.91-alt1
- 0.1.91

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- new lib%%name, lib%%name-devel, python-module-%%name subpackages

* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt2
- Conflicts with farsight2 (ALT #27058)

* Sun Feb 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

