
%define _unpackaged_files_terminate_build 1

%define zl_build_type RelWithDebInfo

# see cmake-includes/SharedCodeDefaults.cmake
%define _optlevel 3


%define common_summary A multifunctional splitter plugin

%define common_description ZL Splitter is a multifunctional audio splitter plugin, \
which can split the input signal into: \
- left/right signal; \
- mid/side signal; \
- low/high signal; \
- transient/steady signal; \
- peak/steady signal. \
%nil


Name:    ZLSplitter
Version: 0.3.0
Release: alt1

Summary: %common_summary
License: AGPL-3.0
Group:   Sound
Url:     https://zl-audio.github.io/plugins/zlsplitter/
Vcs:     https://github.com/ZL-Audio/ZLSplitter.git

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
  -DCMAKE_BUILD_TYPE=%zl_build_type \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DFOOBAR_VERSION:string=%version \
  -DGIT_EXECUTABLE:string='' \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  -DKFR_ENABLE_MULTIARCH:BOOL=ON \
  -DZL_JUCE_FORMATS="VST3;LV2" \
  -DZL_JUCE_COPY_PLUGIN=FALSE \
  %nil

%cmake_build

%install
cd %_cmake__builddir/*_artefacts/%zl_build_type

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
* Wed Apr 08 2026 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sun Dec 14 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2.1-alt1
- 0.2.1

* Wed Dec 10 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2.0-alt1
- Build for Sisyphus (based on ZLEqualizer.spec).
