Name:    icewm-regular
Version: 1.2
Release: alt1

Group: Graphical desktop/Icewm
Summary: IceWM common collection
URL: http://www.icewm.org/
License: GPL

BuildArch: noarch

Requires: icewm
Requires: xinit

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-droid

Requires: SysVinit-usermode
Requires: fdisk

Requires: mutt
Requires: elinks

Requires: icewm-startup-xxkb-tray
Requires: icewm-startup-tray_mixer_plus
Requires: icewm-startup-grun
Requires: design-icewm-themes
Requires: icewm-theme-darkt
Requires: icewm-theme-silverxp

Requires: leafpad
Requires: gqview
Requires: screengrab
Requires: htop
Requires: scrot
Requires: ucview
Requires: mplayer

Requires: rp-pppoe-gui

Source: .gear-rules

%description
IceWM collection package to easy select packages during install

%description -l ru_RU.UTF-8
Сборный пакет на основе IceWM, облегчающий выбор пакетов при установке

%files

%changelog
* Tue Dec 23 2014 Dmitriy Khanzhin <jinn@altlinux.org> 1.2-alt1
- removed requires: sysklogd

* Thu Nov 20 2014 Dmitriy Khanzhin <jinn@altlinux.org> 1.1-alt1
- added requires: xinit, icewm-theme-darkt, icewm-theme-silverxp
- removed requires: deepsolver

* Wed May 15 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt1
- initial build (based on kde4-regular.spec)
