Name: sox
Summary: A general purpose sound file conversion tool
Version: 14.3.2
Release: alt2
License: LGPL
Group: Sound
BuildRequires: glibc-devel-static libalsa-devel libao-devel libavformat-devel libflac-devel libgomp-devel libgsm-devel libid3tag-devel liblame-devel libltdl7-devel libmad-devel libmagic-devel libopencore-amrnb-devel libopencore-amrwb-devel libpng-devel libpulseaudio-devel libsndfile-devel libvorbis-devel libwavpack-devel rpm-build-ruby
BuildRequires: ladspa_sdk libalsa-devel libao-devel libavformat-devel libflac-devel libgomp-devel libgsm-devel libid3tag-devel liblame-devel libltdl-devel libmad-devel libmagic-devel libpng-devel libpulseaudio-devel libsndfile-devel libvorbis-devel libwavpack-devel
BuildRequires: libopencore-amrnb-devel libopencore-amrwb-devel
Packager: Denis Smirnov <mithraen@altlinux.org>
Url: http://%name.sourceforge.net/
Source: %name-%version.tar
Source1: soxeffect
Requires: sox-play = %version-%release
Requires: sox-base = %version-%release
Requires: libsox-fmt-alsa = %version-%release
Requires: libsox-fmt-ao = %version-%release
Requires: libsox-fmt-caf = %version-%release
Requires: libsox-fmt-fap = %version-%release
Requires: libsox-fmt-ffmpeg = %version-%release
Requires: libsox-fmt-flac = %version-%release
Requires: libsox-fmt-gsm = %version-%release
Requires: libsox-fmt-lpc10 = %version-%release
Requires: libsox-fmt-mat4 = %version-%release
Requires: libsox-fmt-mat5 = %version-%release
Requires: libsox-fmt-mp3 = %version-%release
Requires: libsox-fmt-oss = %version-%release
Requires: libsox-fmt-paf = %version-%release
Requires: libsox-fmt-pulseaudio = %version-%release
Requires: libsox-fmt-pvf = %version-%release
Requires: libsox-fmt-sd2 = %version-%release
Requires: libsox-fmt-sndfile = %version-%release
Requires: libsox-fmt-vorbis = %version-%release
Requires: libsox-fmt-w64 = %version-%release
Requires: libsox-fmt-wavpack = %version-%release
Requires: libsox-fmt-xi = %version-%release
Requires: libsox-fmt-caf = %version-%release
Requires: libsox-fmt-fap = %version-%release
Patch1: %name-13.0.0-alt-gsm.patch
Patch2: %name.ffmpeg.patch

%package -n libsox
Summary: The SoX sound file format converter libraries
Group: Development/C
Provides: libsox-fmt-sndfile = %version-%release

%description -n libsox
This package contains libraries for SoX


%package -n libsox-devel
Summary: The SoX sound file format converter headers files and libraries
Group: Sound
Requires: %name = %version-%release
Obsoletes: sox-devel < %version-%release
Provides:  sox-devel = %version-%release
Requires: libsox = %version-%release

%description -n libsox-devel
This package contains the headers and library needed for compiling
applications which will use the SoX sound file format converter.


%package -n libsox-devel-static
Summary: The SoX sound file format converter headers files and libraries
Group: Sound
Requires: %name = %version-%release
Obsoletes: sox-devel

%description -n libsox-devel-static
This package contains the headers and library needed for compiling
applications which will use the SoX sound file format converter.
Install %name-devel if you want to develop applications which will use SoX.


%package -n libsox-fmt-alsa
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-alsa
%summary

%package -n libsox-fmt-ao
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-ao
%summary

%package -n libsox-fmt-caf
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-caf
%summary

%package -n libsox-fmt-fap
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-fap
%summary

%package -n libsox-fmt-ffmpeg
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-ffmpeg
%summary

%package -n libsox-fmt-flac
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-flac
%summary

%package -n libsox-fmt-gsm
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-gsm
%summary

%package -n libsox-fmt-lpc10
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-lpc10
%summary

%package -n libsox-fmt-mat4
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-mat4
%summary

%package -n libsox-fmt-mat5
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-mat5
%summary

%package -n libsox-fmt-mp3
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-mp3
%summary

%package -n libsox-fmt-oss
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-oss
%summary

%package -n libsox-fmt-paf
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-paf
%summary

%package -n libsox-fmt-pulseaudio
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-pulseaudio
%summary

%package -n libsox-fmt-pvf
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-pvf
%summary

%package -n libsox-fmt-sd2
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-sd2
%summary

%package -n libsox-fmt-sndfile
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-sndfile
%summary

%package -n libsox-fmt-vorbis
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-vorbis
%summary

%package -n libsox-fmt-w64
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-w64
%summary

%package -n libsox-fmt-wavpack
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-wavpack
%summary

%package -n libsox-fmt-xi
Summary: %summary
Group: Sound
Requires: libsox = %version-%release

%description -n libsox-fmt-xi
%summary

%package base
Summary: A general purpose sound file conversion tool
Group: Sound
Conflicts: sox < %version-%release
Requires: libsox = %version-%release

%description base
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.
Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.


%package play
Summary: A general purpose sound file conversion tool
Group: Sound
BuildArch: noarch
Requires: sox-base = %version-%release
Requires: libsox-fmt-oss = %version-%release
Requires: libsox-fmt-alsa = %version-%release
Requires: libsox-fmt-vorbis = %version-%release

%description play
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.
Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.


%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.
Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.


%prep
%setup -q
sed -i 's,\-I/lib/modules/`uname -r`/build/include,,' configure*
sed -i 's,CODEC_TYPE_AUDIO,AVMEDIA_TYPE_AUDIO,' src/ffmpeg.c
sed -i 's,PKT_FLAG_KEY,AV_PKT_FLAG_KEY,' src/ffmpeg.c
sed -i 's,av_alloc_format_context,avformat_alloc_context,' src/ffmpeg.c

%build
%configure --with-dyn-default --enable-dl-amrnb --enable-dl-amrwb --enable-dl-sndfile
%make_build

%install
%makeinstall install
install %SOURCE1 %buildroot%_bindir/soxeffect
sed -i 's,\(/usr/\)local/,\1,' %buildroot%_bindir/soxeffect
rm -f %buildroot%_bindir/rec
ln -s play %buildroot%_bindir/rec
cat << EOF >%buildroot%_bindir/%{name}play
%_bindir/%name \$1 -t .au - >/dev/audio
EOF
chmod 755 %buildroot%_bindir/%{name}play

%files
%doc ChangeLog README

%files -n libsox
%_libdir/libsox.so.*
%dir %_libdir/sox

%files -n libsox-devel
%_includedir/*
%_libdir/libsox.so
%_pkgconfigdir/*.pc
%_man3dir/*
%exclude %_libdir/libsox.a

%files -n libsox-devel-static
%_libdir/sox/*.a
%exclude %_libdir/sox/*.la

%files -n libsox-fmt-alsa
%_libdir/sox/libsox_fmt_alsa.so

%files -n libsox-fmt-ao
%_libdir/sox/libsox_fmt_ao.so

%files -n libsox-fmt-caf
%_libdir/sox/libsox_fmt_caf.so

%files -n libsox-fmt-fap
%_libdir/sox/libsox_fmt_fap.so

%files -n libsox-fmt-ffmpeg
%_libdir/sox/libsox_fmt_ffmpeg.so

%files -n libsox-fmt-flac
%_libdir/sox/libsox_fmt_flac.so

%files -n libsox-fmt-gsm
%_libdir/sox/libsox_fmt_gsm.so

%files -n libsox-fmt-lpc10
%_libdir/sox/libsox_fmt_lpc10.so

%files -n libsox-fmt-mat4
%_libdir/sox/libsox_fmt_mat4.so

%files -n libsox-fmt-mat5
%_libdir/sox/libsox_fmt_mat5.so

%files -n libsox-fmt-mp3
%_libdir/sox/libsox_fmt_mp3.so

%files -n libsox-fmt-oss
%_libdir/sox/libsox_fmt_oss.so

%files -n libsox-fmt-paf
%_libdir/sox/libsox_fmt_paf.so

%files -n libsox-fmt-pulseaudio
%_libdir/sox/libsox_fmt_pulseaudio.so

%files -n libsox-fmt-pvf
%_libdir/sox/libsox_fmt_pvf.so

%files -n libsox-fmt-sd2
%_libdir/sox/libsox_fmt_sd2.so

%files -n libsox-fmt-sndfile
%_libdir/sox/libsox_fmt_sndfile.so

%files -n libsox-fmt-vorbis
%_libdir/sox/libsox_fmt_vorbis.so

%files -n libsox-fmt-w64
%_libdir/sox/libsox_fmt_w64.so

%files -n libsox-fmt-wavpack
%_libdir/sox/libsox_fmt_wavpack.so

%files -n libsox-fmt-xi
%_libdir/sox/libsox_fmt_xi.so

%files base
%_bindir/*
%_man1dir/sox.*
%_man1dir/play.*
%_man1dir/rec.*
%_man1dir/soxi.*
%_man7dir/*

%files play

%changelog
* Wed May 23 2012 Denis Smirnov <mithraen@altlinux.ru> 14.3.2-alt2
- fix build
- build more subpackages
- some cleanups

* Fri Aug 12 2011 Denis Smirnov <mithraen@altlinux.ru> 14.3.2-alt1
- 14.3.2

* Mon Jan 17 2011 Denis Smirnov <mithraen@altlinux.ru> 14.3.1-alt2
- fix package %_libdir/sox

* Wed Nov 17 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.1-alt1
- 14.3.1

* Fri May 07 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt5
- add Provides sox-devel to libsox-devel

* Sun Feb 21 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt4
- conflicts sox-base with sox < %%version-%%release (closes: #23001)

* Fri Jan 22 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt3
- reimport changes by ldv@ (closes: #21321)

* Tue Jan 19 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt2
- add sox-play subpackage (ALT #21728)

* Wed Sep 02 2009 Dmitry V. Levin <ldv@altlinux.org> 14.3.0-alt1.1
- NMU.
- Moved %%_pkgconfigdir/* files to -devel subpackage (closes: #21321).

* Wed Jul 01 2009 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt1
- update to 14.3.0
- move additional formats to subpackages

* Tue Feb 10 2009 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt4
- fix build with new ffmpeg (thanks to shrek@)

* Sun Aug 10 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt3
- fix build in hasher
- spec cleanup

* Tue Apr 01 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt2
- move devel to separate package

* Sun Feb 03 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt1
- Update to 14.0.1

* Sun Oct 07 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt3
- fix typo in Packager field

* Tue Apr 24 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt2
- add requires sox-devel -> sox (fix #11602)

* Fri Feb 16 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt1
- 13.0.0
- multiple changes, that affects scripts that used sox!
  Please see changelog for  details
- build dynamic libst (and don't build static)

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 12.18.2-alt2
- build with external libgsm

* Sat Oct 14 2006 Denis Smirnov <mithraen@altlinux.ru> 12.18.2-alt1
- 12.18.2

* Wed May 03 2006 Denis Smirnov <mithraen@altlinux.ru> 12.17.9-alt1
- 12.17.9

* Tue Dec 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.7-alt1
- 12.17.7

* Thu Oct 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.6-alt1
- 12.17.6

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.5-alt1
- new version.
- security fix for previous release applied in upstream.

* Mon Aug 02 2004 Stanislav Ievlev <inger@altlinux.org> 12.17.4-alt1.1
- NMU: security fix

* Tue Mar 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 12.17.4-alt1
- new version.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 12.17.3-alt2
- Rebuild with gcc-3.2.
- Alsa dsp support disabled.

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 12.17.3-alt1.1
- rebuild with new vorbis

* Mon Dec 17 2001 Yuri N. Sedunov <aris@altlinux.ru> 12.17.3-alt1
- Updated to 12.7.3, major fix in the spec.

* Wed Dec 12 2001 Yuri N. Sedunov <aris@altlinux.ru> 12.17.2-alt1
- Updated to 12.7.2, built with gsmlib.

* Wed Apr 10 2001 Rider <rider@altlinux.ru> 12.17.1-alt1
- 12.17.1

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 12.17-ipl1mdk
- RE adaptions.

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 12.17-1mdk
- new and shiny version.
- fix the build.

* Wed Aug 30 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-9mdk
- minor fix in the spec

* Tue Aug 29 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-8mdk
- simplified the installation

* Mon Aug 28 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-7mdk
- fixed installation directories

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 12.16-6mdk
- fixed groups

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix dangling symlinks (use rpmlint luke).

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP check/build

* Sat Aug 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- -DHAVE_SYS_SOUNDCARD_H=1, cause configure is slightly broken

* Thu Jul 22 1999 Gregus <gregus@etudiant.net>
- fr locale

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- A new life for the spec file :).
- 12.16.
- Removed obsoletes patchs.

* Tue Jun 01 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Cleanup from Mandrake adaptions

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Jan 20 1999 Bill Nottingham <notting@redhat.com>
- allow spaces in filenames for play/rec

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- fix docs

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- update to 12.15

* Sat Oct 10 1998 Michael Maher <mike@redhat.com>
- fixed broken spec file

* Mon Jul 13 1998 Michael Maher <mike@redhat.com>
- updated source from Chris Bagwell.

* Wed Jun 23 1998 Michael Maher <mike@redhat.com>
- made patch to fix the '-e' option. BUG 580
- added buildroot

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 06 1997 Erik Troan <ewt@redhat.com>
- built against glibc

