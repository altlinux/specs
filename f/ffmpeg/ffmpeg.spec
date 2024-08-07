# defined macro based on Sergey Bolshakov <sbolshakov@altlinux.org> libav spec

# Macros
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_with() %{expand:%%{?_enable_%{1}:--enable-%{2}} } %{expand:%%{?_disable_%{1}:--disable-%{2}} }
%if "%(rpmvercmp '%{get_version glibc-kernheaders}' '6.0')" <= "0"
%def_disable v4l2_request
%else
%def_enable v4l2_request
%endif

# License
%def_enable gpl
%def_enable version3
%def_disable nonfree

# Enable/Disable stuff
%def_enable doc
%def_enable ffplay
%def_enable ffprobe
%def_enable pthreads
%def_enable shared
%def_disable static
%ifarch %ix86 x86_64
%def_enable mmx
%else
%def_disable mmx
%endif
%def_enable debug
# External library support
%def_enable bzlib
%def_enable chromaprint
%def_enable frei0r
%def_enable gnutls
%def_enable libaom
%def_enable libass
%def_enable libbluray
%def_enable libbs2b
%def_enable libcaca
%def_enable libcdio
%def_enable libcodec2
%def_enable libdav1d
%ifarch %e2k
%def_disable libdc1394
%else
%def_enable libdc1394
%endif
%def_enable libdrm
%def_disable libflite
%def_enable libfontconfig
%def_enable libfreetype
%def_enable libfribidi
%def_disable libglslang
%def_enable libgme
%def_enable libgsm
%def_enable libjack
# https://trac.ffmpeg.org/ticket/9112
%def_disable liblensfun
%def_enable libmp3lame
%ifarch x86_64 aarch64
%def_disable libmfx
%def_enable libvpl
%endif
%{?_enable_version3:%def_enable libopencore_amrnb}
%{?_enable_version3:%def_enable libopencore_amrwb}
%def_enable libopenjpeg
%def_enable libopus
%def_enable libplacebo
%def_enable libpulse
%def_enable librabbitmq
%def_enable librsvg
%def_disable librtmp
%def_enable librubberband
%def_enable libsnappy
%def_enable libsoxr
%def_enable libspeex
%def_enable libssh
%def_enable libtheora
%def_enable libtwolame
%def_enable libudev
%def_enable libv4l2
%def_enable libvidstab
%def_enable libvorbis
%def_enable libvpx
%def_enable libwebp
%def_enable libx264
%def_enable libx265
%def_enable libxml2
%def_enable libxvid
%def_enable libzimg
%def_enable libzmq
%def_enable libzvbi
%def_enable lv2
%def_enable openal
%def_enable opengl
%def_enable sdl2
%def_enable vaapi
%def_enable vdpau
%def_enable vulkan
%def_enable zlib

# library needed
%def_disable avisynth
%def_disable crystalhd
%def_disable ladspa
%def_disable libaribb24
%def_disable libdavs2
%def_disable libilbc
%def_disable libklvanc
%def_disable libkvazaar
%def_disable libmodplug
%def_disable libmysofa
%def_disable libopenh264
%def_disable libopenmpt
%def_disable librav1e
%def_disable libshine
%def_enable libsrt
%def_disable libtensorflow
%def_disable libtesseract
%def_disable libvmaf
%def_disable libxavs2
%def_disable mbedtls
%def_disable omx
%def_disable opencl
%def_disable pocketsphinx
%def_disable vapoursynth
%def_enable v4l2_m2m

# need libcelt >= 0.11.0
%def_disable libcelt

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif

%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif
#soversion

# nvidia cuda doesn't support arm, mips and others
# https://developer.nvidia.com/nvidia-video-codec-sdk/download
%ifarch %ix86 x86_64 aarch64 ppc64le
%def_enable cuvid
%else
%def_disable cuvid
%endif # cuvid

%define avdevicever 60
%define avformatver 60
%define avfilterver 9
%define avcodecver 60
%define postprocver 57
%define swresamplever 4
%define swscalever 7
%define avutilver 58
%ifarch ppc64le armh
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

%ifarch %ix86
%global optflags_lto %nil
%endif

Name:		ffmpeg
Epoch:		2
Version:	6.1.2
Release:	alt1

Summary:	A command line toolbox to manipulate, convert and stream multimedia content
License:	GPLv3
Group:		Video

Url:		http://ffmpeg.org

# https://git.ffmpeg.org/ffmpeg.git
Source:		%name-%version.tar
Patch:		%name-%version-%release.patch
Patch2000: %name-e2k-simd.patch
BuildRequires:	libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires:	libalsa-devel
%ifarch %ix86 x86_64
BuildRequires:	yasm
%endif

%{?_enable_doc:BuildRequires: perl-podlators texi2html}
%{?_enable_ffplay:BuildRequires: libSDL2-devel}
%{?_enable_bzlib:BuildRequires: bzlib-devel}
%{?_enable_chromaprint:BuildRequires: libchromaprint-devel}
%{?_enable_frei0r:BuildRequires: frei0r-devel}
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%{?_enable_libaom:BuildRequires: libaom-devel >= 1.0.0}
%{?_enable_libass:BuildRequires: libass-devel}
%{?_enable_libbluray:BuildRequires: libbluray-devel}
%{?_enable_libbs2b:BuildRequires: libbs2b-devel}
%{?_enable_libcaca:BuildRequires: libcaca-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel libcdio-paranoia-devel}
%{?_enable_libcelt:BuildRequires: libcelt-devel}
%{?_enable_libcodec2:BuildRequires: libcodec2-devel}
%{?_enable_libdav1d:BuildRequires: libdav1d-devel}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel libraw1394-devel}
%{?_enable_libdrm:BuildRequires: libdrm-devel}
%{?_enable_libfreetype:BuildRequires: libfreetype-devel}
%{?_enable_libflite:BuildRequires: flite-devel}
%{?_enable_libfontconfig:BuildRequires: fontconfig-devel}
%{?_enable_libfribidi:BuildRequires: libfribidi-devel}
%{?_enable_libglslang:BuildRequires: glslang-devel}
%{?_enable_libgme:BuildRequires: libgme-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libjack:BuildRequires: libjack-devel}
%{?_enable_liblensfun:BuildRequires: liblensfun-devel}
%{?_enable_libmp3lame:BuildRequires: liblame-devel}
%{?_enable_libmfx:BuildRequires: libmfx-devel}
%{?_enable_libvpl:BuildRequires: libvpl-devel}
%{?_enable_librabbitmq:BuildRequires: librabbitmq-c-devel}
%{?_enable_libopencore_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_libopencore_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_libopenjpeg:BuildRequires: libopenjpeg2.0-devel}
%{?_enable_libopus:BuildRequires: libopus-devel}
%{?_enable_libplacebo:BuildRequires: libplacebo-devel}
%{?_enable_libpulse:BuildRequires: libpulseaudio-devel}
%{?_enable_librsvg:BuildRequires: librsvg-devel}
%{?_enable_librubberband:BuildRequires: librubberband-devel libstdc++-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_libsnappy:BuildRequires: libsnappy-devel}
%{?_enable_libsrt:BuildRequires: libsrt-devel}
%{?_enable_libsoxr:BuildRequires: libsoxr-devel}
%{?_enable_libssh:BuildRequires: libssh-devel}
%{?_enable_libspeex:BuildRequires: libspeex-devel}
%{?_enable_libtheora:BuildRequires: libtheora-devel}
%{?_enable_libtwolame:BuildRequires: libtwolame-devel}
%{?_enable_libudev:BuildRequires: libudev-devel}
%{?_enable_libv4l2:BuildRequires: libv4l-devel}
%{?_enable_libvidstab:BuildRequires: libvidstab-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel}
%{?_enable_libvpx:BuildRequires: libvpx-devel}
%{?_enable_libwebp:BuildRequires: libwebp-devel}
%{?_enable_libx264:BuildRequires: libx264-devel >= 118}
%{?_enable_libx265:BuildRequires: libx265-devel}
%{?_enable_libxml2:BuildRequires: libxml2-devel}
%{?_enable_libxvid:BuildRequires: libxvid-devel}
%{?_enable_libzimg:BuildRequires: libzimg-devel}
%{?_enable_libzmq:BuildRequires: libzeromq-devel}
%{?_enable_libzvbi:BuildRequires: libzvbi-devel}
%{?_enable_lv2:BuildRequires: liblilv-devel lv2-devel}
%{?_enable_openal:BuildRequires: libopenal-devel}
%{?_enable_opengl:BuildRequires: libGL-devel}
%{?_enable_sdl2:BuildRequires: libSDL2-devel}
%{?_enable_vaapi:BuildRequires: libva-devel}
%{?_enable_vdpau:BuildRequires: libvdpau-devel}
%{?_enable_vulkan:BuildRequires: libvulkan-devel}
%{?_enable_cuvid:BuildRequires: nv-codec-headers}

%define common_descr \
FFmpeg is a collection of libraries and tools to process multimedia content\
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
Obsoletes:	avplay
Provides:	avplay

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
Obsoletes:	avprobe
Provides:	avprobe

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


%package -n	libavcodec%avcodecver
Summary:	provides implementation of a wider range of codecs
Group:		System/Libraries

%description -n libavcodec%avcodecver
%common_descr

The libavcodec library provides implementation of a wider range of
codecs.

%package -n libavcodec-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavcodec%avcodecver = %EVR
Requires: libavutil-devel = %EVR

%description -n libavcodec-devel
This package contains development files for libavcodec.

%package -n libavcodec-devel-static
Summary: Static development files for libavcodec
Group: Development/C
Requires: libavcodec-devel = %EVR


%description -n libavcodec-devel-static
This package contains static development files for libavcodec.


%package -n	libavdevice%avdevicever
Summary:	FFmpeg device handling library
Group:		System/Libraries

%description -n libavdevice%avdevicever
%common_descr

The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package -n libavdevice-devel
Summary: Development files for libavdevice
Group: Development/C
Requires: libavdevice%avdevicever = %EVR

%description -n libavdevice-devel
This package contains development files for libavdevice.

%package -n libavdevice-devel-static
Summary: Static development files for libavdevice
Group: Development/C
Requires: libavdevice-devel = %EVR

%description -n libavdevice-devel-static
This package contains static development files for libavdevice.

%package -n	libavfilter%avfilterver
Summary:	FFmpeg filter layer library
Group:		System/Libraries

%description -n libavfilter%avfilterver
%common_descr

The libavfilter library provides a mean to alter decoded Audio and Video
through chain of filters.

%package -n libavfilter-devel
Summary: Development files for libavfilter
Group: Development/C
Requires: libavfilter%avfilterver = %EVR

%description -n libavfilter-devel
This package contains development files for libavfilter.

%package -n libavfilter-devel-static
Summary: Static development files for libavfilter
Group: Development/C
Requires: libavfilter-devel = %EVR

%description -n libavfilter-devel-static
This package contains static development files for libavfilter.

%package -n	libavformat%avformatver
Summary:	FFmpeg audio, video and subtitle streams (de)multiplexing library
Group:		System/Libraries

%description -n libavformat%avformatver
%common_descr

The libavformat library implements streaming protocols, container
formats and basic I/O access.

%package -n libavformat-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavformat%avformatver = %EVR
Requires: libavcodec-devel = %EVR

%description -n libavformat-devel
This package contains development files for libavformat.


%package -n libavformat-devel-static
Summary: Static development files for libavformat
Group: Development/C
Requires: libavformat-devel = %EVR

%description -n libavformat-devel-static
This package contains static development files for libavformat.

%package -n	libavutil%avutilver
Summary:	Utility library to aid portable multimedia programming
Group:		System/Libraries

%description -n libavutil%avutilver
%common_descr

The libavutil library includes hashers, decompressors and miscellaneous
utility functions.

%package -n libavutil-devel
Summary: Development files for libavutil
Group: Development/C
Requires: libavutil%avutilver = %EVR

%description -n libavutil-devel
This package contains development files for libavutil.

%package -n libavutil-devel-static
Summary: Static development files for libavutil
Group: Development/C
Requires: libavutil-devel = %EVR

%description -n libavutil-devel-static
This package contains static development files for libavutil.

%package -n	libpostproc%postprocver
Summary:	FFmpeg postprocessing library
Group:		System/Libraries

%description -n libpostproc%postprocver
%common_descr

The libpostproc library implements video postprocessing routines.

%package -n libpostproc-devel
Summary: Development files for libpostproc
Group: Development/C
Requires: libpostproc%postprocver = %EVR
Requires: libavutil-devel = %EVR

%description -n libpostproc-devel
This package contains development files for libpostproc.

%package -n libpostproc-devel-static
Summary: Static development files for libpostproc
Group: Development/C
Requires: libpostproc-devel = %EVR

%description -n libpostproc-devel-static
This package contains static development files for libpostproc.

%package -n	libswresample%swresamplever
Summary:	FFmpeg audio resampling, rematrixing and sample format conversion library
Group:		System/Libraries

%description -n libswresample%swresamplever
%common_descr

The libswresample library implements audio mixing and resampling
routines.

%package -n libswresample-devel
Summary: Development files for libswresample
Group: Development/C
Requires: libswresample%swresamplever = %EVR
Requires: libavutil-devel = %EVR

%description -n libswresample-devel
This package contains development files for libswresample.

%package -n libswresample-devel-static
Summary: Static development files for libswresample
Group: Development/C
Requires: libswresample-devel = %EVR

%description -n libswresample-devel-static
This package contains static development files for libswresample.


%package -n	libswscale%swscalever
Summary:	FFmpeg image scaling and colorspace and pixel format conversion library
Group:		System/Libraries

%description -n libswscale%swscalever
%common_descr

The libswscale library implements color conversion and scaling routines.

%package -n libswscale-devel
Summary: Development files for libswscale
Group: Development/C
Requires: libswscale%swscalever = %EVR
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
%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif

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
%ifarch armh aarch64
	%{subst_enable_with v4l2_request v4l2-request} \
%endif
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
	--extra-libs="-latomic" \
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
	--enable-avfilter \
	%{subst_enable avisynth} \
	%{subst_enable bzlib} \
	%{subst_enable chromaprint} \
	%{subst_enable frei0r} \
	%{subst_enable gnutls} \
	%{subst_enable ladspa} \
	%{subst_enable libaom} \
	%{subst_enable libaribb24} \
	%{subst_enable libass} \
	%{subst_enable libbluray} \
	%{subst_enable libbs2b} \
	%{subst_enable libcaca} \
	%{subst_enable libcdio} \
	%{subst_enable libcelt} \
	%{subst_enable libcodec2} \
	%{subst_enable libdav1d} \
	%{subst_enable libdavs2} \
	%{subst_enable libdc1394} \
	%{subst_enable libdrm} \
	%{subst_enable libflite} \
	%{subst_enable libfontconfig} \
	%{subst_enable libfreetype} \
	%{subst_enable libfribidi} \
	%{subst_enable libglslang} \
	%{subst_enable libgme} \
	%{subst_enable libgsm} \
	%{subst_enable libilbc} \
	%{subst_enable libjack} \
	%{subst_enable libklvanc} \
	%{subst_enable libkvazaar} \
	%{subst_enable liblensfun} \
	%{subst_enable libmfx} \
	%{subst_enable libvpl} \
	%{subst_enable libmodplug} \
	%{subst_enable libmp3lame} \
	%{subst_enable librabbitmq} \
	%{subst_enable libmysofa} \
	%{subst_enable_with libopencore_amrnb libopencore-amrnb} \
	%{subst_enable_with libopencore_amrwb libopencore-amrwb} \
	%{subst_enable libopenjpeg} \
	%{subst_enable libopenmpt} \
	%{subst_enable libopus} \
	%{subst_enable libplacebo} \
	%{subst_enable libpulse} \
	%{subst_enable librsvg} \
	%{subst_enable librtmp} \
	%{subst_enable librubberband} \
	%{subst_enable libshine} \
	%{subst_enable libsnappy} \
	%{subst_enable libsoxr} \
	%{subst_enable libspeex} \
	%{subst_enable libssh} \
	%{subst_enable libtesseract} \
	%{subst_enable libtheora} \
	%{subst_enable libtwolame} \
	%{subst_enable libudev} \
	%{subst_enable libv4l2} \
	%{subst_enable libvidstab} \
	%{subst_enable libvmaf} \
	%{subst_enable libvorbis} \
	%{subst_enable libvpx} \
	%{subst_enable libwebp} \
	%{subst_enable libx264} \
	%{subst_enable libx265} \
	%{subst_enable libxavs2} \
	%{subst_enable libxml2} \
	%{subst_enable libxvid} \
	%{subst_enable libzimg} \
	%{subst_enable libzmq} \
	%{subst_enable libzvbi} \
	%{subst_enable lv2} \
	%{subst_enable omx} \
	%{subst_enable openal} \
	%{subst_enable opencl} \
	%{subst_enable opengl} \
	%{subst_enable pocketsphinx} \
	%{subst_enable sdl2} \
	%{subst_enable v4l2_m2m} \
	%{subst_enable vaapi} \
	%{subst_enable vapoursynth} \
	%{subst_enable vdpau} \
	%{subst_enable vulkan} \
	%{subst_enable zlib} \
	%{subst_enable cuvid} \
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
%ifarch ppc64le armh
	 --extra-ldflags='-flto -fuse-linker-plugin' \
	 --ar=gcc-ar \
%endif	
%ifarch x86_64 aarch64
	%{?optflags_lto:--enable-lto } \
%endif
	--extra-version='%release' \
	#
%make_build all checkasm

%install
%makeinstall_std

%check
%ifnarch armh
tests/checkasm/checkasm
%endif

%files
%doc README.md
%doc MAINTAINERS
%doc Changelog*
%doc LICENSE.md
%_bindir/ffmpeg
%{?_enable_doc:%_man1dir/ffmpeg*}
%_datadir/ffmpeg
%exclude %_datadir/ffmpeg/examples

%if_enabled doc
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
%endif

%if_enabled ffplay
%files -n ffplay
%_bindir/ffplay
%{?_enable_doc:%_man1dir/ffplay*}

%if_enabled doc
%files -n ffplay-doc
%doc doc/ffplay*.html
%endif
%endif

%if_enabled ffprobe
%files -n ffprobe
%_bindir/ffprobe
%{?_enable_doc:%_man1dir/ffprobe*}

%if_enabled doc
%files -n ffprobe-doc
%doc doc/ffprobe*.html
%endif
%endif

%if_enabled ffserver
%files -n ffserver
%_bindir/ffserver
%{?_enable_doc:%_man1dir/ffserver*}
%endif

%if_enabled doc
%files -n ffserver-doc
%{?_enable_ffserver:%doc doc/ffserver*.html}
%endif

%files -n libavcodec%avcodecver
%_libdir/libavcodec.so.%{avcodecver}*

%files -n libavcodec-devel
%_includedir/libavcodec
%_libdir/libavcodec.so
%_pkgconfigdir/libavcodec.pc

%files -n libavdevice%avdevicever
%_libdir/libavdevice.so.%{avdevicever}*

%files -n libavdevice-devel
%_includedir/libavdevice
%_libdir/libavdevice.so
%_pkgconfigdir/libavdevice.pc

%files -n libavfilter%avfilterver
%_libdir/libavfilter.so.%{avfilterver}*

%files -n libavfilter-devel
%_includedir/libavfilter
%_libdir/libavfilter.so
%_pkgconfigdir/libavfilter.pc

%files -n libavformat%avformatver
%_libdir/libavformat.so.%{avformatver}*

%files -n libavformat-devel
%_includedir/libavformat
%_pkgconfigdir/libavformat.pc
%_libdir/libavformat.so

%files -n libavutil%avutilver
%_libdir/libavutil.so.%{avutilver}*

%files -n libavutil-devel
%_includedir/libavutil
%_libdir/libavutil.so
%_pkgconfigdir/libavutil.pc

%files -n libpostproc%postprocver
%_libdir/libpostproc.so.%{postprocver}*

%files -n libpostproc-devel
%_includedir/libpostproc
%_libdir/libpostproc.so
%_pkgconfigdir/libpostproc.pc

%files -n libswresample%swresamplever
%_libdir/libswresample.so.%{swresamplever}*

%files -n libswresample-devel
%_includedir/libswresample
%_libdir/libswresample.so
%_pkgconfigdir/libswresample.pc



%files -n libswscale%swscalever
%_libdir/libswscale.so.%{swscalever}*

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
* Wed Aug 07 2024 Anton Farygin <rider@altlinux.ru> 2:6.1.2-alt1
- 6.1.1 -> 6.1.2 (Fixes: CVE-2024-7055)

* Tue Mar 12 2024 Anton Farygin <rider@altlinux.ru> 2:6.1.1-alt3
- added upstream fix against vulkan-headers 1.3.277

* Thu Feb 22 2024 Anton Farygin <rider@altlinux.ru> 2:6.1.1-alt2
- built with libvpl instead of libmfx

* Mon Jan 15 2024 Anton Farygin <rider@altlinux.ru> 2:6.1.1-alt1
- 6.1.1

* Thu Dec 28 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:6.1-alt2
- fixed build for Elbrus

* Wed Dec 27 2023 Anton Farygin <rider@altlinux.ru> 2:6.1-alt1
- 6.1

* Sun Nov 26 2023 Anton Farygin <rider@altlinux.ru> 2:6.0.1-alt1
- 6.0.1

* Thu Sep 21 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:6.0-alt2.1
- fixed build for Elbrus

* Sun Sep 17 2023 Anton Farygin <rider@altlinux.ru> 2:6.0-alt2
- built with libzimg (Closes: #42625)

* Mon Sep 04 2023 Anton Farygin <rider@altlinux.ru> 2:6.0-alt1
- 4.4.4 -> 6.0
- built with libmfx (x86_64 only)
- built with libplacebo
- updated v4l2-request path from https://github.com/jernejsk/FFmpeg

* Tue Jun 20 2023 Anton Farygin <rider@altlinux.ru> 2:4.4.4-alt1
- 4.4.3 -> 4.4.4 (Fixes: CVE-2022-3964, CVE-2022-3341, CVE-2022-3109)

* Sat Jan 28 2023 Anton Farygin <rider@altlinux.ru> 2:4.4.3-alt2
- fixed build on arm/aarch64 and glibc-kernheaders < 6.0 (thx for sbolshakov)

* Sat Oct 22 2022 Anton Farygin <rider@altlinux.ru> 2:4.4.3-alt1
- 4.4.2 -> 4.4.3
- rebased to kernel-6.0 request-api
- disabled request-api for glibc-kernheaders < 6.0

* Thu Jun 23 2022 Anton Farygin <rider@altlinux.ru> 2:4.4.2-alt1
- 4.4.1 -> 4.4.2

* Fri Oct 29 2021 Anton Farygin <rider@altlinux.ru> 2:4.4.1-alt1
- 4.4.1

* Sat Sep 25 2021 Anton Farygin <rider@altlinux.ru> 2:4.4-alt7
- Fixes:
  * CVE-2021-38171 in FFmpeg 4.4 does not check the return value of the init_vlc function
  * CVE-2021-38114 libavformat/adtsenc.c in FFmpeg 4.4 does not check the init_get_bits return value

* Mon Sep 13 2021 Anton Farygin <rider@altlinux.ru> 2:4.4-alt6
- built with LTO if lto_optflags macros defined
- built with libsrt (closes: #39534)

* Wed Jul 14 2021 Slava Aseev <ptrnine@altlinux.org> 2:4.4-alt5
- fixed build on arm (closes: #40437)

* Wed May 26 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:4.4-alt4
- disabled checkasm for armh due to segfault

* Wed May 26 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:4.4-alt3
- e2k: added SIMD patch, disabled libdc1394
- added checkasm run

* Thu Apr 22 2021 Ivan A. Melnikov <iv@altlinux.org> 2:4.4-alt2
- enable cuvid on supported architectures only
- link with libatomic on %%mips32

* Thu Apr 15 2021 Anton Farygin <rider@altlinux.org> 2:4.4-alt1
- 4.4

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 2:4.3.2-alt1
- 4.3.2

* Wed Feb 17 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:4.3.1-alt5
- fixed build on arm arches

* Wed Jan 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2:4.3.1-alt4
- Applied security fixes from upstream (Fixes: CVE-2020-35964, CVE-2020-35965).

* Wed Dec 09 2020 L.A. Kostis <lakostis@altlinux.ru> 2:4.3.1-alt3.2
- Disable cuvid on arm.

* Mon Dec 07 2020 L.A. Kostis <lakostis@altlinux.ru> 2:4.3.1-alt3.1
- Enable cuvid support.

* Mon Aug 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:4.3.1-alt3
- enable v4l2 mem2mem and request-api on arm arches

* Wed Jul 22 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.3.1-alt2
- Built with support of:
  + chromaprint;
  + frei0r plugins;
  + liblensfun;
  + librabbitmq;
  + libxml2;
  + sdl2;
  + vulkan.

* Mon Jul 13 2020 Anton Farygin <rider@altlinux.ru> 2:4.3.1-alt1
- 4.3.1
- removed support of the libwavpack (by upstream)

* Thu Jun 18 2020 Anton Farygin <rider@altlinux.ru> 2:4.3-alt1
- 4.3

* Mon May 25 2020 Anton Farygin <rider@altlinux.ru> 2:4.2.3-alt1
- 4.2.3 (Fixes: CVE-2019-13312,CVE-2020-12284)

* Thu Apr 30 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.2.2-alt2
- Built against libdav1d.

* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 2:4.2.2-alt1
- 4.2.2

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 2:4.2.1-alt1
- 4.2.1 (Fixes: CVE-2019-15942)

* Sat Aug 10 2019 Anton Farygin <rider@altlinux.ru> 2:4.2-alt1
- 4.1.4 -> 4.2

* Wed Jul 31 2019 Nikita Ermakov <arei@altlinux.org> 2:4.1.4-alt2
- NMU: Remove duplicates of libbluray-devel and libass-devel from BR.

* Tue Jul 23 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.4-alt1
- 4.1.4 (fixes: CVE-2019-12730)

* Sun May 26 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.1.3-alt3
- Built with support of:
  + libaom and HAP codecs;
  + bs2b, flite, livl, rubberband and vidstab filters;
  + Direct Rendering Manager;
  + Game Music Emu format;
  + SFTP protocol.

* Fri Apr 19 2019 Michael Shigorin <mike@altlinux.org> 2:4.1.3-alt2
- fixed doc knob (former docs one, renamed for consistency)

* Thu Apr 04 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.3-alt1
- 4.1.3

* Mon Mar 25 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.2-alt1
- 4.1.2 (fixes: CVE-2019-9718, CVE-2019-9721)

* Tue Feb 26 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.1-alt2
- added provides and obsoletes for avplay and avprobe packages (closes: #36109)

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.1-alt1
- 4.1.1

* Thu Nov 08 2018 Anton Farygin <rider@altlinux.ru> 2:4.1-alt1
- 4.1

* Mon Nov 05 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.3-alt1
- 4.0.3 (fixes: CVE-2018-15822)

* Sat Sep 01 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt4
- disabled build with librtmp (this library is not supported by anyone)

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt3
- fixed build with disabled glpv3 codecs

* Sun Aug 12 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.0.2-alt2
- built with new external libraries:
  + libcodec2
  + libjack
  + librsvg
- return changes that were accidentally dropped by one of previous builds:
  + built with new de/encoder: libopus
  + built with new encoders:
    - libass
    - libbluray
    - libcaca
    - libfontconfig
    - libfribidi
    - libopenjpeg
    - libsoxr
    - libzmq
    - libzvbi
    - openal
    - opengl
  + disabled some optimizations on MIPS arch family (by glebfm@)
  + disabled devel-static subpackage build

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt1
- 4.0.2

* Mon Jun 25 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.1-alt2
- enabled documentation build

* Fri Jun 22 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.1-alt1
- 4.0 -> 4.0.1

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 2:4.0-alt1
- 4.0 

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

