Name: lxdm-conf
Version: 0.2.0
Release: alt5.1

Summary: Configuring Utility for LXDM
Summary(ru_RU.UTF-8): Утилита для конфигурирования менеджера дисплея LXDM

License: GPLv3
Group: System/Configuration/Other
Url: https://noc.sidux.com/lxde/browser/lxdm-conf
Packager: LXDE Development Team <lxde@packages.altlinux.org>
BuildArch: noarch

Source0: %name-%version.tar.bz2
Source1: lxdmconf.desktop
Source2: lxdmconfrun_a
Source3: lxdmconfrun_p

Requires: lxde-lxdm python-base

%description
lxdm config file editor  python program to allow easy editing of the
lxdm configuration file


%description -l ru_RU.UTF-8
Это программа на языке Python позволяющая легко конфигурировать
менеджер дисплеев LXDM. Выбор темы, фонового рисунка, управление
автологином, включение NumLock и т.д.

%prep
%setup

%install
mkdir %buildroot
cp -R * %buildroot
mkdir -p %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_sysconfdir/security/console.apps
install -Dp -m0644 %SOURCE3 %buildroot%_sysconfdir/pam.d/lxdmconfrun
install -Dp -m0644 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/lxdmconfrun
install -Dp -m0644 %SOURCE1 %buildroot%_desktopdir/
cd %buildroot%_bindir
ln -s /usr/bin/consolehelper lxdmconfrun

%files
%_bindir/*
%_desktopdir/lxdmconf.desktop
%lang(de) %_datadir/locale/de/LC_MESSAGES/lxdmconf.moo
%lang(it) %_datadir/locale/it/LC_MESSAGES/lxdmconf.moo
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/lxdmconf.moo
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt5.1
- Rebuild with Python-2.7

* Sun Mar 13 2011 Radik Usupov <radik@altlinux.org> 0.2.0-alt5
- Build from sisyphus

* Tue Oct 12 2010 Slava Semushin <php-coder@altlinux.ru> 0.2.0-alt4.1
- NMU
- Fixed typo in russian Summary (Closes: #24271)
- Spec cleanup

* Sun Oct 03 2010 Radik Usupov <radik@altlinux.org> 0.2.0-alt4
- package is now noarch

* Thu Jun 10 2010 Radik Usupov <radik@altlinux.org> 0.2.0-alt3
- added icons
- changed Packager

* Wed Jun 02 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.0-alt2
- package only locale files, not dirs

* Wed Jun 02 2010 Radik Usupov <radik@altlinux.org> 0.2.0-alt1
- corrected version release for sisyphus

* Wed Jun 02 2010 Radik Usupov <radik@altlinux.org> 3.8.4-alt0.3
- corrected packager
- corrected GROUP parameters

* Wed May 26 2010 Anatoly Chernov <aichernov@umail.ru> 3.8.4-alt0.2
- Rebuilt with branch 5.1 for antique - linux.

* Wed May 26 2010 YYY <http://forum.altlinux.org/index.php?action=profile;u=2784> 3.8.4-alt0.1
- First built for antique - linux.


