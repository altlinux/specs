
%define _unpackaged_files_terminate_build 1

%define common_summary A Dual Delay audio plugin with more features than it should

%define common_description QDelay (short for quick-delay) is a dual-delay with more \
features than it should for a free plugin that's supposed \
to be quick. It features: \
* Stereo Dual Delay with independent delay times and multiple modes. \
* Ping-Pong mode with feedback width control. \
* Tap mode with offset time (tap) and delay time. \
* Swing and Feel offset. \
* Accent odd or even taps. \
* Reverse delay. \
* Parametric EQ on feedback and input signal. \
* Diffusion on pre or post delay signal. \
* Modulation of delay line time. \
* Pitch Shifter on the feedback or post delay signal. \
* Saturation on pre and post delay signal (optionally on Feedback path). \
* Color, Bias and Dynamics controls for saturation. \
* Ducking to muffle the delayed signal on input. \
* Tape wow and flutter to add tone variation. \
* Taps preview display. \
%nil


Name:    qdelay
Version: 1.1.1
Release: alt1

Summary: %common_summary
License: GPL-3.0
Group:   Sound
Url:     https://github.com/tiagolr/qdelay
Vcs:     https://github.com/tiagolr/qdelay.git

# Exclude i586 just because I can
ExcludeArch: %ix86

Source: %name-%version.tar
Patch:  %name-%version-%release.patch

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)


%description
%common_description


%package -n lv2-%name-plugin
Summary: %common_summary -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains %name built as LV2 plugin.


%package -n vst3-%name-plugin
Summary: %common_summary -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains %name built as VST3 plugin.


%prep
%setup
# unpack sub-merged sources
sh -eux "%SOURCE2"

%autopatch -p1

%build
# for the nested cmake that builds juceaid
export CMAKE_BUILD_PARALLEL_LEVEL=%_smp_build_ncpus

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  %nil
%cmake_build

%install
cd %_cmake__builddir/*_artefacts/RelWithDebInfo

mkdir -p %buildroot%_libdir/lv2
cp -a LV2/*.lv2 %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a VST3/*.vst3 %buildroot%_libdir/vst3


%files -n lv2-%name-plugin
%doc README.md
%_libdir/lv2/*

%files -n vst3-%name-plugin
%doc README.md
%_libdir/vst3/*


%changelog
* Sat Mar 14 2026 Ivan A. Melnikov <iv@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Feb 20 2026 Ivan A. Melnikov <iv@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Jan 27 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.8-alt1
- 1.0.8

* Thu Jan 22 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.7-alt1
- 1.0.7

* Sat Jan 10 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt1
- 1.0.6

* Fri Jan 09 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.5-alt1
- 1.0.5

* Tue Jan 06 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.4-alt1
- build for Sisyphus
