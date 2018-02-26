%define binary_name mocp
%define decoder_plugins %_libdir/%name/decoder_plugins

%def_disable debug
%def_disable static

%def_without aac
%def_with ffmpeg
%def_with flac
%def_with modplug
%def_with mp3
%def_with musepack
%def_without sidplay2
%def_with sndfile
%def_with speex
%def_with timidity
%def_with vorbis 
%def_with wavpack

Name: moc
Version: 2.5.0
Release: alt0.10

Summary: Console player
Group: Sound
License: GPL
Url: http://moc.daper.net/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: moc-%version.tar

Requires: %name-player %name-plugin-flac %name-plugin-mp3 %name-plugin-sndfile %name-plugin-vorbis

# Automatically added by buildreq on Wed Jun 07 2006
BuildRequires: gcc-c++ glibc-devel-static jackit-devel libalsa-devel libcurl-devel 
BuildRequires: libncursesw-devel libsamplerate-devel pkg-config libltdl7-devel
BuildRequires: libdb4.7-devel libmagic-devel

%description
MOC is a console audio player with simple ncurses interface in
playmp3list style.

Supported file formats are: mp3, Ogg Vorbis, FLAC, Musepack (mpc), Speex, WAVE,
supported by FFmpeg (WMA, RealAudio, AAC, MP4), AIFF, AU, SVX, Sphere Nist WAV,
IRCAM SF, Creative VOC.

%package player
Summary: Console player
Group: Sound
Requires: %name-decoder-plugin

Conflicts: %name-plugin-ffmpeg <= 2.5.0-alt0.7

%description player
MOC is a console audio player with simple ncurses interface in
playmp3list style.

%if_with aac
%package plugin-aac
Summary: AAC decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libfaad-devel

%description plugin-aac
AAC decoder plugin for %name.
%endif

%if_with ffmpeg
%package plugin-ffmpeg
Summary: ffmpeg decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libavformat-devel liblame-devel

%description plugin-ffmpeg
ffmpeg decoder plugin for %name.
Formats: wma, ra, ,m4a, aac.
%endif

%if_with flac
%package plugin-flac
Summary: flac decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libflac-devel

%description plugin-flac
FLAC support.
Formats: flac, fla.
%endif

%if_with modplug
%package plugin-modplug
Summary: modplug decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libmodplug-devel

%description plugin-modplug
modplug decoder plugin for %name.
%endif

%if_with mp3
%package plugin-mp3
Summary: mp3 decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libid3tag-devel libmad-devel librcc-devel

%description plugin-mp3
mp3 support (libmad).
Formats: mp3, mpga, mp2, mp1.
%endif

%if_with musepack
%package plugin-musepack
Summary: musepack decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libtag-devel libmpcdec-devel

%description plugin-musepack
musepack support.
Formats: mpc.
%endif

%if_with sidplay2
%package plugin-sidplay2
Summary: sidplay2 decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libsidplay2-devel

%description plugin-sidplay2
sidplay2 decoder plugin for %name.
%endif

%if_with sndfile
%package plugin-sndfile
Summary: sndfile decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libsndfile-devel

%description plugin-sndfile
sndfile decoder plugin for %name.
Formats: au, snd, wav, aif, aiff, 8svx, sph, sf, voc.
%endif

%if_with speex
%package plugin-speex
Summary: speex decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libspeex-devel

%description plugin-speex
speex decoder plugin for %name.
Formats: spx.
%endif

%if_with timidity
%package plugin-timidity
Summary: timidity decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libtimidity-devel

%description plugin-timidity
timidity decoder plugin for %name.
%endif

%if_with vorbis
%package plugin-vorbis
Summary: vorbis decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libvorbis-devel

%description plugin-vorbis
Ogg Vorbis support.
Formats: ogg.
%endif

%if_with wavpack
%package plugin-wavpack
Summary: wavpack decoder plugin for %name
Group: Sound
Provides: %name-decoder-plugin
Requires: %name-player
BuildRequires: libwavpack-devel

%description plugin-wavpack
Hybrid Lossless Wavefile Compressor support.
%endif

%prep
%setup -q

%build
%add_optflags %optflags_warnings
%autoreconf

%configure \
	--with-rcc \
	--without-oss \
	%{subst_enable debug} \
	%{subst_with aac} \
	%{subst_with modplug} \
	%{subst_with sidplay2} \
	%{subst_with timidity} \
	%{subst_with musepack} \
	%{subst_with sndfile} \
	%{subst_with wavpack} \
	%{subst_with vorbis} \
	%{subst_with ffmpeg} \
	%{subst_with speex} \
	%{subst_with flac} \
	%{subst_with mp3} \
	#

%make_build

%install
%make_install DESTDIR=%buildroot install

%__mkdir_p %buildroot/%_desktopdir
%__cat >%buildroot/%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Categories=Audio;Player
Exec=%_bindir/%binary_name
Icon=sound_section
Name=Music On Console
Terminal=true
EOF

%__rm -rf %buildroot%_docdir/%name %buildroot/%decoder_plugins/*.la
%add_findprov_lib_path %decoder_plugins

%files

%files player
%_bindir/*
%dir %_libdir/%name
%dir %decoder_plugins
%_datadir/%name
%_man1dir/*
%_desktopdir/%name.desktop
%doc AUTHORS NEWS TODO README *.example

%if_with aac
%files plugin-aac
%decoder_plugins/libaac_decoder.so
%endif

%if_with ffmpeg
%files plugin-ffmpeg
%decoder_plugins/libffmpeg_decoder.so
%endif

%if_with flac
%files plugin-flac
%decoder_plugins/libflac_decoder.so
%endif

%if_with modplug
%files plugin-modplug
%decoder_plugins/libmodplug_decoder.so
%endif

%if_with mp3
%files plugin-mp3
%decoder_plugins/libmp3_decoder.so
%endif

%if_with musepack
%files plugin-musepack
%decoder_plugins/libmusepack_decoder.so
%endif

%if_with sidplay2
%files plugin-sidplay2
%decoder_plugins/libsidplay2_decoder.so
%endif

%if_with sndfile
%files plugin-sndfile
%decoder_plugins/libsndfile_decoder.so
%endif

%if_with speex
%files plugin-speex
%decoder_plugins/libspeex_decoder.so
%endif

%if_with timidity
%files plugin-timidity
%decoder_plugins/libtimidity_decoder.so
%endif

%if_with vorbis
%files plugin-vorbis
%decoder_plugins/libvorbis_decoder.so
%endif

%if_with wavpack
%files plugin-wavpack
%decoder_plugins/libwavpack_decoder.so
%endif

%changelog
* Fri May 25 2012 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.10
- New snapshot from trunk (2.5.0 r2425)

* Wed Aug 17 2011 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.9
- New snapshot from trunk (2.5.0 r2360)
- Enable ffmpeg plugin (thanks Eugeny A. Rostovtsev).
- Add libmagic support.

* Tue Aug 16 2011 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.8
- Disable ffmpeg plugin.

* Mon Aug 16 2010 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.7
- New version (2.5.0-alpha4)
- Remove libfaac-devel.

* Tue Sep 29 2009 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.6
- Fix malformed Layout1 (ALT#21671).

* Mon Aug 24 2009 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.5
- Add modplug and timidity plugins.

* Sun Aug 23 2009 L.A. Kostis <lakostis@altlinux.ru> 2.5.0-alt0.4
- NMU:
  + Add APE format support thru ffmpeg (see http://moc.daper.net/node/110).
  + Fix for newer ffmpeg (use avcodec_decode_audio2).

* Tue Jun 02 2009 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.3
- New version (2.5.0-alpha3)

* Mon Mar 10 2008 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.2
- New version (2.5.0-alpha2)
- Add new decoder plugins: wavpack.

* Thu May 10 2007 Alexey Gladkov <legion@altlinux.ru> 2.5.0-alt0.1
- New version (2.5.0-alpha1)

* Tue Oct 31 2006 Alexey Gladkov <legion@altlinux.ru> 2.4.1-alt2
- Add patch for recode filnames and directories. This is useful 
  for non UTF-8 locales.

* Fri Oct 27 2006 Alexey Gladkov <legion@altlinux.ru> 2.4.1-alt1
- new version

* Fri Sep 22 2006 Alexey Gladkov <legion@altlinux.ru> 2.4.0-alt2
- Package split on: moc, moc-player, moc-plugin-*.
  + moc - virtual package for back compatibity.
- Add new decoder plugins: ffmpeg, musepack, speex.

* Wed Jun 07 2006 Alexey Gladkov <legion@altlinux.ru> 2.4.0-alt1
- new version
- librcc support fixed

* Thu Dec 29 2005 Alexey Gladkov <legion@altlinux.ru> 2.3.2-alt3
- librcc support was added.
- build with -Werror

* Mon Oct 10 2005 Alexey Gladkov <legion@altlinux.ru> 2.3.2-alt2
- %%_libdir/%%name was added to files list.

* Fri Oct 07 2005 Alexey Gladkov <legion@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Aug 03 2005 Alexey Gladkov <legion@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Jun 20 2005 Alexey Gladkov <legion@altlinux.ru> 2.3.0.beta1-alt1
- 2.3.0

* Thu May 26 2005 Alexey Gladkov <legion@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Mar 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- new version.

* Sat Jan 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Sun Nov 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- new version.

* Tue May 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt0.3
- Binary renamed to music-on-console (inger) to avoid incredible
  conflict with QT utility with the same name.
- menu (ZerG)

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt0.2
- new version
- qt-devel added to conflict list.

* Fri Nov 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.1
- First build for Sisyphus.

