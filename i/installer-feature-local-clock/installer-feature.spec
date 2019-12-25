Name: installer-feature-local-clock
Version: 0.3
Release: alt1

Summary: Sets UTC=false in sysconfig/clock
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch

%description
Sets UTC=false in sysconfig/clock for desktop distributions
(unless it's e2k where it's just not needed).

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Dec 25 2019 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- no need to keep Windows-style local clock in RTC on Elbrus

* Wed Apr 01 2015 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Fix UTC setup.

* Sat Oct 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build


