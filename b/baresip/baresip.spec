Name: baresip
Version: 0.4.2
Release: alt1

Summary: Baresip is a portable and modular SIP User-Agent with audio and video support

Url: http://www.creytiv.com/baresip.html
License: BSD Revised
Group: System/X11

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.creytiv.com/pub/baresip-%version.tar

# Automatically added by buildreq on Mon Sep 17 2012
# optimized out: glib2-devel libX11-devel libavcodec-devel libavutil-devel libxml2-devel pkg-config xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gstreamer-devel libSDL-devel libXext-devel libalsa-devel libavdevice-devel libavformat-devel libcairo-devel libgsm-devel libmpg123-devel libportaudio2-devel libre-devel librem-devel libsndfile-devel libspeex-devel libssl-devel libswscale-devel libuuid-devel libv4l-devel libx264-devel

%description
baresip is a bare-bones SIP user agent. It supports SIP, SDP, RTP/RTCP,
and STUN/TURN/ICE, and IPv4 and IPv6, and is RFC-compliant and has
portable C89 and C99 source code. A modular plugin architecture provides
stdio, cons, and evdev user interfaces, celt, g711, g722, gsm, ilbc, l16,
and speex audio codecs, alsa, coreaudio, gst, portaudio, oss, winwav,
and mda audio drivers, speex_pp, speex_aec, speex_resamp, and sndfile
audio filters, the avcodec video codec, avformat, quicktime, qtcapture,
v4l, and v4l2 video sources, sdl, opengl, and x11 video display drivers,
and srtp media encoding.

%prep
%setup

%build
%make_build RELEASE=1 MOD_AUTODETECT=1

%install
%makeinstall_std RELEASE=1 MOD_AUTODETECT=1 LIBDIR=%_libdir

%files
%doc docs/*
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
#%_desktopdir/%name.desktop
#%_man1dir/*

%changelog
* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
