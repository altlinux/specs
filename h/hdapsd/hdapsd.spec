Name: hdapsd
Version: 20090401
Release: alt1

Summary: HardDrive Active Protection System
License: GPL v2
Group: System/Kernel and hardware

Url: http://www.thinkwiki.org/wiki/How_to_protect_the_harddisk_through_APS
Source: hdapsd-20090401.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.udev
Packager: Michael Shigorin <mike@altlinux.org>

# relies on kernel hdaps driver, which depends on CONFIG_X86
ExclusiveArch: %ix86 x86_64

Summary(pl.UTF-8): HDAPS - system aktywnej ochrony dysku twardego

%description
HardDrive Active Protection System.

The APS is a protection system for the ThinkPads internal harddrive. A
sensor inside the ThinkPad recognizes when the notebook is
accelerated. A software applet then is triggered to park the harddisk.
This way the risk of data loss in case of when the notebook is dropped
is significantly reduced since the read/write head of the harddrive is
parked and hence can't crash onto the platter when the notebook drops
onto the floor.

Note: requires kernel 2.6.28+ or patched previous versions,
see http://www.thinkwiki.org/wiki/HDAPS

%description -l pl.UTF-8
HardDrive Active Protection System - system aktywnej ochrony dysku
twardego.

APS to system ochrony dla wewnętrznego dysku twardego ThinkPadów.
Czujnik wewnątrz ThinkPada rozpoznaje kiedy notebook podlega
przyspieszeniu. Aplet programowy reaguje na to parkując dysk twardy. W
ten sposób ryzyko utraty danych w przypadku upuszczenia notebooka jest
znacząco zmniejszane, ponieważ głowica odczytująco-zapisująca dysku
jest zaparkowana, dzięki czemu nie może uderzyć w talerz dysku przy
uderzeniu o podłoże.

%prep
%setup

%build
%configure
%make_build

%install
%make_install
install -pDm755 src/%name %buildroot%_sbindir/%name
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/udev/rules.d/51-hdaps.rules

%files
%_sbindir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/udev/rules.d/51-hdaps.rules

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 20090401-alt1
- 20081004 -> 20090401 (thx fedorawatch)

* Thu Apr 02 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- built for ALT Linux (based on heavily cleaned up PLD spec)
- ALT-style initscript
- added udev rules (from http://www.thinkwiki.org/wiki/HDAPS)
- NB: untested, see also #19459
