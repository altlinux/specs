Name: make-initrd-propagator
Version: 0.15
Release: alt1

Summary: Put propagator into make-initrd generated image
License: GPL
Group: System/Base

Source0: %name-%version.tar 

Requires: console-vt-tools fdisk /sbin/addpart grep
Requires: aufs2-util sysvinit-utils net-tools
Requires: sed procps psmisc findutils nfs-utils
Requires: make-initrd
Requires: e2fsprogs
Requires: udev-rules udev-extras

# For new put-file utility
Requires: make-initrd >= 0.7.6-alt1

BuildArch: noarch
AutoReq: noshell, noshebang


%description
Make-initrd feature, able to make hybrid propagator/make-initrd initrd

%prep
%setup

%install
mkdir -p %buildroot%_datadir/make-initrd/features/
cp -a propagator %buildroot%_datadir/make-initrd/features/
mkdir -p %buildroot%_datadir/make-initrd/features/propagator/data/image

%files 
%_datadir/make-initrd/features/propagator

%changelog
* Sun Feb 10 2013 Michael Shigorin <mike@altlinux.org> 0.15-alt1
- add name-slot-rules conditionally (see also #28484)
- fix a typo

* Thu Jan 31 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.14-alt1
- add name-slot-rules

* Fri Dec 28 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.13-alt2
- creating aufs slice on hybrid rw media temporary disabled

* Fri Nov 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.13-alt1
- mount.nfs added

* Mon Sep 17 2012 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Provide /proc/cmdline parser
- Add overlays profiling support

* Wed Sep 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11-alt1
- put-file usage fix from sin@ (closes #27725)

* Wed Sep 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt1
- added --numeric-ports option to netstat (dans@), (closes: #27698)

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- NMU: merged legion@'s update for current make-initrd

* Thu Mar 22 2012 Andriy Stepanov <stanv@altlinux.ru> 0.8-alt1.2
- Works independent from propagator

* Wed Sep 14 2011 Michael Shigorin <mike@altlinux.org> 0.8-alt1.1
- NMU: add Requires: make-initrd (closes: #26133)
- trivial spec cleanup

* Tue Aug 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- nfs live overlays order fixed

* Tue Jun 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt4
- nfs live overlays fixed

* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt3
- head added to initramfs for nfs livecd overlays

* Tue Jun 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt2
- udba=notify deleted for compatibility with 2.6.32

* Wed Jun 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- remount root for live to aufs

* Wed Dec 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- create /image in rootfs (fixes http and ftp methods)

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- do not copy plymouth files if plymouth not installed

* Wed Dec 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- creating /lib/firmware in rootfs

* Tue Dec 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- hack 60-persistent-storage-rules to not link sd[a-z] to disk/by-label

* Wed Dec 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- boot-duration copying added

* Tue Nov 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



