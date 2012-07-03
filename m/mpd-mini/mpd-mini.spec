%def_disable debug
%def_disable prof
%def_disable werror
%def_disable ao
%def_disable shout
%def_enable tcp
%def_enable un
%def_disable curl
%def_disable ipv6
%def_disable fluidsynth
%def_disable wildmidi
%def_disable oss
%def_enable alsa
%def_disable jack
%def_disable pulse
%def_disable fifo
%def_disable mvp
%def_enable vorbis
%def_disable oggflac
%def_disable flac
%def_enable mad
%def_disable vorbisenc
%def_disable lameenc
%def_disable aac
%def_disable audiofile
%def_disable mikmod
%def_disable modplug
%def_disable faad
%def_disable mpc
%def_enable ffmpeg
%def_disable mp4ff
%def_disable wavpack
%def_enable id3
%def_disable lsr
%def_disable mms
%def_disable bzip2
%def_disable zzip
%def_disable iso9660
%def_disable sqlite
%def_disable sidplay
%def_disable httpd_output
%def_disable doc
%def_without tremor
# auto|avahi|bonjour|no
%define zeroconf no
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

%define Name MPD
%define oname mpd

Name: mpd-mini
Version: 0.16.4
%define prerel %nil
Release: alt1
Summary: Light version of Music Player Daemon (%Name)
License: GPLv2+
Group: Sound
Url: http://musicpd.org
Source0: %url/uploads/files/%oname-%version%prerel.tar.bz2
Source1: %oname.conf
Source2: %oname.sys.conf.in
Source3: %oname.init.in
Source4: %oname.logrotate
Packager: Slava Semushin <php-coder@altlinux.ru>

Conflicts: %oname
BuildRequires: zlib-devel gcc-c++
BuildRequires: glib2-devel >= 2.12
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
%{?_enable_lameenc:BuildRequires: liblame-devel}
%{?_enable_mpc:BuildRequires: libmpcdec-devel}
%{?_enable_ffmpeg:BuildRequires: libavformat-devel}
%{?_enable_mp4ff:BuildRequires: libmp4ff-devel}
%{?_enable_wavpack:BuildRequires: libwavpack-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_vorbis:BuildRequires: libvorbis-devel}
%{?_enable_lsr:BuildRequires: libsamplerate-devel}
%{?_enable_mms:BuildRequires: libmms-devel >= 0.4}
%{?_enable_sidplay:BuildRequires: libsidplay2-devel}
%{?_enable_zzip:BuildRequires: zziplib-devel >= 0.13}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_iso9660:BuildRequires: libcdio-devel}
%{?_enable_sqlite:BuildRequires: libsqlite3-devel}
%{?_enable_fluidsynth:BuildRequires: libfluidsynth-devel}
%{?_enable_doc:BuildRequires: docbook-dtds doxygen xmlto >= 0.0.21-alt2}
%if %zeroconf == avahi
BuildRequires: libavahi-glib-devel
%endif

%description
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC and WMA files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.


%if_enabled doc
%package doc
Summary: Music Player Daemon (%Name) documentation
Group: Documentation
BuildArch: noarch
Conflicts: %oname-doc

%description doc
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC and WMA files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.
This package contains %Name documentation.


%package doc-api
Summary: Music Player Daemon (%Name) documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: %oname-doc-api

%description doc-api
Music Player Daemon (%Name) allows remote access for playing music
(MP3, Ogg Vorbis, FLAC, AAC and WMA files) and managing
playlists. %Name is designed for integrating a computer into a stereo
system that provides control for music playback over a local network.
It is also makes a great desktop music player, especially if you are a
console junkie, like frontend options, or restart X often.
This package contains %Name's API documentation.
%endif


%prep
%setup -n %oname-%version%prerel

%if_enabled flac
[ $(rpmvercmp %{get_version libflac-devel} 1.1.3) -lt 0 ] || sed -i 's/AM_PATH_LIBOGGFLAC/AM_PATH_LIBFLAC/' configure.ac
%endif

%if_enabled mad
# libmad.pc describes 'libmad', not 'mad'
sed -i 's/\[mad\]/[libmad]/' configure.ac
%endif


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
    %{subst_enable_to lameenc lame-encoder} \
    %{subst_enable_to vorbisenc: vorbis-encoder} \
    %{subst_enable aac} \
    %{subst_enable audiofile} \
    %{subst_enable mikmod} \
    %{subst_enable modplug} \
    %{subst_enable mpc} \
    %{subst_enable ffmpeg} \
    %{subst_enable mp4ff} \
    %{subst_enable wavpack} \
    %{subst_enable id3} \
    %{subst_enable lsr} \
    %{subst_enable mms} \
    %{subst_enable sidplay} \
    %{subst_enable bzip2} \
    %{subst_enable zzip} \
    %{subst_enable iso9660} \
    %{subst_enable sqlite} \
    %{subst_enable fluidsynth} \
    %{subst_enable wildmidi} \
    %{subst_enable_to httpd_output httpd-output} \
    %{subst_enable_to doc documentation} \
    --with-zeroconf=%zeroconf \
    --docdir=%_docdir/%oname-%version
%make_build --silent --no-print-directory
bzip2 --best --keep --force NEWS


%check
%make_build --silent --no-print-directory check


%install
%makeinstall_std protocoldir=%_docdir/%oname-%version/html
ln -s html %buildroot%_docdir/%oname-%version/protocol
install -d %buildroot{%_localstatedir/%oname/playlists,{/var/run,%_logdir}/%oname,%_sysconfdir,%_initdir}
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/%oname.conf
sed 's/@MPD_USER@/%mpd_user/g' %SOURCE2 > %buildroot%_sysconfdir/%oname.sys.conf
chmod 640 %buildroot%_sysconfdir/%oname.sys.conf
sed 's/@MPD_USER@/%mpd_user/g' %SOURCE3 > %buildroot%_initdir/%oname
chmod 755 %buildroot%_initdir/%oname
install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/%oname
bzip2 --best %buildroot%_docdir/%oname-%version/NEWS


%pre
%_sbindir/groupadd -r -f %mpd_group &>/dev/null ||:
%_sbindir/useradd -r -n -M -s /dev/null -d %_localstatedir/%oname -g %mpd_group \
    -c "Music Player Daemon (%Name)" %mpd_user &>/dev/null ||:
%_sbindir/usermod -g %mpd_group -G audio %mpd_user &>/dev/null ||:


%post
%post_service %oname ||:


%preun
%preun_service %oname ||:


%files
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/AUTHORS
%doc %_docdir/%oname-%version/README
%doc %_docdir/%oname-%version/COPYING
%doc %_docdir/%oname-%version/%{oname}conf.example
%if_disabled doc
%doc %_docdir/%oname-%version/NEWS.*
%doc %_docdir/%oname-%version/UPGRADING
%endif
%config(noreplace) %_sysconfdir/%oname.conf
%config(noreplace) %_sysconfdir/%oname.sys.conf
%config(noreplace) %_sysconfdir/logrotate.d/*
%_bindir/*
%_man1dir/*
%_man5dir/*
%_initdir/*
%attr(775,root,%mpd_group) %dir %_localstatedir/%oname
%attr(775,root,%mpd_group) %dir %_localstatedir/%oname/playlists
%attr(775,root,%mpd_group) %dir /var/run/%oname
%attr(775,root,%mpd_group) %dir %_logdir/%oname


%if_enabled doc
%files doc
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/NEWS.*
%doc %_docdir/%oname-%version/UPGRADING
%doc %_docdir/%oname-%version/html
%doc %_docdir/%oname-%version/protocol
%doc %_docdir/%oname-%version/user
%doc %_docdir/%oname-%version/developer


%files doc-api
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/api
%endif


%changelog
* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 0.16.4-alt1
- Updated to 0.16.4

* Tue Mar 22 2011 Slava Semushin <php-coder@altlinux.ru> 0.16.2-alt1
- Updated to 0.16.2

* Sat Jan 15 2011 Slava Semushin <php-coder@altlinux.ru> 0.16.1-alt1
- Updated to 0.16.1 (new stable release)
- Enabled test suite
- Be careful during update: some defaults was changed and deprecated
  options was removed (see NEWS file for details)

* Fri Nov 12 2010 Slava Semushin <php-coder@altlinux.ru> 0.15.15-alt1
- Updated to 0.15.15

* Sun Nov 07 2010 Slava Semushin <php-coder@altlinux.ru> 0.15.14-alt1
- Updated to 0.15.14
- Updated Summary

* Sat Jul 31 2010 Slava Semushin <php-coder@altlinux.ru> 0.15.12-alt1
- Fork package from mpd
- Updated to 0.15.12
- Disabled 27 miscellaneous options by default
- Don't build doc and doc-api subpackages

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
- added %oname-0.13.2-alt.patch

* Sun Jul 27 2008 Led <led@altlinux.ru> 0.13.2-alt2
- added script for logrotate (#16420)

* Sat Jul 05 2008 Led <led@altlinux.ru> 0.13.2-alt1
- 0.13.2:
  + several bugfixes
  + faster stored playlists
  + Bonjour support
  + .oga suffix support for Ogg containers
- fixed "Security packaging Policy violation" (#15830)
- added %oname-0.13.2-alt-encoding_output_fix.patch for resolve #8655
  (thanx php-coder for concept)

* Thu Mar 06 2008 Led <led@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Fri Sep 14 2007 Led <led@altlinux.ru> 0.13.0-alt3
- libflac-devel version qualifing with rmpvercmp

* Thu Sep 13 2007 Led <led@altlinux.ru> 0.13.0-alt2
- added init script (fixed #12707)
- updated default %_sysconfdir/%oname.conf
- added default %_sysconfdir/%oname.sys.conf (for system wide service)
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
- added %oname-0.12.1-configure.patch
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
