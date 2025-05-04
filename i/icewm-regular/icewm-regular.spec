Name:    icewm-regular
Version: 1.3
Release: alt1

Group: Graphical desktop/Icewm
Summary: IceWM common collection
URL: https://www.altlinux.org/IceWM
License: GPLv2+

BuildArch: noarch

Requires: xinit
Requires: icewm

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-liberation

Requires: SysVinit-usermode
Requires: cfdisk

#Requires: mutt
Requires: elinks

Requires: icewm-themes
Requires: icewm-theme-darkt

Requires: icewm-startup-fbxkb
Requires: icewm-startup-grun
Requires: icewm-startup-mount-tray
Requires: icewm-startup-networkmanager
Requires: icewm-startup-notification-daemon
Requires: icewm-startup-pnmixer
Requires: qasmixer

Requires: gqview
Requires: htop
Requires: leafpad
Requires: mplayer
Requires: screengrab
Requires: scrot

Requires: altlinux-freedesktop-menu-generic

Source: .gear-rules

%description
IceWM collection package to easy select packages during install

%description -l ru_RU.UTF-8
Сборный пакет на основе IceWM, облегчающий выбор пакетов при установке

%files

%changelog
* Sun May 04 2025 Dmitriy Khanzhin <jinn@altlinux.org> 1.3-alt1
- updated the set of dependencies
- updated Url
- updated License

* Tue Dec 23 2014 Dmitriy Khanzhin <jinn@altlinux.org> 1.2-alt1
- removed requires: sysklogd

* Thu Nov 20 2014 Dmitriy Khanzhin <jinn@altlinux.org> 1.1-alt1
- added requires: xinit, icewm-theme-darkt, icewm-theme-silverxp
- removed requires: deepsolver

* Wed May 15 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt1
- initial build (based on kde4-regular.spec)
