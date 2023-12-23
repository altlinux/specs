%def_without xtdesktop
%def_without desklaunch
%def_without ivman
%def_without blueberry
Name: icewm-startup
Version: 0.215
Release: alt2

Summary: simple pluggable IceWM autostart manager

Summary(ru_RU.UTF-8): менеджер автозапуска программ IceWM
License: GPLv2+
Group: Graphical desktop/Icewm
Url: http://git.altlinux.org

Packager: Dmitriy Khanzhin <jinn@altlinux.org>
#Source: %name-%version.tar.bz2
Source1: XXkb.conf

BuildArch: noarch
AutoReq: no

%define icewmconfdir %_sysconfdir/X11/icewm
#due to new icewmconfdir in /etc/X11
Requires: icewm >= 1.2.25

%description
Simple pluggable icewm autostart manager is a generic IceWM startup script
which allows one to configure IceWM default autostart via installing corresponding rpm plug-ins.

%description -l ru_RU.UTF-8
менеджер автозапуска программ IceWM
позволяет путем установки rpm расширений просто настраивать
рабочий стол IceWM по умолчанию сразу для всех пользователей,
сохраняя за пользователями полную свободу персональной настройки
автозапуска.

Имеющиеся модули позволяют при старте icewm обновлять локальное меню пользователя
(если у него оно есть), запускать ivman, gkrellm, xxkb, mount-tray, WiFi manager,
запускать рабочий стол (idesk, kdesktop) и т. д.

%package apt-indicator
Group: Graphical desktop/Icewm
Summary: apt-indicator autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск apt-indicator при старте IceWM
Requires: %name apt-indicator
AutoReq: no

%description apt-indicator
apt-indicator plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 apt-indicator
запуск apt-indicator при старте IceWM
(Требует менеджер автозапуска программ IceWM).

%package at-spi-dbus-bus
Group: Graphical desktop/Icewm
Summary: at-spi autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск at-spi при старте IceWM
Requires: %name at-spi2-core
AutoReq: no

%description at-spi-dbus-bus
Launch at-spi bus at IceWM start.
at-spi bus is required for accessibility services.
%description -l ru_RU.UTF-8 at-spi-dbus-bus
запуск сервиса вспомогатальных технологий поддержки доступности
компьютерного интерфейса для людей с ограниченными возможностями
при старте IceWM (Требует менеджер автозапуска программ IceWM).

%if_with blueberry
%package blueberry-tray
Group: Graphical desktop/Icewm
Summary: blueberry-tray autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск blueberry-tray при старте IceWM
Requires: %name blueberry
AutoReq: no

%description blueberry-tray
blueberry is the Bluetooth devices graphical configuration utility.
This package provides blueberry-tray plug-in for IceWM autostart manager.

%description -l ru_RU.UTF-8 blueberry-tray
blueberry является графической утилитой для настройки и работы с Bluetooth устройствами.
Установите этот пакет, если вы хотите запускать blueberry-tray при старте IceWM.
%endif

%package delay
Group: Graphical desktop/Icewm
Summary: delay before starting programs
Summary(ru_RU.UTF-8): задержка запуска программ
Requires: %name
AutoReq: no

%description delay
delay before starting programs, to eliminate possible artifacts,
typically used to have time to start icewmtray.
%description -l ru_RU.UTF-8 delay
задержка перед запуском программ, чтобы устранить возможные артефакты,
обычно используется, чтобы успел стартовать icewmtray.

%if_with desklaunch
%package desklaunch
Group: Graphical desktop/Icewm
Summary: desklaunch autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск desklaunch при старте IceWM
Requires: %name desklaunch
AutoReq: no
%endif #desklaunch

%if_with desklaunch
%description desklaunch
desklaunch plug-in for simple pluggable IceWM autostart manager.
desklaunch is only launched for users that have ~/.desklaunchrc.
%description -l ru_RU.UTF-8 desklaunch
desklaunch plug-in для менеджера автозапуска программ IceWM.
Плагин запускает desklaunch только при наличии ~/.desklaunchrc.
%endif #desklaunch

%package gkrellm
Group: Graphical desktop/Icewm
Summary: gkrellm autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск gkrellm при старте IceWM
# xtoolwait is required because icewm is not launched yet
Requires: %name gkrellm xtoolwait
AutoReq: no

%description gkrellm
gkrellm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 gkrellm
запуск gkrellm при старте IceWM
(Требует менеджер автозапуска программ IceWM).

%package grun
Group: Graphical desktop/Icewm
Summary: setup Run dialog
Requires: %name grun
AutoReq: no

%description grun
grun plug-in for setup dialog of launching applications in console mode.

%package idesk
Group: Graphical desktop/Icewm
Summary: idesk autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск idesk при старте IceWM
Requires: %name idesk
Conflicts: %name-kdesktop
AutoReq: no

%description idesk
idesk plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 idesk
idesk plug-in для менеджера автозапуска программ при старте IceWM.

%if_with ivman
%package ivman
Group: Graphical desktop/Icewm
Summary: ivman autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск ivman при старте IceWM
Requires: %name ivman
AutoReq: no

%description ivman
ivman plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 ivman
ivman plug-in для менеджера автозапуска программ IceWM.
%endif

%package mount-tray
Group: Graphical desktop/Icewm
Summary: mount-tray autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск mount-tray при старте IceWM
Requires: %name mount-tray
AutoReq: no

%description mount-tray
mount-tray is a small Qt-based tray application for mount and unmount
removable devices like USB storage or CD and DVD-ROM. It used udisks
for mount and unmount operations, udev for device detection and DBus
for take information about external mounting and unmounting.

This package provides mount-tray plug-in for IceWM autostart manager.

%description -l ru_RU.UTF-8 mount-tray
mount-tray - это небольшой аплет для монтирования и размонтирования
извлекаемых устройств наподобие USB флешки, CD или DVD-ROM.

Установите этот пакет, если вы хотите запускать mount-tray при старте IceWM.

%package networkmanager
Group: Graphical desktop/Icewm
Summary: start gnome networkmanager applet
Requires: %name ModemManager NetworkManager-applet-gtk
Requires: NetworkManager-wifi usb-modeswitch
AutoReq: no

%description networkmanager
networkmanager plug-in for simple network configuration.
Start gnome networkmanager applet into tray.

%package notification-daemon
Group: Graphical desktop/Icewm
Summary: notification-daemon autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск notification-daemon при старте IceWM
Requires: %name
Requires: /usr/bin/nm-applet
Requires: /usr/libexec/polkit-1/polkit-gnome-authentication-agent-1
AutoReq: no

%description notification-daemon
notification-daemon provides a notification server according to Desktop Notifications Specification.
This package provides notification-daemon plug-in for IceWM autostart manager.

%description -l ru_RU.UTF-8 notification-daemon
notification-daemon используется для отображения уведомлений от других программ.
Установите этот пакет, если вы хотите запускать notification-daemon при старте IceWM.

%package pnmixer
Group: Graphical desktop/Icewm
Summary: pnmixer autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск pnmixer при старте IceWM
Requires: %name pnmixer
AutoReq: no

%description pnmixer
pnmixer plug-in for simple sound volume control.

%package polkit-gnome
Group: Graphical desktop/Icewm
Summary: polkit-gnome autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск polkit-gnome при старте IceWM
Requires: %name polkit-gnome
AutoReq: no

%description polkit-gnome
polkit-gnome plug-in for polkit authentication agent autostart.

%package redshift-gtk
Group: Graphical desktop/Icewm
Summary: redshift-gtk autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск redshift-gtk при старте IceWM
Requires: %name redshift
AutoReq: no

%description redshift-gtk
redshift-gtk plug-in for screen brightness control.
Redshift should be configured first in ~/.config/redshift.conf.

%package simple-sound
Group: Graphical desktop/Icewm
Summary: Startup and shutdown simple sound for IceWM
Summary(ru_RU.UTF-8): Простейшие звуки при старте и выключении IceWM
Requires: %name aplay
AutoReq: no

%description simple-sound
Startup and shutdown simple sound for IceWM.
%description -l ru_RU.UTF-8 simple-sound
Простейшие звуки при старте и выключении IceWM.

%package spacefm
Group: Graphical desktop/Icewm
Summary: spacefm autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск spacefm при старте IceWM
Requires: %name spacefm
AutoReq: no

%description spacefm
spacefm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 spacefm
spacefm plug-in для менеджера автозапуска программ IceWM.

%package tray_mixer_plus
Group: Graphical desktop/Icewm
Summary: start simple tray sound volume control
Requires: %name tray_mixer_plus
AutoReq: no

%description tray_mixer_plus
tray_mixer_plus plug-in for simple sound volume control.

%package update-menus
Group: Graphical desktop/Icewm
Summary: autoupdate of user menu at IceWM startup
Summary(ru_RU.UTF-8): автообновление меню пользователя при старте IceWM (при необходимости)
Requires: %name menu
AutoReq: no

%description update-menus
update-menus plug-in for simple pluggable IceWM autostart manager.
Does autoupdate of user menu at IceWM startup. (~/.icewm/menu).

%description -l ru_RU.UTF-8 update-menus
update-menus plug-in для менеджера автозапуска программ IceWM.
автообновление меню пользователя при старте IceWM.
Автообновление запускается только если пользователь
не пользуется общесистемным меню, а предпочитает
локальное меню из ~/.icewm/menu.

%if_with xtdesktop
%package xtdesktop
Group: Graphical desktop/Icewm
Summary: xtdesktop autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xtdesktop при старте IceWM
Requires: %name xtdesktop
AutoReq: no
%endif #xtdesktop

%package xscreensaver
Group: Graphical desktop/Icewm
Summary: add xscreensaver to icewm session
Summary(ru_RU.UTF-8): Включение хранителя экрана xscreensaver для IceWM
Requires: %name xscreensaver
AutoReq: no

%description xscreensaver
xscreensaver plug-in for icewm startup.
%description -l ru_RU.UTF-8 xscreensaver
Включение хранителя экрана xscreensaver для IceWM.

%if_with xtdesktop
%description xtdesktop
xtdesktop plug-in for simple pluggable IceWM autostart manager.
xtdesktop is only launched for users that have ~/.xtdeskrc.
%description -l ru_RU.UTF-8 xtdesktop
xtdesktop plug-in для менеджера автозапуска программ IceWM.
Плагин запускает xtdesktop только при наличии ~/.xtdeskrc.
%endif #xtdesktop

%package xxkb
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb-tray

%description xxkb
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
%description -l ru_RU.UTF-8 xxkb
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или
/etc/X11/app-defaults/XXkb.

%package xxkb-tray
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb

%description xxkb-tray
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
When you install package the file /etc/X11/app-defaults/XXkb
will be overwritten, and after removing returned to the old file.
%description -l ru_RU.UTF-8 xxkb-tray
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.
При установке пакета файл /etc/X11/app-defaults/XXkb будет
перезаписан, а после удаления возвращен старый файл.

%prep
%setup -q -c -T

%build

cat > README.ru_RU.UTF-8 <<EOF



~/.icewm/startup.d

# starting all system-wide icewm autostart programs
for file in %icewmconfdir/startup.d/*; do
  userfile=~/.icewm/startup.d/`echo $file | sed -e 's,%icewmconfdir/startup.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program
    # by touching file in ~/.icewm/startup.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs
for file in ~/.icewm/startup.d/*; do
  # running user files
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done


EOF



%install

# Startup

mkdir -p %buildroot/%icewmconfdir/startup.d
cat <<'EOF' > %buildroot/%icewmconfdir/startup
#!/bin/sh

# starting all system-wide icewm autostart programs
for file in %icewmconfdir/startup.d/*; do
  userfile=~/.icewm/startup.d/`echo $file | sed -e 's,%icewmconfdir/startup.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program
    # by touching file in ~/.icewm/startup.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs
for file in ~/.icewm/startup.d/*; do
  # running user files
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done
EOF

# Shutdown

mkdir -p %buildroot/%icewmconfdir/shutdown.d
cat <<'EOF' > %buildroot/%icewmconfdir/shutdown
#!/bin/sh

# starting all system-wide icewm autostart programs in shutdown time
for file in %icewmconfdir/shutdown.d/*; do
  userfile=~/.icewm/shutdown.d/`echo $file | sed -e 's,%icewmconfdir/shutdown.d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program
    # by touching file in ~/.icewm/shutdown.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs in shutdown time
for file in ~/.icewm/shutdown.d/*; do
  # running user files
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/001-update-menus
#!/bin/sh
# if user has no local menu we will not create it either.
# otherwise it is worth updating it.
if [ -e ~/.icewm/menu ]; then
  update-menus&
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/000-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/startup.wav ]; then
    aplay ~/.icewm/sounds/startup.wav 2&> /dev/null&
else
    if [ -e /usr/share/X11/icewm/sounds/startup.wav ]; then
    aplay /usr/share/X11/icewm/sounds/startup.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/shutdown.d/000-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/shutdown.wav ]; then
    aplay ~/.icewm/sounds/shutdown.wav 2&> /dev/null&
else
    if [ -e /usr/share/X11/icewm/sounds/shutdown.wav ]; then
    aplay /usr/share/X11/icewm/sounds/shutdown.wav 2&> /dev/null&
    fi
fi
EOF

cat <<'EOF' > %buildroot/%icewmconfdir/startup.d/010-delay
#!/bin/sh

# delay before starting programs, to eliminate possible artifacts
# name index 010- to save ability to run programs before this
tmem=`free -m | awk '/Mem/{print $2}'`
    if [ $tmem -le 512 ]
	then delay=7
    elif [ $tmem -gt 1024 ]
	then delay=3
    else delay=5
    fi
sleep $delay
EOF

cat <<'EOF' > %buildroot/%icewmconfdir/startup.d/015-at-spi-dbus-bus
#!/bin/sh
# AT-SPI D-Bus Bus
/usr/libexec/at-spi-bus-launcher --launch-immediately&
EOF

# 20 is for desktop
cat <<EOF > %buildroot/%icewmconfdir/startup.d/020-idesk
#!/bin/sh
if [ -e ~/.ideskrc ]; then 
  idesk &
else # first run
  startidesk &
fi
EOF

# 60+ and w/o priority is for tray and other
install -pD -m 644 %SOURCE1 %buildroot/%icewmconfdir/XXkb.conf
cat <<EOF > %buildroot/%icewmconfdir/startup.d/060-xxkb
#!/bin/sh
# it is not wise to run non-configured xxkb, so we look 
# whether it is configured.
# if [ -e ~/.xxkbrc ] then user has configured xxkb properly
# if [ -e /etc/X11/app-defaults/XXkb ]
# then sysadmin has configured xxkb properly.

if [ -e ~/.xxkbrc ] || [ -e /etc/X11/app-defaults/XXkb ]; then
  xxkb&
fi
EOF
cp %buildroot/%icewmconfdir/startup.d/060-xxkb %buildroot/%icewmconfdir/startup.d/060-xxkb-tray

echo 'tray_mixer_plus&' > %buildroot/%icewmconfdir/startup.d/070-tray_mixer_plus
echo '/usr/bin/nm-applet&' > %buildroot/%icewmconfdir/startup.d/080-networkmanager

echo 'apt-indicator&'> %buildroot/%icewmconfdir/startup.d/apt-indicator
%if_with blueberry
echo 'blueberry-tray&'> %buildroot/%icewmconfdir/startup.d/blueberry-tray
%endif
echo 'xtoolwait gkrellm'> %buildroot/%icewmconfdir/startup.d/gkrellm
echo 'mount-tray&'> %buildroot/%icewmconfdir/startup.d/mount-tray
%if_with ivman
echo 'ivman&'> %buildroot/%icewmconfdir/startup.d/ivman
%endif
echo "/usr/libexec/notification-daemon&" > %buildroot/%icewmconfdir/startup.d/notification-daemon
echo "pnmixer&" > %buildroot/%icewmconfdir/startup.d/pnmixer
echo "/usr/libexec/polkit-1/polkit-gnome-authentication-agent-1&" > %buildroot/%icewmconfdir/startup.d/polkit-gnome
echo "spacefm --desktop&" > %buildroot/%icewmconfdir/startup.d/spacefm
echo 'xscreensaver -nosplash&'> %buildroot/%icewmconfdir/startup.d/xscreensaver

%define startup_if_config() \
cat <<EOF > %buildroot/%icewmconfdir/startup.d/%1\
#!/bin/sh\
# it is not wise to run non-configured %1, so we look\
# whether it is configured.\
# if [ -e %2 ] then user has configured %1 properly\
if [ -e %2 ]; then\
  %3\
fi\
EOF\
%nil

%startup_if_config redshift-gtk ~/.config/redshift.conf redshift-gtk&

%if_with desklaunch
%startup_if_config desklaunch ~/.desklaunchrc desklaunch&
%endif #desklaunch

%if_with xtdesktop
%startup_if_config xtdesktop ~/.xtdeskrc xtdesktop&
%endif #xtdesktop

chmod 755 %buildroot/%icewmconfdir/startup.d/*
chmod 755 %buildroot/%icewmconfdir/startup
chmod 755 %buildroot/%icewmconfdir/shutdown.d/*
chmod 755 %buildroot/%icewmconfdir/shutdown

%post xxkb-tray
if [ $1 -eq 1 ]; then
if [ -e /etc/X11/app-defaults/XXkb ]; then
cp -fp /etc/X11/app-defaults/XXkb %icewmconfdir/XXkb~
cp -fp %icewmconfdir/XXkb.conf /etc/X11/app-defaults/XXkb
fi
fi

%post grun
if [ $1 -eq 1 ]; then
echo "RunCommand=\"grun\"" >> %icewmconfdir/prefoverride
fi

%preun xxkb-tray
if [ $1 -eq 0 ]; then
if [ -e %icewmconfdir/XXkb~ ]; then
mv -f %icewmconfdir/XXkb~ /etc/X11/app-defaults/XXkb
else
rm -f /etc/X11/app-defaults/XXkb
fi
fi

%preun grun
if [ $1 -eq 0 ]; then
sed -i '/RunCommand=\"grun\"/d' %icewmconfdir/prefoverride
if [ "`wc -w %icewmconfdir/prefoverride | cut -d" " -f1`" == "0" ]; then
rm -f %icewmconfdir/prefoverride
fi
fi

%files
#%doc README
%dir %icewmconfdir/startup.d
%config %icewmconfdir/startup
%dir %icewmconfdir/shutdown.d
%config %icewmconfdir/shutdown
#%_man1dir/*

%files apt-indicator
%config %icewmconfdir/startup.d/apt-indicator

%files at-spi-dbus-bus
%config %icewmconfdir/startup.d/015-at-spi-dbus-bus

%if_with blueberry
%files blueberry-tray
%config %icewmconfdir/startup.d/blueberry-tray
%endif

%files delay
%config %icewmconfdir/startup.d/010-delay

%if_with desklaunch
%files desklaunch
%config %icewmconfdir/startup.d/desklaunch
%endif #desklaunch

%files gkrellm
%config %icewmconfdir/startup.d/gkrellm

%files grun

%files idesk
%config %icewmconfdir/startup.d/020-idesk

%if_with ivman
%files ivman
%config %icewmconfdir/startup.d/ivman
%endif

%files mount-tray
%config %icewmconfdir/startup.d/mount-tray

%files networkmanager
%config %icewmconfdir/startup.d/080-networkmanager

%files notification-daemon
%config %icewmconfdir/startup.d/notification-daemon

%files pnmixer
%config %icewmconfdir/startup.d/pnmixer

%files polkit-gnome
%config %icewmconfdir/startup.d/polkit-gnome

%files redshift-gtk
%config %icewmconfdir/startup.d/redshift-gtk

%files simple-sound
%config %icewmconfdir/startup.d/000-simple-sound
%config %icewmconfdir/shutdown.d/000-simple-sound

%files spacefm
%config %icewmconfdir/startup.d/spacefm

%files tray_mixer_plus
%config %icewmconfdir/startup.d/070-tray_mixer_plus

%files update-menus
%config %icewmconfdir/startup.d/001-update-menus

%files xscreensaver
%config %icewmconfdir/startup.d/xscreensaver

%if_with xtdesktop
%files xtdesktop
%config %icewmconfdir/startup.d/xtdesktop
%endif #xtdesktop

%files xxkb
%config %icewmconfdir/startup.d/060-xxkb

%files xxkb-tray
%config %icewmconfdir/startup.d/060-xxkb-tray
%icewmconfdir/XXkb.conf

%changelog
* Sat Dec 23 2023 Anton Midyukov <antohami@altlinux.org> 0.215-alt2
- NMU: disable build blueberry-tray

* Sun Dec 03 2023 Anton Midyukov <antohami@altlinux.org> 0.215-alt1
- added polkit-gnome

* Mon Nov 16 2020 Igor Vlasenko <viy@altlinux.ru> 0.214-alt1
- added blueberry-tray

* Sun Nov 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.213-alt1
- added redshift-gtk

* Fri Nov 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.212-alt1
- added xscreenserver; removed kde3kdesktop
- at-spi-dbus-bus changed from 020 to 015
- sorted subpackages
- updated license

* Sun Oct 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.211-alt1
- added launcher for AT-SPI D-Bus
- extended versions to 3 digits due to frequent updates

* Sat Sep 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- bugfix: launch nm-applet properly w/o polkit-gnome

* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3
- fixed requires for notification-daemon

* Sat Apr 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt2
- build without ivman subpackage

* Sat Mar 30 2019 Anton Midyukov <antohami@altlinux.org> 0.20-alt1
- added pnmixer

* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- fixed unpackaged files

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added spacefm (closes: 34794)

* Thu Sep 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- removed kdesktop

* Tue Nov 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- added notification-daemon

* Tue Oct 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- added apt-indicator

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- updated description

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt0.M70T.1
- backport for t7

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- conditional def_with networkmanager (t7 support)

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added mount-tray subpackage

* Sat Sep 26 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt2
- updated requires for networkmanager subpackage

* Sun May 31 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt1
- added "shutdown" script, thx to YYY at forum
- added simple-sound subpackage, thx to YYY and Leo-sp150 at forum
- delay moved to separate subpackage
- cosmetic fix of xxkb conf file
- some programs are assigned numeric indexes
- changed Url: and Packager:

* Mon Feb 09 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt3
- fixed typo in networkmanager subpackage

* Tue May 14 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt2
- delay before starting programs made customizable

* Wed Apr 10 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt1
- added grun subpackage

* Sat Mar 30 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.13-alt1
- added xxkb-tray subpackage
- added tray_mixer_plus subpackage
- spec converted to utf-8

* Thu Feb 28 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.12-alt1
- added delay before starting programs, to eliminate possible artifacts
- added networkmanager

* Wed Mar 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- removed artsd support (obsolete)

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- disabled unmet subpackages using nmu script

* Fri Sep 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- fixed requires in update-menus

* Thu Sep 20 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added arts, update-menus
- TODO: README

* Sat Sep 08 2007 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- added ivman, desklaunch and xtdesktop support

* Mon Apr 17 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt2
- added kdesktop support

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt1
- build for Sisyphus

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.M30.1
- backport for M30

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0
- initial build
