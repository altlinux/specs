Name:    SG-323
Version: 1.0.1
Release: alt1

%define common_summary Emulation of the Ursa Major Stargate 323 digital reverb
%define common_description SG-323 provides emulation of the Ursa Major Stargate 323 \
digital reverb.

Summary: %common_summary
License: GPL-3.0
Group:   Sound
Url:     https://github.com/greyboxaudio/SG-323
Vcs:     https://github.com/greyboxaudio/SG-323.git

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
Summary: Dynamic Equalizer Plugin from ZL Audio (v2) -- VST3
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
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  %nil
%cmake_build


%install
cd "%_cmake__builddir/SG323_artefacts"
mkdir -p %buildroot%_libdir/lv2
cp -a "LV2/SG-323.lv2" %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/SG-323.vst3" %buildroot%_libdir/vst3


%files -n lv2-%name-plugin
%doc README.md
%_libdir/lv2/*

%files -n vst3-%name-plugin
%doc README.md
%_libdir/vst3/*


%changelog
* Wed Nov 26 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.1-alt1
- initial build
