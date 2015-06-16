Name: polkit-sysvinit
Version: 0.2
Release: alt1

Summary: Allow media/network changes to xgrp users
License: public domain
Group: System/Configuration/Hardware

Url: http://altlinux.org/sysvinit
Source0: 60-sysvinit-mount.rules
Source1: 60-sysvinit-nm.rules
Source2: 60-xfsm-shutdown-helper.rules
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
AutoReqProv: no

%define pkdir %_sysconfdir/polkit-1/rules.d

%description
%summary
on SysVinit-based systems.

%prep

%install
mkdir -p %buildroot%pkdir
install -pm644 %SOURCE0 %SOURCE1 %SOURCE2 %buildroot%pkdir

%files
%pkdir/*

%changelog
* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added xfsm-shutdown-helper rule (thx Speccyfighter)

* Sat Mar 14 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (thx sem@)

