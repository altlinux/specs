Name: aqualung
Summary: Aqualung is a music player for the GNU/Linux operating system
Version: 1.0
Release: alt2
License: GPL
Group: Sound
# http://aqualung.factorial.hu/download.php?key=svntgzd
Source: %name-%version.tar.gz
Patch: use_glib_instead_of_libmac_for_charconv.patch
Patch1: %name-%version-upstream-ffmpeg.patch
#Source:			%name-%version.tar.gz
Url: http://aqualung.sf.net

# Automatically added by buildreq on Mon Sep 14 2015
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libavcodec-devel libavutil-devel libcairo-devel libcdio-devel libcdio-paranoia libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpango-devel libstdc++-devel libusb-compat libwayland-client libwayland-server pkg-config raptor2-devel xz zlib-devel
BuildRequires: gcc-c++ libalsa-devel libavformat-devel libcddb-devel libcdio-paranoia-devel libflac-devel libgtk+2-devel libifp-devel libjack-devel liblame-devel liblrdf-devel lua-devel libmac-devel libmad-devel libmodplug-devel libmpcdec-devel liboggz-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel libspeex-devel libusb-compat-devel libvorbis-devel libwavpack-devel libxml2-devel

%description
Aqualung is a music player for the GNU/Linux operating system.

It plays audio files from your filesystem and has the feature of
inserting no gaps between adjacent tracks. It also supports high
quality sample rate conversion between the file and the output
device, when necessary.

Almost all sample-based, uncompressed formats (eg. WAV, AIFF, AU
etc.) are supported. Files encoded with FLAC (the Free Lossless
Audio Codec), Ogg Vorbis, MPEG Audio (including the infamous MP3
format) and MOD files (MOD, S3M, XM, IT, etc.) are also supported.

The program can play the music through OSS, ALSA or the JACK Audio
Connection Kit.

Aqualung supports the LADSPA 1.1 plugin standard. You can use any
suitable plugin to enhance the music you are listening to.

Other features of the program: internally working volume and balance
controls (not touching the soundcard mixer), multiple skin support,
random seeking during playback, track repeat, list repeat and shuffle
mode (besides normal playback). It will come up in the same state as
it was when you closed it, including playback modes, volume & balance
settings, currently processing LADSPA plugins, window sizes,
positions & visibility, and other miscellaneous options.

You can control any running instance of the program remotely from the
command line (start, stop, pause etc.). Remote loading or enqueueing
soundfiles as well as complete playlists is also supported.

In addition to all this, Aqualung provides a so-called Music Store
that is an XML-based music database, capable of storing various
metadata about music on your computer (including, but not limited
to, the names of artists, and the titles of records and tracks).
You can (and should) organize your music into a tree of
Artists/Records/Tracks, thereby making life easier than with the
all-in-one Winamp/XMMS playlist.

Author: Tom Szilagyi <tszilagyi@users.sourceforge.net>

%prep
%setup
%patch
%patch1 -p1

sed -i 's/\[mad], \[mad],/[mad], [libmad],/' configure.ac

%build
%autoreconf
%configure \
	--enable-debug \
	--prefix=%prefix \
	--with-alsa=yes \
	--with-cdda=yes \
	--with-cddb=yes \
	--with-flac=yes \
	--with-ifp=yes \
	--with-jack=yes \
	--with-ladspa=yes \
	--with-lame=yes \
	--with-lavc=yes \
	--with-mac=yes \
	--with-mpc=yes \
	--with-mpeg=yes \
	--with-mod=yes \
	--with-oss=yes \
	--with-sndfile=yes \
	--with-speex=yes \
	--with-src=yes \
	--with-pulse=yes \
	--with-vorbisenc=yes \
	--with-wavpack=yes

# *64 patch
sed -i 's@/usr/lib/@%_libdir/@g' src/plugin.c

%make_build

%install
%makeinstall

# icon
install -Dm 644 src/img/icon_48.png %buildroot%_liconsdir/%name.png

# menu-entry
install -dm 755 %buildroot/%_desktopdir
cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Comment=A music player with LADSPA plugins support
Categories=AudioVideo;Audio;Player;
Terminal=false
Exec=%name
Icon=%name
Name=Aqualung
EOF
install -m 0644 %name.desktop \
	%buildroot/%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README
%doc %_defaultdocdir/aqualung
%_bindir/%name
%_mandir/man1/*
%dir %_datadir/%name
%_datadir/%name/*
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Fri Jan 12 2018 Fr. Br. George <george@altlinux.ru> 1.0-alt2
- Build with new libcdio

* Fri Jul 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Updated to upstream version 1.0

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.9svn1311-alt1.1
- rebuild with new lua 5.3

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 0.9svn1311-alt1
- Autobuild version bump to 0.9svn1311

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1309-alt1
- Autobuild version bump to 0.9svn1309

* Wed Aug 20 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1306-alt1
- Autobuild version bump to 0.9svn1306
- Apply http://aqualung.factorial.hu/mantis/bug_view_page.php?bug_id=0000191 patch

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1303-alt1
- Autobuild version bump to 0.9svn1303

* Tue May 27 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1298-alt1
- Autobuild version bump to 0.9svn1298

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1297-alt1
- Autobuild version bump to 0.9svn1297

* Sat Jan 11 2014 Fr. Br. George <george@altlinux.ru> 0.9svn1272-alt2
- Fix x86_64 typo

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 0.9svn1272-alt1
- Autobuild version bump to 0.9svn1272

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 0.9svn1270-alt1
- Autobuild version bump to 0.9svn1270
- Cosmetic build fix

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 0.9svn1251-alt1
- Autobuild version bump to 0.9svn1251

* Sun Sep 09 2012 Fr. Br. George <george@altlinux.ru> 0.9svn1249-alt1
- Autobuild version bump to 0.9svn1249
- Fix build

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9svn1155-alt1.1
- Rebuilt with ffmpeg 0.7.1

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 0.9svn1155-alt1
- Version up
- Remove direct ALSA output selection in desktop file

* Sun Apr 18 2010 Fr. Br. George <george@altlinux.ru> 0.9svn1140-alt1
- Version up
- Desktop file clean

* Sun Dec 06 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1084-alt1
- Version up

* Tue Nov 17 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1082-alt3
- libcdio soname change

* Tue Oct 20 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1082-alt2
- Version up
- *64 ladspa path fix

* Thu Aug 27 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1075-alt2
- Version up

* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1065-alt2
- Repocop fail fixed

* Wed May 27 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1065-alt1
- Version up
GCC4.4 build fixup

* Tue Jan 06 2009 Fr. Br. George <george@altlinux.ru> 0.9svn1051-alt1
- Version up

* Wed Sep 19 2007 Fr. Br. George <george@altlinux.ru> 0.9beta8-alt1
- Initial build for ALT
- Update to R-827

* Sat Sep 08 2007 Toni Graffy <toni@links2linux.de> - 0.9beta8-826.pm.1
- openSUSE-10.3 build: switched to wavpack
- update to 0.9beta8-826
* Wed Sep 05 2007 Toni Graffy <toni@links2linux.de> - 0.9beta8-823.pm.1
- update to 0.9beta8-823
* Tue Aug 28 2007 Toni Graffy <toni@links2linux.de> - 0.9beta8-797.pm.1
- update to 0.9beta8-797
* Sat Jul 07 2007 Toni Graffy <toni@links2linux.de> - 0.9beta8-0.pm.1
- update to 0.9beta8
* Fri Jun 22 2007 Toni Graffy <toni@links2linux.de> - 0.9beta7.1-685.pm.1
- update to 0.9beta7.1-685
* Sat May 26 2007 Toni Graffy <toni@links2linux.de> - 0.9beta7.1-624.pm.1
- update to 0.9beta7.1-624
* Wed Apr 25 2007 Toni Graffy <toni@links2linux.de> - 0.9beta7.1-597.pm.1
- update to 0.9beta7.1-597
* Sun Feb 25 2007 Toni Graffy <toni@links2linux.de> - 0.9beta7.1-592.pm.1
- update to 0.9beta7.1-592
- enabled WavPack and loop
* Mon Feb 05 2007 Toni Graffy <toni@links2linux.de> - 0.9beta7-0.pm.1
- update to 0.9beta7
* Mon Jan 29 2007 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.555.0.pm.1
- update to 0.9beta6-0.555.0
* Fri Jan 12 2007 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.528.0.pm.1
- update to 0.9beta6-0.528.0
- enabled systray for SuSE >= 1020
* Fri Dec 22 2006 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.501.0.pm.1
- update to 0.9beta6-0.501.0
* Thu Nov 30 2006 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.448.0.pm.1
- update to 0.9beta6-0.448.0
- disabled libcdda for SuSE-10.0
* Mon Nov 13 2006 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.402.0.pm.1
- update to 0.9beta6-0.402.0
* Sun Oct 22 2006 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.233.0.pm.1
- update to 0.9beta6-0.233.0
* Sun Oct 08 2006 Toni Graffy <toni@links2linux.de> - 0.9beta6-0.pm.1
- update to 0.9beta6
- enabled iRiver iFP driver support
* Fri Sep 29 2006 Toni Graffy <toni@links2linux.de> - 0.231.4-0.pm.cvs20060929
- update to 0.231.4
* Mon Sep 18 2006 Toni Graffy <toni@links2linux.de> - 0.227.3-0.pm.cvs20060918
- build for packman
- update to 0.227.3
* Mon Sep 11 2006 oc2pus <oc2pus@arcor.de> - 0.221.0-0.oc2pus.cvs20060911
- update to 0.221.0
* Thu Sep 07 2006 oc2pus <oc2pus@arcor.de> - 0.218.0-0.oc2pus.cvs20060907
- update to 0.218.0
* Mon Sep 04 2006 oc2pus <oc2pus@arcor.de> - 0.215.0-0.oc2pus.cvs20060904
- update to 0.215.0
* Fri Sep 01 2006 oc2pus <oc2pus@arcor.de> - 0.212.6-0.oc2pus.cvs20060901
- update to 0.212.6
* Wed Aug 30 2006 oc2pus <oc2pus@arcor.de> - 0.210.1-0.oc2pus.cvs20060830
- update to 0.210.1
* Mon Aug 28 2006 oc2pus <oc2pus@arcor.de> - 0.206.2-0.oc2pus.cvs20060828
- update to 0.206.2
* Fri Aug 25 2006 oc2pus <oc2pus@arcor.de> - 0.203.0-0.oc2pus.cvs20060825
- update to 0.203.0
* Mon Aug 21 2006 oc2pus <oc2pus@arcor.de> - 0.200.1-0.oc2pus.cvs20060821
- update to 0.200.1
* Sat Aug 19 2006 oc2pus <oc2pus@arcor.de> - 0.199.1-0.oc2pus.cvs20060819
- update to 0.199.1
* Sat Aug 12 2006 oc2pus <oc2pus@arcor.de> - 0.196.0-0.oc2pus.cvs20060812
- update to 0.196.0
* Tue Aug 08 2006 oc2pus <oc2pus@arcor.de> - 0.193.3-0.oc2pus.1
- update to 0.193.3
* Sat Aug 05 2006 oc2pus <oc2pus@arcor.de> - 0.192.0-0.oc2pus.1
- update to 0.192.0
* Thu Aug 03 2006 oc2pus <oc2pus@arcor.de> - 0.190.2-0.oc2pus.1
- update to 0.190.2
* Fri Jul 28 2006 oc2pus <oc2pus@arcor.de> - 0.189.0-0.oc2pus.1
- update to 0.189.0
* Sun Jul 23 2006 oc2pus <oc2pus@arcor.de> - 0.188.0-0.oc2pus.1
- update to 0.188.0
* Tue Jul 18 2006 oc2pus <oc2pus@arcor.de> - 0.187.3-0.oc2pus.1
- update to 0.187.3
* Wed Jul 12 2006 oc2pus <oc2pus@arcor.de> - 0.187.0-0.oc2pus.1
- update to 0.187.0
* Fri Jun 30 2006 oc2pus <oc2pus@arcor.de> - 0.186.2-0.oc2pus.1
- update to 0.186.2
- changed desktop-file
* Sat Jun 24 2006 oc2pus <oc2pus@arcor.de> - 0.184.0-0.oc2pus.1
- update to 0.184.0
- added patch1 (core.c)
- added Monkey's Audio Codec support
* Tue Jun 20 2006 oc2pus <oc2pus@arcor.de> - 0.183.5-0.oc2pus.1
- First packaged release 0.183.5
- repacked as tar.bz2
