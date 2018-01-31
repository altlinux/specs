%def_disable debug
%def_disable prof
%def_disable werror
%def_enable ao
%def_enable shout
%def_enable tcp
%def_enable un
%def_enable curl
%def_disable ipv6
%def_enable fluidsynth
%def_disable wildmidi
%def_enable oss
%def_enable alsa
%def_enable jack
%def_enable pulse
%def_enable fifo
%def_enable mvp
%def_enable vorbis
%def_enable oggflac
%def_enable flac
%def_enable mad
%def_enable vorbisenc
%def_enable lame
%def_enable aac
%def_enable audiofile
%def_enable mikmod
%def_disable modplug
%def_enable faad
%def_disable mpc
%def_disable ffmpeg
%def_disable mp4
%def_enable wavpack
%def_enable id3
%def_enable lsr
%def_enable mms
%def_enable bzip2
%def_enable zip
%def_disable iso9660
%def_enable sqlite
%def_disable sidplay
%def_enable doc
%def_without tremor
%def_enable mpg123
# auto|avahi|bonjour|no
%define zeroconf avahi
%define mpd_user _mpd
%define mpd_group _mpd
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}

%if_with tremor
%set_disable shout
%set_disable oggflac
%endif
%{!?zeroconf:%define zeroconf no}

%define  Name MPD
Name: 	 mpd
Version: 0.20.15
Release: alt1
Summary: Music Player Daemon (%Name) allows remote access for playing music and managing playlists

License: %gpl2plus
Group:   Sound
URL:     http://musicpd.org

Source: %name-%version.tar
# VCS:   git://git.musicpd.org/master/mpd.git
Source1: %name.conf
Source2: %name.sys.conf.in
Source3: %name.init.in
Source4: %name.logrotate
Source5: %name.tmpfile

BuildRequires(pre): rpm-build-licenses
BuildRequires: zlib-devel gcc-c++
%{?_enable_curl:BuildRequires: libcurl-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel >= 0.9.0}
%{?_enable_jack:BuildRequires: jackit-devel}
%{?_enable_ao:BuildRequires: libao-devel}
%{?_enable_shout:BuildRequires: libshout2-devel}
%{?_enable_audiofile:BuildRequires: libaudiofile-devel >= 0.1.7}
%{?_enable_mikmod:BuildRequires: libmikmod-devel >= 3.1.7}
%{?_enable_modplug:BuildRequires: libmmodplug-devel}
%{?_enable_faad:BuildRequires: libfaad-devel}
%{?_enable_flac:BuildRequires: libflac-devel >= 1.1.3}
%{?_enable_oggflac:BuildRequires: liboggflac-devel}
%{?_enable_id3:BuildRequires: libid3tag-devel}
%{?_enable_mad:BuildRequires: libmad-devel}
%{?_enable_vorbisenc:BuildRequires: libvorbis-devel}
%{?_enable_lame:BuildRequires: liblame-devel}
%{?_enable_mpc:BuildRequires: libmpcdec-devel}
%{?_enable_ffmpeg:BuildRequires: libavformat-devel}
%{?_enable_mp4:BuildRequires: libmp4ff-devel}
%{?_enable_wavpack:BuildRequires: libwavpack-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_vorbis:BuildRequires: libvorbis-devel}
%{?_enable_lsr:BuildRequires: libsamplerate-devel}
%{?_enable_mms:BuildRequires: libmms-devel >= 0.4}
%{?_enable_sidplay:BuildRequires: libsidplay2-devel}
%{?_enable_zip:BuildRequires: zziplib-devel >= 0.13}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_iso9660:BuildRequires: libcdio-devel}
%{?_enable_sqlite:BuildRequires: libsqlite3-devel}
%{?_enable_fluidsynth:BuildRequires: libfluidsynth-devel}
%{?_enable_mpg123:BuildRequires: libmpg123-devel}
%{?_enable_doc:BuildRequires: docbook-dtds doxygen xmlto >= 0.0.21-alt2 /usr/bin/dot}
BuildRequires: systemd-devel
%if %zeroconf == avahi
BuildRequires: libavahi-glib-devel libdbus-devel
%endif

BuildRequires: boost-devel libicu-devel

%description
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.


%if_enabled doc
%package doc
Summary: Music Player Daemon (%Name) documentation
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version

%description doc
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.
This package contains %Name documentation.


%package doc-api
Summary: Music Player Daemon (%Name) documentation
Group: Development/Documentation
BuildArch: noarch

%description doc-api
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.
This package contains %Name's API documentation.
%endif


%prep
%setup
[ $(rpmvercmp %{get_version libflac-devel} 1.1.3) -lt 0 ] || sed -i 's/AM_PATH_LIBOGGFLAC/AM_PATH_LIBFLAC/' configure.ac
# libmad.pc describes 'libmad', not 'mad'
sed -i 's/\[mad\]/[libmad]/' configure.ac

%build
%define _optlevel 3
%autoreconf
%configure \
    %{subst_enable debug} \
    %{subst_enable_to prof gprof} \
    %{subst_enable werror} \
    %{subst_with tremor} \
    %{subst_enable ao} \
    %{subst_enable shout} \
    %{subst_enable tcp} \
    %{subst_enable un} \
    %{subst_enable curl} \
    %{?_enable_curl:--enable-lastfm} \
    %{subst_enable ipv6} \
    %{subst_enable sun} \
    %{subst_enable oss} \
    %{subst_enable alsa} \
    %{subst_enable jack} \
    %{subst_enable pulse} \
    %{subst_enable fifo} \
    %{subst_enable mvp} \
    %{subst_enable vorbis} \
    %{subst_enable flac} \
    %{subst_enable oggflac} \
    %{subst_enable mad} \
    %{?_enable_lame:--enable-lame-encoder} \
    %{?_enable_vorbisenc:--enable-vorbis-encoder} \
    %{subst_enable aac} \
    %{subst_enable audiofile} \
    %{subst_enable mikmod} \
    %{subst_enable modplug} \
    %{subst_enable mpc} \
    %{subst_enable ffmpeg} \
    %{subst_enable mp4} \
    %{subst_enable wavpack} \
    %{subst_enable id3} \
    %{subst_enable lsr} \
    %{subst_enable mms} \
    %{subst_enable sidplay} \
    %{subst_enable bzip2} \
    %{subst_enable zip} \
    %{subst_enable iso9660} \
    %{subst_enable sqlite} \
    %{subst_enable fluidsynth} \
    %{subst_enable wildmidi} \
    %{subst_enable mpg123} \
    %{subst_enable_to doc documentation} \
    --with-systemdsystemunitdir=/lib/systemd/system \
    --with-zeroconf=%zeroconf \
    --docdir=%_docdir/%name-%version
%make_build
bzip2 --best --keep --force NEWS


%install
%makeinstall_std protocoldir=%_docdir/%name-%version/html
ln -s html %buildroot%_docdir/%name-%version/protocol
install -d %buildroot{%_localstatedir/%name/playlists,{%_runtimedir,%_logdir}/%name,%_sysconfdir,%_initdir,%_tmpfilesdir}
sed -e "s|@localstatedir@|%_localstatedir|g" -e "s|@logdir@|%_logdir|g" %SOURCE1 > %buildroot%_sysconfdir/%name.conf
chmod 644 %buildroot%_sysconfdir/%name.conf
sed 's/@MPD_USER@/%mpd_user/g' %SOURCE2 > %buildroot%_sysconfdir/%name.sys.conf
chmod 640 %buildroot%_sysconfdir/%name.sys.conf
sed 's/@MPD_USER@/%mpd_user/g' %SOURCE3 > %buildroot%_initdir/%name
chmod 755 %buildroot%_initdir/%name
sed 's/@MPD_USER@/%mpd_user/g' %SOURCE5 > %buildroot%_tmpfilesdir/%name.conf
chmod 644 %buildroot%_tmpfilesdir/%name.conf
install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/%name
bzip2 --best %buildroot%_docdir/%name-%version/NEWS

%pre
%_sbindir/groupadd -r -f %mpd_group &>/dev/null ||:
%_sbindir/useradd -r -n -M -s /dev/null -d %_localstatedir/%name -g %mpd_group \
    -c "Music Player Daemon (%Name)" %mpd_user &>/dev/null ||:
%_sbindir/usermod -g %mpd_group -G audio %mpd_user &>/dev/null ||:


%post
%post_service %name ||:


%preun
%preun_service %name ||:


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/README.md
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/%{name}conf.example
%if_disabled doc
%doc %_docdir/%name-%version/NEWS.*
%endif
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/%name.sys.conf
%config(noreplace) %_sysconfdir/logrotate.d/*
%_bindir/*
%_man1dir/*
%_man5dir/*
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
%attr(775,root,%mpd_group) %dir %_localstatedir/%name
%attr(775,root,%mpd_group) %dir %_localstatedir/%name/playlists
%attr(775,root,%mpd_group) %dir %_logdir/%name


%if_enabled doc
%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/NEWS.*
%doc %_docdir/%name-%version/html
%doc %_docdir/%name-%version/protocol
%doc %_docdir/%name-%version/user
%doc %_docdir/%name-%version/developer


%files doc-api
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/api
%endif


%changelog
* Wed Jan 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.15-alt1
- Updated to upstream version 0.20.15.
- Disabled iso9660 support since it isn't ported yet to new libcdio.

* Thu Apr 06 2017 Denis Smirnov <mithraen@altlinux.ru> 0.20.6-alt1
- update to 0.20.6

* Tue Mar 17 2015 Denis Smirnov <mithraen@altlinux.ru> 0.19.9-alt1
- update to 0.19.9

* Tue Nov 18 2014 Denis Smirnov <mithraen@altlinux.ru> 0.18.14-alt2
- add mpg123 decoder

* Fri Sep 12 2014 Alexey Shabalin <shaba@altlinux.ru> 0.18.14-alt1
- 0.18.14
- fix init script
- add systemd unit files
- add tmpfiles conf

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.11-alt1.1
- Rebuilt with new audiofile

* Mon Jul 28 2014 Andrey Cherepanov <cas@altlinux.org> 0.18.11-alt1
- New version

* Fri Apr 18 2014 Andrey Cherepanov <cas@altlinux.org> 0.18.10-alt1
- New version
- Disable mpc support to build new version

* Wed Feb 08 2012 Alexey Morsov <swi@altlinux.ru> 0.17.0-alt0.3.git050212
- new git version
- disable ffmpeg

* Tue Sep 20 2011 Alexey Morsov <swi@altlinux.ru> 0.17.0-alt0.2.git200911
- new git version

* Thu Aug 04 2011 Alexey Morsov <swi@altlinux.ru> 0.17.0-alt0.1
- new git version

* Tue Apr 12 2011 Alexey Morsov <swi@altlinux.ru> 0.16.2-alt2
- remove error_file from mpd.sys.conf.in (closes: 25410)

* Tue Mar 01 2011 Alexey Morsov <swi@altlinux.ru> 0.16.2-alt1
- new release version

* Sun Oct 24 2010 Alexey Morsov <swi@altlinux.ru> 0.15.13-alt1
- new release version

* Wed Apr 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.15.8-alt2
- rebuild with new zziplib

* Thu Mar 11 2010 Alexey Rusakov <ktirf@altlinux.org> 0.15.8-alt1
- 0.15.8

* Thu Nov 05 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.3-alt1.1
- rebuild with new libcdio

* Thu Sep 03 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.3-alt1
- 0.15.3

* Wed Aug 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.0-alt2
- fixed Packager tag
- rebuild with new libcdio

* Mon Jul 06 2009 Alexey Rusakov <ktirf@altlinux.org> 0.15.0-alt1
- 0.15.0
- updated buildreqs and files list
- enabled last.fm streams parsing
- no more separate 'shout_mp3' and 'shout_ogg' switches, there is 'shout'
  switch instead
- Renamed switches:
  + oggvorbis -> vorbis
  + mp3 -> mad
  + mod -> mikmod

* Fri Feb 20 2009 Led <led@altlinux.ru> 0.14.2-alt1
- 0.14.2
- cleaned up spec
- enabled support:
  + mms
  + zip
  + bzip2
  + fluidsynth
  + sqlite
  + iso9660
  + modplug
- added doc and doc-api subpackages

* Sat Dec 27 2008 Led <led@altlinux.ru> 0.14-alt1
- 0.14 release

* Sun Dec 21 2008 Led <led@altlinux.ru> 0.14-alt0.1
- 0.14-beta3:
  + new plugins: fifo, null, ffmpeg, aac, wavpack
  + new commands: addid, idle
  + support connecting via unix domain socket
  + 24 bit audio support
  + allow authenticated local users to add any local file to the
    playlist

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.13.2-alt3
- fixed spec
- added %name-0.13.2-alt.patch

* Sun Jul 27 2008 Led <led@altlinux.ru> 0.13.2-alt2
- added script for logrotate (#16420)

* Sat Jul 05 2008 Led <led@altlinux.ru> 0.13.2-alt1
- 0.13.2:
  + several bugfixes
  + faster stored playlists
  + Bonjour support
  + .oga suffix support for Ogg containers
- fixed "Security packaging Policy violation" (#15830)
- added %name-0.13.2-alt-encoding_output_fix.patch for resolve #8655
  (thanx php-coder for concept)

* Thu Mar 06 2008 Led <led@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Fri Sep 14 2007 Led <led@altlinux.ru> 0.13.0-alt3
- libflac-devel version qualifing with rmpvercmp

* Thu Sep 13 2007 Led <led@altlinux.ru> 0.13.0-alt2
- added init script (fixed #12707)
- updated default %_sysconfdir/%name.conf
- added default %_sysconfdir/%name.sys.conf (for system wide service)
- updated mpd-0.13.0-configure.patch
- fixed License

* Mon Sep 10 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.13.0-alt1
-  0.13.0.
-  fix build with libshout2 (#12708).

* Sat Apr 21 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.12.1-alt1.0
- Rebuilt due to libFLAC.so.7 -> libFLAC.so.8 soname change.

* Mon Feb 26 2007 Led <led@altlinux.ru> 0.12.1-alt1
- NMU (fixed #10874)
- 0.12.1
- fixed BuildRequires
- added %name-0.12.1-configure.patch
- added mpd-0.12.1+flac-1.1.3.patch
- cleaned up spec

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.0-alt1
- 0.12

* Fri Sep 15 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.0rc4-alt1
-  0.12.0rc4.
	- libao support;
	- pulseaudio support;
	- support for more media formats.

* Wed Nov 02 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.5-alt1.2
-  fix for #8395 (10x to Alexei V. Mezin).

* Thu Feb 10 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.5-alt1
-  initial build.
