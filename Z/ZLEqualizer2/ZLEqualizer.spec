
%define _unpackaged_files_terminate_build 1

%define zl_build_type RelWithDebInfo

# see cmake-includes/SharedCodeDefaults.cmake
%define _optlevel 3

Name:    ZLEqualizer2
Version: 1.0.2
Release: alt1

Summary: Dynamic Equalizer Plugin from ZL Audio (v2)
License: AGPL-3.0
Group:   Sound
Url:     https://zl-audio.github.io/plugins/zlequalizer2/
Vcs:     https://github.com/ZL-Audio/ZLEqualizer.git

ExcludeArch: %ix86 ppc64le

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
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%define common_description ZL Equalizer 2 is a dynamic equalizer plugin with the following key features: \
\
* Unmatched Versatility: Sculpt your sound with 6 filter structures, \
  8 filter types, 5 stereo modes, 7 variable slopes, and up to 24 \
  frequency bands. \
* Integrated Dynamic Control: Go beyond static EQ with adjustable \
  threshold, attack, release, and side-chain filters for powerful \
  dynamic equalization. \
* Pristine Precision: 64-bit floating-point processing and advanced \
  de-cramping technique deliver outstanding performance, ensuring \
  exceptional clarity from the deepest lows to the highest highs. \
* Intuitive Workflow: A carefully designed interface with \
  an interactive spectrum graph, smart collision detection, and \
  smooth animations makes equalization fast and fluid.

%description
%common_description

%package -n lv2-%name-plugin
Summary: Dynamic Equalizer Plugin from ZL Audio (v2) -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains ZL Equalizer 2 built as LV2 plugin.


%package -n vst3-%name-plugin
Summary: Dynamic Equalizer Plugin from ZL Audio (v2) -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains ZL Equalizer 2 built as VST3 plugin.


%prep
%setup
# unpack sub-merged sources
sh -eux "%SOURCE2"

%autopatch -p1

# build juceaid on in parallel
sed -i -r "s/(--config\s+Custom)/\1 --parallel %_smp_build_ncpus/" \
    JUCE/extras/Build/juceaide/CMakeLists.txt
grep parallel JUCE/extras/Build/juceaide/CMakeLists.txt || exit 1

%build

%cmake \
  -DCMAKE_BUILD_TYPE=%zl_build_type \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DFOOBAR_VERSION:string=%version \
  -DGIT_EXECUTABLE:string='' \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  -DKFR_ENABLE_MULTIARCH:BOOL=ON \
  -DZL_JUCE_FORMATS="VST3;LV2" \
  -DDZL_JUCE_COPY_PLUGIN=FALSE \
  %nil

%cmake_build

%install
cd "%_cmake__builddir/ZLEqualizer_artefacts/%zl_build_type"

mkdir -p %buildroot%_libdir/lv2
cp -a "LV2/ZL Equalizer 2.lv2" %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/ZL Equalizer 2.vst3" %buildroot%_libdir/vst3


%files -n lv2-%name-plugin
%doc README.md
%_libdir/lv2/*

%files -n vst3-%name-plugin
%doc README.md
%_libdir/vst3/*


%changelog
* Sat Nov 15 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Nov 14 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Nov 09 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.0-alt1
- Build for Sisyphus (based on ZLEqualizer.spec).
