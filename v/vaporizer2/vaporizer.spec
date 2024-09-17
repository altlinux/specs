Name: vaporizer2
Version: 3.5.0
Release: alt1

Summary: Hybrid wavetable additive/subtractive synthesizer
License: GPLv3
Group: Sound
Url: https://github.com/VASTDynamics/Vaporizer2

Requires: vaporizer2-common = %version-%release

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(glx)
BuildRequires: /usr/bin/convert

%package common
Summary: Common data for Vaporizer2 synthesizer
Group: Sound
BuildArch: noarch

%package -n lv2-vaporizer2-plugin
Summary: Vaporizer2 synthesizer as LV2 plugin
Group: Sound
Requires: vaporizer2-common = %version-%release

%package -n vst3-vaporizer2-plugin
Summary: Vaporizer2 synthesizer as VST3 plugin
Group: Sound
Requires: vaporizer2-common = %version-%release

%description
%summary

%description common
Common data for Vaporizer2 synthesizer.

%description -n lv2-vaporizer2-plugin
Vaporizer2 synthesizer as LV2 plugin.

%description -n vst3-vaporizer2-plugin
Vaporizer2 synthesizer as VST3 plugin.

%prep
%setup
tar ixf %SOURCE1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/vaporizer2.desktop << 'E_O_F'
[Desktop Entry]
Name=Vaporizer2
GenericName=Hybrid Synthesizer
Exec=VASTvaporizer2
Icon=vaporizer2
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Midi;
E_O_F

f=VASTvaporizer/InstallerFiles/logokreisvdalpha.png
for sz in 16x16 32x32 48x48; do
    d=%buildroot%_iconsdir/hicolor/$sz/apps; mkdir -p $d
    convert $f -resize $sz $d/vaporizer2.png
done

%files
%doc LICENSE* README*
%_bindir/VASTvaporizer2
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png

%files common
%_datadir/Vaporizer2

%files -n lv2-vaporizer2-plugin
%_libdir/lv2/*

%files -n vst3-vaporizer2-plugin
%_libdir/vst3/*

%changelog
* Tue Sep 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.0-alt1
- 3.5.0 released

