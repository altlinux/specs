%define _name gst-rtsp-server
%define ver_major 1.4
%define api_ver 1.0

%def_enable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major.5
Release: alt1

Summary: GStreamer-%api_ver RTSP server library
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/modules/%_name-server.html

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

%define glib_ver 2.32.0
%define gst_ver 1.4.4

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: gstreamer%api_ver-devel >= %gst_ver
BuildPreReq: gst-plugins%api_ver-devel >= %gst_ver
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
%doc README TODO NEWS

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
* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- first build for Sisyphus

