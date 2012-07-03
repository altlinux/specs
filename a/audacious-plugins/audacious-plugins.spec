#%define rel -beta4
%define rel %nil
%define oname audacious
Name: audacious-plugins
Version: 2.5.0
Release: alt2

Summary: Plugins for Audacious

License: GPL
Group: Sound
Url: http://audacious-media-player.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.atheme.org/%name-%version%rel.tar
Patch: audacious2-plugins.patch
Patch1: audacious-plugins-1.5.1-gentoo-libmtp.patch

# Sync vorbis with mercurial tip.  Impact: several bugfixes.
# http://redmine.atheme.org/issues/show/102
# http://bugs.debian.org/531835
Patch2: audacious-plugins-2.0.1-vorbis-hg-tip.patch

# Keep mixer open and not start at only 50 percent volume. (thanks, Fedora)
Patch3: audacious-plugins-2.1-keep-mixer-open.patch

Patch4: %name-2.1-alt-fix-build.patch

# From Mandriva:
Patch5: %name-2.1-fix-build.patch
Patch6: audacious-plugins-2.1-beta1-format-strings.patch
Patch7: audacious-plugins-2.1-beta1-linking.patch
Patch8: audacious-plugins-ffmpeg-0.7.1.patch

Requires: %oname = %version

# Automatically added by buildreq on Mon Apr 18 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXfixes-devel libXmu-devel libXrender-devel libXt-devel libalsa-devel libatk-devel libavcodec-devel libavcore-devel libavutil-devel libcairo-devel libdbus-devel libdbus-glib libdbus-glib-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libmcs-devel libmowgli-devel libogg-devel libpango-devel libsndfile-devel libstdc++-devel libusb-compat libusb-compat-devel pkg-config termutils xorg-compositeproto-devel xorg-fixesproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ libSDL-devel libXcomposite-devel libaudacious-devel libavformat-devel libbinio-devel libcddb-devel libcdio-devel libcue-devel libcurl-devel libfaad-devel libflac-devel libfluidsynth-devel libgtkglext-devel liblame-devel liblirc-devel libmms-devel libmtp-devel libneon-devel libnotify4-devel libprojectM-devel libpulseaudio-devel libsamplerate-devel libvorbis-devel libwavpack-devel libxml2-devel zlib-devel

# wait for altbug #20165
# libsidplay2-devel
BuildRequires: libglade-devel libprojectM-devel >= 1.1

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
%setup -q -n %name-%version%rel
%patch
# do not include glib headers separately
find -name "*.c" | xargs %__subst "s|#include <glib/gmacros.h>|#include <glib.h>|g"
#%patch2 -p1
#%patch3 -p1
#%patch4

#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
%patch8 -p2

%build
#autoconf -f -I m4
#autoheader
%configure \
	--enable-amidiplug --enable-sid \
	--disable-jack --enable-pulse \
%ifnarch x86_64
    --disable-sse2 \
%endif
	--disable-esd
%make_build

%install
%makeinstall_std
%find_lang audacious-plugins

%files -f audacious-plugins.lang
%doc AUTHORS
%_datadir/%oname/
%dir %_libdir/%oname/
%_libdir/%oname/*

%changelog
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
