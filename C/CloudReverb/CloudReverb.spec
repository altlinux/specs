
%define _unpackaged_files_terminate_build 1
#define snapshot %nil
%define build_type Release

Name:    CloudReverb
Version: 0.5
Release: alt1

Summary: Algorithmic reverb plugin based on CloudSeed
License: MIT
Group:   Sound
Url:     https://github.com/xunil-cloud/CloudReverb
Vcs:     https://github.com/xunil-cloud/CloudReverb.git

# VST3 plugin fails to build on i586
ExcludeArch: %ix86

Source: %name-%version%{?snapshot:-%snapshot}.tar

Source1: sub-merge.sources.txt
Source2: sub-merge.unpack.sh

# Import sub-merge sources right here
%(cat %SOURCE1)

BuildRequires(pre): rpm-macros-cmake
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


%define common_description CloudReverb is an audio plugin for algorithmic reverb. The algorithm\
is borrowed from CloudSeed VST by Valdemar Erlingsson, but the plugin\
was rewritten in JUCE for portability.\
\
This plugin was designed for emulating huge, endless spaces and\
modulated echoes. does not attempt to model any specific device,\
or even to be a general-purpose reverb plugin at all. It is best\
employed as a special effect, for creating thick, lush pads out\
of simple input sounds.\

%description
%common_description

%package -n lv2-%name-plugin
Summary: Algorithmic reverb plugin based on CloudSeed -- LV2
Group:   Sound

%description -n lv2-%name-plugin
%common_description

This package contains Cloud Reverb built as LV2 plugin.


%package -n vst3-%name-plugin
Summary: Algorithmic reverb plugin based on CloudSeed -- VST3
Group:   Sound

%description -n vst3-%name-plugin
%common_description

This package contains Cloud Reverb built as VST3 plugin.

%prep
%setup -n %name-%version%{?snapshot:-%snapshot}
# unpack sub-merged sources
sh -eux "%SOURCE2"

%autopatch -p1

# build juceaid on in parallel
sed -i -r "s/(--config\s+\S+)/\1 --parallel %_smp_build_ncpus/" \
    JUCE/extras/Build/juceaide/CMakeLists.txt
grep parallel JUCE/extras/Build/juceaide/CMakeLists.txt || exit 1

%build
%cmake \
  -DJUCE_TARGET_ARCHITECTURE:string=%_arch \
  -DCMAKE_BUILD_TYPE=%build_type \
  %nil

%cmake_build

%install
cd "%_cmake__builddir/CloudReverb_artefacts/%build_type"

mkdir -p %buildroot%_libdir/lv2
cp -a "LV2/CloudReverb.lv2" %buildroot%_libdir/lv2
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/CloudReverb.vst3" %buildroot%_libdir/vst3

%files -n lv2-%name-plugin
%doc README.md
%_libdir/lv2/*

%files -n vst3-%name-plugin
%doc README.md
%_libdir/vst3/*

%changelog
* Wed Apr 29 2026 Ivan A. Melnikov <iv@altlinux.org> 0.5-alt1
- 0.5

* Sat Jan 03 2026 Ivan A. Melnikov <iv@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Nov 26 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4-alt3
- explicitly define JUCE_TARGET_ARCHITECTURE (fixes FTBFS
  on loongarch64).

* Wed Nov 26 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4-alt2
- drop i586 support

* Tue Nov 25 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4-alt1
- v0.4

* Sat Sep 20 2025 Ivan A. Melnikov <iv@altlinux.org> 0.3.1-alt1
- v0.3.1

* Thu Aug 21 2025 Ivan A. Melnikov <iv@altlinux.org> 0.3-alt1
- v0.3

* Fri May 09 2025 Ivan A. Melnikov <iv@altlinux.org> 0.2-alt1.gitceb5e1df
- initial build
