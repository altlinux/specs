%define _unpackaged_files_terminate_build 1

%def_enable ao
%def_enable shout
%def_enable tcp
%def_enable curl
%def_enable ipv6
%def_enable fluidsynth
%def_disable wildmidi
%def_enable oss
%def_enable alsa
%def_enable jack
%def_enable pulse
%def_enable pipewire
%def_enable fifo
%def_enable vorbis
%def_enable flac
%def_enable mad
%def_enable vorbisenc
%def_enable lame
%def_enable audiofile
%def_enable mikmod
%def_disable modplug
%def_enable faad
%def_disable mpc
%def_enable ffmpeg
%def_enable wavpack
%def_enable id3
%def_enable lsr
%def_enable mms
%def_enable bzip2
%def_enable zip
%def_enable iso9660
%def_enable sqlite
%def_disable sidplay
%def_enable doc
%def_disable tremor
%def_enable mpg123
%def_enable nfs
%def_enable webdav
%def_enable upnp
%def_enable mpdclient
%def_enable smbclient
%def_enable opus
%def_enable pcre
%def_enable chromaprint
%def_enable systemd
%def_enable snapcast
# auto|avahi|bonjour|disabled
%define zeroconf avahi
%define mpd_user _mpd
%define mpd_group _mpd
#----------------------------------------------------------------------
%define subst_enable_meson_feature() %{expand:%%{?_enable_%{1}:-D%{2}=enabled}} %{expand:%%{?_disable_%{1}:-D%{2}=disabled}}
%define subst_enable_meson_bool() %{expand:%%{?_enable_%{1}:-D%{2}=true}} %{expand:%%{?_disable_%{1}:-D%{2}=false}}
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}

%if_enabled systemd
%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)
%endif

%if_enabled tremor
%def_disable shout
%endif
%{!?zeroconf:%define zeroconf disabled}

%define  Name MPD

Name:    mpd
Version: 0.23.11
Release: alt1

Summary: Music Player Daemon (%Name) allows remote access for playing music and managing playlists
License: %gpl2plus
Group:   Sound
Url:     https://musicpd.org

Vcs: https://github.com/MusicPlayerDaemon/MPD.git
Source:  %name-%version.tar
Source1: %name.conf
Source2: %name.sys.conf.in
Source3: %name.init.in
Source4: %name.logrotate
Source5: %name.tmpfile

Patch: %name-0.23.8-alt-fluidsynth-fix-sound-font-location.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-meson
%if_enabled systemd
BuildRequires(pre): rpm-build-systemd /usr/bin/pkg-config
%endif
BuildRequires: meson gcc-c++ zlib-devel libfmt-devel
%{?_enable_curl:BuildRequires: libcurl-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel >= 0.9.0}
%{?_enable_jack:BuildRequires: jackit-devel}
%{?_enable_ao:BuildRequires: libao-devel}
%{?_enable_shout:BuildRequires: libshout2-devel >= 2.4.0}
%{?_enable_audiofile:BuildRequires: libaudiofile-devel >= 0.1.7}
%{?_enable_mikmod:BuildRequires: libmikmod-devel >= 3.1.7}
%{?_enable_modplug:BuildRequires: libmmodplug-devel}
%{?_enable_faad:BuildRequires: libfaad-devel}
%{?_enable_flac:BuildRequires: libflac-devel >= 1.1.3}
%{?_enable_id3:BuildRequires: libid3tag-devel}
%{?_enable_mad:BuildRequires: libmad-devel}
%{?_enable_vorbisenc:BuildRequires: libvorbis-devel}
%{?_enable_lame:BuildRequires: liblame-devel}
%{?_enable_mpc:BuildRequires: libmpcdec-devel}
%{?_enable_ffmpeg:BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libavfilter-devel}
%{?_enable_wavpack:BuildRequires: libwavpack-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_pipewire:BuildRequires: pkgconfig(libpipewire-0.3)}
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
%{?_enable_nfs:BuildRequires: libnfs-devel}
%{?_enable_webdav:BuildRequires: libcurl-devel libexpat-devel}
%{?_enable_upnp:BuildRequires: libnpupnp-devel}
%{?_enable_mpdclient:BuildRequires: libmpdclient-devel}
%{?_enable_smbclient:BuildRequires: libsmbclient-devel}
%{?_enable_opus:BuildRequires: libopus-devel}
%{?_enable_pcre:BuildRequires: libpcre2-devel}
%{?_enable_chromaprint:BuildRequires: libchromaprint-devel}
%{?_enable_doc:BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink}
%if %zeroconf == avahi
BuildRequires: libavahi-glib-devel libdbus-devel
%endif

BuildRequires: boost-complete libicu-devel cmake libfmt-devel

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
%endif

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%meson \
	%{subst_enable_meson_feature tremor tremor} \
	%{subst_enable_meson_feature ao ao} \
	%{subst_enable_meson_feature shout shout} \
	%{subst_enable_meson_bool tcp tcp} \
	%{subst_enable_meson_feature curl curl} \
	%{subst_enable_meson_feature ipv6 ipv6} \
	%{subst_enable_meson_feature oss oss} \
	%{subst_enable_meson_feature alsa alsa} \
	%{subst_enable_meson_feature jack jack} \
	%{subst_enable_meson_feature pulse pulse} \
	%{subst_enable_meson_feature pipewire pipewire} \
	%{subst_enable_meson_bool fifo fifo} \
	%{subst_enable_meson_feature vorbis vorbis} \
	%{subst_enable_meson_feature flac flac} \
	%{subst_enable_meson_feature mad mad} \
	%{subst_enable_meson_feature lame lame} \
	%{subst_enable_meson_feature vorbisenc vorbisenc} \
	%{subst_enable_meson_feature audiofile audiofile} \
	%{subst_enable_meson_feature mikmod mikmod} \
	%{subst_enable_meson_feature modplug modplug} \
	%{subst_enable_meson_feature mpc mpcdec} \
	%{subst_enable_meson_feature ffmpeg ffmpeg} \
	%{subst_enable_meson_feature wavpack wavpack} \
	%{subst_enable_meson_feature id3 id3tag} \
	%{subst_enable_meson_feature lsr libsamplerate} \
	%{subst_enable_meson_feature mms mms} \
	%{subst_enable_meson_feature sidplay sidplay} \
	%{subst_enable_meson_feature bzip2 bzip2} \
	%{subst_enable_meson_feature zip zzip} \
	%{subst_enable_meson_feature iso9660 iso9660} \
	%{subst_enable_meson_feature sqlite sqlite} \
	%{subst_enable_meson_feature fluidsynth fluidsynth} \
	%{subst_enable_meson_feature wildmidi wildmidi} \
	%{subst_enable_meson_feature mpg123 mpg123} \
	%{subst_enable_meson_feature nfs nfs} \
	%{subst_enable_meson_feature webdav webdav} \
	%{?_enable_upnp:-Dupnp='npupnp'} \
	%{subst_enable_meson_feature mpdclient libmpdclient} \
	%{subst_enable_meson_feature smbclient smbclient} \
	%{subst_enable_meson_feature opus opus} \
	%{subst_enable_meson_feature doc documentation} \
	%{subst_enable_meson_feature pcre pcre} \
	%{subst_enable_meson_feature chromaprint chromaprint} \
	%{subst_enable_meson_feature systemd systemd} \
	%{subst_enable_meson_bool snapcast snapcast} \
%if_enabled systemd
	-Dsystemd_system_unit_dir=%_unitdir \
	-Dsystemd_user_unit_dir=%_userunitdir \
%endif
	-Dzeroconf=%zeroconf \
	%nil

%meson_build

%install
%meson_install

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
%if_disabled doc
%_defaultdocdir/%name
%endif
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/%name.sys.conf
%config(noreplace) %_sysconfdir/logrotate.d/*
%_bindir/*
%if_enabled doc
%_man1dir/*
%_man5dir/*
%endif
%_initdir/*
%if_enabled systemd
%_unitdir/*
%_userunitdir/*
%endif
%_tmpfilesdir/*
%attr(775,root,%mpd_group) %dir %_localstatedir/%name
%attr(775,root,%mpd_group) %dir %_localstatedir/%name/playlists
%attr(775,root,%mpd_group) %dir %_logdir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg

%if_enabled doc
%files doc
%_defaultdocdir/%name
%endif

%changelog
* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 0.23.11-alt1
- 0.23.11.

* Wed Jul 20 2022 L.A. Kostis <lakostis@altlinux.ru> 0.23.8-alt3
- fluidsynth: fix sound font path.

* Sat Jul 16 2022 L.A. Kostis <lakostis@altlinux.ru> 0.23.8-alt2
- merge aris@ .spec changes.

* Thu Jul 14 2022 L.A. Kostis <lakostis@altlinux.ru> 0.23.8-alt1
- 0.23.8.
- enable snapcast.
- enable ipv6.

* Tue May 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.23.7-alt1
- 0.23.7 (ported to PCRE2, new PipeWire plugin)

* Mon Jun 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.22.9-alt1
- 0.22.9

* Tue Jun 22 2021 Yuri N. Sedunov <aris@altlinux.org> 0.22.8-alt1
- updated to v0.22.8-35-gab487b9a9
- enabled pcre, chromaprint support
- enabled ffmpeg again

* Fri May 28 2021 Yuri N. Sedunov <aris@altlinux.org> 0.21.24-alt1.1
- doc/meson.build: remove "upload" target
  (https://github.com/MusicPlayerDaemon/MPD/issues/1161)

* Mon Jul 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.24-alt1
- Updated to upstream version 0.21.24.
- Enabled again iso9660 support.
- Switched to meson build system.

* Thu May 09 2019 Michael Shigorin <mike@altlinux.org> 0.20.23-alt3
- fixed doc knob
- minor spec cleanup

* Fri Apr 19 2019 Anton Midyukov <antohami@altlinux.org> 0.20.23-alt2
- moved /var/run -> /run
- moved /var/lock -> /run/lock
- enable nfs
- enable webdav
- enable upnp
- enable mpdclient
- enable smbclient
- enable opus decoder

* Fri Jan 18 2019 Yuri N. Sedunov <aris@altlinux.org> 0.20.23-alt1
- 0.20.23
- built against libfluidsynth.so.2

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.21-alt1
- Updated to upstream version 0.20.21.

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
