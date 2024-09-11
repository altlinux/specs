Name: baresip
Version: 3.15.0
Release: alt1

Summary: Baresip is a portable and modular SIP User-Agent with audio and video support
License: BSD-3-Clause
Group: Communications

Url: https://github.com/baresip/baresip

#Source-url: https://github.com/baresip/baresip/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libssl-devel zlib-devel
BuildRequires: libre-devel >= 3.15.0

%description
baresip is a bare-bones SIP user agent. It supports SIP, SDP, RTP/RTCP,
and STUN/TURN/ICE, and IPv4 and IPv6, and is RFC-compliant and has
portable C89 and C99 source code. A modular plugin architecture provides
stdio, cons, and evdev user interfaces, codec2, g711, g722, g726, ilbc, l16,
and opus codecs, alsa, pulseaudio, pipewire, jack, coreaudio, gst, portaudio,
winwave, opensles and sndio audio drivers, the audio filters, av1, h264, h265,
vp8, vp9 video codec, avformat, acvapture and v4l2 video sources, sdl2,
directfb and x11 video display drivers, and srtp media encoding.

%package devel
Summary: Development files for %name library
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package includes libraries and header files for developing
appications which use the baresip C library.

%package aac
Summary: AAC audio codec module for baresip
Group: Communications
BuildRequires: libfdk-aac-devel
Requires: %name = %version-%release

%description aac
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Advanced Audio Coding (AAC) audio codec.

%package alsa
Summary: ALSA audio driver module for baresip
Group: Communications
BuildRequires:  libalsa-devel
Requires: %name = %version-%release

%description alsa
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Advanced Linux Sound Architecture (ALSA) audio
driver.

%package av1
Summary: AV1 video codec module for baresip
Group: Communications
BuildRequires: libaom-devel
Requires: %name = %version-%release

%description av1
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the AOMedia Video 1 (AV1) video codec.

%package codec2
Summary: Codec2 speech codec module for baresip
Group: Communications
BuildRequires: libcodec2-devel
Requires: %name = %version-%release

%description codec2
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Codec2 low-bitrate speech audio codec.

%package ctrl_dbus
Summary: D-BUS module for baresip
Group: Communications
BuildRequires: libgio-devel
Requires: %name = %version-%release

%description ctrl_dbus
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the communication channel to control and monitor baresip via D-BUS.

%package g722
Summary: G.722 audio codec module for baresip
Group: Communications
BuildRequires: libspandsp-devel
Requires: %name = %version-%release

%description g722
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the G.722 audio codec.

%package g726
Summary: G.726 audio codec module for baresip
Group: Communications
BuildRequires: libspandsp-devel
Requires: %name = %version-%release

%description g726
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the G.726 audio codec.

%package gst
Summary: GStreamer audio source driver module for baresip
Group: Communications
BuildRequires: gstreamer1.0-devel
Requires: %name = %version-%release

%description gst
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Gstreamer framework to play external media
and provide this as an internal audio source.

%package gtk
Summary: GTK+ Menu-based User-Interface module for baresip
Group: Communications
BuildRequires: libgtk+3-devel
Requires: %name = %version-%release

%description gtk
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides a GTK+ menu-based user interface.

%package jack
Summary: JACK audio driver module for baresip
Group: Communications
BuildRequires: pkgconfig(jack)
Requires: %name = %version-%release

%description jack
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the JACK Audio Connection Kit audio driver.

%package mpa
Summary: MPA speech and audio codec module for baresip
Group: Communications
BuildRequires: libmpg123-devel libtwolame-devel liblame-devel libspeexdsp-devel
Requires: %name = %version-%release

%description mpa
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the MPA speech and audio codec.

%package mqtt
Summary: MQTT management module for baresip
Group: Communications
BuildRequires: libmosquitto-devel
Requires: %name = %version-%release

%description mqtt
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Message Queue Telemetry Transport (MQTT)
management module.

%package opus
Summary: Opus audio codec module for baresip
Group: Communications
BuildRequires: libopus-devel
Requires: %name = %version-%release

%description opus
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Opus speech and audio codec.

%package plc
Summary: Packet Loss Concealment module for baresip
Group: Communications
BuildRequires: libspandsp-devel
Requires: %name = %version-%release

%package pipewire
Summary: Pipewire audio driver module for baresip
Group: Communications
BuildRequires: pipewire-libs-devel
Requires: %name = %version-%release

%description pipewire
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Pipewire audio driver.

%package portaudio
Summary: PortAudio audio driver module for baresip
Group: Communications
BuildRequires: libportaudio2-devel
Requires: %name = %version-%release

%description portaudio
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the PortAudio audio driver.

%description plc
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Packet Loss Concealment (PLC) audio-filter using spandsp.

%package pulse
Summary: PulseAudio audio driver module for baresip
Group: Communications
BuildRequires: libpulseaudio-devel
Requires: %name = %version-%release

%description pulse
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the PulseAudio audio driver.

%package sdl
Summary: SDL2 video output driver module for baresip
Group: Communications
BuildRequires: libSDL2-devel
Requires: %name = %version-%release

%description sdl
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Simple DirectMedia Layer 2.0 (SDL) video output driver.

%package snapshot
Summary: Snapshot module for baresip
Group: Communications
BuildRequires: libpng-devel
Requires: %name = %version-%release

%description snapshot
Baresip is a portable and modular SIP User-Agent with audio and video support

This module takes snapshots of the video-stream and save them as PNG images.

%package sndfile
Summary: Snapshot module for baresip
Group: Communications
BuildRequires: libsndfile-devel
Requires: %name = %version-%release

%description sndfile
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides audio filter that writes audio samples to WAV-file.

%package vp8
Summary: VP8 video codec module for baresip
Group: Communications
BuildRequires: libvpx-devel
Requires: %name = %version-%release

%description vp8
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the VP8 video codec.

%package vp9
Summary: VP9 video codec module for baresip
Group: Communications
BuildRequires: libvpx-devel
Requires: %name = %version-%release

%description vp9
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the VP9 video codec.

%package v4l2
Summary: Video4Linux video source driver module for baresip
Group: Communications
BuildRequires: libv4l-devel
Requires: %name = %version-%release

%description v4l2
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the Video4Linux video source driver.

%package x11
Summary: X11 video output driver module for baresip
Group: Communications
BuildRequires: libXext-devel
Requires: %name = %version-%release

%description x11
Baresip is a portable and modular SIP User-Agent with audio and video support

This module provides the X11 video output driver.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md LICENSE README.md docs/examples/*
%_bindir/%name
%_libdir/lib%name.so.17*
%dir %_libdir/%name/
%dir %_libdir/%name/modules/
%_libdir/%name/modules/account.so
%_libdir/%name/modules/aubridge.so
%_libdir/%name/modules/auconv.so
%_libdir/%name/modules/aufile.so
%_libdir/%name/modules/auresamp.so
%_libdir/%name/modules/ausine.so
%_libdir/%name/modules/cons.so
%_libdir/%name/modules/contact.so
%_libdir/%name/modules/ctrl_tcp.so
%_libdir/%name/modules/debug_cmd.so
%_libdir/%name/modules/dtls_srtp.so
%_libdir/%name/modules/ebuacip.so
%_libdir/%name/modules/echo.so
%_libdir/%name/modules/evdev.so
%_libdir/%name/modules/fakevideo.so
%_libdir/%name/modules/g711.so
%_libdir/%name/modules/httpd.so
%_libdir/%name/modules/httpreq.so
%_libdir/%name/modules/ice.so
%_libdir/%name/modules/l16.so
%_libdir/%name/modules/menu.so
%_libdir/%name/modules/mixausrc.so
%_libdir/%name/modules/mixminus.so
%_libdir/%name/modules/mwi.so
%_libdir/%name/modules/natpmp.so
%_libdir/%name/modules/netroam.so
%_libdir/%name/modules/pcp.so
%_libdir/%name/modules/presence.so
%_libdir/%name/modules/rtcpsummary.so
%_libdir/%name/modules/selfview.so
%_libdir/%name/modules/serreg.so
%_libdir/%name/modules/srtp.so
%_libdir/%name/modules/stdio.so
%_libdir/%name/modules/stun.so
%_libdir/%name/modules/syslog.so
%_libdir/%name/modules/turn.so
%_libdir/%name/modules/uuid.so
%_libdir/%name/modules/vidbridge.so
%_libdir/%name/modules/vidinfo.so
%_libdir/%name/modules/vumeter.so
%_datadir/%name

%files devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%files aac
%_libdir/%name/modules/aac.so

%files alsa
%_libdir/%name/modules/alsa.so

%files av1
%_libdir/%name/modules/av1.so

%files codec2
%_libdir/%name/modules/codec2.so

%files ctrl_dbus
%_libdir/%name/modules/ctrl_dbus.so

%files g722
%_libdir/%name/modules/g722.so

%files g726
%_libdir/%name/modules/g726.so

%files gst
%_libdir/%name/modules/gst.so

%files gtk
%_libdir/%name/modules/gtk.so

%files jack
%_libdir/%name/modules/jack.so

%files mpa
%_libdir/%name/modules/mpa.so

%files mqtt
%_libdir/%name/modules/mqtt.so

%files opus
%_libdir/%name/modules/opus.so
%_libdir/%name/modules/opus_multistream.so

%files pipewire
%_libdir/%name/modules/pipewire.so

%files portaudio
%_libdir/%name/modules/portaudio.so

%files plc
%_libdir/%name/modules/plc.so

%files pulse
%_libdir/%name/modules/pulse.so

%files sdl
%_libdir/%name/modules/sdl.so

%files snapshot
%_libdir/%name/modules/snapshot.so

%files sndfile
%_libdir/%name/modules/sndfile.so

%files vp8
%_libdir/%name/modules/vp8.so

%files vp9
%_libdir/%name/modules/vp9.so

%files v4l2
%_libdir/%name/modules/v4l2.so

%files x11
%_libdir/%name/modules/x11.so

%changelog
* Tue Sep 10 2024 Ilya Demyanov <turbid@altlinux.org> 3.15.0-alt1
- new version 3.15.0

* Tue Jul 30 2024 Ilya Demyanov <turbid@altlinux.org> 3.14.0-alt1
- new version 3.14.0

* Thu Jun 27 2024 Ilya Demyanov <turbid@altlinux.org> 3.13.0-alt1
- new version 3.13.0

* Fri Apr 19 2024 Ilya Demyanov <turbid@altlinux.org> 3.11.0-alt1
- new version 3.11.0
- switch to cmake build system
- split package into modules
- update description, urls and license

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- new version 0.6.5 (with rpmrb script)

* Fri Jul 12 2019 Michael Shigorin <mike@altlinux.org> 0.6.1-alt2
- fix modpath properly

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Oct 12 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.11-alt1
- new version 0.5.11 (with rpmrb script)

* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.10-alt1
- new version 0.5.10 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt2
- rebuild with ffmpeg 4.0

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt1
- new version 0.5.9 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.7-alt1
- new version 0.5.7 (with rpmrb script)

* Fri Nov 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.6-alt1
- new version 0.5.6 (with rpmrb script)

* Thu Jun 08 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.5.3-alt1
- new version 0.5.3 (with rpmrb script)

* Fri Nov 18 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.20-alt1
- 0.4.20

* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.12-alt2.qa1
- Fixed build with glibc >= 2.24.

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.12-alt2
- rebuilt with recent libx264

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.12-alt1.1
- NMU: added BR: libspeexdsp-devel

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Mon May 26 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.10-alt1
- 0.4.10

* Tue May 13 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt5
- rebuilt with recent x264, again

* Tue Sep 10 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt4
- rebuilt with recent libx264

* Tue Mar 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt3
- fixed build with recent glibc

* Mon Oct 01 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt2
- revisit buildreqs and modules
- fixed module path

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
