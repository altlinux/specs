# defined macro based on Sergey Bolshakov <sbolshakov@altlinux.org> libav spec

# Macros
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_with() %{expand:%%{?_enable_%{1}:--enable-%{2}} } %{expand:%%{?_disable_%{1}:--disable-%{2}} }

# Enable/Disable stuff
%def_disable nonfree
%def_enable gpl
%def_enable version3
%def_enable ffplay
%def_enable ffprobe
%def_enable ffserver
%def_enable shared
%def_disable static
%def_enable pthreads
%ifarch %ix86 x86_64
%def_enable mmx
%else
%def_disable mmx
%endif
%def_enable debug
# External library support
%def_disable avisynth
%def_enable bzlib
%def_disable frei0r
%def_enable gnutls
%def_enable libass
%def_enable libbluray
%def_enable libcaca
%def_enable libcdio
%def_enable libdc1394
%def_enable libfontconfig
%def_enable libfreetype
%def_enable libfribidi
%def_enable libgsm
%def_enable libmp3lame
%def_enable libopencore_amrnb
%def_enable libopencore_amrwb
%def_enable libopenjpeg
%def_enable libopus
%def_enable libpulse
%def_disable librtmp
%def_enable librubberband
%def_enable libschroedinger
%def_enable libsnappy
%def_enable libsoxr
%def_enable libspeex
%def_enable libtheora
%def_enable libtwolame
%def_enable libv4l2
%def_enable libvorbis
%def_enable libvpx
%def_enable libwavpack
%def_enable libwebp
%def_enable libx264
%def_enable libx265
%def_enable libxvid
%def_enable libzmq
%def_enable libzvbi
%def_enable openal
%def_enable opengl
%def_enable vaapi
%def_enable vdpau
%def_enable zlib

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif

%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif

Name:		ffmpeg3.3
Epoch:		2
Version:	3.3.9
Release:	alt1

Summary:	A command line toolbox to manipulate, convert and stream multimedia content
License:	GPLv3
Group:		Video

Url:		http://ffmpeg.org

Source:		%name-%version.tar
BuildRequires:	libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires:	libalsa-devel
BuildRequires:	perl-podlators texi2html
%ifarch %ix86 x86_64
BuildRequires:	yasm
%endif

%{?_enable_ffplay:BuildRequires: libSDL2-devel}

%{?_enable_bzlib:BuildRequires: bzlib-devel}
%{?_enable_frei0r:BuildRequires: frei0r-devel}
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%{?_enable_libass:BuildRequires: libass-devel}
%{?_enable_libbluray:BuildRequires: libbluray-devel}
%{?_enable_libcaca:BuildRequires: libcaca-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel libcdio-paranoia-devel}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel libraw1394-devel}
%{?_enable_libfreetype:BuildRequires: libfreetype-devel}
%{?_enable_libfribidi:BuildRequires: fontconfig-devel}
%{?_enable_libfribidi:BuildRequires: libfribidi-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libmp3lame:BuildRequires: liblame-devel}
%{?_enable_libopencore_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_libopencore_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_libopenjpeg:BuildRequires: libopenjpeg-devel}
%{?_enable_libopus:BuildRequires: libopus-devel}
%{?_enable_libpulse:BuildRequires: libpulseaudio-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_librubberband:BuildRequires: librubberband-devel}
%{?_enable_libschroedinger:BuildRequires: libschroedinger-devel}
%{?_enable_libsnappy:BuildRequires: libsnappy-devel}
%{?_enable_libsoxr:BuildRequires: libsoxr-devel}
%{?_enable_libspeex:BuildRequires: libspeex-devel}
%{?_enable_libtheora:BuildRequires: libtheora-devel}
%{?_enable_libtwolame:BuildRequires: libtwolame-devel}
%{?_enable_libv4l2:BuildRequires: libv4l-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel}
%{?_enable_libvpx:BuildRequires: libvpx-devel}
%{?_enable_libwavpack:BuildRequires: libwavpack-devel}
%{?_enable_libwebp:BuildRequires: libwebp-devel}
%{?_enable_libx264:BuildRequires: libx264-devel >= 118}
%{?_enable_libx265:BuildRequires: libx265-devel}
%{?_enable_libxvid:BuildRequires: libxvid-devel}
%{?_enable_libzmq:BuildRequires: libzeromq-devel}
%{?_enable_libzvbi:BuildRequires: libzvbi-devel}
%{?_enable_openal:BuildRequires: libopenal-devel}
%{?_enable_opengl:BuildRequires: libGL-devel}
%{?_enable_vaapi:BuildRequires: libva-devel}
%{?_enable_vdpau:BuildRequires: libvdpau-devel}

%define common_descr \
FFmpeg is a collection of libraries and tools to process multimedia content \
such as audio, video, subtitles and related metadata.

%description
%common_descr

The ffmpeg is a command line toolbox to manipulate, convert and stream
multimedia content.


%package -n	libavcodec57
Summary:	provides implementation of a wider range of codecs
Group:		System/Libraries

%description -n libavcodec57
%common_descr

The libavcodec library provides implementation of a wider range of
codecs.


%package -n	libavdevice57
Summary:	FFmpeg device handling library
Group:		System/Libraries

%description -n libavdevice57
%common_descr

The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.


%package -n	libavfilter6
Summary:	FFmpeg filter layer library
Group:		System/Libraries

%description -n libavfilter6
%common_descr

The libavfilter library provides a mean to alter decoded Audio and Video
through chain of filters.

%package -n	libavformat57
Summary:	FFmpeg audio, video and subtitle streams (de)multiplexing library
Group:		System/Libraries

%description -n libavformat57
%common_descr

The libavformat library implements streaming protocols, container
formats and basic I/O access.

%package -n	libavutil55
Summary:	Utility library to aid portable multimedia programming
Group:		System/Libraries

%description -n libavutil55
%common_descr

The libavutil library includes hashers, decompressors and miscellaneous
utility functions.


%package -n	libpostproc54
Summary:	FFmpeg postprocessing library
Group:		System/Libraries

%description -n libpostproc54
%common_descr

The libpostproc library implements video postprocessing routines.


%package -n	libswresample2
Summary:	FFmpeg audio resampling, rematrixing and sample format conversion library
Group:		System/Libraries

%description -n libswresample2
%common_descr

The libswresample library implements audio mixing and resampling
routines.

%package -n	libavresample3
Summary:	FFmpeg video postprocessing library
Group:		System/Libraries

%description -n libavresample3
%common_descr
This package contains libavresample, the ffmpeg project video postprocessing library.



%package -n	libswscale4
Summary:	FFmpeg image scaling and colorspace and pixel format conversion library
Group:		System/Libraries

%description -n libswscale4
%common_descr

The libswscale library implements color conversion and scaling routines.


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
%ifarch mips mipsel mips64 mips64el
	--disable-mipsdsp \
	--disable-mipsdspr2 \
	--disable-loongson2 \
	--disable-loongson3 \
	--disable-mmi \
	--disable-mips32r5 \
	--disable-mips32r6 \
	--disable-mips64r6 \
	--disable-msa \
%endif
%ifarch mips mipsel
	--disable-mipsfpu \
%endif
	%{subst_enable gpl} \
	%{subst_enable version3} \
	%{subst_enable pthreads} \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable mmx} \
	%{subst_enable nonfree} \
	%{subst_enable ffplay} \
	%{subst_enable ffprobe} \
	%{subst_enable ffserver} \
	--enable-avfilter \
	--enable-avresample \
	%{subst_enable avisynth} \
	%{subst_enable bzlib} \
	%{subst_enable frei0r} \
	%{subst_enable gnutls} \
	%{subst_enable libass} \
	%{subst_enable libbluray} \
	%{subst_enable libcaca} \
	%{subst_enable libcdio} \
	%{subst_enable libdc1394} \
	%{subst_enable libfontconfig} \
	%{subst_enable libfreetype} \
	%{subst_enable libfribidi} \
	%{subst_enable libgsm} \
	%{subst_enable libmp3lame} \
	%{subst_enable_with libopencore_amrnb libopencore-amrnb} \
	%{subst_enable_with libopencore_amrwb libopencore-amrwb} \
	%{subst_enable libopenjpeg} \
	%{subst_enable libopus} \
	%{subst_enable libpulse} \
	%{subst_enable librtmp} \
	%{subst_enable librubberband} \
	%{subst_enable libschroedinger} \
	%{subst_enable libsnappy} \
	%{subst_enable libsoxr} \
	%{subst_enable libspeex} \
	%{subst_enable libtheora} \
	%{subst_enable libtwolame} \
	%{subst_enable libv4l2} \
	%{subst_enable libvorbis} \
	%{subst_enable libvpx} \
	%{subst_enable libwavpack} \
	%{subst_enable libwebp} \
	%{subst_enable libx264} \
	%{subst_enable libx265} \
	%{subst_enable libxvid} \
	%{subst_enable libzmq} \
	%{subst_enable libzvbi} \
	%{subst_enable openal} \
	%{subst_enable opengl} \
	%{subst_enable vaapi} \
	%{subst_enable vdpau} \
	%{subst_enable zlib} \
	--enable-hardcoded-tables \
	--enable-runtime-cpudetect \
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

%files -n libavcodec57
%_libdir/libavcodec.so.57*


%files -n libavdevice57
%_libdir/libavdevice.so.57*


%files -n libavfilter6
%_libdir/libavfilter.so.6*


%files -n libavformat57
%_libdir/libavformat.so.57*


%files -n libavutil55
%_libdir/libavutil.so.55*

%files -n libpostproc54
%_libdir/libpostproc.so.54*

%files -n libswresample2
%_libdir/libswresample.so.2*

%files -n libavresample3
%_libdir/libavresample.so.*

%files -n libswscale4
%_libdir/libswscale.so.4*

%changelog
* Tue Dec 18 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.9-alt1
- up to 3.3.9 (compatability package)
- build without librtmp

* Tue Jun 19 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.6-alt4
- build as compat library without devel packages and tools

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.6-alt3
- rebuilt in new environment

* Thu Mar 15 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:3.3.6-alt2
- built with new de/encoder: libopus
- built with new encoders:
  + libtwolame
  + libwavpack
  + libwebp
- built with new external libraries:
  + libass
  + libbluray
  + libcaca
  + libfontconfig
  + libfribidi
  + libopenjpeg
  + librubberband
  + libsnappy
  + libsoxr
  + libzmq
  + libzvbi
  + openal
  + opengl
- disabled some optimizations on MIPS arch family (by glebfm@)
- disabled devel-static subpackage build

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
- Reintroduce to Sisyphus

