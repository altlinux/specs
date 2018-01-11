%set_verify_elf_method textrel=relaxed 
%define gtkver 3
Name:		deadbeef
Version:	0.7.1
Release:	alt3.20160419.1.1
Summary:	DeaDBeeF is an audio player
Url:		http://deadbeef.sf.net
#https://github.com/Alexey-Yakovenko/deadbeef
Source0:	%name-%version.tar
Group:		Sound
License:	zlib, GPLv2, LGPLv2.1

Patch1:		deadbeef-plugins-ffmpeg-aac-support.patch
Patch2:		deadbeef-repocop-desktop-file.patch
Patch3:		deadbeef-0.5.1-alt-libav-using.patch
Patch4:		deadbeef-0.5.1-fr-fix-build.patch
Patch5:		deadbeef-0.5.1-using-tt.patch
Patch6:		deadbeef-0.5.4-alt-categories-desktop-file.patch
Patch7:		deadbeef-0.5.6-alt-gdk-threads.patch

BuildRequires: /usr/bin/yasm gcc-c++ intltool glib2-devel libX11-devel libatk-devel libcairo-devel libcddb-devel libcdio-devel libcdparanoia-devel libcurl-devel libfaad-devel libflac-devel libgdk-pixbuf-devel libgtk+2-devel libjpeg-devel libmad-devel libmpg123-devel libogg-devel libpango-devel libpng-devel libsndfile-devel libvorbis-devel libwavpack-devel perl(Exporter.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(IPC/Open3.pm) perl(Locale/Country.pm) perl(Locale/Language.pm) perl(base.pm) pkgconfig(alsa) pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(gtk+-3.0) pkgconfig(imlib2) pkgconfig(jansson) pkgconfig(libavcodec) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(libpulse-simple) pkgconfig(libzip) pkgconfig(samplerate) swig zlib-devel

Requires:	%name-out-alsa %name-gtk%gtkver

Obsoletes:	%name-medialib	

%description
DeaDBeeF is an audio player for GNU/Linux systems with
X11 written in C and C++. Features: minimal depends,
native GTK%gtkver GUI, cuesheet support, mp3, ogg, flac, ape,
chiptune formats with subtunes, song-length databases, etc,
small memory footprint.

# Virlual packages
%package -n %name-incomplete
Summary: DeaDBeeF is an audio player
Group: Sound
BuildArch: noarch
# Out
Requires: %name-out-pulseaudio
# In
Requires: %name-in-flac %name-in-mp3 %name-in-psf %name-in-ffmpeg %name-in-oggvorbis %name-in-ape %name-in-musepack %name-in-aac %name-in-wavpack %name-in-sndfile

# DSP
#Requires: %name-dsp-supereq %name-dsp-libsrc

# General
Requires: %name-artwork %name-hotkeys %name-notify %name-gtk%gtkver %name-shellexec %name-m3u

%description -n %name-incomplete
Virtual package for incomplete installation DeaDBeeF
(like full but excluding midi, oss, another crap)

%package -n %name-full
Summary: DeaDBeeF is an audio player
Group: Sound
BuildArch: noarch
# Out
Requires: %name-out-pulseaudio %name-out-oss %name-out-alsa %name-out-null
# In
Requires: %name-in-wavpack %name-in-vtx %name-in-oggvorbis %name-in-sndfile
Requires: %name-in-sid %name-in-gme %name-in-flac %name-in-ffmpeg
Requires: %name-in-ape %name-in-cdaudio %name-in-adplug %name-in-vfs_curl
Requires: %name-in-dca %name-in-musepack %name-in-tta %name-in-wildmidi
Requires: %name-in-mms %name-in-aac %name-in-alac %name-in-dumb
Requires: %name-in-shn %name-in-mp3 %name-in-psf

# General
Requires: %name-artwork %name-hotkeys %name-lastfm %name-notify 
Requires: %name-gtk%gtkver %name-pltbrowser_gtk%gtkver
Requires: %name-shellexec
Requires: %name-m3u
Requires: %name-dsp-supereq %name-dsp-libsrc %name-dsp-mono2stereo

%description -n %name-full
Virtual package for full installation DeaDBeeF (exclude %name-devel,
%name-statusnotifier, %name-in-sc68).

# Development
%package -n %name-devel
Summary: DeaDBeeF header files
Group: Development/C++
BuildArch: noarch

%description -n %name-devel
%name-devel contains the header files needed to develop
programs which make use of DeaDBeeF.

# Output plugins
%package -n %name-out-pulseaudio
Summary: DeaDBeeF PulseAudio Output Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-out-pulseaudio
DeaDBeeF PulseAudio Output Plugin
plays sound via pulse API

%package -n %name-out-oss
Summary: DeaDBeeF OSS Output Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-out-oss
DeaDBeeF OSS Output Plugin
plays sound via OSS API

%package -n %name-out-alsa
Summary: DeaDBeeF ALSA Output Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-out-alsa
DeaDBeeF ALSA Output Plugin
plays sound through linux standard alsa library

%package -n %name-out-null
Summary: DeaDBeeF Null Output Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-out-null
DeaDBeeF Null Output Plugin
doesn't play anything

# Input plugins
%package -n %name-in-alac
Summary: DeaDBeeF ALAC Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-alac
DeaDBeeF ALAC Input Plugin
plays alac files from MP4 and M4A files

%package -n %name-in-dumb
Summary: DeaDBeeF DUMB module player Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-dumb
DeaDBeeF DUMB module player Plugin
module player based on DUMB library

%package -n %name-in-wavpack
Summary: DeaDBeeF WavPack Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-wavpack
DeaDBeeF WavPack Input Plugin
.wv player using libwavpack

%package -n %name-in-vtx
Summary: DeaDBeeF VTX Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-vtx
DeaDBeeF VTX Input Plugin
AY8910/12 chip emulator and vtx file player

%package -n %name-in-oggvorbis
Summary: DeaDBeeF OggVorbis Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-oggvorbis
DeaDBeeF OggVorbis Input Plugin
OggVorbis decoder using standard xiph.org libraries


%package -n %name-in-shn
Summary: DeaDBeeF Shorten player Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-shn
DeaDBeeF Shorten player Input Plugin
decodes shn files

%package -n %name-in-sndfile
Summary: DeaDBeeF SndFile Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-sndfile
DeaDBeeF SndFile Input Plugin
wav/aiff player using libsndfile

%package -n %name-in-sid
Summary: DeaDBeeF SID Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-sid
DeaDBeeF SID Input Plugin
SID player based on libsidplay2

%package -n %name-in-gme
Summary: DeaDBeeF GME Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-gme
DeaDBeeF GME Input Plugin
chiptune music player based on GME

%package -n %name-in-flac
Summary: DeaDBeeF FLAC Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-flac
DeaDBeeF FLAC Input Plugin
FLAC decoder using libFLAC

%package -n %name-in-psf
Summary: DeaDBeeF psf Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-psf
DeaDBeeF psf Input Plugin
psf decoder

%package -n %name-in-ffmpeg
Summary: DeaDBeeF FFMPEG Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-ffmpeg
DeaDBeeF FFMPEG Input Plugin
decodes audio formats using FFMPEG libavcodec

%package -n %name-in-ape
Summary: DeaDBeeF APE Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-ape
DeaDBeeF Monkey's Audio (APE) Input Plugin
APE player based on code from libavc and rockbox

%package -n %name-in-cdaudio
Summary: DeaDBeeF Audio CD Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-cdaudio
DeaDBeeF Audio CD Input Plugin
using libcdio, includes .nrg image support

%package -n %name-in-adplug
Summary: DeaDBeeF Adplug Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-adplug
DeaDBeeF Adplug Input Plugin
Adplug player (ADLIB OPL2/OPL3 emulator)

%package -n %name-in-vfs_curl
Summary: DeaDBeeF cURL VFS Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-vfs_curl
DeaDBeeF cURL VFS Plugin
http and ftp streaming module using libcurl, with ICY protocol support

%package -n %name-in-dca
Summary: DeaDBeeF DCA Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-dca
DeaDBeeF DCA Input Plugin

%package -n %name-in-musepack
Summary: DeaDBeeF MusePack Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-musepack
DeaDBeeF MusePack Input Plugin

%package -n %name-in-tta
Summary: DeaDBeeF TTA Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-tta
DeaDBeeF TTA Input Plugin

%package -n %name-in-wildmidi
Summary: DeaDBeeF WildMidi Input Plugin
Group: Sound
Requires: %name = %version-%release
Requires: timidity-freepats

%description -n %name-in-wildmidi
DeaDBeeF WildMidi Input Plugin

%package -n %name-in-mms
Summary: DeaDBeeF MMS Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-mms
DeaDBeeF MMS Input Plugin

%package -n %name-in-aac
Summary: DeaDBeeF AAC Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-aac
DeaDBeeF AAC Input Plugin

%package -n %name-in-wma
Summary: DeaDBeeF WMA Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-wma
DeaDBeeF Windows Media Audio (WMA) Input Plugin

%package -n %name-in-mp3
Summary: DeaDBeeF mp3 Input Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-mp3
DeaDBeeF mp3 Input Plugin
mp3 decoder

# General plugins
%package -n %name-dsp-supereq
Summary: DeaDBeeF SuperEQ Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-dsp-supereq
DeaDBeeF SuperEQ Plugin
equalizer plugin using SuperEQ library by Naoki Shibata

%package -n %name-dsp-mono2stereo
Summary: DeaDBeeF Mono to stereo Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-dsp-mono2stereo
DeaDBeeF Mono to stereo Plugin
DSP plugin to convert mono to stereo

%package -n %name-artwork
Summary: DeaDBeeF Album Artwork Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-artwork
DeaDBeeF Album Artwork Plugin
Loads album artwork either from local directories or from internet
Requires: %name = %version-%release
Requires: %name-in-vfs_curl

%package -n %name-hotkeys
Summary: DeaDBeeF Hotkeys Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-hotkeys
DeaDBeeF Hotkeys Plugin
Allows to control player with global hotkeys

%package -n %name-lastfm
Summary: DeaDBeeF Last.FM Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-lastfm
DeaDBeeF Last.FM Plugin
sends played songs information to your last.fm account

%package -n %name-notify
Summary: DeaDBeeF OSD Notify Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-notify
DeaDBeeF OSD Notify Plugin
notification daemon OSD

%package -n %name-statusnotifier
Summary: KDE Status Notifier
Group: Sound
Requires: %name = %version-%release

%description -n %name-statusnotifier
System tray icon support for KDE 5

%package -n %name-gtk%gtkver
Summary: DeaDBeeF GTK%gtkver UI Plugin
Group: Sound
Requires: %name = %version-%release
Obsoletes: %name-gtkui

%description -n %name-gtk%gtkver
DeaDBeeF GTK%gtkver UI Plugin
Default DeaDBeeF GUI

%package -n %name-shellexec
Summary: DeaDBeeF ShellExec Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-shellexec
DeaDBeeF ShellExec Plugin

%package -n %name-m3u
Summary: DeaDBeeF m3u playlist support
Group: Sound
Requires: %name = %version-%release

%description -n %name-m3u
DeaDBeeF m3u Plugin
Allows to load/save playlists in m3u format

%package -n %name-dsp-libsrc
Summary: DeaDBeeF libsamplerate Plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-dsp-libsrc
DeaDBeeF libsamplerate resampler

%package -n %name-converter
Summary: DeaDBeeF audio format converter
Group: Sound
Requires: %name = %version-%release
Requires: ttaenc
Requires: faac
Requires: wavpack
Requires: musepack
Requires: lame
Requires: vorbis-tools
Requires: opus-tools
Requires: ffmpeg

%description -n %name-converter
Allows file conversion between various containers and codecs.


#package -n %name-medialib
#Summary: DeaDBeeF medialib plugin
#Group: Sound
#Requires: %name = %version-%release

#description -n %name-medialib
#DeaDBeeF medialib Plugin
#Scans disk for music files and manages them as database.

%package -n %name-pltbrowser_gtk%gtkver
Summary: Deadbeef plugin
Group: Sound
Requires: %name = %version-%release

%description -n %name-pltbrowser_gtk%gtkver
Playlist browser plugin.

%package -n %name-in-sc68
Summary: DeaDBeeF SC68 player
Group: Sound
Requires: %name = %version-%release

%description -n %name-in-sc68
SC68 player (Atari ST SNDH YM2149)

%prep
%setup
#patch1 -p2
#patch2 -p1
#patch3 -p2
#patch4 -p2
#patch5 -p2
%patch6 -p2
#patch7 -p2

sed -i '/m4/ d' Makefile.am

%build
#%%autoreconf 
./autogen.sh
%configure --enable-notify --docdir=%_docdir/%name-%version --disable-static \
		--enable-src=yes \
		--enable-m3u=yes \
		--enable-ffmpeg=yes \
		--enable-gtk%gtkver=yes \
		#--enable-medialib=yes \


%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name
rm -rf %buildroot/%_libdir/%name/*.la

%files  -f %name.lang
%dir %_libdir/%name
%doc AUTHORS COPYING COPYING.* NEWS README ChangeLog about.txt help.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/*/*/*/%name.*

# Output plugins
%files -n %name-out-pulseaudio
%_libdir/%name/pulse.*

%files -n %name-out-oss
%_libdir/%name/oss.*

%files -n %name-out-alsa
%_libdir/%name/alsa.*

%files -n %name-out-null
%_libdir/%name/nullout.*

# Input plugins
%files -n %name-in-alac
%_libdir/%name/alac.*

%files -n %name-in-dumb
%_libdir/%name/ddb_dumb.*

%files -n %name-in-wavpack
%_libdir/%name/wavpack.*

%files -n %name-in-vtx
%_libdir/%name/vtx.*

%files -n %name-in-oggvorbis
%_libdir/%name/vorbis.*

%files -n %name-in-shn
%_libdir/%name/ddb_shn.*

%files -n %name-in-sndfile
%_libdir/%name/sndfile.*

%files -n %name-in-sid
%_libdir/%name/sid.*

%files -n %name-in-gme
%_libdir/%name/gme.*

%files -n %name-in-flac
%_libdir/%name/flac.*

%files -n %name-in-ffmpeg
%_libdir/%name/ffmpeg.*

%files -n %name-in-ape
%_libdir/%name/ffap.*

%files -n %name-in-cdaudio
%_libdir/%name/cdda.*

%files -n %name-in-adplug
%_libdir/%name/adplug.*

%files -n %name-in-vfs_curl
%_libdir/%name/vfs_curl.*

%files -n %name-in-dca
%_libdir/%name/dca.*

%files -n %name-in-musepack
%_libdir/%name/musepack.*

%files -n %name-in-tta
%_libdir/%name/tta.*

%files -n %name-in-wildmidi
%_libdir/%name/wildmidi.*

%files -n %name-in-mms
%_libdir/%name/mms.*

%files -n %name-in-aac
%_libdir/%name/aac.*

%files -n %name-in-wma
%_libdir/%name/wma.*

%files -n %name-in-mp3
%_libdir/%name/mp3.*

%files -n %name-in-psf
%_libdir/%name/psf.*

%files -n %name-in-sc68
%_libdir/%name/data68/Replay/*
%_libdir/%name/in_sc68.*

# General plugins
%files -n %name-artwork
%_libdir/%name/artwork.*

%files -n %name-hotkeys
%_libdir/%name/hotkeys.*

%files -n %name-lastfm
%_libdir/%name/lastfm.*

%files -n %name-notify
%_libdir/%name/notify.*

%files -n %name-statusnotifier
%_libdir/%name/statusnotifier.so

%files -n %name-gtk%gtkver
%_libdir/%name/ddb_gui_GTK%gtkver.*

%files -n %name-dsp-supereq
%_libdir/%name/supereq.*

%files -n %name-shellexec
%_libdir/%name/shellexec*

%files -n %name-m3u
%_libdir/%name/m3u.*

%files -n %name-dsp-libsrc
%_libdir/%name/dsp_libsrc.*

%files -n %name-dsp-mono2stereo
%_libdir/%name/ddb_mono2stereo.*

%files -n %name-converter
%_libdir/%name/converter.so*
%_libdir/%name/converter_gtk*.so*
%_libdir/%name/convpresets

#files -n %name-medialib
#_libdir/%name/medialib.*

%files -n %name-pltbrowser_gtk%gtkver
%_libdir/%name/pltbrowser_gtk%gtkver.*

# Development
%files -n %name-devel
%dir %_includedir/%name
%_includedir/%name/*.h

# Virtual packages
%files -n %name-full
%files -n %name-incomplete

%changelog
* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt3.20160419.1.1
- rebuild against libcdio.so.18

* Mon Aug 14 2017 Anton Midyukov <antohami@altlinux.org> 0.7.1-alt3.20160419.1
- Added missing requires for deadbeef-converter (Closes: 33755)

* Tue Jun 06 2017 Anton Midyukov <antohami@altlinux.org> 0.7.1-alt2.20160419.1
- Rebuild with ffmpeg.

* Thu Apr 21 2016 Anton Midyukov <antohami@altlinux.org> 0.7.1-alt1.20160419.1
- version update to 0.7.1-alt1.20160419.1 (Closes: 31763)
- build with gtk3
- remove packages:
  - deadbeef-in-ao
  - deadbeef-in-mpeg
- added packages:
  + deadbeef-in-psf
  + deadbeef-in-mp3
  + deadbeef-in-sc68

* Sun Dec 28 2014 Andrew Clark <andyc@altlinux.org> 0.6.2-alt2.b647da7f
- version update to 0.6.2-alt2.b647da7f

* Mon Sep 22 2014 Andrew Clark <andyc@altlinux.org> 0.6.2-alt1.860f7de5
- version update to 0.6.2-alt1.860f7de5

* Thu Jan 9 2014 Andrew Clark <andyc@altlinux.org> 0.6.0-alt1.5f781386
- version update to 0.6.0-alt1.5f781386

* Sat Oct 12 2013 Andrew Clark <andyc@altlinux.org> 0.5.6-alt4.5390e6de
- version update to 0.5.6-alt4.5390e6de

* Mon May 27 2013 Andrew Clark <andyc@altlinux.org> 0.5.6-alt3.252d7cbf
- version update to 0.5.6-alt3.252d7cbf

* Fri Dec 14 2012 Vladimir Didenko <cow@altlinux.org> 0.5.6-alt2.47f64084
- remove waste gdk_threads_enter(Closes: 27966)

* Sun Oct 28 2012 Andrew Clark <andyc@altlinux.org> 0.5.6-alt1.47f64084
- new version

* Thu Oct 11 2012 Alexander Plehanov <tonik@altlinux.org> 0.5.4-alt4.bfca08d0
- Changed "Categories" in deadbeef.desktop.in

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt3.bfca08d0.1
- Rebuilt with libpng15

* Sun Jun 10 2012 Andrew Clark <andyc@altlinux.ru> 0.5.4-alt3.bfca08d0
- relaxed elf check. thanks to real@ for the tip.

* Thu Jun 7 2012 Andrew Clark <andyc@altlinux.ru> 0.5.4-alt2.bfca08d0
- Monkey's Audio plugin has been enabled

* Sun Jun 3 2012 Andrew Clark <andyc@altlinux.org> 0.5.4-alt1.bfca08d0
- version update to 0.5.4-alt1.bfca08d0
- Monkey's Audio plugin has been disabled

* Thu Sep 22 2011 Radik Usupov <radik@altlinux.org> 0.5.1-alt4
- really using tt_RU
- fixed fr language
- renamed libav patch

* Tue Aug 09 2011 Radik Usupov <radik@altlinux.org> 0.5.1-alt3
- Fixed build errors

* Wed Jun 22 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.1-alt2
- internal requires fixed for %name-artwork

* Mon May 23 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.1-alt1
- new version

* Fri May 20 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt4
- converter subpackage.
- virtual package fixed.

* Thu May 19 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt3
- new upstream snapshot
- added virtual package for incomplete installation

* Wed May 18 2011 Radik Usupov <radik@altlinux.org> 0.5.0-alt2
- Added requires to wildmidi-plugin (Closes: 25474)

* Mon May 16 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt1
- new upstream release

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt0.1
- new (beta) version

* Wed Apr 13 2011 Lenar Shakirov <snejok@altlinux.ru> 0.4.4-alt4
- AAC plugin added

* Wed Apr 13 2011 Lenar Shakirov <snejok@altlinux.ru> 0.4.4-alt3
- fixed build: zlib-devel libfaad-devel added to BuildReqs
- desktop file cleaned: thanks to repocop!

* Fri Feb 04 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.4-alt2
- pushed to sisyphus (thanks andyc@)

* Sat Jan 15 2011 Andrew Clark <andyc@altlinux.org> 0.4.4-alt1
- version update to 0.4.4-alt1

* Mon Nov 01 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.3-alt1
- new version

* Tue Oct 19 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.2-alt2
- MMS plugin addded (thanks vvk@)

* Sat Oct 16 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.2-alt0.M51.1
- build for M51

* Sat Oct 16 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.2-alt1
- new version

* Wed Sep 22 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt4
- upstream snapshot

* Thu Jul 22 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt2.M51.1
- build for M51

* Thu Jul 22 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt3
- *.aac support at ffmpeg plugin

* Sun Jun 06 2010 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1.M51.1
- build for M51

* Sun Jun 06 2010 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt2
- merged from Radik Usupov git.alt (added localization)

* Mon May 31 2010 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1
- 0.4.1 release

* Sat May 22 2010 Andrew Clark <andyc@altlinux.org> 0.4.0-alt1
- version update to 0.4.0-alt1

* Sun Mar 28 2010 Andrew Clark <andyc@altlinux.org> 0.3.3-alt1
- version update to 0.3.3-alt1

* Thu Oct 22 2009 Igor Zubkov <icesik@altlinux.org> 0.2.3.2-alt2
- enable wavpack plugin

* Wed Oct 14 2009 Igor Zubkov <icesik@altlinux.org> 0.2.3.2-alt1
- 0.2.2.2 -> 0.2.3.2

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 0.2.2.2-alt1
- 0.2.1 -> 0.2.2.2

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 0.2.1-alt1
- 0.2.0 -> 0.2.1

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt3
- fix desktop file

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt2
- disable asm optimization for sse2

* Thu Sep 10 2009 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt1
- 0.1.1 -> 0.2.0

* Sun Aug 30 2009 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt1
- build for Sisyphus
