Name: alsa-set-initial-options
Version: 1.4
Release: alt1

Summary: Initial setup of ALSA options
License: GPL
Group: Sound

Url: http://altlinux.org
Source: alsa-set-initial-options
BuildArch: noarch

%description
Initial setup of ALSA options and mixer volumes at first system startup.


%install
install -m 0755 -D %SOURCE0 %buildroot/%_sysconfdir/firsttime.d/%name


%files
%_sysconfdir/firsttime.d/*


%changelog
* Thu Feb 15 2024 Michael Shigorin <mike@altlinux.org> 1.4-alt1
- refactor script for reliability and performance
- minor spec cleanup (see also ALT#46206)

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- execute `alsactl init` first

* Fri Aug 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- modprobe snd-seq-midi instantly if alsa found

* Thu Aug 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- setup of loading snd-seq-midi kernel module

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M51.1
- built for M51

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
