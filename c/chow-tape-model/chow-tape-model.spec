
%define _unpackaged_files_terminate_build 1

Name:     chow-tape-model
Version:  2.8.0
Release:  alt1

ExclusiveArch: x86_64

Summary:  Physical modelling of analog tape machine
License:  GPL-3.0
Group:    Sound
#Vcs:     https://github.com/jatinchowdhury18/AnalogTapeModel
Url:      https://chowdsp.com/products.html#tape


Source:   AnalogTapeModel-%version.tar

# Submodules are dealt with via sub-merge
# http://git.altlinux.org/people/iv/public/sub-merge.git

# https://github.com/Chowdhury-DSP/DISTRHO-JUCE.git
Source10: DISTRHO-JUCE-5d503f334ddb849b3e13f5d7d28e553686f44f9e.tar
# https://github.com/jatinchowdhury18/foleys_gui_magic.git
Source11: foleys_gui_magic-5d0e230d052c66cc96e7ac5e609b37ab7b4acb08.tar
# https://github.com/Chowdhury-DSP/chowdsp_utils
Source12: chowdsp_utils-52361ab411b23d19d45ded1184bb3802c1a4e2ce.tar
# https://github.com/jatinchowdhury18/RTNeural
Source13: RTNeural-fcd9b66b6a6dd85a014cca1f52c87d2424fdf0f2.tar
# https://github.com/xtensor-stack/xsimd
Source14: xsimd-aaba949c4b57d234fa2356fcf13368a74cac99ec.tar


BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)


%description
Chow Tape Model is a digital emulation of a reel-to-reel
analog tape machine.  The original algorithm was developed to
emulate the Sony TC-260, but has since been expanded to be
able to model a wide variety of tape machines. As well as
a tool for mixing engineers and producers, ChowTape is
a research project on developing physics-based models
of analog tape emulation.


%package -n lv2-%name-plugin
Summary: Physical modelling of analog tape machine as LV2 plugin
Group:   Sound

%description -n lv2-%name-plugin
Chow Tape Model is a digital emulation of a reel-to-reel
analog tape machine.  The original algorithm was developed to
emulate the Sony TC-260, but has since been expanded to be
able to model a wide variety of tape machines. As well as
a tool for mixing engineers and producers, ChowTape is
a research project on developing physics-based models
of analog tape emulation.

This package contains Chow Tape Model built as LV2 plugin.


%prep
%setup -n AnalogTapeModel-%version

tar -xf %SOURCE10 -C 'Plugin/modules/DISTRHO-JUCE' --strip-components 1
tar -xf %SOURCE11 -C 'Plugin/modules/foleys_gui_magic' --strip-components 1
tar -xf %SOURCE12 -C 'Plugin/modules/chowdsp_utils' --strip-components 1
tar -xf %SOURCE13 -C 'Plugin/modules/RTNeural' --strip-components 1
tar -xf %SOURCE14 -C 'Plugin/modules/RTNeural/modules/xsimd' --strip-components 1

%build
pushd Plugin
%cmake
%cmake_build -t CHOWTapeModel_LV2
popd

%install
src_path="$(pwd)/Plugin/%_cmake__builddir/CHOWTapeModel_artefacts/LV2/CHOWTapeModel.lv2"
dst_path="%buildroot%_libdir/lv2/CHOWTapeModel.lv2"
install -Dm644 -t "$dst_path" "$src_path/CHOWTapeModel.so"
install -m644  -t "$dst_path" "$src_path/"*.ttl

%files -n lv2-%name-plugin
%_libdir/lv2/*
%doc Manual/ChowTapeManual.pdf

%changelog
* Wed Jul 14 2021 Ivan A. Melnikov <iv@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
