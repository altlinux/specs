Name: mcelog
Version: 138
Release: alt1

Summary: Tool to translate x86_64 CPU Machine Check Exception data
License: GPLv2
Group: System/Kernel and hardware

Url: https://github.com/andikleen/mcelog.git
Source0: %name-%version.tar.gz
Source1: mcelog.conf
Source2: mcelog.init
Source3: mcelog.service
Source4: mcelog.cron
Source5: mcelog.logrotate

ExclusiveArch: x86_64 %ix86

%define trigdir %_sysconfdir/mcelog/triggers

%package cron
Summary: Optional cronjob for mcelog
Group: System/Kernel and hardware
BuildArch: noarch

%description
mcelog is a utility that collects and decodes Machine Check Exception
data on x86-32 and x86-64 systems. It should be run as a service.

%description cron
This package contains the cronjob and logrotate configuration
for mcelog; note though that it's much preferred to run it as
a service.

%prep
%setup

%build
mkdir -p %buildroot{%_sysconfdir,%_sbindir,%_mandir}
make CFLAGS="%optflags -fpie -pie"

%install
install -pDm755 mcelog %buildroot%_sbindir/mcelog
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/mcelog/mcelog.conf
install -pDm755 triggers/cache-error-trigger %buildroot%trigdir/cache-error-trigger
install -pDm755 triggers/dimm-error-trigger %buildroot%trigdir/dimm-error-trigger
install -pDm755 triggers/page-error-trigger %buildroot%trigdir/page-error-trigger
install -pDm755 triggers/socket-memory-error-trigger %buildroot%trigdir/socket-memory-error-trigger
install -pDm755 %SOURCE2 %buildroot%_initdir/mcelog
install -pDm644 %SOURCE3 %buildroot%_unitdir/mcelog.service
install -pDm755 %SOURCE4 %buildroot%_sysconfdir/cron.hourly/mcelog.cron
install -pDm600 %SOURCE5 %buildroot%_sysconfdir/logrotate.d/mcelog
install -pDm644 mcelog.8 %buildroot%_man8dir/mcelog.8

%files
%doc README CHANGES
%_sbindir/mcelog
%dir %_sysconfdir/mcelog
%config(noreplace) %_sysconfdir/mcelog/mcelog.conf
%trigdir
%_initdir/mcelog
%_unitdir/mcelog.service
%_man8dir/*

%files cron
%_sysconfdir/cron.hourly/mcelog.cron
%_sysconfdir/logrotate.d/mcelog

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 138-alt1
- Autobuild version bump to 138

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 128-alt1
- Autobuild version bump to 128

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 125-alt1
- Autobuild version bump to 125

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 121-alt1
- Autobuild version bump to 121

* Wed Apr 29 2015 Fr. Br. George <george@altlinux.ru> 116-alt1
- Autobuild version bump to 116

* Wed Apr 29 2015 Fr. Br. George <george@altlinux.ru> 102-alt1
- Rebuild with new packaging scheme, version up

* Thu Jul 03 2014 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Update to v101

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 1.0-alt0.2
- cron subpackage made noarch

* Tue Mar 26 2013 Michael Shigorin <mike@altlinux.org> 1.0-alt0.1
- rebuilt for Sisyphus from ground up
  + upstream version is roughly 1.0 (gc824617)
  + package modeled after fedora's one (thx viy@ for autoimport)
  + systemd unit borrowed from opensuse
  + cron/logrotate files by lakostis@ (packaged separately)
  + sysv initscript written from scratch
- spec *cleanup*

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 2:1.0-alt1_0.6.6e4e2a00
- initial fc import

* Thu Jun 28 2007 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt0.1
- Initial revision.
