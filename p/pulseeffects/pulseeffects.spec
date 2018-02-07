%define gst_api_ver 1.0
%define gst_ver 1.12
%define gtk_ver 3.18
%define xdg_name com.github.wwmm.pulseeffects

Name: pulseeffects
Version: 3.2.0
Release: alt1

Summary: Audio effects for Pulseaudio applications
License: GPLv3
Group: Sound
Url: https://github.com/wwmm/pulseeffects

Source: https://github.com/wwmm/pulseeffects/archive/%name-%version.tar.gz

BuildArch: noarch

Requires: libgtk+3-gir >= %gtk_ver
Requires: pulseaudio-daemon dconf
Requires: gst-plugins-good%gst_api_ver >= %gst_ver
Requires: gst-plugins-bad%gst_api_ver >= %gst_ver
Requires: ladspa-swh-plugins ladspa-rubberband
#Requires: liblilv calf-plugins zam-plugins

# for CubicSpline
Requires: python3-module-scipy >= 0.19

# python3 used
AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): meson rpm-build-gir rpm-build-python3
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: python3-module-pycairo-devel
BuildRequires: libgtk+3-devel libgtk+3-gir-devel
BuildRequires: gst-plugins-bad%gst_api_ver-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libbs2b-devel
#BuildRequires: liblilv-devel

%description
PulseEffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for Pulseaudio applications.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --output=%name.lang PulseEffects

%files -f %name.lang
%_bindir/%name
#%_bindir/%{name}_calibration
%python3_sitelibdir_noarch/*
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/com.github.wwmm.%name.gschema.xml
%_datadir/glib-2.0/schemas/com.github.wwmm.%name.sinkinputs.gschema.xml
%_datadir/glib-2.0/schemas/com.github.wwmm.%name.sourceoutputs.gschema.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README*

%changelog
* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.1.7-alt1
- 3.1.7

* Sun Nov 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Sun Nov 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Sat Oct 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri Oct 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Sep 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1
- 2.3.5

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sat Jul 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Sun Jul 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9

* Wed Jul 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Jul 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sat Jul 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Jun 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.5-alt1
- 1.6.5

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Sun Jun 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.8-alt1
- 1.5.8

* Mon Jun 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

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


