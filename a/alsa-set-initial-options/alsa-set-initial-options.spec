Name: alsa-set-initial-options
Version: 1.3
Release: alt1

Summary: Initial setup of alsa options
License: GPL
Group: Sound
Url: http://altlinux.ru/

Provides: alsa-set-initial-mixer = %version-%release
Obsoletes: alsa-set-initial-mixer < %version-%release

BuildArch: noarch

Source0: alsa-set-initial-options

%description
Initial setup of alsa options and volumes at first system start


%install
install -m 0755 -D %SOURCE0 %buildroot/%_sysconfdir/firsttime.d/%name


%files
%_sysconfdir/firsttime.d/*


%changelog
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
