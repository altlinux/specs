Name: mcelog
Version: 191
Release: alt1

Summary: Tool to translate x86_64 CPU Machine Check Exception data
License: GPLv2
Group: System/Kernel and hardware

Url: https://github.com/andikleen/mcelog.git
Source0: %name-%version.tar
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

%post
%post_service mcelog

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
%doc README.md
%_sbindir/mcelog
%dir %_sysconfdir/mcelog
%_sysconfdir/logrotate.d/mcelog
%config(noreplace) %_sysconfdir/mcelog/mcelog.conf
%trigdir
%_initdir/mcelog
%_unitdir/mcelog.service
%_man8dir/*

%files cron
%_sysconfdir/cron.hourly/mcelog.cron

%changelog
* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 191-alt1
- 189 -> 191

* Fri Oct 07 2022 Anton Farygin <rider@altlinux.ru> 189-alt1
- 181 -> 189

* Thu May 19 2022 Anton Farygin <rider@altlinux.ru> 181-alt1
- 180 -> 181

* Wed Feb 23 2022 Anton Farygin <rider@altlinux.ru> 180-alt1
- 179 -> 180

* Tue Dec 07 2021 Anton Farygin <rider@altlinux.ru> 179-alt1
- 178 -> 179

* Mon Sep 06 2021 Anton Farygin <rider@altlinux.ru> 178-alt1
- 175 -> 178

* Thu Mar 25 2021 Anton Farygin <rider@altlinux.org> 175-alt1
- 173 -> 175

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 173-alt1
- 170 -> 173

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 170-alt1
- 162 -> 170

* Fri Mar 22 2019 Anton Farygin <rider@altlinux.ru> 162-alt2
- added post script for service mcelog (closes: #36342)

* Thu Mar 21 2019 Anton Farygin <rider@altlinux.ru> 162-alt1
- 159 -> 162
- fixed condreload target in initscript (closes: #36328)
- logrotate setting has been moved from cron to main package (closes: #36329)
- updated logrotate settings from ALT bug #36329

* Wed Aug 08 2018 Anton Farygin <rider@altlinux.ru> 159-alt1
- version up to 159
- built from upstream git

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
