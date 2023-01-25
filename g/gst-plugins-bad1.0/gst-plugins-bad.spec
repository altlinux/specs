%def_disable snapshot

%def_enable aom
%def_enable ladspa
%def_enable libdc1394
%def_enable libkate
%def_enable mjpegtools
%def_enable opencv
%def_enable timidity
%def_enable vulkan
%def_enable wayland
%def_enable zbar
%def_enable faad
%def_enable srtp
%def_disable rtmp
%def_enable openh264
%def_enable chromaprint
%def_enable gpl

%ifnarch %e2k
%def_enable liblilv
%endif

%def_disable debug
%def_enable tests
# required network
%def_disable gst_player_tests
%def_disable check

%define _name gst-plugins
%define api_ver 1.0
%define ver_major 1.22

%define _gst_libdir %_libdir/gstreamer-%api_ver

%def_disable doc

Name: %_name-bad%api_ver
Version: %ver_major.0
Release: alt1

Summary: A set of GStreamer plugins that need more quality
Group: System/Libraries
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/

%if_disabled snapshot
Source: http://gstreamer.freedesktop.org/src/%_name-bad/%_name-bad-%version.tar.xz
%else
Source: %_name-bad-%version.tar
%endif

Provides: %_name-bad = %EVR

Obsoletes: gst-transcoder < 1.17
Provides: gst-transcoder = %EVR

Requires: lib%_name%api_ver >= %ver_major
Requires: gstreamer%api_ver >= %ver_major

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gcc-c++ 
BuildRequires: gst-plugins%api_ver-devel >= %version gst-plugins%api_ver-gir-devel
BuildRequires: bzlib-devel libSDL-devel libX11-devel
BuildRequires: libalsa-devel libcdaudio-devel libdca-devel libdirac-devel libdvdnav-devel libexif-devel
BuildRequires: libgio-devel libgsm-devel libjasper-devel libmms-devel libzvbi-devel
%{?_enable_mjpegtools:BuildRequires: libmjpegtools-devel}
BuildRequires: libmpcdec-devel libneon-devel liboil-devel libsoundtouch-devel libssl-devel libmodplug-devel
BuildRequires: libcelt-devel libxvid-devel
%{?_enable_timidity:BuildRequires: libtimidity-devel timidity-instruments}
%{?_enable_libkate:BuildRequires: libkate-devel libtiger-devel}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel}
BuildRequires: libvpx-devel liborc-devel orc libofa-devel libmusicbrainz-devel libass-devel
%{?_enable_wayland:BuildRequires: libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel wayland-protocols}
%{?_enable_zbar:BuildRequires: libzbar-devel}
BuildRequires: libEGL-devel libwebp-devel libopenjpeg2.0-devel libbluez-devel
BuildRequires: libsoup-devel libspandsp-devel libfreeaptx-devel
BuildRequires: libdbus-devel libxml2-devel libgnutls-devel libvdpau-devel
BuildRequires: libsbc-devel libusb-devel libgudev-devel libopus-devel
BuildRequires: libcurl-devel libssh2-devel
BuildRequires: libvo-amrwbenc-devel librsvg-devel libvo-aacenc-devel libgcrypt-devel
BuildRequires: gobject-introspection-devel libgstreamer1.0-gir-devel
BuildRequires: libvisual0.4-devel openexr-devel libx265-devel
BuildRequires: libclutter-devel
BuildRequires: libbs2b-devel
%{?_enable_srtp:BuildRequires: libsrtp2-devel >= 2.1.0}
#BuildRequires: pkgconfig(wpe-webkit-1.0) pkgconfig(wpebackend-fdo-1.0)
BuildRequires: liborc-test-devel
%{?_enable_faad:BuildRequires: libfaad-devel}
%{?_enable_openh264:BuildRequires: libopenh264-devel >= 1.3.0}
%{?_enable_opencv:BuildRequires: libopencv-devel}
%{?_enable_aom:BuildRequires: libaom-devel}
%{?_enable_ladspa:BuildRequires: ladspa_sdk liblrdf-devel libfluidsynth-devel}
%{?_enable_vulkan:BuildRequires: vulkan-devel}
%{?_enable_rtmp:BuildRequires: librtmp-devel}
%{?_enable_chromaprint:BuildRequires: libchromaprint-devel}
# webrtc-audio-processing for webrtcdsp
BuildRequires: libwebrtc-devel >= 0.3
# since 1.13.x
BuildRequires: libnice-devel libva-devel liblcms2-devel
%{?_enable_liblilv:BuildRequires: liblilv-devel}
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}
%{?_enable_check: BuildRequires: /proc %_bindir/gst-tester-%api_ver}

%description
GStreamer Bad Plug-ins is a set of plug-ins that aren't up to par
compared to the rest.  They might be close to being good quality, but
they're missing something - be it a good code review, some
documentation, a set of tests, a real live maintainer, or some actual
wide use.  If the blanks are filled in they might be upgraded to
become part of either gst-plugins-good or gst-plugins-ugly, depending
on the other factors.

%package devel
Summary: Development files for GStreamer Bad Plug-ins
Group: Development/C
Provides: %_name-bad-devel = %EVR
Requires: %name = %EVR
Obsoletes: gst-transcoder-devel < 1.17
Provides: gst-transcoder-devel = %EVR

%description devel
This package contains the libraries, headers and other files necessary
to develop GStreamer Bad Plug-ins.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
Provides: %_name-bad-doc = %EVR
Obsoletes: gst-transcoder-devel-doc < 1.17
Provides: gst-transcoder-devel-doc = %EVR

%description doc
This package contains documentation for GStreamer Bad Plug-ins.

%prep
%setup -n %_name-bad-%version

%build
%meson \
	%{?_enable_gpl:-Dgpl=enabled} \
	-Dexamples=disabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_enable_debug:-Dgst_debug=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-bad-%api_ver

%files -f %_name-bad-%api_ver.lang
%_bindir/gst-transcoder-%api_ver
%_libdir/*.so.*
%dir %_gst_libdir
%_gst_libdir/*.so
%_typelibdir/GstBadAudio-%api_ver.typelib
%_typelibdir/GstCodecs-%api_ver.typelib
%_typelibdir/GstInsertBin-%api_ver.typelib
%_typelibdir/GstMpegts-%api_ver.typelib
%_typelibdir/GstPlayer-%api_ver.typelib
%_typelibdir/GstPlay-%api_ver.typelib
%_typelibdir/GstTranscoder-%api_ver.typelib
%_typelibdir/GstWebRTC-%api_ver.typelib
%_typelibdir/GstCuda-%api_ver.typelib
%_typelibdir/CudaGst-%api_ver.typelib
%_typelibdir/GstVa-%api_ver.typelib
%_datadir/gstreamer-%api_ver/presets/GstVoAmrwbEnc.prs
%_datadir/gstreamer-%api_ver/presets/GstFreeverb.prs
%_datadir/gstreamer-%api_ver/encoding-profiles/device/dvd.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/avi.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/flv.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/mkv.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/mp3.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/mp4.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/oga.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/ogv.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/webm.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/online-services/youtube.gep
%_datadir/gstreamer-%api_ver/encoding-profiles/file-extension/ts.gep
%doc AUTHORS NEWS README* RELEASE

%files devel
%_includedir/gstreamer-%api_ver/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_girdir/GstInsertBin-%api_ver.gir
%_girdir/GstMpegts-%api_ver.gir
%_girdir/GstPlayer-%api_ver.gir
%_girdir/GstWebRTC-%api_ver.gir
%_girdir/GstBadAudio-%api_ver.gir
%_girdir/GstCodecs-%api_ver.gir
%_girdir/GstTranscoder-%api_ver.gir
%_girdir/GstPlay-%api_ver.gir
%_girdir/CudaGst-%api_ver.gir
%_girdir/GstCuda-%api_ver.gir
%_girdir/GstVa-%api_ver.gir


%if_enabled doc
%files doc
%_gtk_docdir/gst-plugins-bad-plugins-%api_ver
%_gtk_docdir/gst-plugins-bad-libs-%api_ver
%endif

%changelog
* Wed Jan 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1.1
- enabled AOM plugin

* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Thu Oct 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.4-alt1
- 1.20.4

* Tue Aug 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt2
- enabled chromaprint plugin

* Thu Jun 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Tue May 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1.1
- fixed meson options

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1
- 1.18.5
- enabled openh264 plugin for all arhes

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Sun Feb 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt2
- enabled srtp plugin
- enabled faad plugin again

* Sat Feb 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1.1
- disabled faad plugin

* Thu Jan 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Mon Dec 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0
- obsoletes/provides: gst-transcoder

* Sun Jun 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt3
- fixed build against newest Vulkan

* Tue Apr 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.16.2-alt2
- Rebuilt with opencv-4.3.0.

* Wed Dec 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- rebuilt with libopenh264-2.0.0

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.2
- enabled OpenH264 encoder/decoder plugin for x86_64

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.1
- disabled ext/lv2 on %%e2k

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Sun Jan 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt6
- updated to 1.14.4-22-ge87fb02c1

* Fri Jan 25 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.4-alt5
- Fixed build with libopencv-3.4.5 (Closes: #35971)

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt4
- rebuilt against libfluidsynth.so.2

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt3
- disabled obsolete librtmp support

* Mon Oct 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt2
- rebuilt with librtmp-2.4-alt2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt2
- rebuilt with openssl-1.1

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt3
- rebuilt against libx265-2.8

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- built webrtcdsp plugin

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Tue Feb 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt3
- enabled bs2b support for pulseefects crossfeed plugin

* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt2
- rebuild against libopencv_*.so.3

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Oct 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt2
- rebuilt against libx265.so.130
- fixed build with libopenjpeg2.0-2.3.0

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Thu Aug 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt2
- mike@:
  BOOTSTRAP: ladspa, libdc1394, libkate, mjpegtools, opencv,
  timidity, vulkan, wayland, zbar knobs (on by default)

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Fri May 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt2
- rebuilt against libx265.so.116

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt2
- updated buildreqs for build ladspa, wayland and vulkan plugins

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

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libSoundTouch.so.1

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt2
- rebuilt against libwebp.so.6

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

* Tue Aug 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt2
- rebuilt against libx265.so.59

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt2
- rebuilt with libsoundtouch-1.8.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt2
- rebuilt against mjpegtools libs 2.1.0

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.4

* Thu Feb 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt2
- enabled VisualOn AAC support via libvo-aacenc (ALT #29852)

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- rebuilt against libwebp.so.5

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

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus


