
%define _unpackaged_files_terminate_build 1

Name:     ChowMatrix
Version:  1.2.0
Release:  alt1

ExclusiveArch: x86_64 aarch64

Summary:  Matrix delay effect
License:  BSD-3-Clause AND GPL-3.0+
Group:    Sound
Url:      https://github.com/Chowdhury-DSP/ChowMatrix

Source:   %name-%version.tar

# Submodules are dealt with via sub-merge
# http://git.altlinux.org/people/iv/public/sub-merge.git

# https://github.com/Chowdhury-DSP/DISTRHO-JUCE.git
Source10: DISTRHO-JUCE-197d7e9370e66e63846a971ef8061af6c1d6b9fb.tar
# https://github.com/ffAudio/foleys_gui_magic.git
Source11: foleys_gui_magic-8055fd375f810f71f03d4aefa73c0fcb4d843868.tar
# https://github.com/Chowdhury-DSP/chowdsp_utils.git
Source12: chowdsp_utils-f37cd76c3ddbbbd772f2455f6b2c0fa4f9d86862.tar
# https://github.com/juce-framework/JUCE.git
Source13: JUCE-545e9f353a6a336c5d1616796024b30d4bbed04b.tar

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
CHOW Matrix is a delay effect, made up of an infinitely growable
tree of delay lines, each with individual controls for feedback,
panning, distortion, and more.


%package -n lv2-%name-plugin
Group: Sound
Summary: Matrix delay effect - LV2 version

%description -n lv2-%name-plugin
CHOW Matrix is a delay effect, made up of an infinitely growable
tree of delay lines, each with individual controls for feedback,
panning, distortion, and more.

This package contains the LV2 version of the effect.


%prep
%setup

tar -xf %SOURCE10 -C 'modules/DISTRHO-JUCE' --strip-components 1
tar -xf %SOURCE11 -C 'modules/foleys_gui_magic' --strip-components 1
tar -xf %SOURCE12 -C 'modules/chowdsp_utils' --strip-components 1
tar -xf %SOURCE13 -C 'modules/JUCE' --strip-components 1

%build
%cmake
%cmake_build -t ChowMatrix_LV2

%install
mkdir -p %buildroot%_libdir/lv2
cp -r %_cmake__builddir/ChowMatrix_artefacts/LV2/ChowMatrix.lv2 \
    %buildroot%_libdir/lv2
chmod 644 %buildroot%_libdir/lv2/*/*


%files -n lv2-%name-plugin
%_libdir/lv2/*
%doc README.md manual/ChowMatrixManual.pdf

%changelog
* Mon Jul 12 2021 Ivan A. Melnikov <iv@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
