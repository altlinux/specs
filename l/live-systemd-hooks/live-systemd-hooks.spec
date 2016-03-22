Name: live-systemd-hooks
Version: 20160322
Release: alt1

Summary: Run additional scripts from live boot media
License: GPL
Group: System/Configuration/Other

Source0: systemd-hooks
Source1: systemd-hooks.service

BuildArch: noarch

%description
%summary

%prep

%install
mkdir -p %buildroot/%_unitdir/
install -pD -m0755 %SOURCE0 %buildroot/lib/systemd/systemd-hooks
install -pD -m0644 %SOURCE1 %buildroot/%_unitdir/systemd-hooks.service

%files
/lib/systemd/systemd-hooks
%_unitdir/systemd-hooks.service

%changelog
* Tue Mar 22 2016 Eugene Prokopiev <enp@altlinux.ru> 20160322-alt1
- fix service file permissions

* Fri Jan 15 2016 Eugene Prokopiev <enp@altlinux.ru> 20160115-alt1
- fix start before network

* Mon Sep 14 2015 Eugene Prokopiev <enp@altlinux.ru> 20150914-alt1
- first build

