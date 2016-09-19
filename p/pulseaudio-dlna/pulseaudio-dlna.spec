Name: pulseaudio-dlna
Version: 0.5.2
Release: alt1
Summary: A lightweight streaming server which brings DLNA/UPNP and Chromecast

License: GPLv3
Group: Development/Python
Url: https://github.com/masmu/pulseaudio-dlna
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
Requires: python-module-protobuf >= 2.5.0
Requires: python-module-psutil >= 1.2.1

%description
This is pulseaudio-dlna. A lightweight streaming server which brings DLNA / UPNP
and Chromecast support to PulseAudio and Linux. It can stream your current
PulseAudio playback to different UPNP devices (UPNP Media Renderers) or
Chromecasts in your network. It's main goals are: easy to use, no configuration
hassle, no big dependencies.

UPNP renderers in your network will show up as pulseaudio sinks.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*
%doc LICENSE
%doc README.*
%python_sitelibdir/pulseaudio_dlna
%python_sitelibdir/*.egg-info
%_man1dir/%name.1.*

%changelog
* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.5.2-alt1
- Initial build for ALT Linux Sisyphus.
