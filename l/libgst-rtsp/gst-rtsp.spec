%define _name gst-rtsp
%def_enable introspection

Name: lib%_name
Version: 0.10.8
Release: alt1.1

Summary: GStreamer RTSP server library
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/modules/%_name-server.html

Source: http://people.freedesktop.org/src/%_name/%_name-%version.tar.bz2
Patch: gst-rtsp-0.10.8-alt-link.patch
Patch1: gst-rtsp-0.10.8-up-configure.patch

%define glib_ver 2.10.0
%define gst_ver 0.10.29

BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: gstreamer-devel >= %gst_ver
BuildPreReq: gst-plugins-devel >= %gst_ver
BuildRequires: gtk-doc
# for Python bindings
BuildRequires: python-module-gst-devel python-module-pygobject-devel
# fro Vala bindings
BuildRequires: libvala-devel >= 0.12.0
BuildRequires: gobject-introspection-devel gst-plugins-gir-devel

%description
A GStreamer-based RTSP server library with Python and Vala bindings.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for the GStreamer RTSP server library.

%package -n python-module-%_name
Summary: Python bindings for %_name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%_name
Python bindings for GStreamer RTSP server library.

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

%package vala
Summary: Vala bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description vala
Vala bindings for the GStreamer RTSP server library.

%prep
%setup -n %_name-%version
%patch
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable introspection}

%make_build

%install
make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc README TODO NEWS

%files devel
%_includedir/gstreamer-0.10/gst/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files -n python-module-%_name
%python_sitelibdir/gst-0.10/gst/*.so
%_datadir/%_name/
%exclude %python_sitelibdir/gst-0.10/gst/*.la

%files gir
%_typelibdir/GstRtspServer-0.10.typelib

%files gir-devel
%_girdir/GstRtspServer-0.10.gir

%files vala
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi


%changelog
* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.8-alt1.1
- Rebuild with Python-2.7

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt1
- 0.10.8
- new -gir{,-devel} subpackages

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.7-alt1
- 0.10.7

* Thu Jan 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- first build for Sisyphus

