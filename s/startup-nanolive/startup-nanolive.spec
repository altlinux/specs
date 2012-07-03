Name: startup-nanolive
Version: 0.1.0
Release: alt1

Summary: The system startup scripts for NanoLive CD
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Kirill A. Shutemov <kas@altlinux.ru>

Source: nanolive-%version.tar

Requires: sfdisk evms console-vt-tools libshell

#Optional requires
Requires: dmidecode ddcprobe

%description
This package contains scripts used to boot your system from NanoLive CD.

%prep
%setup -q -n nanolive-%version

%install
mkdir -p -- %buildroot{/sbin,/etc/rc.d}

install -m755 mount-system *-fstab %buildroot/sbin
install -m644 inittab.nanolive %buildroot/etc/
install -m755 rc.sysinit.nanolive %buildroot/etc/rc.d/

%files
/sbin/*
/etc/inittab.nanolive
/etc/rc.d/rc.sysinit.nanolive

%changelog
* Wed Aug 06 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.1.0-alt1
- First build for ALT Linux
- Based on startup-rescue 0.4.2-alt2
