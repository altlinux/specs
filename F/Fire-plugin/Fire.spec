
Name:    Fire-plugin
Version: 1.5.0
Release: alt1

Summary: A mutiband distortion plugin
License: AGPL-3.0
Group:   Sound
Url:     https://www.bluewingsmusic.com/Fire/#about
Vcs:     https://github.com/jerryuhoo/Fire.git

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


%define common_description Fire is a multiband distortion/downsampler plugin. It offers \
independent drive, tone, and mix controls for each band, \
global filter and lo-fi (downsampler) effects, and advanced \
modulation system with four fully customizable LFOs available \
for modulating most of the parameters of the plug-in. \
%nil

%description
%common_description


%package -n vst3-%name
Summary: A mutiband distortion plugin -- VST3
Group:   Sound

%description -n vst3-%name
%common_description

This package contains Fire built as VST3 plugin.


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
%cmake
%cmake_build

%install
cd "%_cmake__builddir/Fire_artefacts"
mkdir -p %buildroot%_libdir/vst3
cp -a "VST3/Fire.vst3" %buildroot%_libdir/vst3

%files -n vst3-%name
%_libdir/vst3/*

%changelog
* Fri Nov 21 2025 Ivan A. Melnikov <iv@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
