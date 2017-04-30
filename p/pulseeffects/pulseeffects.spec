%define gst_api_ver 1.0

Name: pulseeffects
Version: 1.2.5
Release: alt1

Summary: Audio effects for Pulseaudio applications
License: GPLv3
Group: Sound
Url: https://github.com/wwmm/pulseeffects

Source: %name-%version.tar.gz

BuildArch: noarch

Requires: pulseaudio-daemon dconf
Requires: gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver
Requires: ladspa-swh-plugins

# python3 used
AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-gir rpm-build-python3 python3-module-setuptools
BuildRequires: python3-devel python3-module-pygobject3-devel

%description
PulseEffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for Pulseaudio applications.

%prep
%setup

%build
%python3_build

%install
%python3_install
cp -r share %buildroot%_prefix

%find_lang --output=%name.lang PulseEffects

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/*
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/com.github.wwmm.pulseeffects.gschema.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%doc README*

%changelog
* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- first build for Sisyphus


