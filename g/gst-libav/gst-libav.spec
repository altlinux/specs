%define ver_major 1.0
%define gst_api_ver 1.0
%define _gst_libdir %_libdir/gstreamer-%gst_api_ver
%def_with system_libav

Name: gst-libav
Version: %ver_major.5
Release: alt1

Summary: GStreamer (%gst_api_ver API) streaming media framework plug-in using FFmpeg
Group: System/Libraries
License: GPL
Url: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz

BuildRequires: gst-plugins%gst_api_ver-devel libavformat-devel liborc-devel libswscale-devel zlib-devel bzlib-devel gtk-doc
%{?_without_system_libav:BuildRequires: glibc-devel-static libSDL-devel libXvMC-devel liblzo2-devel libvdpau-devel orc nasm}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

GStreamer Libav plug-in contains one plugin with a set of elements
using the FFmpeg library code. It contains most popular decoders as
well as very fast colorspace conversion elements.

%prep
%setup

#touch ABOUT-NLS config.rpath

%build
%autoreconf
%configure \
    --disable-static \
    %{?_with_system_libav:--with-system-libav}

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS README TODO
%_gst_libdir/*.so
%exclude %_gst_libdir/*.la

%changelog
* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus

