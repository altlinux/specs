Name: startup-rescue
Version: 0.13
Release: alt1

Summary: The system startup scripts for rescue disk
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Source: rescue-%version.tar

Requires(post): %post_service
Requires(preun): %preun_service
Requires: sfdisk console-vt-tools libshell system-report

#Optional requires
Requires: dmidecode ddcprobe

%description
This package contains scripts used to boot your system from rescue disk.

%prep
%setup -q -n rescue-%version

%install
mkdir -p -- %buildroot{%_bindir,/sbin,/etc/rc.d}

install -m755 rescue-shell %buildroot%_bindir/
install -m755 fixmbr mount-system *-fstab %buildroot/sbin
install -m644 inittab.rescue %buildroot/etc/
install -m755 rc.sysinit.rescue %buildroot/etc/rc.d/
install -pDm755 sysreport.init %buildroot%_initdir/sysreport

%files
/sbin/*
%_bindir/*
/etc/inittab.rescue
/etc/rc.d/rc.sysinit.rescue
%_initdir/sysreport

%changelog
* Fri Dec 24 2010 Anton Protopopov <aspsk@altlinux.org> 0.13-alt1
- add --grub option, use it by default

* Thu Dec 23 2010 Anton Protopopov <aspsk@altlinux.org> 0.12-alt1
- lilo support; totally rewrite algorithm

* Tue Nov 09 2010 Anton Farygin <rider@altlinux.ru> 0.11-alt1
- fixmbr:
    - do not use evms
    - display errors from mount-system only in verbose mode
    - reinstall grub only on block devices

* Mon Nov 08 2010 Anton Farygin <rider@altlinux.ru> 0.10-alt1
- do not start evms and system-report on boot
- do not use evms for mount-system
- fixed system search bug in fixmbr

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- fixmbr rewriten to work with grub (but lilo support dropped)

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- fix from cas@ to fixmbr

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- using aufs instead unionfs 

* Mon Nov 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- fixmbr fixed to work better with new alterator-lilo 

* Tue Sep 16 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt2
- inittab fixed (openvt is in /bin/ now) 

* Mon Aug 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- fixmbr totally rewritten 

* Thu May 22 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.2
- fix prompt (text and highlighting)

* Mon May 19 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.1
- fix prompt

* Mon May 19 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.0
- new version of mbrresc
- mbrresc is renamed to `fixmbr'

* Thu May 15 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.4
- fix mbrresc

* Fri May 02 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.3
- new version

* Mon Apr 28 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.2
- add rescue-0.4.2-mbrresc.diff

* Mon Mar 10 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.2-alt2.eter1
- Merged with stanv@ lilo restore feature

* Tue Jan 29 2008 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt2
- Use system sysreport utility.
- Fix for kbd-1.13*.
- Minimize requires.

* Wed Dec 12 2007 Andriy Stepanov <stanv@altlinux.ru> 0.4.2-alt1.2
- No LVM activation (EVMS fixed)
  fix lilo restore

* Thu Dec 06 2007 Andriy Stepanov <stanv@altlinux.ru> 0.4.2-alt1.1
- Added:
  + LVM activation at boot time
  + mbrresc utility (say `mbrresc' at command before kernel loading)

* Thu Aug 09 2007 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt1
- Added:
  + Report information about x86 hardware as described in
    the system BIOS according to the SMBIOS/DMI standard.
  + Report information from Display Data Channel (DDC).
- Added requires dmidecode and ddcprobe.
- mount-fstab: Fix for new libshell.

* Thu May 03 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Added rescue-shell.

* Wed May 02 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- rc.sysinit.rescue: Mounted /mnt to overlay.
- inittab.rescue: Added runlevel scripts execution.
- inittab.rescue: Added shell execution to vc5 and vc6.
- rc.sysinit.rescue: Removed developer-report execution.
- Renamed developer-report to system-report.
- Added sysreport service.

* Sat Apr 28 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- rc.sysinit.rescue: Added necessary $USEMODULES initialization.

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- inittab.rescue: Run bash with -l option.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Updated sysreport email address.

* Wed Feb 28 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- First build for ALT Linux.
