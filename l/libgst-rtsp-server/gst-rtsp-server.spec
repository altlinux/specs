%define _name gst-rtsp-server
%define ver_major 1.12
%define gst_api_ver 1.0
%define api_ver 1.0

%def_enable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major.4
Release: alt1

Summary: GStreamer-%api_ver RTSP server library
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/modules/%_name-server.html

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

%define glib_ver 2.32.0
%define gst_ver 1.6.1

Requires: gst-plugins-base%api_ver >= %gst_ver gst-plugins-good%api_ver gst-plugins-bad%api_ver

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: gstreamer gstreamer%api_ver-devel >= %gst_ver
BuildPreReq: gst-plugins%api_ver-devel >= %gst_ver gst-plugins-good%api_ver gst-plugins-bad%api_ver-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel gst-plugins%api_ver-gir-devel
BuildRequires: libcgroup-devel

%description
A GStreamer-based RTSP server library.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for the GStreamer RTSP server library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides developer documentation for %name.

%package gir
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GStreamer RTSP server library.

%package gir-devel
Summary: GObject introspection devel data for %_name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GStreamer RTSP server library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable introspection} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%files
%_libdir/libgstrtspserver-%api_ver.so.*
%_libdir/gstreamer-%gst_api_ver/libgstrtspclientsink.so
%doc README TODO NEWS

%exclude %_libdir/gstreamer-%gst_api_ver/*.la

%files devel
%_includedir/gstreamer-%api_ver/gst/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/

%files gir
%_typelibdir/GstRtspServer-%api_ver.typelib

%files gir-devel
%_girdir/GstRtspServer-%api_ver.gir


%changelog
* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- first build for Sisyphus

