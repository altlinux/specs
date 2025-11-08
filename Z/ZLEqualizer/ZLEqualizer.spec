
%define _unpackaged_files_terminate_build 1

# Workaround for https://bugzilla.altlinux.org/53250
%add_debuginfo_skiplist %_libdir
%define optflags_debug -g0
# Change this to RelWithDebInfo when the issue is resolverd
%define zl_build_type Release

# see cmake-includes/SharedCodeDefaults.cmake
%define _optlevel 3

Name:    ZLEqualizer
Version: 0.6.2
Release: alt2

Summary: Dynamic Equalizer Plugin from ZL Audio (v1)
License: AGPL-3.0
Group:   Sound
Url:     https://zl-audio.github.io/plugins/zlequalizer/
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

%define common_description ZL Equalizer is an equalizer plugin with the following key features:\
- Multiple Filter Settings: Supports 6 filter structures, 16\
  frequency bands, 8 filter types, 5 stereo modes, 7 variable\
  slopes.\
- High-Quality Sound: With 64-bit floating-point processing\
  and de-cramping technique, outstanding performance is\
  ensured in both low-end and high-end.\
- Adjustable Dynamics: Adjustable threshold, attack, release,\
  and side-chain frequency, etc.\
- Carefully Designed Interface: Interactive spectrum graph,\
  smart collision detection, and smooth animations.\
\
Note: ZL Equalizer is in the legacy state. Consider using \
ZL Equalizer v2 for new projects.

%description
%common_description

%package -n lv2-%name-plugin
Summary: Dynamic Equalizer Plugin from ZL Audio (v1) -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains ZL Equalizer built as LV2 plugin.


%package -n vst3-%name-plugin
Summary: Dynamic Equalizer Plugin from ZL Audio (v1) -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains ZL Equalizer built as VST3 plugin.


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
cp -a "LV2/ZL Equalizer.lv2" %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/ZL Equalizer.vst3" %buildroot%_libdir/vst3


%files -n lv2-%name-plugin
%doc README.md
%_libdir/lv2/*

%files -n vst3-%name-plugin
%doc README.md
%_libdir/vst3/*


%changelog
* Sat Nov 08 2025 Ivan A. Melnikov <iv@altlinux.org> 0.6.2-alt2
- backport fixes from upstream/v1 bracnh
- note that ZL Equalizer v1 is "in the legacy state"

* Thu May 01 2025 Ivan A. Melnikov <iv@altlinux.org> 0.6.2-alt1
- 0.6.2
- build with clang

* Thu Apr 10 2025 Ivan A. Melnikov <iv@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Mar 17 2025 Ivan A. Melnikov <iv@altlinux.org> 0.6.0-alt1
- 0.6.0
  + BREAKING: new compressor model from ZL Compressor
  + BREAKING: smooth filter frequency/gain/Q changes

* Fri Feb 28 2025 Ivan A. Melnikov <iv@altlinux.org> 0.5.0-alt2
- Explicitly specify target architecture (fixes FTBFS
  on loongarch64).

* Wed Feb 26 2025 Ivan A. Melnikov <iv@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
