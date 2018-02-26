%define api_ver 0.1
%define gst_api_ver 0.10

%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: farstream
Version: 0.1.2
Release: alt1

Summary: A audio/video conferencing framework
Group: System/Libraries
License: LGPLv2.1+
URL: http://www.freedesktop.org/wiki/Software/Farstream

Source: http://freedesktop.org/software/%name/releases/%name/%name-%version.tar.gz
Patch: %name-0.1.1-alt-python_link.patch

%define nice_ver 0.1.0
%define gst_ver 0.10.36
%define glib_ver 2.30

#Obsoletes: farsight2
Conflicts: farsight2

Requires: gst-plugins-nice gst-plugins-good gst-plugins-bad

BuildRequires: libgio-devel >= %glib_ver libnice-devel >= %nice_ver
BuildRequires: gst-plugins-devel  >= %gst_ver
BuildRequires: libgupnp-igd-devel gtk-doc
BuildRequires: rpm-build-python python-module-gst-devel python-module-pygobject-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel gstreamer-gir-devel}

%description
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

The %name-devel package contains libraries and header files for
developing applications that use Farstream.

%package devel-doc
Summary: Development files for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

The %name-devel-doc package contains documentation for developing
applications that use Farstream.

%package -n lib%name-gir
Summary: GObject introspection data for the Farstream
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Farstream library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Farstream
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: %name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Farstream library.

%prep
%setup -q
%patch

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/lib%name-%api_ver.so.*
%dir %_libdir/%name-%api_ver
%_libdir/%name-%api_ver/libmulticast-transmitter.so
%_libdir/%name-%api_ver/libnice-transmitter.so
%_libdir/%name-%api_ver/librawudp-transmitter.so
%_libdir/%name-%api_ver/libshm-transmitter.so
%_libdir/gstreamer-%gst_api_ver/libfsfunnel.so
%_libdir/gstreamer-%gst_api_ver/libfsmsnconference.so
%_libdir/gstreamer-%gst_api_ver/libfsrawconference.so
%_libdir/gstreamer-%gst_api_ver/libfsrtcpfilter.so
%_libdir/gstreamer-%gst_api_ver/libfsrtpconference.so
%_libdir/gstreamer-%gst_api_ver/libfsvideoanyrate.so
%python_sitelibdir/*.so
%_datadir/%name/
%doc AUTHORS ChangeLog

%exclude %_libdir/%name-%api_ver/*.la
%exclude %_libdir/gstreamer-%gst_api_ver/*.la
%exclude %python_sitelibdir/*.la

%files devel
%_includedir/%name-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/*

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n lib%name-gir
%_typelibdir/Farstream-0.1.typelib

%files -n lib%name-gir-devel
%_girdir/Farstream-0.1.gir

%changelog
* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt2
- Conflicts with farsight2 (ALT #27058)

* Sun Feb 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

