%def_enable with_polyp
%def_enable with_gpl

%define rname akode
Name: lib%rname
Version: 2.0.2
%define beta %nil
%define rlz alt11
%if "%beta" == "%nil"
Release: %rlz
%else
Release: %rlz.%beta
%endif

Group: Sound
Summary: A simple audio backend
%if_enabled with_gpl
License: GPL
%else
License: LGPL
%endif
Url: http://carewolf.com/akode/
#http://www.kde-apps.org/usermanager/search.php?username=carewolf


Provides: kdemultimedia-akode = 3.5.0
Obsoletes: kdemultimedia-akode <= 3.5.0

Source0: %rname-%version%beta.tar.bz2
Source1: admin.tar.bz2

# RH
Patch1: akode-pulseaudio.patch

# MDK
Patch11: akode-2.0.2-ffmpeg-new-location.patch
Patch12: akode-2.0.2-ffmpeg-int64_c.patch
Patch13: akode-2.0.2-flac113-portable.patch
Patch14: akode-2.0.2-ffmpeg-extern-c.patch
Patch15: akode-2.0.2-fix-gcc-build.patch
Patch16: akode-2.0.2-alt-ffmpeg-new.patch

# ALT
Patch101: akode-2.0.2-alt-ffmpeg-new.patch
Patch102: akode-2.0.2-alt-libav07.patch

#BuildRequires: gcc-c++ jackit-devel libalsa-devel libffmpeg-devel libflac-devel
#BuildRequires: libmad-devel libogg-devel liboggflac-devel libsamplerate-devel
#BuildRequires: libstdc++-devel libtheora-devel libvorbis-devel
#BuildRequires: pkg-config zlib-devel libspeex-devel libfaad-devel
#BuildRequires: libfaac-devel libdts-devel libx264-devel libdc1394-devel
#BuildRequires: libxvid-devel liblame-devel libgsm-devel

# Automatically added by buildreq on Mon May 28 2007
#BuildRequires: gcc-c++ gcc-fortran jackit-devel libalsa-devel libavformat-devel libflac-devel libmad-devel libsamplerate-devel libspeex-devel libvorbis-devel zlib-devel
BuildRequires: gcc-c++ jackit-devel libalsa-devel libavformat-devel libflac-devel libmad-devel libsamplerate-devel
BuildRequires: libspeex-devel libvorbis-devel zlib-devel pkg-config
%if_enabled with_polyp
BuildRequires: libpolypaudio-devel
%endif

%description
aKode is a simple audio-decoding frame-work that provides a uniform 
interface to decode the most common audio-formats. It also has a 
direct playback option for a number of audio-outputs. 
aKode currently has the following decoder plugins: 
 mpeg: Uses libMAD to decoder all MPEG 1/2 layer I-III audio. 
       GPL licensed and 
       patent issue in the US. 
 mpc:  Decodes musepack aka mpc audio. LGPL licensed. 
 xiph: Decodes FLAC, Ogg/FLAC, Speex and Ogg Vorbis audio. LGPL 
       licensed, patent free. 
 ffmpeg: Experimental decoder using the FFMPEG decoding library. 
       Enables WMA and 
       RealAudio 
       playback. LGPL and possible patent and reengineering issues 
       in the US. 

aKode also has the following audio outputs: 
 oss:  Outputs to the OSS (Open Sound System) of for instance FreeBSD
       and Linux 2.4 
 alsa: Outputs to ALSA of Linux 2.6 (version 0.9 or 1.x required) 
       (dmix is recommended). 
 sun:  Outputs to Sun OS/Solaris audio device . 
 jack: Outputs using Jack audio backend. 
 polyp:Output to the polypaudio server. Recommended for network 
       transparent audio.

%package devel
Summary: a simple audio backend
Group: Development/KDE and QT
Requires: %name = %version-%release
Requires: libstdc++-devel

%description devel
aKode is a simple audio backend suitable for simple actions.

%package out-jack
Summary: Jack support for libakode
Group: Sound
Requires: %name = %version-%release
%description out-jack
Jack support for %name

%package out-polypaudio
Summary: Polypaudio support for libakode
Group: Sound
Requires: %name = %version-%release
%description out-polypaudio
Polypaudio support for %name

%prep
%setup -q -n %rname-%version%beta -a1
%patch1 -p1
#
%patch11 -p0
%patch12 -p1
%patch13 -p4
%patch14 -p1
%patch15 -p0
#
%patch101 -p1
%patch102 -p1

%make -f admin/Makefile.common cvs


%build
%add_optflags -I%_includedir/speex
%configure \
  --enable-shared \
  --disable-static \
  --disable-final \
  --enable-pch \
  --without-libltdl \
  --with-gnu-ld \
  --enable-new-ldflags \
  --with-pic \
%if_enabled with_gpl
  --with-libmad \
  --with-libsamplerate \
%else
  --without-libmad \
  --without-libsamplerate \
%endif
  --with-jack \
%if_enabled with_polyp
  --with-pulseaudio \
%else
  --without-pulseaudio \
%endif
  --with-ffmpeg \
  --with-oss \
  --with-alsa \
  --with-flac \
  --with-speex \
  --with-vorbis

%make_build


%install
%make DESTDIR=%buildroot install



%files
%_bindir/akodeplay
%_libdir/libakode.*
%_libdir/libakode_mpc_decoder.*
%_libdir/libakode_oss_sink.*
%_libdir/libakode_xiph_decoder.*
%_libdir/libakode_alsa_sink.*
%_libdir/libakode_ffmpeg_decoder.*
%if_enabled with_gpl
%_libdir/libakode_src_resampler.*
%_libdir/libakode_mpeg_decoder.*
%endif
%if_enabled with_polyp
%_libdir/libakode_polyp_sink.*
%endif

%files out-jack
%_libdir/libakode_jack_sink.*

%files devel
%_bindir/akode-config
%_includedir/akode/


%changelog
* Mon Aug 08 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt11
- fix to build with libav

* Fri Nov 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt10
- rebuilt

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt9
- fix to build with new autotools

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt8
- fix compile

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt7
- remove deprecated macroses from specfile
- built with pulseaudio
- sync patches with MDK

* Tue Jan 29 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt6
- rebuilt with new ffmpeg

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt5
- fix linking
- add patches from MDK to fix built on x86_64

* Fri Apr 06 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.2-alt4
- new version

* Wed Mar 28 2007 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt4
- fix compile with new ffmpeg

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt3
- rebuilt

* Tue Oct 10 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt2
- rebuilt

* Mon Jul 31 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt1
- new version
- fix license (src_resampler and mpeg_decoder conflicts with LGPL)
- split jack_sink to separate package

* Mon Jun 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt4
- update build requires

* Thu May 18 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt3
- fix sample rate list for new ffmpeg
- fix build requires

* Tue Feb 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt2
- fix requires

* Wed Dec 21 2005 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt1
- 2.0

* Wed Dec 14 2005 Sergey V Turchin <zerg at altlinux dot org> 2.0-alt0.2.rc1
- built for ALT

* Tue Nov 29 2005 - dmueller@suse.de
- split out mpeg/mp3 decoding
* Wed Nov 23 2005 - dmueller@suse.de
- update 2.0rc1
* Tue Nov 22 2005 - dmueller@suse.de
- fix crash without sound hardware
* Tue Oct 25 2005 - ro@suse.de
- added gcc-c++ to nfb
* Mon Oct 24 2005 - dmueller@suse.de
- update 2.0b3
* Mon Oct 17 2005 - ro@suse.de
- fix dependency of libakode-devel ...
* Mon Sep 26 2005 - stbinner@suse.de
- fix dependency of libakode-devel
* Mon Sep 26 2005 - coolo@suse.de
- fix build on lib64
* Wed Sep 21 2005 - dmueller@suse.de
- initial package
