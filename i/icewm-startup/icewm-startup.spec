%def_without xtdesktop
%def_without desklaunch
Name: icewm-startup
Version: 0.11
Release: alt3

Summary: simple pluggable IceWM autostart manager

Summary(ru_RU.CP1251): менеджер автозапуска программ IceWM
License: GPL
Group: Graphical desktop/Icewm
Url: http://www.imath.kiev.ua/~vlasenko/

Packager: Igor Vlasenko <viy@altlinux.ru>
#Source: %name-%version.tar.bz2

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

%description -l ru_RU.CP1251
менеджер автозапуска программ IceWM
позвол€ет путем установки rpm расширений просто настраивать 
рабочий стол IceWM по умолчанию сразу дл€ всех пользователей, 
сохран€€ за пользовател€ми полную свободу персональной настройки
автозапуска.

»меющиес€ модули позвол€ют при старте icewm обновл€ть локальное меню пользовател€
(если у него оно есть), запускать ivman, gkrellm, xxkb,
запускать рабочий стол (idesk, xtdesktop, desklaunch, kdesktop) и т. д.

%package gkrellm
Group: Graphical desktop/Icewm
Summary: gkrellm autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск gkrellm при старте IceWM
# xtoolwait is required because icewm is not launched yet
Requires: %name gkrellm xtoolwait
AutoReq: no

%description gkrellm
gkrellm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.CP1251 gkrellm
запуск gkrellm при старте IceWM
(“ребует менеджер автозапуска программ IceWM).

%package idesk
Group: Graphical desktop/Icewm
Summary: idesk autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск idesk при старте IceWM
Requires: %name idesk
Conflicts: %name-kdesktop
AutoReq: no

%description idesk
idesk plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.CP1251 idesk
idesk plug-in дл€ менеджера автозапуска программ при старте IceWM.

%package kdesktop
Group: Graphical desktop/Icewm
Summary: kdesktop autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск kdesktop при старте IceWM
Requires: %name kdebase-wm
Conflicts: %name-idesk
AutoReq: no

%description kdesktop
kdesktop plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.CP1251 kdesktop
kdesktop plug-in дл€ менеджера автозапуска программ при старте IceWM.

%package xxkb
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no

%description xxkb
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
%description -l ru_RU.CP1251 xxkb
xxkb plug-in дл€ менеджера автозапуска программ при старте IceWM.
ѕлагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.

%if_with desklaunch
%package desklaunch
Group: Graphical desktop/Icewm
Summary: desklaunch autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск desklaunch при старте IceWM
Requires: %name desklaunch
AutoReq: no
%endif #desklaunch

%if_with desklaunch
%description desklaunch
desklaunch plug-in for simple pluggable IceWM autostart manager.
desklaunch is only launched for users that have ~/.desklaunchrc.
%description -l ru_RU.CP1251 desklaunch
desklaunch plug-in дл€ менеджера автозапуска программ IceWM.
ѕлагин запускает desklaunch только при наличии ~/.desklaunchrc.
%endif #desklaunch

%if_with xtdesktop
%package xtdesktop
Group: Graphical desktop/Icewm
Summary: xtdesktop autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск xtdesktop при старте IceWM
Requires: %name xtdesktop
AutoReq: no
%endif #xtdesktop

%if_with xtdesktop
%description xtdesktop
xtdesktop plug-in for simple pluggable IceWM autostart manager.
xtdesktop is only launched for users that have ~/.xtdeskrc.
%description -l ru_RU.CP1251 xtdesktop
xtdesktop plug-in дл€ менеджера автозапуска программ IceWM.
ѕлагин запускает xtdesktop только при наличии ~/.xtdeskrc.
%endif #xtdesktop

%package ivman
Group: Graphical desktop/Icewm
Summary: ivman autostart at IceWM startup
Summary(ru_RU.CP1251): автозапуск ivman при старте IceWM
Requires: %name ivman
AutoReq: no

%description ivman
ivman plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.CP1251 ivman
ivman plug-in дл€ менеджера автозапуска программ IceWM.

%package update-menus
Group: Graphical desktop/Icewm
Summary: autoupdate of user menu at IceWM startup
Summary(ru_RU.CP1251): автообновление меню пользовател€ при старте IceWM (при необходимости)
Requires: %name menu
AutoReq: no

%description update-menus
update-menus plug-in for simple pluggable IceWM autostart manager.
Does autoupdate of user menu at IceWM startup. (~/.icewm/menu).

%description -l ru_RU.CP1251 update-menus
update-menus plug-in дл€ менеджера автозапуска программ IceWM.
автообновление меню пользовател€ при старте IceWM. 
јвтообновление запускаетс€ только если пользователь 
не пользуетс€ общесистемным меню, а предпочитает 
локальное меню из ~/.icewm/menu.

%prep
%setup -q -c -T

%build

cat > README.ru_RU.CP1251 <<EOF



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
echo 'artsd&'> %buildroot/%icewmconfdir/startup.d/arts

cat <<EOF > %buildroot/%icewmconfdir/startup.d/idesk
#!/bin/sh
if [ -e ~/.ideskrc ]; then 
  idesk &
else # first run
  startidesk &
fi
EOF

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

cat <<EOF > %buildroot/%icewmconfdir/startup.d/desklaunch
#!/bin/sh
# it is not wise to run non-configured desklaunch, so we look 
# whether it is configured.
# if [ -e ~/.desklaunchrc ] then user has configured desklaunch properly
if [ -e ~/.desklaunchrc ]; then
  desklaunch&
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/xtdesktop
#!/bin/sh
# it is not wise to run non-configured xtdesktop, so we look 
# whether it is configured.
# if [ -e ~/.xtdeskrc ] then user has configured xtdesktop properly
if [ -e ~/.xtdeskrc ]; then
  xtdesktop&
fi
EOF

cat <<EOF > %buildroot/%icewmconfdir/startup.d/update-menus
#!/bin/sh
# if user has no local menu we will not create it either.
# otherwise it is worth updating it.
if [ -e ~/.icewm/menu ]; then
  update-menus&
fi
EOF

chmod 755 %buildroot/%icewmconfdir/startup.d/*
chmod 755 %buildroot/%icewmconfdir/startup

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

%changelog
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
