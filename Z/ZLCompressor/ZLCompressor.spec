
%define _unpackaged_files_terminate_build 1

# Change this to RelWithDebInfo when the issue is resolverd
%define zl_build_type RelWithDebInfo

Name:    ZLCompressor
Version: 0.2.1
Release: alt2

Summary: A compressor plugin from ZL Audio
License: AGPL-3.0
Group:   Sound
Url:     https://zl-audio.github.io/plugins/zlcompressor/
Vcs:     https://github.com/ZL-Audio/ZLCompressor.git

ExcludeArch: %ix86

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %name-%version.tar

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)

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

%define common_description ZL Compressor is a dynamic range compressor with the following\
key features:\
- compression styles include Clean (VCA), Classic (FET) and Optical;\
- side-chain control with 8-band EQ and adjustable stereo link;\
- up to 8x oversampling;\
- intuitive visual interface.\
%nil

%description
%common_description


%package standalone
Summary: A compressor plugin from ZL Audio -- Standalone
Group:   Sound

%description standalone
%common_description

This package contains ZL Compressor built as a standalone
application, capable of working with Jack or ALSA.


%package -n lv2-%name-plugin
Summary: A compressor plugin from ZL Audio -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains ZL Compressor built as a LV2 plugin.


%package -n vst3-%name-plugin
Summary: A compressor plugin from ZL Audio -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains ZL Compressor built as a VST3 plugin.


%prep
%setup

# unpack sub-merged sources
sh -eux "%SOURCE2"

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
  -DZL_JUCE_FORMATS="VST3;LV2;Standalone" \
  -DZL_JUCE_COPY_PLUGIN=FALSE \
  %nil

%cmake_build

%install
cd "%_cmake__builddir/ZLCompressor_artefacts/%zl_build_type"

install -Dm755 Standalone/ZL\ Compressor \
    %buildroot%_bindir/ZL\ Compressor
mkdir -p %buildroot%_libdir/lv2
cp -a "LV2/ZL Compressor.lv2" %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/ZL Compressor.vst3" %buildroot%_libdir/vst3


%files standalone
%_bindir/*

%files -n lv2-%name-plugin
%_libdir/lv2/*

%files -n vst3-%name-plugin
%_libdir/vst3/*

%changelog
* Sat Sep 20 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2.1-alt2
- 0.2.1 was retagged (sic!) by upstream, udpate to that new tag

* Thu Sep 11 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2.1-alt1
- 0.2.1

* Thu Aug 21 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Aug 02 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1.2-alt1
- 0.1.2

* Thu Jun 26 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Jun 25 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1.0-alt1
- initial build
