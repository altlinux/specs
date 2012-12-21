Name: installer-scripts-remount-stage2
Version: 0.1
Release: alt1

Summary: Shared installer scripts: remount
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

Conflicts: installer-common-stage2 < 1.8.11-alt1

%description
This package contains shared installer scripts,
namely a script to remount filesystems after
employing EVMS to partition and mkfs them
so that preinstall/postinstall scripts would
work in block device and devmapper environment
that's close to the target system's one.

%prep
%setup

%build

%install
# a single script is not worth two makefiles yet
install -pDm755 scripts/install2-remount-functions \
	%buildroot%_sbindir/install2-remount-functions

%files
%_sbindir/*

%changelog
* Fri Dec 21 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- split off installer-1.8.10-alt1 to use with livecd-install too
