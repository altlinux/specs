Name: auto-fstrim
Summary: Daily run fstrim for all SSD-based partitions
Version: 1.0
Release: alt1
License: GPLv2+
Group: System/Kernel and hardware
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
%makeinstall install

%files
/etc/cron.daily/auto-fstrim
%_sbindir/auto-fstrim

%changelog
* Thu Jul 26 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
