Name: volumes-profile-lite
Version: 0.4.2
Release: alt1

Summary: Volumes description for School Lite distribution
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org> 

BuildArch: noarch

%description
Volumes description for School Lite distribution

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability

* Mon Aug 05 2019 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- e2k support (/boot)

* Fri Jul 15 2016 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- Increase size of / to 15G

* Mon Sep 30 2013 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Change autopartition algorithm: swap==RAM, 10G for / and 512M minimum for home

* Fri Dec 17 2010 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Reduce total installation to 8 Gb

* Thu Dec 09 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- initial build (derived from volumes-profile-master)

