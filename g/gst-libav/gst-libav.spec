%define ver_major 1.22
%define gst_api_ver 1.0
%define _gst_libdir %_libdir/gstreamer-%gst_api_ver
# switched from libav to ffmpeg since 1.5.90
# was 11.4 for libav fork
%define libav_ver 4.3

%ifarch %ix86 x86_64
%def_enable mmx
%else
%def_disable mmx
%endif

%def_disable doc
%def_with system_libav

%if_without system_libav
%def_enable gpl
%def_enable gnutls
%def_enable libxvid
%def_enable libx264
%def_enable libx265
%def_enable libmp3lame
%def_enable libvorbis
%def_enable libcdio
%def_enable libfreetype
%def_enable libpulse
%def_enable libgsm
%def_enable libdc1394
%def_enable shared
%def_enable static
%def_enable pthreads
%def_enable zlib
%def_disable avisynth
%def_enable libtheora
%def_enable debug
%def_enable bzlib
%def_enable vaapi
%def_enable vdpau
%def_enable libopencore_amrwb
%def_enable libopencore_amrnb
%def_enable libvpx
%def_enable libv4l2
%def_enable libspeex
%def_disable librtmp
%def_disable frei0r

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif

%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif
%endif

Name: gst-libav
Version: %ver_major.0
Release: alt1

Summary: GStreamer (%gst_api_ver API) streaming media framework plug-in using FFmpeg
Group: System/Libraries
License: LGPL-2.1
Url: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ orc
BuildRequires: gst-plugins%gst_api_ver-devel >= %version
BuildRequires: liborc-test-devel zlib-devel bzlib-devel liblzma-devel
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}
%if_with system_libav
BuildRequires: libavformat-devel >= %libav_ver
BuildRequires: libswscale-devel libavresample-devel libavfilter-devel
%else
BuildRequires: glibc-devel-static
BuildRequires: libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires: libalsa-devel
BuildRequires: libbluray-devel libass-devel
%ifarch %ix86 x86_64
BuildRequires: yasm
%endif
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%{?_enable_libmp3lame:BuildRequires: liblame-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel}
%{?_enable_libfreetype:BuildRequires: libfreetype-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel libcdio-paranoia-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libpulse:BuildRequires: libpulseaudio-devel}
%{?_enable_libxvid:BuildRequires: libxvid-devel}
%{?_enable_libx264:BuildRequires: libx264-devel >= 118}
%{?_enable_libx265:BuildRequires: libx265-devel}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel libraw1394-devel}
%{?_enable_libtheora:BuildRequires: libtheora-devel}
%{?_enable_bzlib:BuildRequires: bzlib-devel}
%{?_enable_vaapi:BuildRequires: libva-devel}
%{?_enable_vdpau:BuildRequires: libvdpau-devel}
%{?_enable_libopencore_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_libopencore_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_libvpx:BuildRequires: libvpx-devel}
%{?_enable_libv4l2:BuildRequires: libv4l-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_frei0r:BuildRequires: frei0r-devel}
%{?_enable_libspeex:BuildRequires: libspeex-devel}
%endif

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

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for the GStreamer Libav
plug-in.

%prep
%setup

%build
%meson %{?_disable_doc:-Ddoc=disabled}
%meson_build

%install
%meson_install

%files
%_gst_libdir/*.so
%doc AUTHORS NEWS README* RELEASE

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/%name-plugins-%gst_api_ver/
%endif

%changelog
* Wed Jan 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Thu Oct 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.4-alt1
- 1.20.4

* Thu Jun 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Tue May 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1
- 1.18.5

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Thu Jan 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Mon Dec 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0 (ported to Meson build system)

* Wed Dec 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt2
- disabled obsolete librtmp support

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt3
- updated buildreqs for bundled ffmpeg

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- rebuilt with bundled ffmpeg, not ready for ffmpeg-4.0

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Fri Aug 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt2
- rebuilt with system libav (ffmpeg-3.3.3)

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

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Fri Aug 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt2
- switch to build with bundled ffmpeg
- fixed BGO #753869 (upstream patch)

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0
- built against system libav
- new devel-doc subpackage

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt2
- use internal libav code

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Dec 29 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Fri Jul 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


