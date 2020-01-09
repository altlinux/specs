
%define _unpackaged_files_terminate_build 1

Name: a2jmidid
Version: 9
Release: alt1.git9f87918

Summary: ALSA sequencer to JACK MIDI bridging
License: GPL-2.0
Group:   Sound
URL:     https://github.com/linuxaudio/a2jmidid

BuildRequires(pre): meson
BuildRequires: libjack-devel libalsa-devel libdbus-devel

Source:  %name-%version-%release.tar

%description
a2jmidid aims to ease the usage of legacy, non JACK
enabled applications, in a JACK MIDI enabled system,
when using JACK 2. It can also bridge hardware ports.

%prep
%setup -n %name-%version-%release

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/*
%_datadir/dbus-1/services/org.gna.home.a2jmidid.service
%doc %_man1dir/*

%changelog
* Thu Jan 09 2020 Ivan A. Melnikov <iv@altlinux.org> 9-alt1.git9f87918
- initial build
