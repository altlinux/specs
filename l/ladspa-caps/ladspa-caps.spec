Name: ladspa-caps
Version: 0.4.2
Release: alt1
Summary: Collection of refined realtime-capable LADSPA plugins
Summary(ru_RU.UTF-8): Сборник плагинов LADSPA реального времени
License: GPL
Group: Sound
Url: http://quitte.de/dsp/caps.html
Packager: Mikhail Yakshin <greycat@altlinux.ru>
Source: caps_%version.tar.gz
#Patch: caps-makefile.patch.gz

# Automatically added by buildreq on Tue Jan 18 2005
BuildRequires: gcc-c++ libstdc++-devel ladspa_sdk

%description
CAPS, the C* Audio Plugin Suite, is a collection of refined LADSPA units
including instrument amplifier emulation, stomp-box classics, versatile
'virtual analog' oscillators, fractal oscillation, reverb, equalization
and others.

This package contains the following plugins:

* Generic (Eq, Eq2x2, Compress, Pan)
* Emulation (PreampIII, PreampIV, ToneStack, ToneStackLT, AmpIII, AmpIV,
  AmpV, AmpVTS, CabinetI, CabinetII, Clip)
* Effects (ChorusI, StereoChorusI, ChorusII, StereoChorusII, PhaserI,
  PhaserII, SweepVFI, SweepVFII, AutoWah, Scape)
* Generators (VCOs, VCOd, CEO, Sin, White, Lorenz, Roessler)
* Reverb (JVRev, Plate, Plate2x2)
* Others (Click, Dirac, HRTF)

%description -l ru_RU.UTF-8
CAPS, C* Audio Plugin Suite - сборник плагинов LADSPA, включающий в себя
эмуляцию инструментальных (гитарных) усилителей, классические
эффекты-педали, гибкие виртуальные представления аналоговых
осцилляторов, фрактальные осцилляторы, реверберацию, эквализацию и
кое-что еще.

В этот пакет входят следующие плагины:

* Generic (Eq, Eq2x2, Compress, Pan)
* Emulation (PreampIII, PreampIV, ToneStack, ToneStackLT, AmpIII, AmpIV,
  AmpV, AmpVTS, CabinetI, CabinetII, Clip)
* Effects (ChorusI, StereoChorusI, ChorusII, StereoChorusII, PhaserI,
  PhaserII, SweepVFI, SweepVFII, AutoWah, Scape)
* Generators (VCOs, VCOd, CEO, Sin, White, Lorenz, Roessler)
* Reverb (JVRev, Plate, Plate2x2)
* Others (Click, Dirac, HRTF)

%prep
%setup -n caps-%version
#%patch -p1

%build
%add_optflags %optflags_shared
sed -i 's/^OPTS = -O2 -ffast-math -funroll-loops -Wall -fPIC -DPIC$/OPTS = -O2 -funroll-loops -Wall -fPIC -DPIC/' Makefile
%make_build

%install
%__install -D -m644 caps.so %buildroot%_ladspa_path/caps.so

%files
%doc README CHANGES caps.html
%_ladspa_path/*.so

%changelog
* Sun Jul 05 2009 Mikhail Yakshin <greycat@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sat Jun 03 2006 Mikhail Yakshin <greycat@altlinux.org> 0.3.0-alt1
- 0.3.0

* Tue Jan 18 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.2.0-alt1
- Initial build for Sisyphus

