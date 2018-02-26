Name: sound_handler
Version: 0.6.0
Release: alt1

Summary: Scripts for sound wrapping
Group: Sound
License: GPL
BuildArch: noarch

Requires: /usr/bin/play /usr/bin/sox libsox-fmt-oss libsox-fmt-alsa libsox-fmt-sndfile libsox-fmt-vorbis
Requires: /usr/bin/aoss
AutoReqProv: yes, noshell

Source0: sound_wrapper.sh
Source1: play_wrapper.sh

%description
Scripts for sound wrapping via pulseaudio or artsd or esd

%install
mkdir -p %buildroot/%_bindir
install -pm755 %SOURCE0 %buildroot/%_bindir/sound_wrapper
ln -s sound_wrapper %buildroot/%_bindir/sound_wrapper.sh
install -pm755 %SOURCE1 %buildroot/%_bindir/play_wrapper
ln -s play_wrapper %buildroot/%_bindir/play_wrapper.sh

%files
%_bindir/*

%changelog
* Mon Apr 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- remove arts support

* Thu Aug 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- check utility available before execution (ALT#26115)

* Fri Dec 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- export PULSE_PROP to allow change volume with pulseaudio
- provide programs without .sh extension
- update package description

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt2
- add basic libsox-fmt-* to requires

* Fri Sep 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.3-alt1
- Cleaned up wrappers, reenabled automatic package dependencies.

* Tue Jul 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- fix check for pulseaudio (ALT#20690)

* Fri Oct 24 2008 Sergey V Turchin <zerg at altlinux dot org> 0.3.1-alt1
- fix to check arguments (#17665)

* Wed Sep 10 2008 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- don't use aplay
- add pulseaudio support

* Thu Jun 30 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- use aplay and aoss when alsa detected

* Wed Jun 30 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- decrease volume for raw play

* Fri May 21 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- initial spec

