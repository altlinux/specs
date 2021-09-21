Name: startup-installer-acos
Version: 0.2.1
Release: alt1
#Architectures which grub-common exists on
ExclusiveArch: %ix86 x86_64 aarch64 ppc64le riscv64

Summary: The system startup and install scripts for ACOS installation disk
License: GPL-3.0-or-later
Group: System/Base

Source: acos-%version.tar

Requires: bash, /etc/rc.d/init.d/functions, /etc/rc.d/scripts/framebuffer_init, /sbin/reboot
Requires: coreutils, e2fsprogs, grep, grub-common, kmod, mount, ostree, parted, procps
Requires: psmisc, sed, sfdisk, sysvinit-utils, tar, termutils, util-linux, grub-common

%ifarch %ix86 x86_64
Requires: grub-pc
%endif

# /etc/rc.d/init.d/gpm is optional
%filter_from_requires /^\/etc\/rc.d\/init.d\/gpm$/d

%description
This package contains scripts used to boot from ACOS (ALT Container OS) installation disk and to install ACOS.

%prep
%setup -n acos-%version

%install
mkdir -p -- %buildroot{%_bindir,%_initdir,%_datadir/acos}

install -pm755 acos-shell acos-installer.sh %buildroot%_bindir/
install -pm644 inittab.acos %buildroot/etc/
install -pm755 rc.sysinit.acos %buildroot/etc/rc.d/
install -pm444 config_example.ign %buildroot%_datadir/acos/

%files
%_bindir/*
/etc/inittab.acos
/etc/rc.d/rc.sysinit.acos
%_datadir/acos

%changelog
* Thu Sep 21 2021 Andrey Sokolov <keremet@altlinux.org> 0.2.1-alt1
- Fix example ignition config. User acos has already been created before starting of ignition. Ignition should set password only

* Wed Sep 1 2021 Andrey Sokolov <keremet@altlinux.org> 0.2-alt1
- Show unpacking progress
- Add hint how to change password hash
- Add dependency on grub-pc

* Fri Aug 27 2021 Andrey Sokolov <keremet@altlinux.org> 0.1-alt1
- Initial release
