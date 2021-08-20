Name: volumes-profile-jeos
Version: 0.2.1
Release: alt1

Summary: Volumes description for JeOS distribution
License: GPL
Group: System/Configuration/Other

Url: http://altlinux.org/starterkits
Source: %name-%version.tar
BuildArch: noarch

%define hookdir %_datadir/install2/initinstall.d

%description
Volumes description for JeOS distribution

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- E2K:
  + increase /boot size to 1 Gb for serviceability
  + increase / size from >= 768 Mb to >= 1 Gb

* Tue Aug 14 2018 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- e2k support (/boot)

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial build (derived from volumes-profile-lite)

