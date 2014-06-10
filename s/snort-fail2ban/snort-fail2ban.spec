Name: snort-fail2ban
Version: 0.1
Release: alt1

BuildArch: noarch

Summary: Configuration files for fail2ban
License: GPLv3
Group: System/Configuration/Other

Requires: fail2ban

Source: %name-%version.tar

%description
This package contains configuration files for fail2ban.
Snort must output into syslog.

%prep
%setup

%build

%install
mkdir -p %buildroot%_sysconfdir/fail2ban
cp -r filter.d %buildroot%_sysconfdir/fail2ban/
cp -r jail.d %buildroot%_sysconfdir/fail2ban/

%files
%config %_sysconfdir/fail2ban/filter.d/snort.conf
%config %_sysconfdir/fail2ban/jail.d/snort.conf

%changelog
* Tue Jun 10 2014 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- first build

