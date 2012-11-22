%define _name farstream
%define api_ver 0.2
%define gst_api_ver 1.0

%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: %_name%api_ver
Version: 0.2.2
Release: alt1

Summary: A audio/video conferencing framework (0.2)
Group: System/Libraries
License: LGPLv2.1+
URL: http://www.freedesktop.org/wiki/Software/Farstream

Source: http://freedesktop.org/software/%_name/releases/%_name/%_name-%version.tar.gz

%define nice_ver 0.1.3
%define gst_ver 0.11.94
%define glib_ver 2.30

#Obsoletes: farsight2
Conflicts: farsight2

Requires: lib%name = %version-%release
Requires: gst-plugins-nice%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver

BuildRequires: libgio-devel >= %glib_ver libnice-devel >= %nice_ver
BuildRequires: gst-plugins%gst_api_ver-devel  >= %gst_ver
BuildRequires: libgupnp-igd-devel gtk-doc
BuildRequires: rpm-build-python python-module-gst-devel python-module-pygobject-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgstreamer%gst_api_ver-gir-devel}

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

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/gstreamer-%gst_api_ver/libfsmsnconference.so
%_libdir/gstreamer-%gst_api_ver/libfsrawconference.so
%_libdir/gstreamer-%gst_api_ver/libfsrtcpfilter.so
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
%_libdir/pkgconfig/*

%files -n lib%name-gir
%_typelibdir/Farstream-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Farstream-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%exclude %_libdir/%_name-%api_ver/*.la
%exclude %_libdir/gstreamer-%gst_api_ver/*.la


%changelog
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

