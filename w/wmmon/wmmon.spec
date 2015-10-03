# vim: set ft=spec: -*- rpm-spec -*-
# $Id: wmmon,v 1.1 2005/02/15 21:03:39 raorn Exp $

Name: wmmon
Version: 1.0b2
Release: alt5

Summary: Nice system monitor for WindowMaker
Group: Graphical desktop/Window Maker
License: GPL

Url: http://repo.or.cz/w/dockapps.git
Source0: %name-%version.tar.gz
Source1: %name.menu
Patch: %name-1.0b2-deb-fixes.patch
Packager: Sir Raorn <raorn@altlinux.ru>

# Automatically added by buildreq on Tue Feb 15 2005
BuildRequires: libXt-devel libXext-devel libXpm-devel

%description
WMMon monitors the realtime CPU load as well the average
system load and gives you some nice additional features too...

WMMon currently provides:

 * Realtime CPU 'stress' meter;
 * Average systemload, like xload & wmavgload;
 * Average systemload graphic is autoscaling;
 * Realtime Disk I/O 'stress' meter;
 * Average Disk I/O load grapic (autoscaling);
 * Realtime total Mem & Swap usage meters;
 * System uptime display;
 * Realtime cycling through all monitor modes;
 * Can lauch 3 user definable commands through ~/.wmmonrc;
 * Can be started multiple times;
 * Commandline options for help (-h), version (-v),
   start mode (-i & -s) and display (-d);

%prep
%setup -n %name.app
%patch -p1
sed -i 's,cc ,cc -std=gnu89 ,' wmmon/Makefile

%build
cd %name
%make_build

%install
cd %name
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %SOURCE1 %buildroot%_menudir/%name
install -pDm644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc BUGS CHANGES COPYING HINTS INSTALL README TODO
%_bindir/%name
%_man1dir/%name.1*
%_menudir/%name

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 1.0b2-alt5
- gcc5 FTBFS workaround (-std=gnu89)
- moved to %_bindir
- added an Url:
- minor spec cleanup

* Tue Oct 15 2013 Michael Shigorin <mike@altlinux.org> 1.0b2-alt4
- fixed menu file to reference %_bindir/%name

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0b2-alt3.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * update_menus for wmmon
  * postclean-03-private-rpm-macros for the spec file

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 1.0b2-alt3.qa1
- Remove xorg-x11-devel build requires

* Tue Feb 15 2005 Sir Raorn <raorn@altlinux.ru> 1.0b2-alt3
- Updated to debian 1.0b2-14:
  * Add the ability to lock the mode, preventing cycling.  Thanks go to
    Chris Bechberger <bechberger@yahoo.com>.
  * Added a manual page.
  * Added the -geometry option.
  * Ensure that I/O mode works the same no matter how it is started.
  * Support new /proc/meminfo format in 2.6 kernels.
  * Fixed some buffer overflow problems.
  * Applied patch from Simon Fowler <simon@himi.org> to fix /proc/meminfo
    parsing for linux 2.5.
  * Applied patch from Frederik Schueler <fs@lowpingbastards.de>
    to fix /proc/stat parsing on linux 2.4
  * Patch from Salvador Pinto Abreu <spa@sc.uevora.pt>:
    Fixed behavior when APM causes the system to sleep/suspend.

* Mon Oct 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0b2-alt2
- rebuild with gcc3

* Mon Dec 03 2001 Sir Raorn <raorn@altlinux.ru> 1.0b2-alt1
- Built for Sisyphus

