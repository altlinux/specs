%define gst_api_ver 1.0
%define gst_ver 1.12

Name: pulseeffects
Version: 1.5.3
Release: alt1

Summary: Audio effects for Pulseaudio applications
License: GPLv3
Group: Sound
Url: https://github.com/wwmm/pulseeffects

Source: %name-%version.tar.gz

BuildArch: noarch

Requires: pulseaudio-daemon dconf
Requires: gst-plugins-good%gst_api_ver >= %gst_ver
Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
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
* Wed Jun 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 05 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun May 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Mon May 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.6-alt1
- 1.3.6

* Sat May 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4

* Fri May 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue May 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Sun May 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat May 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- 1.2.8

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- first build for Sisyphus


