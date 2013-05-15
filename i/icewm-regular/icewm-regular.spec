Name:    icewm-regular
Version: 1.0
Release: alt1

Group: Graphical desktop/Icewm
Summary: IceWM common collection
URL: http://www.icewm.org/
License: GPL

BuildArch: noarch

Requires: fonts-ttf-dejavu
Requires: fonts-ttf-droid

Requires: sysklogd
Requires: SysVinit-usermode
Requires: fdisk

Requires: deepsolver
Requires: deepsolver-repo

Requires: mutt
Requires: elinks

Requires: icewm-startup-xxkb-tray
Requires: icewm-startup-tray_mixer_plus
Requires: icewm-startup-grun
Requires: design-icewm-themes

Requires: leafpad
Requires: gqview
Requires: screengrab
Requires: htop
Requires: scrot
Requires: ucview
Requires: mplayer-gui

Requires: rp-pppoe-gui

Source: .gear-rules

%description
IceWM collection package to easy select packages during install
%description -l ru_RU.UTF-8
Сборный пакет на основе IceWM, облегчающий выбор пакетов при установке

%files

%changelog
* Wed May 15 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt1
- initial build (based on kde4-regular.spec)
