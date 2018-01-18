#%define rel -beta4
%define rel %nil
%define oname audacious
Name: audacious-plugins
Version: 3.9
Release: alt2.1

Summary: Plugins for Audacious

License: GPL
Group: Sound
Url: http://audacious-media-player.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.audacious-media-player.org/%name-%version%rel.tar

Requires: %oname = %version

# manually removed: i586-libxcb  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Tue Sep 02 2014
# optimized out: glib2-devel gnu-config libGL-devel libX11-devel libXfixes-devel libXrender-devel libalsa-devel libatk-devel libavcodec-devel libavutil-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcloog-isl4 libdbus-devel libdbus-glib libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libogg-devel libpango-devel libsndfile-devel libstdc++-devel pkg-config python-base python-devel python-module-distribute python-module-zope python-modules python-modules-xml python3-base termutils xorg-compositeproto-devel xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ libSDL-devel libXcomposite-devel libaudacious-devel libavformat-devel libbinio-devel libbs2b-devel libcddb-devel libcdio-paranoia-devel libcue-devel libcurl-devel libdbus-glib-devel libfaad-devel libflac-devel libfluidsynth-devel libgtk+3-devel liblame-devel liblirc-devel libmms-devel libmodplug-devel libmpg123-devel libneon-devel libnotify-devel libpulseaudio-devel libsamplerate-devel libsidplayfp-devel libvorbis-devel libwavpack-devel libxml2-devel python-module-PyXML python-module-cmd2 python-module-google python-module-mwlib

BuildRequires: lib%oname-devel = %version

BuildRequires: libglade-devel libprojectM-devel >= 1.1 libsidplayfp-devel libsoxr-devel

%description
Base plugins for Audacious.
It includes some great other features like various output plugins, last.fm plugins, LIRC support.
This package contains the base I/O plugins:
  * Audio CD reading
  * MPEG support (mp3)
  * Ogg Vorbis support
  * WMA support
  * AAC support
  * FLAC support
  * ALAC support
  * WAVE support
  * ALSA output
  * OSS output
  * Disk writer output

%prep
%setup -n %name-%version%rel

%build
%configure \
	--enable-amidiplug --enable-sid \
	--disable-jack \
%ifnarch x86_64
	--disable-sse2 \
%endif
	 --enable-pulse
%make_build

%install
%makeinstall_std
%find_lang audacious-plugins

%files -f audacious-plugins.lang
%_datadir/%oname/
%dir %_libdir/%oname/
%_libdir/%oname/*

%changelog
* Sat Jan 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt2.1
- autorebuild with libcdio-2.0.0

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt2
- rebuild with libsidplayfp 1.8.7

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9 (with rpmrb script)

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 3.8.2-alt3
- rebuilt with debuginfo-enabled ffmpeg

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 3.8.2-alt2
- rebuilt with recent ffmpeg-3.3.1

* Thu Jan 26 2017 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version 3.8.2 (with rpmrb script)

* Sat Dec 31 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt1
- new version 3.8.1 (with rpmrb script)

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.2-alt1
- new version 3.7.2 (with rpmrb script)

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.1-alt1
- new version 3.7.1 (with rpmrb script)

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1.1
- rebuilt with newest libcdio{,-paranoia}

* Sun Jul 12 2015 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version 3.6.2 (with rpmrb script)
- disable adplug plugin (uses libbinio)

* Wed May 06 2015 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5.2-alt1
- new version 3.5.2 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5.1-alt1
- new version 3.5.1 (with rpmrb script)

* Tue May 06 2014 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5 (with rpmrb script)

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 3.4.3-alt1
- new version 3.4.3 (with rpmrb script)

* Sat Oct 12 2013 Vitaly Lipatov <lav@altlinux.ru> 3.4.1-alt1
- new version 3.4.1 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4 (with rpmrb script)

* Sun Jun 02 2013 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- new version 3.3.4

* Sun Dec 09 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3.2-alt1
- new version 3.3.2 (with rpmrb script)

* Sun Aug 05 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3 (with rpmrb script)
- update buildreqs

* Sat Apr 21 2012 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- fix build without extra glib headers

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.1
- Rebuilt with ffmpeg 0.7.1

* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Wed May 26 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt2
- disable jack build

* Sat Dec 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version (2.2)
- update buildreqs, enable SID build

* Thu Nov 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt3
- rebuil with new libcdio 0.82

* Sun Aug 30 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- fix build, disable SID build (due DT_TEXTREL)

* Sat Jul 11 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Tue Jun 30 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- fix freeze after end of file playing (thanks, Debian)

* Mon May 25 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sun Mar 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt8
- build with flac support (fix bug #19180)

* Fri Mar 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt7
- enable sse2 on x86_64

* Mon Dec 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt6
- fix build with libmtp >= 0.3.0 (thanks, Gentoo)
- use configure with --disable-sse2

* Tue Jul 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt5
- rebuild without esound

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt4
- rebuild with new libmowgli

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt3
- really build with last libneon

* Mon Jun 30 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- rebuild with libneon 0.28 (new libneon conflicts with libneon0.26)

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)
- update buildreqs

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Fri Mar 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt2
- rebuild with libmtp-0.2.6

* Sun Feb 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- new version 1.4.5 (with rpmrb script)

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.3.2-alt1
- new version 1.4.3.2 (with rpmrb script)

* Wed Dec 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Nov 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- enable projectM plugin

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- release 1.4.0

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1beta4
- new version (1.4.0 beta4)
- drop patches (mainstreamed)

* Sat Oct 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1beta3
- new version (1.4.0 beta 3)
- update buildreq
- add patches for fix linking

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt4
- just rebuild due bug #12422 (needs to rebuild with current compiler options)

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt3
- set CDDA path to /var/empty (has to exist, but not used): fix bug #12129 again

* Mon Jun 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt2
- set /media/cdrom as default path for cd audio plugin (fix bug #12129)
- build with libmms

* Sat Jun 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script)

* Mon May 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- disable SSE2 using (fix bug #11799)

* Wed May 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version 1.3.4
- build without libarts
- update buildreq

* Wed Apr 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0

* Sun Jan 14 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- enable all modules - add pulseaudio, wavpack, musepack, adlib, paranormal support

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt0.1
- new version 1.2.5 (with rpmrb script)

* Thu Nov 16 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- initial build for ALT Linux Sisyphus
