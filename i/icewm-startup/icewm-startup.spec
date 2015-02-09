%def_without xtdesktop
%def_without desklaunch
Name: icewm-startup
Version: 0.14
Release: alt3

Summary: simple pluggable IceWM autostart manager

Summary(ru_RU.UTF-8): менеджер автозапуска программ IceWM
License: GPL
Group: Graphical desktop/Icewm
Url: http://www.imath.kiev.ua/~vlasenko/

Packager: Igor Vlasenko <viy@altlinux.ru>
#Source: %name-%version.tar.bz2
Source1: XXkb.conf

BuildArch: noarch
AutoReq: no

# uncomment if you want to backport prior to M30
#define icewmconfdir #_x11x11dir/icewm
#Requires: icewm
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
(если у него оно есть), запускать ivman, gkrellm, xxkb,
запускать рабочий стол (idesk, xtdesktop, desklaunch, kdesktop) и т. д.

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

%package kdesktop
Group: Graphical desktop/Icewm
Summary: kdesktop autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск kdesktop при старте IceWM
Requires: %name kdebase-wm
Conflicts: %name-idesk
AutoReq: no

%description kdesktop
kdesktop plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 kdesktop
kdesktop plug-in для менеджера автозапуска программ при старте IceWM.

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

%if_with xtdesktop
%package xtdesktop
Group: Graphical desktop/Icewm
Summary: xtdesktop autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xtdesktop при старте IceWM
Requires: %name xtdesktop
AutoReq: no
%endif #xtdesktop

%if_with xtdesktop
%description xtdesktop
xtdesktop plug-in for simple pluggable IceWM autostart manager.
xtdesktop is only launched for users that have ~/.xtdeskrc.
%description -l ru_RU.UTF-8 xtdesktop
xtdesktop plug-in для менеджера автозапуска программ IceWM.
Плагин запускает xtdesktop только при наличии ~/.xtdeskrc.
%endif #xtdesktop

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

%package networkmanager
Group: Graphical desktop/Icewm
Summary: start gnome networkmanager applet
Requires: %name NetworkManager-gnome polkit-gnome
AutoReq: no

%description networkmanager
networkmanager plug-in for simple network configuration.
Start gnome networkmanager applet into tray.

%package tray_mixer_plus
Group: Graphical desktop/Icewm
Summary: start simple tray sound volume control
Requires: %name tray_mixer_plus
AutoReq: no

%description tray_mixer_plus
tray_mixer_plus plug-in for simple sound volume control.

%package grun
Group: Graphical desktop/Icewm
Summary: setup Run dialog
Requires: %name grun
AutoReq: no

%description grun
grun plug-in for setup dialog of launching applications in console mode.

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
%__mkdir_p %buildroot/%icewmconfdir/startup.d
cat <<'EOF' > %buildroot/%icewmconfdir/startup
#!/bin/sh

# delay before starting programs, to eliminate possible artifacts
tmem=`free -m | awk '/Mem/{print $2}'`
    if [ $tmem -le 512 ]
	then delay=7
    elif [ $tmem -gt 1024 ]
	then delay=3
    else delay=5
    fi
sleep $delay
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

echo 'xtoolwait gkrellm'> %buildroot/%icewmconfdir/startup.d/gkrellm
echo 'kdesktop&'> %buildroot/%icewmconfdir/startup.d/kdesktop
echo 'ivman&'> %buildroot/%icewmconfdir/startup.d/ivman

cat <<EOF > %buildroot/%icewmconfdir/startup.d/idesk
#!/bin/sh
if [ -e ~/.ideskrc ]; then 
  idesk &
else # first run
  startidesk &
fi
EOF

install -pD -m 644 %SOURCE1 %buildroot/%icewmconfdir/XXkb.conf
cat <<EOF > %buildroot/%icewmconfdir/startup.d/xxkb
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

install -pD -m 644 %SOURCE1 %buildroot/%icewmconfdir/XXkb.conf
cp %buildroot/%icewmconfdir/startup.d/xxkb %buildroot/%icewmconfdir/startup.d/xxkb-tray

%if_with desklaunch
cat <<EOF > %buildroot/%icewmconfdir/startup.d/desklaunch
#!/bin/sh
# it is not wise to run non-configured desklaunch, so we look 
# whether it is configured.
# if [ -e ~/.desklaunchrc ] then user has configured desklaunch properly
if [ -e ~/.desklaunchrc ]; then
  desklaunch&
fi
EOF
%endif #desklaunch

%if_with xtdesktop
cat <<EOF > %buildroot/%icewmconfdir/startup.d/xtdesktop
#!/bin/sh
# it is not wise to run non-configured xtdesktop, so we look 
# whether it is configured.
# if [ -e ~/.xtdeskrc ] then user has configured xtdesktop properly
if [ -e ~/.xtdeskrc ]; then
  xtdesktop&
fi
EOF
%endif #xtdesktop

cat <<EOF > %buildroot/%icewmconfdir/startup.d/update-menus
#!/bin/sh
# if user has no local menu we will not create it either.
# otherwise it is worth updating it.
if [ -e ~/.icewm/menu ]; then
  update-menus&
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/networkmanager
#!/bin/sh
/usr/libexec/polkit-1/polkit-gnome-authentication-agent-1&
/usr/bin/nm-applet&
EOF

echo "tray_mixer_plus&" > %buildroot/%icewmconfdir/startup.d/tray_mixer_plus

chmod 755 %buildroot/%icewmconfdir/startup.d/*
chmod 755 %buildroot/%icewmconfdir/startup

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
#%_man1dir/*

%if_with desklaunch
%files desklaunch
%config %icewmconfdir/startup.d/desklaunch
%endif #desklaunch

%files gkrellm
%config %icewmconfdir/startup.d/gkrellm

%files idesk
%config %icewmconfdir/startup.d/idesk

%files ivman
%config %icewmconfdir/startup.d/ivman

%files kdesktop
%config %icewmconfdir/startup.d/kdesktop

%files update-menus
%config %icewmconfdir/startup.d/update-menus

%if_with xtdesktop
%files xtdesktop
%config %icewmconfdir/startup.d/xtdesktop
%endif #xtdesktop

%files xxkb
%config %icewmconfdir/startup.d/xxkb

%files xxkb-tray
%config %icewmconfdir/startup.d/xxkb-tray
%icewmconfdir/XXkb.conf

%files networkmanager
%config %icewmconfdir/startup.d/networkmanager

%files tray_mixer_plus
%config %icewmconfdir/startup.d/tray_mixer_plus

%files grun

%changelog
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
