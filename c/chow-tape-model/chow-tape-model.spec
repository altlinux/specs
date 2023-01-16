
%define _unpackaged_files_terminate_build 1

Name:     chow-tape-model
Version:  2.11.1
Release:  alt2

ExclusiveArch: x86_64

Summary:  Physical modelling of analog tape machine
License:  GPL-3.0
Group:    Sound
#Vcs:     https://github.com/jatinchowdhury18/AnalogTapeModel
Url:      https://chowdsp.com/products.html#tape


Source:   AnalogTapeModel-%version.tar

# Submodules are dealt with via sub-merge
# http://git.altlinux.org/people/iv/public/sub-merge.git
Source1:  sub-merge.sources.txt
Source2:  sub-merge.unpack.sh
%(cat %SOURCE1)

Patch1:   juice-alt-fix-build.patch
Patch2:   chow-tape-model-2.11.1-alt-restrict-to-stereo.patch


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
. %SOURCE2

%autopatch -p1

%build
# for nested cmake:
export CMAKE_BUILD_PARALLEL_LEVEL=%_smp_build_ncpus

pushd Plugin
%cmake \
  -DCHOWTAPE_BUILD_CLAP=OFF
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
* Mon Jan 16 2023 Ivan A. Melnikov <iv@altlinux.org> 2.11.1-alt2
- Build stereo-only version of LV2 plugin to avoid
  crashes in Ardour.

* Sat Jan 14 2023 Ivan A. Melnikov <iv@altlinux.org> 2.11.1-alt1
- 2.11.1

* Wed Jul 14 2021 Ivan A. Melnikov <iv@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
