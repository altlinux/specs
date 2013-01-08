%define _name gstreamer
%define ver_major 1.0
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_disable gtk-doc

Name: %_name%api_ver
Version: %ver_major.5
Release: alt1

Summary: GStreamer streaming media framework runtime
License: LGPL
Group: System/Libraries
URL: http://gstreamer.freedesktop.org

Requires: lib%name = %version-%release

Source: http://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
Patch: %_name-0.11.94-alt-intltool.patch

BuildRequires: docbook-utils flex gcc-c++ ghostscript-utils glib2-devel gtk-doc intltool libcheck-devel libxml2-devel
BuildRequires: python-modules sgml-common transfig xml-utils gobject-introspection-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package -n lib%name
Summary: Shared libraries of GStreamer
Group: System/Libraries

%description -n lib%name
This package contains the shared libraries of the GStreamer media framework

%package -n lib%name-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GStreamer library

%package devel
Summary: Development files for GStreamer streaming-media framework
Group: Development/C
Requires: lib%name = %version-%release

%description devel
This package contains the libraries and header files necessary to
develop applications and plugins for GStreamer

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release %name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GStreamer library

%package devel-doc
Summary: Development documentation for GStreamer
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer

%package doc
Summary: Documentation for GStreamer
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for GStreamer

%package utils
Summary: GStreamer utilities
Group: System/Libraries
Requires: lib%name = %version-%release

%description utils
This package contains some utilities used to register, analyze, and run
Gstreamer plugins.

%prep
%setup -n %_name-%version
%patch -p1

%build
%autoreconf
%configure \
	--with-package-name=GStreamer \
	--with-package-origin=%name \
	--disable-examples \
	--disable-valgrind \
	--enable-docbook \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-gtk-doc-pdf \
	--disable-rpath \
	--disable-tests \
	--disable-debug \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
%doc AUTHORS NEWS README RELEASE
%_libexecdir/%_name-%api_ver
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%exclude %_libdir/%_name-%api_ver/*.la

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/Gst-%api_ver.typelib
%_typelibdir/GstBase-%api_ver.typelib
%_typelibdir/GstCheck-%api_ver.typelib
%_typelibdir/GstController-%api_ver.typelib
%_typelibdir/GstNet-%api_ver.typelib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%files -n lib%name-gir-devel
%_girdir/Gst-%api_ver.gir
%_girdir/GstBase-%api_ver.gir
%_girdir/GstCheck-%api_ver.gir
%_girdir/GstController-%api_ver.gir
%_girdir/GstNet-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%files utils
%_bindir/*
%_man1dir/*

%files doc
%_datadir/doc/%_name-%api_ver

%changelog
* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

