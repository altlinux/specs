Name: qtractor
Version: 0.5.0.44
Release: alt1
License: GPLv2+
Url: http://qtractor.sourceforge.net/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: dssi-devel gcc-c++ glibc-devel-static ladspa_sdk
BuildRequires: libalsa-devel libgtk+2-devel libjack-devel liblo-devel
BuildRequires: libmad-devel libqt4-xml rasqal-devel librubberband-devel
BuildRequires: libsamplerate-devel libslv2-devel libsndfile-devel
BuildRequires: libvorbis-devel lv2core phonon-devel

Summary: An Audio/MIDI multi-track sequencer
Group: Sound

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup

%build
autoconf
autoheader
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README README.VST TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/32x32/apps/%name.png

%changelog
* Mon Sep 12 2011 Egor Glukhov <kaman@altlinux.org> 0.5.0.44-alt1
- fixed build
- 0.5.0.44

* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.4.9-alt1
- 0.4.9

* Sun Feb 13 2011 Egor Glukhov <kaman@altlinux.org> 0.4.8.18-alt1
- 0.4.8.18

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 0.4.6-alt1
- initial build for Sisyphus
