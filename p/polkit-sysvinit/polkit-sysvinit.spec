Name: polkit-sysvinit
Version: 0.3.2
Release: alt3

Summary: Allow media/network changes to xgrp users
License: public domain
Group: System/Configuration/Hardware

Url: http://altlinux.org/sysvinit
Source0: 60-sysvinit-mount.rules
Source1: 60-sysvinit-nm.rules
Source2: 60-xfsm-shutdown-helper.rules
Source3: 60-sysvinit-console-kit.rules
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
AutoReqProv: no
Requires: polkit

%define pkdir %_sysconfdir/polkit-1/rules.d

%description
%summary
on SysVinit-based systems.

%prep

%install
mkdir -p %buildroot%pkdir
install -pm644 %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %buildroot%pkdir

%files
%pkdir/*

%changelog
* Tue Dec 06 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt3
- R: polkit

* Fri Nov 04 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt2
- built for sisyphus (closes: #31501)

* Fri Aug 12 2016 Yury Pakin <zxwarior@yandex.ru> 0.3.2-alt1
- fixed: absence of LF at the end of file 60-sysvinit-mount.rules

* Thu May  5 2016 Yury Pakin <zxwarior@yandex.ru> 0.3.1-alt1
- added 60-sysvinit-console-kit.rules

* Sat Mar 12 2016 Daniil Golovanov <dangolan@yandex.ru> 0.3-alt1
- change 60-sysvinit-mount.rules (thx Speccyfighter)

* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added xfsm-shutdown-helper rule (thx Speccyfighter)

* Sat Mar 14 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thx sem@)

