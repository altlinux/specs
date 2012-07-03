%define _gst_libdir %_libdir/gstreamer-%ver_major
%define gst_plugins gst-plugins
%define ver_major 0.10

Name: gst-ffmpeg
Version: %ver_major.13
Release: alt1
Summary: GStreamer streaming media framework plug-in using FFmpeg
Group: System/Libraries
License: GPL
Url: http://gstreamer.freedesktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires: bzlib-devel gcc-c++ gst-plugins-devel gtk-doc libavformat-devel liboil-devel
BuildRequires: liborc-devel libpostproc-devel libswscale-devel python-modules zlib-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

GStreamer FFmpeg plug-in contains one plugin with a set of elements
using the FFmpeg library code. It contains most popular decoders as
well as very fast colorspace conversion elements.

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath

%build
%autoreconf
%configure \
    --disable-static \
    --with-system-ffmpeg

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS README TODO
%_gst_libdir/*.so

%changelog
* Wed Nov 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt1
- 0.10.13

* Wed Jul 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12-alt1
- 0.10.12

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt3
- updated build dependencies

* Sun Sep 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt2
- updated build dependencies

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt1
- 0.10.11

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.10-alt1
- 0.10.10

* Thu Mar 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9.4-alt1
- 0.10.9.4 pre-release

* Fri Feb 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9.2-alt1
- 0.10.9.2 pre-release

* Tue Jan 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt3
- ignored all vdpau decoders

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt2
- updated build dependencies

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt1
- 0.10.9

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt2
- rebuild with libavutil.so.50

* Tue Jun 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.6-alt1
- 0.10.6

* Thu Sep 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.5-alt1
- 0.10.5

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.3-alt3
- rebuild

* Tue Jan 29 2008 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt2
- rebuild

* Thu Dec 06 2007 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt1
- 0.10.2.2 -> 0.10.3

* Fri Nov 30 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2.2-alt1
- 0.10.2 -> 0.10.2.2

* Thu Sep 27 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt7
- fix segfaults (thanks shrek@!)

* Mon May 07 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt6
- add libXext-devel to buildrequires

* Wed Apr 11 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt5
- disable check :(

* Wed Apr 11 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt4
- update from cvs
- update patch for building with external version of ffmpeg
- proper link all .so file (closes #11458)
- enable check :)

* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt3
- fix build with new ffmpeg (thanks to led@)
- disable check :(

* Sun Dec 24 2006 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt2
- build with external version ffmpeg (#10493)
- add libffmpeg-devel to buildrequires

* Thu Dec 21 2006 Igor Zubkov <icesik@altlinux.org> 0.10.2-alt1
- 0.10.1 -> 0.10.2 (should fix #6362)
- add liboil-devel to buildrequires

* Sun Jun 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt2
- Patch0: fix linker flags resolve undefined symbols
- Buildreq
- Added libvorbis-devel to build dependencies due to an autoconf macro used

* Mon Apr 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.0-alt1
- First release the for 0.10 branch, under new name gst-ffmpeg
- Disabled Freetype and SDL dependencies
- Corrected license info

* Sun Oct 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.6-alt1
- Updated to 0.8.6

* Fri Jan 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Thu Nov 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1.2
- relax gstreamer dependencies.

* Sun Apr 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1.1
- First build for Sisyphus.
