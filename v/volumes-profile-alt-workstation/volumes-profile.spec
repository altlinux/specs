Name: volumes-profile-alt-workstation
Version: 0.2
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
* Wed Aug 24 2022 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Use a common title for profiles.

* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability

* Thu Jul 22 2021 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build (based on Simply Linux profile).
