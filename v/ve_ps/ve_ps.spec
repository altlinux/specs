Summary: Standart ps extension that makes text snapshots of processes with respective VE ids
Name: ve_ps
Version: 0.1
Release: alt2
License: GPL
Group: Monitoring
Packager: Mikhail A Pokidko <pma@altlinux.org>

BuildArch: noarch

Source1: ve_ps
Source2: ve_ps.cron
Source3: vzpider

Requires: procps
BuildArch: noarch

%description
Standart ps extension that makes text snapshots of processes with respective VE ids.

%install
mkdir -p %buildroot%_sysconfdir/cron.d/ %buildroot%_bindir/ %buildroot%_logdir/%name/
install -pm 755 %SOURCE1 %buildroot%_bindir/
install -pm 755 %SOURCE3 %buildroot%_bindir/
install -pm 644 %SOURCE2 %buildroot%_sysconfdir/cron.d/%name


%files
%dir %_logdir/%name
%_sysconfdir/cron.d/*
%_bindir/*


%changelog
* Mon Nov 15 2010 Mikhail Pokidko <pma@altlinux.org> 0.1-alt2
- Fixed output. Prematurely died processes spoil output no more.

* Thu Nov 05 2009 Mikhail Pokidko <pma@altlinux.org> 0.1-alt1
- initial commit

