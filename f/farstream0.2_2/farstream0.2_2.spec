%define _name farstream
%define api_ver 0.2
%define soname 2
%define gst_api_ver 1.0

%def_disable static
%def_disable gtk_doc
%def_disable introspection

Name: %_name%{api_ver}_%soname
Version: 0.2.4
Release: alt1

Summary: A audio/video conferencing framework (0.2)
Group: System/Libraries
License: LGPLv2.1+
URL: http://www.freedesktop.org/wiki/Software/Farstream

Source: http://freedesktop.org/software/%_name/releases/%_name/%_name-%version.tar.gz

%define nice_ver 0.1.8
%define gst_ver 1.4
%define glib_ver 2.32

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
Summary: Old Farstream library
Group: System/Libraries

%description -n lib%name
The Farstream (formerly Farsight) is a collection of GStreamer modules
and libraries for videoconferencing.

This package provides old completely useless shared Farstream library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/lib%_name-%api_ver.so.*


%changelog
* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- compat library

