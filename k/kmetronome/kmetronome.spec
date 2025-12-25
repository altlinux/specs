%define _unpackaged_files_terminate_build 1

%def_without check

Name: kmetronome
Version: 1.4.1
Release: alt1

Summary: MIDI based metronome using the ALSA sequencer
License: GPL-2.0-or-later
Group: Sound
URL: https://kmetronome.sourceforge.io/kmetronome.shtml
Vcs: https://git.code.sf.net/p/kmetronome/git

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(drumstick-alsa)
BuildRequires: pkgconfig(alsa)
BuildRequires: pandoc

%description
KMetronome is a MIDI based metronome using the ALSA sequencer.

The intended audience are musicians and music students. Like the solid, real
metronomes it is a tool to keep the rhythm while playing musical instruments.

It uses MIDI for sound generation instead of digital audio, allowing low CPU
usage and very accurate timing thanks to the ALSA sequencer

%prep
%setup
sed -i "s/Categories=.*/Categories=AudioVideo;Audio;Midi;Music;/" net.sourceforge.kmetronome.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%check
%ctest

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS readme.md TODO
%_bindir/kmetronome
%_man1dir/kmetronome.1.xz
%_desktopdir/net.sourceforge.kmetronome.desktop
%exclude %_datadir/dbus-1/interfaces/net.sourceforge.kmetronome.xml
%_datadir/dbus-1/services/net.sourceforge.kmetronome.service
%_iconsdir/hicolor/*/apps/kmetronome.png
%_iconsdir/hicolor/scalable/apps/kmetronome.svgz
%dir %_datadir/kmetronome
%dir %_datadir/kmetronome/*
%_datadir/metainfo/net.sourceforge.kmetronome.metainfo.xml

%changelog
* Thu Dec 25 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
