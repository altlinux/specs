# defined macro based on Sergey Bolshakov <sbolshakov@altlinux.org> libav spec

# Macros
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_with() %{expand:%%{?_enable_%{1}:--enable-%{2}} } %{expand:%%{?_disable_%{1}:--disable-%{2}} }

# Enable/Disable stuff
%def_enable gpl
%def_enable version3
%def_enable ffplay
%def_enable ffprobe
%def_enable ffserver
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
%ifarch %ix86 x86_64
%def_enable mmx
%else
%def_disable mmx
%endif
%def_enable libschroedinger
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
%def_enable librtmp
%def_disable frei0r

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif

%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif

Name:		ffmpeg
Epoch:		2
Version:	3.3.6
Release:	alt1

Summary:	A command line toolbox to manipulate, convert and stream multimedia content
License:	GPLv3
Group:		Video

Url:		http://ffmpeg.org

Source:		%name-%version.tar
BuildRequires:	libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires:	libalsa-devel
BuildRequires:	libbluray-devel libass-devel
BuildRequires:	perl-podlators texi2html
%ifarch %ix86 x86_64
BuildRequires:	yasm
%endif

%{?_enable_ffplay:BuildRequires: libSDL2-devel}
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
%{?_enable_libschroedinger:BuildRequires: libschroedinger-devel}
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

%define common_descr \
FFmpeg is a collection of libraries and tools to process multimedia content \
such as audio, video, subtitles and related metadata.

%description
%common_descr

The ffmpeg is a command line toolbox to manipulate, convert and stream
multimedia content.


%package	doc
Summary:	FFmpeg documentation
Group:		Documentation
BuildArch:	noarch

%description	doc
%common_descr

This package contains documentation for FFmpeg.

%package -n	ffplay
Summary:	A minimalistic multimedia player
Group:		Video

%description -n	ffplay
%common_descr

This package contains a minimalistic multimedia player.

%package -n	ffplay-doc
Summary:	Documentation for ffplay
Group:		Documentation
BuildArch:	noarch

%description -n	ffplay-doc
%common_descr

This package contains documentation for ffplay.

%package -n	ffprobe
Summary:	A simple analysis tool to inspect multimedia content
Group:		Video

%description -n	ffprobe
%common_descr

This package contains ffprobe, a simple analysis tool to inspect
multimedia content.

%package -n	ffprobe-doc
Summary:	Documentation for ffprobe
Group:		Documentation
BuildArch:	noarch

%description -n	ffprobe-doc
%common_descr

This package contains documentation for ffprobe.

%package -n	ffserver
Summary:	A multimedia streaming server for live broadcasts
Group:		Video

%description -n ffserver
%common_descr

This package contains a multimedia streaming server for live broadcasts.


%package -n	ffserver-doc
Summary:	Documentation for ffserver
Group:		Documentation
BuildArch:	noarch

%description -n ffserver-doc
%common_descr

This package contains documentation for ffserver.


%package -n	libavcodec57
Summary:	provides implementation of a wider range of codecs
Group:		System/Libraries

%description -n libavcodec57
%common_descr

The libavcodec library provides implementation of a wider range of
codecs.

%package -n libavcodec-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavcodec57 = %EVR
Requires: libavutil-devel = %EVR

%description -n libavcodec-devel
This package contains development files for libavcodec.

%package -n libavcodec-devel-static
Summary: Static development files for libavcodec
Group: Development/C
Requires: libavcodec-devel = %EVR


%description -n libavcodec-devel-static
This package contains static development files for libavcodec.


%package -n	libavdevice57
Summary:	FFmpeg device handling library
Group:		System/Libraries

%description -n libavdevice57
%common_descr

The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package -n libavdevice-devel
Summary: Development files for libavdevice
Group: Development/C
Requires: libavdevice57 = %EVR

%description -n libavdevice-devel
This package contains development files for libavdevice.

%package -n libavdevice-devel-static
Summary: Static development files for libavdevice
Group: Development/C
Requires: libavdevice-devel = %EVR

%description -n libavdevice-devel-static
This package contains static development files for libavdevice.

%package -n	libavfilter6
Summary:	FFmpeg filter layer library
Group:		System/Libraries

%description -n libavfilter6
%common_descr

The libavfilter library provides a mean to alter decoded Audio and Video
through chain of filters.

%package -n libavfilter-devel
Summary: Development files for libavfilter
Group: Development/C
Requires: libavfilter6 = %EVR

%description -n libavfilter-devel
This package contains development files for libavfilter.

%package -n libavfilter-devel-static
Summary: Static development files for libavfilter
Group: Development/C
Requires: libavfilter-devel = %EVR

%description -n libavfilter-devel-static
This package contains static development files for libavfilter.

%package -n	libavformat57
Summary:	FFmpeg audio, video and subtitle streams (de)multiplexing library
Group:		System/Libraries

%description -n libavformat57
%common_descr

The libavformat library implements streaming protocols, container
formats and basic I/O access.

%package -n libavformat-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavformat57 = %EVR
Requires: libavcodec-devel = %EVR

%description -n libavformat-devel
This package contains development files for libavformat.


%package -n libavformat-devel-static
Summary: Static development files for libavformat
Group: Development/C
Requires: libavformat-devel = %EVR

%description -n libavformat-devel-static
This package contains static development files for libavformat.

%package -n	libavutil55
Summary:	Utility library to aid portable multimedia programming
Group:		System/Libraries

%description -n libavutil55
%common_descr

The libavutil library includes hashers, decompressors and miscellaneous
utility functions.

%package -n libavutil-devel
Summary: Development files for libavutil
Group: Development/C
Requires: libavutil55 = %EVR

%description -n libavutil-devel
This package contains development files for libavutil.

%package -n libavutil-devel-static
Summary: Static development files for libavutil
Group: Development/C
Requires: libavutil-devel = %EVR

%description -n libavutil-devel-static
This package contains static development files for libavutil.

%package -n	libpostproc54
Summary:	FFmpeg postprocessing library
Group:		System/Libraries

%description -n libpostproc54
%common_descr

The libpostproc library implements video postprocessing routines.

%package -n libpostproc-devel
Summary: Development files for libpostproc
Group: Development/C
Requires: libpostproc54 = %EVR
Requires: libavutil-devel = %EVR

%description -n libpostproc-devel
This package contains development files for libpostproc.

%package -n libpostproc-devel-static
Summary: Static development files for libpostproc
Group: Development/C
Requires: libpostproc-devel = %EVR

%description -n libpostproc-devel-static
This package contains static development files for libpostproc.

%package -n	libswresample2
Summary:	FFmpeg audio resampling, rematrixing and sample format conversion library
Group:		System/Libraries

%description -n libswresample2
%common_descr

The libswresample library implements audio mixing and resampling
routines.

%package -n libswresample-devel
Summary: Development files for libswresample
Group: Development/C
Requires: libswresample2 = %EVR
Requires: libavutil-devel = %EVR

%description -n libswresample-devel
This package contains development files for libswresample.

%package -n libswresample-devel-static
Summary: Static development files for libswresample
Group: Development/C
Requires: libswresample-devel = %EVR

%description -n libswresample-devel-static
This package contains static development files for libswresample.

%package -n	libavresample3
Summary:	FFmpeg video postprocessing library
Group:		System/Libraries

%description -n libavresample3
%common_descr
This package contains libavresample, the ffmpeg project video postprocessing library.

%package -n libavresample-devel
Summary: Development files for libswresample
Group: Development/C
Requires: libavresample3 = %EVR
Requires: libavutil-devel = %EVR

%description -n libavresample-devel
This package contains development files for libavresample.

%package -n libavresample-devel-static
Summary: Static development files for libavresample
Group: Development/C
Requires: libavresample-devel = %EVR

%description -n libavresample-devel-static
This package contains static development files for libavresample.



%package -n	libswscale4
Summary:	FFmpeg image scaling and colorspace and pixel format conversion library
Group:		System/Libraries

%description -n libswscale4
%common_descr

The libswscale library implements color conversion and scaling routines.

%package -n libswscale-devel
Summary: Development files for libswscale
Group: Development/C
Requires: libswscale4 = %EVR
Requires: libavutil-devel = %EVR

%description -n libswscale-devel
This package contains development files for libswscale.

%package -n libswscale-devel-static
Summary: Static development files for libswscale
Group: Development/C
Requires: libswscale-devel = %EVR

%description -n libswscale-devel-static
This package contains static development files for libswscale.

%prep
%setup

%build
xz Changelog
%ifarch x86_64
%add_optflags %optflags_shared
%else
%ifarch %ix86
%add_optflags %{?_enable_mmx:-DRUNTIME_CPUDETECT}
%endif
%endif
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--shlibdir=%_libdir \
	--mandir=%_mandir \
	--docdir=%_docdir/%name-%version \
	--disable-rpath \
	--enable-avresample \
	%{subst_enable gpl} \
	%{subst_enable pthreads} \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable gnutls} \
	%{subst_enable libvorbis} \
	%{subst_enable libfreetype} \
	%{subst_enable libpulse} \
	%{subst_enable libxvid} \
	%{subst_enable libx264} \
	%{subst_enable libx265} \
	%{subst_enable libmp3lame} \
	%{subst_enable libcdio} \
	%{subst_enable libgsm} \
	%{subst_enable libdc1394} \
	%{subst_enable zlib} \
	%{subst_enable mmx} \
	%{subst_enable ffplay} \
	%{subst_enable ffprobe} \
	%{subst_enable ffserver} \
	%{subst_enable libschroedinger} \
	--enable-avfilter \
	%{subst_enable avisynth} \
	%{subst_enable libtheora} \
	%{subst_enable version3} \
	%{subst_enable_with libopencore_amrwb libopencore-amrwb} \
	%{subst_enable_with libopencore_amrnb libopencore-amrnb} \
	--enable-hardcoded-tables \
	--enable-runtime-cpudetect \
	--enable-bzlib \
	%{subst_enable libvpx} \
	%{subst_enable libv4l2} \
	%{subst_enable libspeex} \
	%{subst_enable frei0r} \
	%{subst_enable nonfree} \
	%{subst_enable librtmp} \
	%{subst_enable vaapi} \
	%{subst_enable vdpau} \
%if_enabled debug
	--enable-debug \
%else
	--disable-debug \
%endif
	--disable-stripping \
	--enable-pic \
	--extra-cflags="%optflags" \
	--extra-version='%release' \
	#
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc MAINTAINERS
%doc Changelog*
%doc LICENSE.md
%_bindir/ffmpeg
%_man1dir/ffmpeg*
%_datadir/ffmpeg
%exclude %_datadir/ffmpeg/examples

%files doc
%doc doc/ffmpeg*.html
%doc doc/faq.html
%doc doc/fate.html
%doc doc/general.html
%doc doc/git-howto.html
%doc doc/lib*.html
%doc doc/nut.html
%doc doc/platform.html
%_man3dir/*

%if_enabled ffplay
%files -n ffplay
%_bindir/ffplay
%_man1dir/ffplay*

%files -n ffplay-doc
%doc doc/ffplay*.html
%endif

%if_enabled ffprobe
%files -n ffprobe
%_bindir/ffprobe
%_man1dir/ffprobe*

%files -n ffprobe-doc
%doc doc/ffprobe*.html
%endif

%if_enabled ffserver
%files -n ffserver
%_bindir/ffserver
%_man1dir/ffserver*

%files -n ffserver-doc
%doc doc/ffserver*.html
%endif

%files -n libavcodec57
%_libdir/libavcodec.so.57*

%files -n libavcodec-devel
%_includedir/libavcodec
%_libdir/libavcodec.so
%_pkgconfigdir/libavcodec.pc

%files -n libavdevice57
%_libdir/libavdevice.so.57*

%files -n libavdevice-devel
%_includedir/libavdevice
%_libdir/libavdevice.so
%_pkgconfigdir/libavdevice.pc

%files -n libavfilter6
%_libdir/libavfilter.so.6*

%files -n libavfilter-devel
%_includedir/libavfilter
%_libdir/libavfilter.so
%_pkgconfigdir/libavfilter.pc

%files -n libavformat57
%_libdir/libavformat.so.57*

%files -n libavformat-devel
%_includedir/libavformat
%_pkgconfigdir/libavformat.pc
%_libdir/libavformat.so

%files -n libavutil55
%_libdir/libavutil.so.55*

%files -n libavutil-devel
%_includedir/libavutil
%_libdir/libavutil.so
%_pkgconfigdir/libavutil.pc

%files -n libpostproc54
%_libdir/libpostproc.so.54*

%files -n libpostproc-devel
%_includedir/libpostproc
%_libdir/libpostproc.so
%_pkgconfigdir/libpostproc.pc

%files -n libswresample2
%_libdir/libswresample.so.2*

%files -n libswresample-devel
%_includedir/libswresample
%_libdir/libswresample.so
%_pkgconfigdir/libswresample.pc

%files -n libavresample3
%_libdir/libavresample.so.*

%files -n libavresample-devel
%_pkgconfigdir/libavresample.pc
%_includedir/libavresample
%_libdir/libavresample.so


%files -n libswscale4
%_libdir/libswscale.so.4*

%files -n libswscale-devel
%_includedir/libswscale
%_libdir/libswscale.so
%_pkgconfigdir/libswscale.pc

%if_enabled static
%files -n libavformat-devel-static
%_libdir/libavformat.a

%files -n libavcodec-devel-static
%_libdir/libavcodec.a

%files -n libavutil-devel-static
%_libdir/libavutil.a

%files -n libswresample-devel-static
%_libdir/libswresample.a

%files -n libavresample-devel-static
%_libdir/libavresample.a

%files -n libswscale-devel-static
%_libdir/libswscale.a

%files -n libavdevice-devel-static
%_libdir/libavdevice.a

%files -n libavfilter-devel-static
%_libdir/libavfilter.a

%files -n libpostproc-devel-static
%_libdir/libpostproc.a

%endif

%changelog
* Tue Jan 23 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.6-alt1
- new version

* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 2:3.3.5-alt1.1
- rebuild against libcdio.so.18

* Sat Oct 28 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.5-alt1
- 3.3.4
- fixes:
   * CVE-2017-15186 double free when ffmpeg parsing an craft AVI file to MKV file using ffvhuff decoder.

* Fri Oct 06 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt3
- rebuild for libx265 2.5

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt2
- rebuild for recent libvpx4 1.6.1

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt1
- 3.3.4 with fixes for multiple vilnerabilities (CVE-2017-14054, CVE-2017-14055,
	CVE-2017-14059, CVE-2017-14058, CVE-2017-14057, CVE-2017-14225, CVE-2017-14170,
	CVE-2017-14056, CVE-2017-14222, CVE-2017-14169, CVE-2017-14223, CVE-2017-14171)

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 2:3.3.3-alt2
- x86-only BR: yasm
- fix libpulse knob
- add doc knob
- minor spec cleanup

* Tue Aug 01 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.3-alt1
- 3.3.3 with fixes for following vulnerabilities:
	* CVE-2017-11399 remote DoS via crafted APE file
	* CVE-2017-11665 remote DoS via crafted RTMP stream
	* CVE-2017-11719 remote DoS via crafted crafted DNxHD file

* Wed Jun 14 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.2-alt1
- 3.3.2

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.1-alt2
- enabled debuginfo

* Thu May 25 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.1-alt1
- updated to 3.3.1
- cleanup spec

* Sun Aug 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:3.1.2-alt1
- Initial build

