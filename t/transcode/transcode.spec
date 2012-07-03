%define subver %nil
%set_verify_elf_method textrel=relaxed

%def_enable a52
%def_enable imagemagick
%def_enable libdv
%def_enable libdvdread
%def_enable libfame
%def_enable libjpeg
%def_enable libquicktime
%def_enable libxml2
%def_enable lzo
%def_enable mjpegtools
%def_enable mmx
%def_enable netstream
%def_enable ogg
%def_enable sdl
%def_enable theora
%def_enable v4l
%def_enable vorbis
%def_enable libpostproc
%def_enable freetype2
%def_enable xvid
%def_enable x264
%def_disable pvm3
%def_enable libmpeg2
%def_enable alsa
%def_disable avifile
%def_disable ibp
%def_disable libmpeg3
%def_disable xio

Name: transcode
Version: 1.1.5
Release: alt5.1

Summary: A linux video stream processing utility

License: GPL
Group: Video
Url: http://tcforge.berlios.de/

Source: %name-%version.tar.bz2
Source1: subtitleripper-0.3-4.tar
Source2: export_dvraw.c
Patch0: %name-subtitleripper.patch
Patch1: %name-mp3merge.patch
# http://article.gmane.org/gmane.comp.video.transcode.user/18434
# http://article.gmane.org/gmane.comp.video.transcode.user/18381
# http://article.gmane.org/gmane.comp.video.transcode.user/18446

# ALTLinux patches
Patch2: transcode-1.1.5-alt-libav.patch
Patch3: transcode-1.1.5-alt-aud_aux.patch
Patch98: transcode-1.1.5-textrel.patch
Patch99: subtitleripper-0.3-4-alt-makefile.patch

%define ffmpeg_ver 0.6
%define avifile_ver 0.737
%define xvid_ver 1.2.2
%define exif_ver 0.6.17

#BuildRequires(pre): xvid-devel >= %xvid_ver
#BuildRequires(pre): libexif-devel >= %exif_ver
# Automatically added by buildreq on Mon Sep 05 2011 (-bi)
# optimized out: elfutils fontconfig libICE-devel libSM-devel libX11-devel libXext-devel libXmu-devel libXt-devel libavcodec-devel libavutil-devel libdv-devel libjpeg-devel libogg-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libquicktime111-core libvorbis-devel pkg-config python-base ruby xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: glibc-devel-static imake libImageMagick-devel libSDL-devel libXaw-devel libXpm-devel libXv-devel liba52-devel libalsa-devel libavformat-devel libdvdread-devel libfreetype-devel liblame-devel liblzo2-devel libmjpegtools-devel libmpeg2-devel libnetpbm-devel libpostproc-devel libquicktime-devel libtheora-devel libv4l-devel libx264-devel libxml2-devel libxvid-devel rpm-build-ruby xorg-cf-files
BuildRequires: glibc-devel imake libImageMagick-devel libSDL-devel libXaw-devel libXpm-devel
BuildRequires: libXv-devel liba52-devel libalsa-devel
BuildRequires: libavformat-devel libdvdread-devel libfreetype-devel liblame-devel liblzo2-devel
BuildRequires: libmjpegtools-devel libmpeg2-devel libnetpbm-devel libpostproc-devel
BuildRequires: libquicktime-devel libtheora-devel libv4l-devel libx264-devel libxml2-devel
BuildRequires: libxvid-devel >= %xvid_ver xorg-cf-files

%description
transcode  is a linux text-console utility for video stream
processing.

Decoding and encoding is done by loading modules that are
responsible for feeding transcode with raw video/audio streams (import
modules) and encoding the frames (export modules).

It supports elementary video and audio frame transformations, including
de-interlacing or fast resizing of video frames and loading of external
filters.

A number of modules are included to enable import of DVDs
on-the-fly, MPEG elementary (ES) or program streams (VOB), MPEG video,
Digital Video (DV), YUV4MPEG streams, NuppelVideo file format and raw or
compressed (pass-through) video frames and export modules for writing
DivX;-), OpenDivX, DivX 4.xx or uncompressed AVI files with MPEG, AC3
(pass-through) or PCM audio. Additional export modules to write single
frames (PPM) or YUV4MPEG streams are available, as well as an interface
import module to the avifile library. It's modular concept is intended
to provide flexibility and easy user extensibility to include other
video/audio codecs or filetypes.

A set of tools is included to demux (tcdemux), extract (tcextract) and
decode (tcdecode) the sources into raw video/audio streams for import,
probing (tcprobe) and scanning (tcscan) your sources and to enable
post-processing of AVI files, fixing AVI file header information
(avifix), merging multiple files (avimerge) or splitting large AVI files
(avisplit) to fit on a CD.

%package -n subtitleripper
Summary: DVD subtitles ripper/converter
Group: Video
Requires: %name

%description -n subtitleripper
This package contains tools to extract DVD subtitles from a
subtitle stream and converts it to pgm or ppm images or into VobSub
format.

%prep
%setup -q -n %name-%{version}%{subver}
mkdir -p contrib/subrip
tar xf %SOURCE1 -C contrib/subrip/
sed -i s/-lppm/-lnetpbm/ contrib/subrip/subtitleripper/Makefile
sed -i s/getline/get_line/ contrib/subrip/subtitleripper/vobsub.c
%patch0 -p0
%patch1 -p1
%patch2 -p2
%patch3 -p0
%patch98 -p2
%patch99 -p1
install -m644 %SOURCE2 filter/

%build
%autoreconf
%configure \
%{subst_enable mmx} \
%{subst_enable a52} \
%if_enabled a52
--enable-a52-default-decoder \
%endif
%{subst_enable avifile} \
%{subst_enable ibp} \
%{subst_enable imagemagick} \
%{subst_enable libdv} \
%{subst_enable libdvdread} \
%{subst_enable libfame} \
%if_enabled libfame
--with-libfame-libs=/usr/lib \
%endif
%{subst_enable libjpeg} \
%{subst_enable libmpeg3} \
%{subst_enable libquicktime} \
%{subst_enable libxml2} \
%{subst_enable lzo} \
%{subst_enable mjpegtools} \
%{subst_enable netstream} \
%{subst_enable ogg} \
%{subst_enable pvm3} \
%{subst_enable sdl} \
%{subst_enable theora} \
%if_enabled v4l
--enable-v4l \
--enable-libv4l2 \
--enable-libv4lconvert \
%endif
%{subst_enable vorbis} \
%{subst_enable libpostproc} \
%{subst_enable alsa} \
%{subst_enable xvid} \
%{subst_enable x264} \
%if_enabled libmpeg2
--enable-libmpeg2 \
--enable-libmpeg2convert \
%endif
%{subst_enable freetype2}

%make_build

pushd contrib/subrip/subtitleripper
%make "CC=gcc $RPM_OPT_FLAGS"
popd

%install
%makeinstall
pushd contrib/subrip/subtitleripper
install -m755 \
srttool \
subtitle2pgm \
subtitle2vobsub \
pgm2txt %buildroot/%_bindir/
popd

# remove non-packaged files
rm -f %buildroot%_libdir/%name/*.la
rm -rf %buildroot%_docdir/%name

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%_bindir/%name
%_bindir/avi*
%_bindir/tc*
%dir %_libdir/%name
%_libdir/%name/*.so
%_libdir/%name/*.cfg
%_libdir/%name/*.awk
%_man1dir/*
%doc AUTHORS ChangeLog README TODO
%doc docs/README*
%doc docs/*.txt docs/html

%files -n subtitleripper
%_bindir/srttool
%_bindir/subtitle2pgm
%_bindir/subtitle2vobsub
%_bindir/pgm2txt
%doc contrib/subrip/subtitleripper/{README*,ChangeLog}

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.1.5-alt5.1
- Rebuild with new libImageMagick

* Mon Sep 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.5-alt5
- fix requires
- build with --enable-libv4l2 and --enable-libv4lconvert

* Thu Aug 11 2011 Sergey Kurakin <kurakin@altlinux.org> 1.1.5-alt4
- Fixed build with recent libav
- k3b dvd-rip patches by zerg@ (closes: #25586, closes: #25587)

* Thu May 26 2011 Roman Savochenko <rom_as@altlinux.ru> 1.1.5-alt3
- Apply path for mp3 audio streams merge fix.

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.1.5-alt2
- Rebuild with new ImageMagick

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.7-alt4.1.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for transcode
  * postclean-05-filetriggers for spec file

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt4.1
- rebuild with libdvdread.so.4

* Wed Sep 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt4
- Added one more hack to workaround yet one linkage error.

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-alt3
- Fixed undefined symbold in import_lzo.so.
- Fixed build with fresh glibc.

* Sat Dec 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt2
- NMU:
  * update to 1.0.7
  * fixed build with new ImageMagick

* Mon Sep 22 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.7-alt1.rc1.cvs20080921
- 2008-09-21 CVS snapshot (fix usual ffmpeg API breakage).

* Tue May 27 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.6-alt1.rc2
- New RC version (1.0.6rc2):
  Fixes:
  + fix libpostproc search paths (ALT-specific);
  Improvements:
  + enable a52 as default encoder;
- .spec cleanup.

* Sun Mar 30 2008 L.A. Kostis <lakostis@altlinux.ru> 1.0.5-alt1
- New stable version (1.0.5):
  Fixes:
  + export_fame breakage (due ALT #15158);
  Improvements:
  + add freetype2 support;
  + add libpostproc support;
- remove obsoleted patches (merged by upstream).

* Mon Jul 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.2-alt3.4
- NMU.
- Fix building with recent ffmpeg:
  Added transcode-1.0.2-remove-direct-usage-of-individual-encoders.patch.

* Fri Oct 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.2-alt3.3
- Rebuild against mjpegtools-1.8.0.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 1.0.2-alt3.2
- fix v4l support;
- fix new ffmpeg detection;
- update buildrequires;
- remove xorg-x11-devel and replace it more less libs.

* Wed May 24 2006 LAKostis <lakostis at altlinux.ru> 1.0.2-alt3.1
- Rebuild w/ new ffmpeg.
- Add xorg-x11-devel for compiling filter_subtitler.

* Wed Apr 12 2006 LAKostis <lakostis at altlinux.ru> 1.0.2-alt3
- Added patches from official Bug Showcase:
  + filter_compare-fixes-try2.patch (more correct than my patch)
  + filter_logo-hangup-try1.patch
  + filter-fix-try2.patch
  + tccat-CVS-iodir-backport-try1.patch
- Added sources from official Bug Showcase:
  + export_pcm.c - fix dvraw export module causes segfault 
  		   whan transcoding dv NTSC -> PAL

* Fri Mar 17 2006 LAKostis <lakostis@altlinux.ru> 1.0.2-alt2.2
- patch subtitleripper against new --as-needed ld flag.

* Tue Jan 24 2006 LAKostis <lakostis@altlinux.ru> 1.0.2-alt2.1
- change package maintainer.
- cleanup buildrequires.
- backported imagemagick support fix from CVS.

* Tue Jan 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- rebuild without imagemagick support (due dvdrip problems)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- rebuild without glib1/gtk+1/gnome1 libraries (gtk support)

* Wed Nov 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- new version
- change Packager
- add patch for subtitleripper against new libnetpbm 

* Tue Sep 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- NMU: new version (fix bug #7947)
- build with quicktime (fix code by subst)

* Wed Jan 19 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.6.14-alt1.1
- rebuild against mjpegtools-1.7.0.
- quicktime support temporarily disabled, not ready for libquicktime-0.9.4

* Wed Dec 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.14-alt1
- 0.6.14

* Thu Nov 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.13-alt1
- 0.6.13

* Sun Jul 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.12-alt1.3
- rebuild with theora support.

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.12-alt1.2
- rebuild against libdv-0.102

* Fri May 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.12-alt1.1
- fixed build.

* Fri Jan 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Fri Dec 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.11-alt2
- rebuild with new libImageMagick.

* Fri Nov 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.11-alt1
- 0.6.11

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.10-alt2
- rebuild due ImageMagick depends on new libexif-0.5.12.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Sun Aug 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.9-alt1
- new version.
- enable building libmpeg3 dependent modules.

* Fri Jul 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.8-alt1
- new version

* Wed May 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.6-alt1
- new version

* Mon Mar 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.3-alt2
- subtitleripper subpackage.

* Mon Feb 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Sun Nov 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Nov 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt0.7
- Updated from weekly snapshot.
- Removed dependence on libmpeg3 which is replaced by the libmpeg2
  dependent modules that are included in transcode's sources.
- Compression support based on liblzo enabled.
- Quicktime support via libquicktime enabled.

* Wed Sep 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt0.6
- 0.6.1

* Mon Sep 23 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt0.5.1
- fix build (no SMP compatible)

* Sun Sep 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt0.5
- 0.6.0 release

* Sun Jul 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt0.1rc3
- First build for Sisyphus.
- quicktime support disabled - libquicktime required.
