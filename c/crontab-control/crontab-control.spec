Name: crontab-control
Version: 1.1
Release: alt1

Summary: Crontab facilities control
License: GPL
Group: System/Servers
BuildArch: noarch

PreReq: shadow-utils
Conflicts: vixie-cron < 0:4.0b1-alt1

Source0: crontab.control
Source1: at.control

%description
This package contains control rules for crontab facilities.
See control(8) for details.

%install
%__install -pD -m755 %SOURCE0 $RPM_BUILD_ROOT%_controldir/crontab
%__install -pD -m755 %SOURCE1 $RPM_BUILD_ROOT%_controldir/at

%pre
/usr/sbin/groupadd -r -f crontab

%files
%config %_controldir/*

%changelog
* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help.

* Thu May 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
