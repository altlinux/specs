Name: startup-mediacheck
Version: 0.1
Release: alt1

Summary: The system startup scripts for mediacheck (warning!)
License: GPL
Group: System/Base

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar

BuildArch: noarch
Requires: console-vt-tools isomd5sum

%description
This package contains scripts to check live/installation media.
/etc/rc.d/rc might need to be emptied for this one to work,
see mkimage-profiles.git::features.in/mediacheck for example.

WARNING: you DO NOT want this package on your own system!

%prep
%setup

%install
mkdir -p -- %buildroot%_sysconfdir/rc.d
install -pm644 inittab.mediacheck %buildroot%_sysconfdir/
install -pm755 rc.sysinit.mediacheck %buildroot%_sysconfdir/rc.d/

%files
%_sysconfdir/inittab.mediacheck
%_sysconfdir/rc.d/rc.sysinit.mediacheck

%changelog
* Mon Mar 31 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on startup-rescue 0.15-alt1)

