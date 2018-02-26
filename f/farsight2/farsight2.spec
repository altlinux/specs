%def_disable static
%def_disable gtk_doc

Name: farsight2
Version: 0.0.31
Release: alt1

Summary: A audio/video conferencing framework
Group: System/Libraries
License: LGPLv2+
URL: http://farsight.freedesktop.org/

Source: http://farsight.freedesktop.org/releases/farsight2/farsight2-%version.tar.gz
Patch: farsight2-0.0.30-alt-python_link.patch

%define nice_ver 0.1.0
%define tp_glib_ver 0.7.34
%define gst_ver 0.10.33

Requires: gst-plugins-nice gst-plugins-good gst-plugins-bad

BuildPreReq: libnice-devel >= %nice_ver
BuildPreReq: libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: gst-plugins-devel  >= %gst_ver
BuildRequires: libgupnp-igd-devel gtk-doc
BuildRequires: rpm-build-python python-module-gst-devel python-module-pygobject-devel

%description
Farsight 2 is a collection of GStreamer modules and libraries for
videoconferencing.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Farsight 2 is a collection of GStreamer modules and libraries for
videoconferencing.

The %name-devel package contains libraries and header files for
developing applications that use Farsight 2.

%package devel-doc
Summary: Development files for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Farsight 2 is a collection of GStreamer modules and libraries for
videoconferencing.

The %name-devel-doc package contains documentation for developing
applications that use Farsight 2.

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
%_libdir/*.so.*
%dir %_libdir/%name-0.0
%_libdir/%name-0.0/libmulticast-transmitter.so
%_libdir/%name-0.0/libnice-transmitter.so
%_libdir/%name-0.0/librawudp-transmitter.so
%_libdir/%name-0.0/libshm-transmitter.so
%_libdir/gstreamer-*/libfsfunnel.so
%_libdir/gstreamer-*/libfsmsnconference.so
%_libdir/gstreamer-*/libfsrawconference.so
%_libdir/gstreamer-*/libfsrtcpfilter.so
%_libdir/gstreamer-*/libfsrtpconference.so
%_libdir/gstreamer-*/libfsvideoanyrate.so
%python_sitelibdir/*.so
%_datadir/%name/
%doc AUTHORS ChangeLog

%exclude %_libdir/%name-0.0/*.la
%exclude %_libdir/gstreamer-*/*.la
%exclude %python_sitelibdir/*.la

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/gstreamer-*/gst/*

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.31-alt1
- 0.0.31

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.30-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.30-alt1
- 0.0.30

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.29-alt1
- 0.0.29

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.21-alt1
- 0.0.21
- don't requires gst-plugins-farsight

* Tue May 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.19-alt1
- 0.0.19

* Fri Jan 08 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.17-alt1
- 0.0.17

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.16-alt2
- rebuild against new lingupnp-igd

* Tue Nov 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.16-alt1
- 0.0.16

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.15-alt1
- 0.0.15

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.14-alt1
- 0.0.14

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.7-alt1
- 0.0.7

* Thu Dec 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- 0.0.6

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.0.4-alt1
- first build for Sisyphus

