%define _gst_libdir %_libdir/gstreamer-%ver_major
%define gst_plugins gst-plugins
%define ver_major 0.10

Name: gst-plugins-gl
Version: %ver_major.2
Release: alt1
Summary: GStreamer OpenGL plugins
Group: System/Libraries
License: GPL
Url: http://gstreamer.freedesktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ gst-plugins-devel gtk-doc intltool libSM-devel libX11-devel libglew-devel liboil-devel libpng-devel python-modules

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

GStreamer OpenGL plugins.

%package devel
Summary: Development files for GStreamer plugins
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libraries, headers and other files necessary
to develop GStreamer plugins.

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath

%build
%autoreconf
%configure \
	--disable-examples \
	--disable-debug \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-%ver_major

%files -f %name-%ver_major.lang
%doc AUTHORS NEWS README TODO
%_libdir/*.so.*
%_gst_libdir/*.so

%files devel
%_includedir/gstreamer-%ver_major/gst/gl
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.1-alt3
- updated build dependencies

* Sun Aug 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.1-alt2
- rebuild with glew-1.5.1

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.1-alt1
- initial release

