%define plugin_version 2.5

Name: libxine2
Version: 1.2.6
Release: alt7

Summary: Free libraries for play video and audio
License: GPLv2+
Group: System/Libraries
Url: http://xinehq.de/

Source: %name-%version-%release.tar

BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libalsa-devel libjack-devel libpulseaudio-devel
BuildRequires: libGL-devel libGLU-devel libSDL-devel
BuildRequires: libxcb-devel libXinerama-devel libXv-devel libXvMC-devel libva-devel libvdpau-devel
BuildRequires: gnome-vfs-devel libsmbclient-devel
BuildRequires: libv4l-devel libdvdread-devel libdvdnav-devel libcdio-devel libbluray-devel
BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libpostproc-devel
BuildRequires: libgdk-pixbuf-devel libjpeg-devel libGraphicsMagick-devel
BuildRequires: liba52-devel libdca-devel libfaad-devel libflac-devel libmad-devel
BuildRequires: libmodplug-devel libmpcdec-devel libmng-devel libspeex-devel
BuildRequires: libtheora-devel libvorbis-devel libwavpack-devel
BuildRequires: libfame-devel libvcd-devel libvpx-devel
BuildRequires: librsvg-utils lynx xmlto

%description
%name is a free gpl-licensed video player libraries and plugins for
unix-like systems. It supports mpeg-2 and mpeg-1 streams as well as AVI
files that contain MS MPEG-4 / DivX / XviD Video.

%package devel
Summary: Includes for xine development
Group: Development/Other
Requires: %name = %version-%release
Conflicts: libxine-devel

%package -n xine2-plugin-gnomevfs
Summary: gnome-vfs input plugin for xine
Group: System/Libraries
PreReq: %name = %version-%release
Provides: xine-plugin-input-gnomevfs = %version
Obsoletes: xine-plugin-input-gnomevfs < %version

%package -n xine2-plugin-samba
Summary: samba input plugin for xine
Group: System/Libraries
PreReq: %name = %version-%release

%description devel
This package contains the include files for development for xine video
output libraries.

%description -n xine2-plugin-gnomevfs
gnome-vfs input plugin for xine.

%description -n xine2-plugin-samba
samba input plugin for xine.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-ipv6 \
	--enable-antialiasing \
	--enable-mmap \
	--enable-shared \
	--disable-oss \
	--with-external-dvdnav \
#
%make_build

%install
%make DESTDIR=%buildroot docdir=%_docdir/%name-devel-%version htmldir=%_docdir/%name-devel-%version/html install
mv %buildroot%_man5dir/xine.5 %buildroot%_man5dir/xine2.5

%find_lang %name

%files -f %name.lang
%_libdir/libxine.so.*
%_libdir/xine/plugins/%plugin_version
%exclude %_libdir/xine/plugins/%plugin_version/xineplug_inp_gnome_vfs.so
%exclude %_libdir/xine/plugins/%plugin_version/xineplug_inp_smb.so
%_datadir/xine-lib
%_man5dir/xine2.*

%files devel
%doc %_docdir/%name-devel-%version
%_bindir/*
%_libdir/libxine.so
%_includedir/xine*
%_datadir/aclocal/*
%_pkgconfigdir/*.pc
%_man1dir/*

%files -n xine2-plugin-gnomevfs
%_libdir/xine/plugins/%plugin_version/xineplug_inp_gnome_vfs.so

%files -n xine2-plugin-samba
%_libdir/xine/plugins/%plugin_version/xineplug_inp_smb.so

%changelog
* Fri Jan 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt7
- rebuild with recent libcdio

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.6-alt6
- rebuild with debuginfo-enabled ffmpeg

* Tue May 30 2017 Anton Farygin <rider@altlinux.ru> 1.2.6-alt5
- rebuild with new ffmpeg

* Fri May 12 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt4
- rebuilt with libmng-2.0.3

* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt3
- fix build with recent libxcb

* Tue Aug 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt2
- rebuilt with recent libcdio

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Wed May 28 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Fri May 23 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Oct 01 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt7
- fix to build with new libav

* Mon Mar 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt5.M60P.1
- built for M60P

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt6
- update from 1.1 branch

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt5
- add woraround against crash; thanks rom_as@alt (ALT#27505)

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt4
- fix to build with new libsmbclient

* Thu Jun 28 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt2.M60P.2
- built for M60P

* Wed Jun 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt3
- built without midi
- disable xine-list and mpgaudio_priority patches

* Wed Jun 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt2
- built with libbluray and external libmad

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt0.M60P.1
- built for M60P

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.21-alt1
- new version

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt3.M60P.2
- rebuild with libav

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt3.M60P.1
- built for M60P

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt4
- built without libmad (use libavcodec)

* Fri Dec 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt3
- built without aalib (see bug 26673)

* Wed Dec 07 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt1.M60P.1
- built for M60P

* Tue Nov 15 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt2
- don't build vcd plugin
- dlopen plugins with RTLD_DEEPBIND
- fix to build with XvMC

* Mon Nov 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.20-alt1
- new version

* Mon Nov 14 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt5.M60P.1
- built for M60P

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt6
- add some fixes from SuSE

* Sun Aug 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.19-alt5
- rebuilt with recent libav

* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt4
- fix build requires

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt3
- built without ImageMagick and GdkPixbuf

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt2
- rebuilt with new ImageMagick

* Thu Aug 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt0.M51.1
- built for M51

* Thu Aug 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.19-alt1
- new version

* Wed Apr 28 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18.1-alt3
- rebuilt with new ImageMagick

* Wed Mar 17 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18.1-alt0.M51.2
- built for M51

* Wed Mar 17 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18.1-alt2
- fix to build alsa plugin

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18.1-alt0.M51.1
- built for M51

* Mon Mar 15 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18.1-alt1
- new version

* Thu Feb 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.18-alt0.M51.1
- built for M51

* Wed Feb 24 2010 Sergey V Turchin <zerg at altlinux dot org> 1.1.18-alt1
- new version

* Wed Jan 13 2010 Sergey V Turchin <zerg at altlinux dot org> 1.1.17-alt0.M51.1
- built for M51

* Tue Jan 12 2010 Sergey V Turchin <zerg at altlinux dot org> 1.1.17-alt1
- 1.1.17
- built with flac, wavpack, vcdimager

* Wed Jul 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.16.3-alt1
- 1.1.16.3

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.1.16.2-alt1
- 1.1.16.2:
  + fixed broken size checks in various input plugins (CVE-2008-5239)
  + more malloc checking (CVE-2008-5240)
  + fixed a possible integer overflow in the 4XM demuxer
    (TKADV2009-004.txt)
- 1.1.16:
  + fixed heap overflow in Quicktime atom parsing (CVE-2008-5234)
  + fixed multiple buffer overflows (CVE-2008-5236)
  + fixed multiple integer overflows (CVE-2008-5237)
  + fixed unchecked or incompletely-checked read function results
    (CVE-2008-5239)
  + fixed unchecked malloc using untrusted values (CVE-2008-5240,
    CVE-2008-5242)
  + fixed underflow in qt compressed atom handling (CVE-2008-5241)
  + fixed buffer indexing using untrusted or unchecked values
    (CVE-2008-5243)
  + fixed integer overflows in the ffmpeg audio decoder and the CDDA
    server
  + fixed heap buffer overflow in the ffmpeg video decoder
  + fixed avoid segfault on invalid track type in Matroska files
  + fixed avoid underflow (compressed atoms) in the Qt demuxer
  + added support H.264 and AAC streams within FLV
  + added a new meta-tag, "Composer", and use it in the FLAC demuxer
  + added position-based seeking independent from seekpoints
  + added a configuration option for Xv bicubic filtering, implemented
    in xf86-video-ati 6.9.1
  + fixed MMS media requests where the URI contains %-encoded characters
- fixed build on non-x86 arches

* Tue Dec 02 2008 Led <led@altlinux.ru> 1.1.16-alt0.3
- updated BuildRequires

* Mon Nov 17 2008 Led <led@altlinux.ru> 1.1.16-alt0.2
- Snapshot at 20081110
- directfb plugins moved to separate subpackage (FR #17804)
- disabled gnomevfs
- added support midi via libtimidity (FR #17888 and patch)

* Sun Sep 07 2008 Led <led@altlinux.ru> 1.1.16-alt0.1
- 1.1.16 prerelease
- added:
  + %name-lib-1.1.15-id3.patch
  + %name-lib-1.1.15-mpgaudio_priority.patch (fixed #11308)
- removed %name-lib-1.1.15-asm-inline.patch (fixed in upstream)

* Tue Sep 02 2008 Led <led@altlinux.ru> 1.1.15-alt2
- added %name-lib-1.1.15-asm-inline.patch (fixed #16995)
  (thanx zerg@ for URL)

* Sun Aug 17 2008 Led <led@altlinux.ru> 1.1.15-alt1
- 1.1.15
- cleaned up %name-lib-1.1.15-add_ff_decoders.patch (fixed in upstream)
- removed %name-lib-1.1.9-ext_faad.patch (fixed in upstream)

* Mon Aug 11 2008 Led <led@altlinux.ru> 1.1.14-alt4
- updated (cleaned up) %name-lib-1.1.14-demux_qt.patch

* Sat Aug 09 2008 Led <led@altlinux.ru> 1.1.14-alt3
- build with really external libdvdnav

* Thu Aug 07 2008 Led <led@altlinux.ru> 1.1.14-alt2
- fixed %name-lib-1.1.14-xine-list.patch

* Sun Jul 06 2008 Led <led@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Sat Jun 21 2008 Led <led@altlinux.ru> 1.1.13-alt1
- 1.1.13:
  + security fix (NSF buffer overflow, CVE-2008-1878)
  + fix integer overflows like the ones found in CVE-2008-1482
- updated %name-lib-1.1.13-alt-tmpdir.patch

* Wed Apr 23 2008 Led <led@altlinux.ru> 1.1.12-alt2
- updated %name-lib-1.1.12-alt-tmpdir.patch (fixed #15410)

* Sat Apr 19 2008 Led <led@altlinux.ru> 1.1.12-alt1
- 1.1.12:
  + fixed insufficient boundary check in speex audio decoder
    (CVE-2008-1686)
  + fixed and improved the PulseAudio driver
  + fixed Quicktime container handling
  + various Real codec improvements
  + added a video output plugin intended for passing raw data to the
    front end
- updated %name-lib-1.1.12-add_ff_decoders.patch
- added %name-lib-1.1.12-xine-list.patch

* Mon Mar 31 2008 Led <led@altlinux.ru> 1.1.11.1-alt1
- 1.1.11.1:
  + security fix (integer overflow, possibly leading to buffer
    overflow, CVE-2008-1482)

* Thu Mar 20 2008 Led <led@altlinux.ru> 1.1.11-alt1
- 1.1.11:
  + fixed Array Indexing Vulnerability (CVE-2008-0073)
  + reworked the plugin directory naming
  + fixed an off-by-one in the FLAC security fix patch
  + support 16-bit big-endian DTS audio
  + fixed long delay when closing stream on dual core systems
- updated %name-lib-1.1.11-add_ff_decoders.patch
- removed %name-lib-1.1.10.1-m4.patch (fixed in upstream)

* Thu Feb 21 2008 Led <led@altlinux.ru> 1.1.10.1-alt3
- replaced Requires with PreReq in %name-plugin-input-gnomevfs

* Tue Feb 12 2008 Led <led@altlinux.ru> 1.1.10.1-alt2
- added %name-lib-1.1.10.1-m4.patch

* Sun Feb 10 2008 Led <led@altlinux.ru> 1.1.10.1-alt1
- 1.1.10.1:
  + fixed CVE-2008-0486
  + fixed a RealPlayer codec detection bug
- enabled xcb

* Sun Jan 27 2008 Led <led@altlinux.ru> 1.1.10-alt1
- 1.1.10:
  + fixed CVE-2006-1664
- fixed %%changelog
- added partial uk translation
- removed %name-lib-1.1.9-rtsp.patch (fixed in upstream)
- fixed %%changelog

* Fri Jan 11 2008 Led <led@altlinux.ru> 1.1.9-alt2
- Fix a buffer overflow in the RTSP header-handling code
  (CVE-2008-0225) (added %name-lib-1.1.9-rtsp.patch - thanx rider@)

* Thu Jan 10 2008 Led <led@altlinux.ru> 1.1.9-alt1
- 1.1.9
- updated:
  + %name-lib-1.1.9-ext_vidix.patch
  + %name-lib-1.1.9-ext_faad.patch
  + %name-lib-1.1.9-add_ff_decoders.patch

* Thu Oct 11 2007 Led <led@altlinux.ru> 1.1.8-alt2
- disabled antialiasing (fixed #13077)

* Sat Oct 06 2007 Led <led@altlinux.ru> 1.1.8-alt1
- 1.1.8
- updated:
  + %name-lib-1.1.8-ext_vidix.patch
  + %name-lib-1.1.8-ext_faad.patch
  + %name-lib-1.1.8-add_ff_decoders.patch
  + %name-lib-1.1.8-demux_qt.patch

* Fri Oct 05 2007 Led <led@altlinux.ru> 1.1.7-alt5
- added %name-lib-1.1.7-configure.patch for fix detect and link with
  libg{object,lib}
- fixed BuildRequires
- fixed License

* Sat Sep 08 2007 Led <led@altlinux.ru> 1.1.7-alt4
- moved gnomevfs input plugin to separate subpackage (FR #12717)

* Mon Jul 30 2007 Led <led@altlinux.ru> 1.1.7-alt3
- updated %name-lib-1.1.7-demux_qt.patch
- added list of supported MIME types

* Mon Jun 11 2007 Led <led@altlinux.ru> 1.1.7-alt2
- without xcb

* Fri Jun 08 2007 Led <led@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Wed May 23 2007 Led <led@altlinux.ru> 1.1.6-alt2.1
- rebuild for xcbless libX*

* Sat May 12 2007 Led <led@altlinux.ru> 1.1.6-alt2
- with xcb

* Tue Apr 24 2007 Led <led@altlinux.ru> 1.1.6-alt1
- 1.1.6
- updated %name-lib-1.1.6-ext_vidix.patch
- removed %name-lib-1.1.5-xcbxv.patch
- removed %name-lib-1.1.5-configure.patch

* Wed Apr 18 2007 Led <led@altlinux.ru> 1.1.5-alt3
- added %name-lib-1.1.5-demux_qt.patch

* Mon Apr 16 2007 Led <led@altlinux.ru> 1.1.5-alt2
- updated %name-lib-1.1.5-configure.patch (from upstream)
- cleaned up spec
- added %name-lib-1.1.5-xcbxv.patch (from upstream)

* Thu Apr 12 2007 Led <led@altlinux.ru> 1.1.5-alt1
- 1.1.5:
  + XCB-based output plugins (Xv and XShm)
  + H.264 video stream in PES packets
  + multiple audio PID in MPEG TS
  + Improved PulseAudio plugin
- removed %name-lib-1.1.4-xcb.patch
- removed %name-lib-1.1.4-pulseaudio.patch
- removed %name-lib-1.1.4-makefile.patch
- updated %name-lib-1.1.5-ext_vidix.patch
- updated %name-lib-1.1.5-ext_faad.patch
- updated %name-lib-1.1.5-ext_a52.patch
- updated %name-lib-1.1.5-add_ff_decoders.patch
- added %name-lib-1.1.5-configure.patch
- enabled modplug

* Tue Mar 13 2007 Led <led@altlinux.ru> 1.1.4-alt2
- added %name-lib-1.1.4-xcb.patch (from CVS)
- added %name-lib-1.1.4-pulseaudio.patch (from CVS)
- build with external libdvdnav (#11074)

* Mon Feb 05 2007 Led <led@altlinux.ru> 1.1.4-alt1
- added some Provides for libxine
- updated %name-lib-1.1.4-add_ff_decoders.patch for support Dirac video
  codec via ffmpeg

* Mon Jan 29 2007 Led <led@altlinux.ru> 1.1.4-alt0.1
- 1.1.4
- enabled wavpack
- enabled libflac
- removed %name-lib-1.1.1-textrels.patch (fixed in upstream)
- removed %name-lib-1.1.2-ext_musepack.patch (fixed in upstream)
- removed %name-lib-1.1.3-ffmpeg.patch (fixed in upstream)
- removed %name-lib-1.1.3-configure.patch (fixed in upstream)
- updated %name-lib-1.1.4-ext_vidix.patch
- updated %name-lib-1.1.4-ext_faad.patch
- updated %name-lib-1.1.4-alt-tmpdir.patch
- updated %name-lib-1.1.4-add_ff_decoders.patch
- added %name-lib-1.1.4-makefile.patch

* Fri Jan 26 2007 Led <led@altlinux.ru> 1.1.3-alt2
- with external ffmpeg due added %name-lib-1.1.3-ffmpeg.patch
- added %%name-lib-1.1.3-configure.patch
- fixed BuildRequires
- with internal libdvdnav

* Wed Dec 27 2006 Led <led@altlinux.ru> 1.1.3-alt1
- fixed BuildRequires
- enabled caca
- fixed %%name-lib-1.1.3-add_ff_decoders.patch

* Thu Dec 21 2006 Led <led@altlinux.ru> 1.1.3-alt0.4
- updated %name-lib-1.1.3-add_ff_decoders.patch: added VP5, VP6, VP6F,
  WAVPACK and enabled Snow, TTA for internal libavcodec (backported
  from ffmpeg's SVN)

* Wed Dec 20 2006 Led <led@altlinux.ru> 1.1.3-alt0.3
- fixed BuildRequires
- with internal ffmpeg

* Tue Dec 19 2006 Led <led@altlinux.ru> 1.1.3-alt0.2
- cleaned up %name-lib-1.1.3-add_ff_decoders.patch

* Mon Dec 04 2006 Led <led@altlinux.ru> 1.1.3-alt0.1
- 1.1.3:
  + add "m4b" to the list of supported file extensions
  + allow 0 for DVD title/chapter (navigation or full title)
  + experimental JACK audio driver
  + allow playing of OggFlac files
  + enabled TrueSpeech codec
  + allow playing FLAC files with an ID3 tag at the start
- cleaned up spec
- removed %%name-lib-1.1.2-pulseaudio.patch (in upstream now)
- updated %%name-lib-1.1.3-ext_vidix.patch
- updated %%name-lib-1.1.3-ext_faad.patch
- updated %%name-lib-1.1.3-add_ff_decoders.patch
- disabled caca (require caca >= 0.99)

* Wed Nov 15 2006 Led <led@altlinux.ru> 1.1.2-alt8
- fixed build with xvmc
- updated %name-lib-1.1.2-pulseaudio.patch
- fixed BuildRequires for building with external libvcd
- enabled build with external musepack lib (libmpcdec):
  %%name-lib-1.1.2-ext_musepack.patch
- enabled build with external faad (libfaad):
  %%name-lib-1.1.2-ext_faad.patch

* Mon Nov 06 2006 Led <led@altlinux.ru> 1.1.2-alt7
- increase audio fifo buffer size (for support files from old OggVorbis
  codec)

* Thu Nov 02 2006 Led <led@altlinux.ru> 1.1.2-alt6
- enabled support VP5, VP6 (#10227), VP6 Flash, Snow decoders for
  ffmpeg plugin: %name-lib-1.1.2-add_ff_decoders.patch

* Wed Nov 01 2006 Led <led@altlinux.ru> 1.1.2-alt5
- fixed build with extrenal libmad (added %name-lib-1.1.2-ext_mad.patch)
- fixed build with extrenal liba52 (added %name-lib-1.1.2-ext_a52.patch)

* Tue Oct 26 2006 Led <led@altlinux.ru> 1.1.2-alt4
- enabled gdkpixbuf again
- cleaned up spec
- changed %%optflags

* Tue Oct 10 2006 Led <led@altlinux.ru> 1.1.2-alt3
- added %name-lib-1.1.0-alt-tmpdir.patch (by shrek@)
- disabled gdkpixbuf
- fixed spec

* Mon Oct 02 2006 Led <led@altlinux.ru> 1.1.2-alt2
- disabled win32 dll's support for non-ix86 arches
- fixed up %%optflags
- enabled samba
- added pulseaudio support (adapted from CVS)
- fixed %%configure parameters
- added %name-lib-1.1.2-pulseaudio.patch
- built with external vidix libs and drivers
- fixed BuildRequires
- fixed %%configure parameters
- added libxine-devel-static package
- added %%name-lib-1.1.2-ext_vidix.patch
- remade spec

* Tue Jul 11 2006 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- new version

* Mon May 22 2006 Anton Farygin <rider@altlinux.ru> 1.1.1-alt5
- build with external libdca

* Fri May 19 2006 Anton Farygin <rider@altlinux.ru> 1.1.1-alt4
- build with external libffmpeg

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 1.1.1-alt3
- fixed build with Xv

* Wed Mar 15 2006 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- disabled xvmc for x86
- added patch from SuSE for resume alsa sound after suspend

* Mon Feb 13 2006 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- new version

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.0-alt2.1.1
- Rebuilt for new pkg-config dependencies.

* Thu Jan 12 2006 LAKostis <lakostis at altlinux.ru> 1.1.0-alt2.1
- NMU;
- x86_64 fix.

* Thu Sep 08 2005 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- rebuild with new libvorbis-devel

* Tue Aug 16 2005 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- new version

* Mon Aug 01 2005 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- new version

* Fri Jun 24 2005 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- new version

* Sat Jan 15 2005 Anton Farygin <rider@altlinux.ru> 1.0.0-alt6
- disabled fpic (gcc 3.4 buildfix)

* Tue Dec 28 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt5
- enable xxmc plugin

* Mon Dec 27 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt4
- 1.0

* Tue Sep 21 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3.rc6a
- rc6a

* Tue Jul 13 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3.rc5
- removed libarts and esound support

* Mon Jun 21 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc5
- rc5

* Thu May 13 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc4a
- rc4a

* Wed May 12 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc4
- rc4

* Mon Apr 19 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc3c
- rc3c

* Thu Mar 18 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc3b
- rc3b
- #2466 fixed (libxine-devel now required libxine-version-release)

* Sun Jan 04 2004 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.rc3a
- rc3a
- build fix

* Thu Oct 30 2003 Rider <rider@altlinux.ru> 1.0.0-alt2.rc2
- rc2

* Tue Oct 07 2003 Rider <rider@altlinux.ru> 1.0.0-alt2.rc1
- rc1

* Tue Sep 30 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030930
- update from CVS
- buildrequires added
- decrease alsa sound plugin priority

* Wed Sep 24 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030924
- update from CVS

* Thu Aug 14 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030814
- update from CVS

* Mon Jul 14 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030714
- update from CVS

* Wed Jul 09 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030709
- update from CVS (beta13 now)

* Mon Apr 28 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030428
- update from CVS

* Wed Apr 09 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030409
- beta 10 from CVS

* Mon Mar 31 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030331
- update from CVS

* Mon Mar 24 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030324
- update from CVS (beta9 now)

* Mon Mar 10 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030310
- beta8

* Wed Mar 05 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030305
- update from CVS
- more decrement alsa priority (alsa may be check after arts)

* Mon Mar 04 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030304
- update from CVS
- removed dvb input plugin (don't work now)

* Tue Feb 25 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030225
- update from CVS

* Sun Feb 17 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030217
- update from CVS
- fix requires to gnome-vfs (rebuild in BTE)

* Fri Feb 14 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.cvs20030214
- update from CVS
- build with libflac for FLAC audio format support

* Thu Jan 30 2003 Rider <rider@altlinux.ru> 1.0.0-alt1.beta4
- beta 4

* Wed Jan 29 2003 Rider <rider@altlinux.ru> 1.0.0-alt0.1.beta4.cvs20030129
- build version 1.0.0 -beta4 from xine-lib CVS

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 0.9.13-alt3
- BuildRequires fix
- rebuild (gcc 3.2)

* Tue Aug 20 2002 Rider <rider@altlinux.ru> 0.9.13-alt2
- vidix pluguns fix

* Mon Aug 05 2002 Rider <rider@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Wed Jul 31 2002 Rider <rider@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Thu Jun 06 2002 Rider <rider@altlinux.ru> 0.9.10-alt4
- rebuild

* Tue Jun 04 2002 Rider <rider@altlinux.ru> 0.9.10-alt3
- with libfame 0.9.0 rebuild

* Mon Jun 03 2002 Rider <rider@altlinux.ru> 0.9.10-alt2
- buildrequires fix
- build with libfame and librte
- specfile cleanup

* Mon May 27 2002 Rider <rider@altlinux.ru> 0.9.10-alt1
- 0.9.10
- buildrequres fix
- build without SDL, OpenGL and DirectFB output plugins
- added xvid decoder

* Tue Apr 30 2002 Rider <rider@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Fri Jan 25 2002 Rider <rider@altlinux.ru> 0.9.8-alt2
- buildrequires fix

* Wed Jan 16 2002 Rider <rider@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Fri Dec 14 2001 Rider <rider@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Sun Dec 02 2001 Rider <rider@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Nov 08 2001 Rider <rider@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Tue Oct 16 2001 Rider <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 0.9.1-alt2
- snapshot from CVS

* Tue Sep 18 2001 Rider <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1 released ;-)

* Tue Sep 18 2001 Rider <rider@altlinux.ru> 0.9.0-alt2
- update from CVS
- removed d4d plugin from this package

* Sat Sep 15 2001 Rider <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0 from CVS

* Tue Sep 12 2001 Rider <rider@altlinux.ru> 0.5.3-alt4
- rebuild from CVS (DVD playback bugfix, fasted playback speed)

* Mon Sep 11 2001 Rider <rider@altlinux.ru> 0.5.3-alt3
- Fixed CFLAGS

* Sat Sep 08 2001 Rider <rider@altlinux.ru> 0.5.3-alt2
- New patch for fix ESD sound init

* Sat Sep 08 2001 Rider <rider@altlinux.ru>
- first build for ALT Linux
