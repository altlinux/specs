
%define _unpackaged_files_terminate_build 1

%define zl_build_type RelWithDebInfo

# see cmake-includes/SharedCodeDefaults.cmake
%define _optlevel 3


%define common_summary Spectrum Equalizer Plugin from ZL Audio
%define common_description ZL Spectrum Equalizer is a dynamic spectrum equalizer plugin \
with the following key features: \
* Unmatched Versatility: Sculpt sound with 9 filter types, 5 stereo \
  modes, 7 variable slopes, and up to 24 linear-phase frequency \
  bands. \
* Spectrum Dynamics: Experience precise frequency-domain dynamic \
  processing that tracks and controls resonances across the \
  spectrum, with adjustable threshold, attack, release, and knee \
  width. \
* Powerful Engine: Tailor behavior and latency with different \
  spectrum resolution settings, side-chain smoothing, and \
  frequency-dependent attack/release skewing, all powered by \
  a high-performance FFT engine. \
* Intuitive Workflow: Achieve fast, fluid equalization with \
  a carefully designed interface featuring an interactive spectrum \
  graph, smart collision detection, and smooth animations. \
%nil

Name:    ZLSpectrumEqualizer
Version: 0.0.1
Release: alt1

Summary: %common_summary
License: AGPL-3.0
Group:   Sound
Url:     https://zl-audio.github.io/plugins/zlspeceq
Vcs:     https://github.com/ZL-Audio/ZLSpectrumEqualizer.git

# For each architecture, a specific value for ZL_HWY_STATIC_TARGET
# should be provided, and that value should be supported in CMakeLists.txt
ExclusiveArch: x86_64 aarch64 loongarch64

%ifarch x86_64
%define zl_hwy_static_target AVX2
%endif
%ifarch aarch64
%define zl_hwy_static_target NEON
%endif
%ifarch loongarch64
%define zl_hwy_static_target LASX
%endif

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %name-%version.tar

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)

Patch: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: clang
BuildRequires: libstdc++-devel
# llvm-ranlib must be used when building with clang
BuildRequires: /usr/bin/llvm-ranlib

# for JUCE tools
BuildRequires: gcc-c++

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%description
%common_description


%package standalone
Summary: %common_summary -- Standalone
Group:   Sound

%description standalone
%common_description

This package contains ZL Spectrum Equalizer built as a standalone
application, capable of working with Jack or ALSA.


%package -n lv2-%name-plugin
Summary: %common_summary -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains ZL Spectrum Equalizer built as LV2 plugin.


%package -n vst3-%name-plugin
Summary: %common_summary -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains ZL Spectrum Equalizer built as VST3 plugin.


%prep
%setup
# unpack sub-merged sources
sh -eux "%SOURCE2"

%autopatch -p1

%build
# for the nested cmake that builds juceaid
export CMAKE_BUILD_PARALLEL_LEVEL=%_smp_build_ncpus

%add_optflags -DJUCE_JACK=1 -DNDEBUG

%cmake \
  -DCMAKE_BUILD_TYPE=%zl_build_type \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DFOOBAR_VERSION:string=%version \
  -DGIT_EXECUTABLE:string='' \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  -DZL_JUCE_FORMATS="VST3;LV2;Standalone" \
  -DZL_JUCE_COPY_PLUGIN=FALSE \
  -DCMAKE_CXX_FLAGS_RELWITHDEBINFO='%optflags' \
  -DCMAKE_C_FLAGS_RELWITHDEBINFO='%optflags' \
  -DZL_HWY_STATIC_TARGET:string=%zl_hwy_static_target \
  %nil

%cmake_build

%install
cd %_cmake__builddir/*_artefacts/%zl_build_type

install -Dm755 Standalone/ZL\ Spectrum\ Equalizer \
    %buildroot%_bindir/ZL\ Spectrum\ Equalizer
mkdir -p %buildroot%_libdir/lv2
cp -a LV2/*.lv2 %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a VST3/*.vst3 %buildroot%_libdir/vst3


%files standalone
%_bindir/*

%files -n lv2-%name-plugin
%_libdir/lv2/*

%files -n vst3-%name-plugin
%_libdir/vst3/*


%changelog
* Thu Jul 30 2026 Ivan A. Melnikov <iv@altlinux.org> 0.0.1-alt1
- Build for Sisyphus (based on ZLEqualizer2 spec).
