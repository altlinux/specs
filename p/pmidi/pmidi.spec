Name: pmidi
Version: 1.6.0
Release: alt1

Summary: A MIDI sound file player.
Group: Sound
License: GPL
Url: http://pmidi.sourceforge.net
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2

%define alsa_ver 0.9.0rc6

Requires: libalsa >= %alsa_ver
BuildPreReq: libalsa-devel >= %alsa_ver

# Automatically added by buildreq on Sun Dec 21 2003
BuildRequires: glib-devel hostinfo libalsa-devel

%description
pmidi is a command line midi player for ALSA. It can play to any MIDI
device that is supported by ALSA. Most external MIDI ports are
supported. The sfxload program included with the awesfx is required to
load a sound font first to using the internal synthesizer on a SB Live!
or SB AWE32/64.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sun Dec 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sat Dec 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.5.5-alt1
- new version for newest alsa.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt2
- Rebuild with gcc-3.2. 

* Fri May 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt1
- First build for Sisyphus.
