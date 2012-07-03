Name: pavucontrol
Version: 1.0
Release: alt1

Summary: PulseAudio Volume Control
Group: Sound
License: GPL
Url: http://pulseaudio.org

Source: %name-%version.tar

Requires: pulseaudio-daemon >= 1.0

BuildRequires: gcc-c++ intltool libcanberra-gtk2-devel libglademm-devel libpulseaudio-devel lynx
#BuildRequires: gcc-c++ intltool libcanberra-gtk3-devel libgtkmm3-devel libsigc++2-devel libpulseaudio-devel lynx

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume
control tool ("mixer") for the Polypaudio sound server. In
contrast to classic mixer tools this one allows you to control both
the volume of hardware devices and of each playback stream seperately.

%prep
%setup

%build
%autoreconf
%configure --disable-gtk3
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_datadir/pavucontrol/
%_datadir/pavucontrol/pavucontrol.glade
%_datadir/applications/pavucontrol.desktop
%doc README doc/README.html doc/style.css

%changelog
* Fri Dec 16 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- 1.0 released

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.10-alt2
- fix requires, build requires

* Sun Dec 05 2010 Radik Usupov <radik@altlinux.org> 0.9.10-alt0.M51.1
- build from branch 5.1

* Thu Jan 21 2010 Sergey Alembekov <rt@altlinux.ru> 0.9.10-alt1
- 0.9.8 > 0.9.10 

* Thu Apr 30 2009 Sergey Alembekov <rt@altlinux.ru> 0.9.8-alt1
- 0.9.7 > 0.9.8

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.7-alt1
- 0.9.6 -> 0.9.7
- buildreq

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt2
- fix desktop file

* Fri Apr 04 2008 Igor Zubkov <icesik@altlinux.org> 0.9.6-alt1
- 0.9.5 -> 0.9.6

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- 0.9.4 -> 0.9.5
- buildreq

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- 0.9.2 -> 0.9.4
- buildreq

* Sat Jul 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Mon May 29 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.0-alt1
- 0.9.0
- add url
- add docs

* Sat Apr 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt1
- Initial build for Sisyphus
