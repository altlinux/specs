Name: bespokesynth
Version: 1.3.0
Release: alt1

Summary: A modular synthesizer
License: GPLv3
Group: Sound
Url: https://www.bespokesynth.com/
VCS: https://github.com/BespokeSynth/BespokeSynth

Source0: %name-%version.tar
Source1: deps-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

%description
Modular synth, featuring live-patchable environment,
LV2/VST3 hosting, MIDI & OSC controller mapping and
Python livecoding.

%prep
%setup -a1
sed -ri '/^int main/ i#pragma GCC diagnostic ignored "-Wreturn-type"' \
    libs/JUCE/extras/Build/juceaide/Main.cpp

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/BespokeSynth
%_datadir/BespokeSynth
%_datadir/metainfo/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Thu Jul 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released
