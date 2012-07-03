Name: installer-feature-vm-altlinux-generic
Version: 0.1
Release: alt1

Summary: alterator-vm profile tuning and filesystem layout hooks
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define hookdir %_datadir/install2

%description
This package contains alterator-vm profile tuning and
filesystem layout hooks for a generic ALT Linux based
distribution.

%package stage2
Summary: Installer stage2 alterator-vm profile tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
This package contains alterator-vm profile tuning hook for
a generic ALT Linux based distribution's installer stage2.

%prep
%setup

%install
install -pDm755 05-vm-profile-altlinux-generic \
	%buildroot%hookdir/initinstall.d/05-vm-profile-altlinux-generic

%files stage2
%hookdir/initinstall.d/*

%changelog
* Tue Jul 19 2011 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial revision based on installer-feature-vm-server-light
  by Anton Farygin
