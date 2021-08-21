Name: volumes-profile-alt-workstation
Version: 0.1.1
Release: alt1

Summary: Volumes description for ALT Workstation
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%define hookdir %_datadir/install2/initinstall.d

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability

* Thu Jul 22 2021 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build (based on Simply Linux profile).
