Name: wavetable
Version: 1.0.21
Release: alt1

Summary: Wavetable synth
License: BSD-3-Clause
Group: Sound
Url: https://github.com/FigBug/Wavetable

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%package -n lv2-wavetable-plugin
Summary: Wavetable synth as LV2 plugin
Group: Sound

%package -n vst3-wavetable-plugin
Summary: Wavetable synth as VST3 plugin
Group: Sound

%description
%summary

%description -n lv2-wavetable-plugin
Wavetable synthesizer as LV2 plugin.

%description -n vst3-wavetable-plugin
Wavetable synthesizer as VST3 plugin.

%prep
%setup
tar ixf %SOURCE1

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_libdir/{lv2,vst3}
cp -av %_cmake__builddir/*/LV2/*.lv2 %buildroot%_libdir/lv2
cp -av %_cmake__builddir/*/VST3/*.vst3 %buildroot%_libdir/vst3

%files -n lv2-wavetable-plugin
%_libdir/lv2/*

%files -n vst3-wavetable-plugin
%_libdir/vst3/*

%changelog
* Fri Jul 19 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.21-alt1
- 1.0.21 released
