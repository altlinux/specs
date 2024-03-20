Name: pianobooster
Version: 1.0.0
Release: alt1

Summary: Boost your Piano playing skills
License: GPLv2
Group: Sound
Url: https://github.com/pianobooster/PianoBooster

Requires: fluid-soundfont-gm
Requires: fonts-ttf-dejavu
Requires: unzip

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(ftgl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)

%description
PianoBooster is a MIDI file player that displays the musical notes and
teaches you how to play the piano.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI piano keyboard.
You can play along to any track in the MIDI file and Piano Booster will
follow your playing.

%prep
%setup

%build
%cmake  -DDATA_DIR=share/pianobooster \
        -DQT_PACKAGE_NAME=Qt6 \
        -DUSE_SYSTEM_FONT=ON \
        -DWITH_MAN=ON
%cmake_build

%install
%cmake_install

%define _customdocdir %_docdir/pianobooster

%files
%doc %_customdocdir
%_bindir/pianobooster
%_datadir/pianobooster
%_desktopdir/*desktop
%_iconsdir/*/*/*/*.png
%_man6dir/pianobooster.*

%changelog
* Wed Mar 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- initial
