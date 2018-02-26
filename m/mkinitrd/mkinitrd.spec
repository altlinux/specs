Name: mkinitrd
Version: 3.0.11
Release: alt1
Serial: 1

Summary: Creates an initial ramdisk image for preloading modules
License: GPL
Group: System/Kernel and hardware
BuildArch: noarch

Packager: Sergey Vlasov <vsu@altlinux.ru>

Source: %name-%version.tar

PreReq: module-init-tools >= 3.1, mktemp >= 1:1.3.1
PreReq: coreutils findutils gawk getopt sed
PreReq: %name-initramfs = %serial:%version-%release
PreReq: klibc-utils-initramfs
PreReq: module-init-tools-initramfs
PreReq: udev-initramfs

# lspci is used for device detection in some cases
Requires: pciutils

%description
Mkinitrd creates filesystem images which are suitable for use as
Linux initial ramdisk (initrd) images.  Such images are often used
for preloading the block device modules (such as IDE, SCSI or RAID)
which are needed to access the root filesystem.  Mkinitrd automatically
loads IDE modules, all scsi_hostadapter entries in /etc/modules.conf,
and raid modules if the system's root partition is on raid, which
makes it simple to build and use kernels using modular device drivers.

In other words, generic kernels can be built without drivers for any
IDE/SCSI/RAID adapters which load appropriate driver as a module.
Since the kernel needs to read those modules, but in this case it
isn't able to address the IDE/SCSI/RAID adapter, an initial ramdisk
is used.  The initial ramdisk is loaded by the operating system loader
(such as LILO or GRUB) and is available to the kernel as soon as the
ramdisk is loaded.  The ramdisk image loads the proper IDE/SCSI/RAID
adapter and allows the kernel to mount the root filesystem.
The %name program creates such a ramdisk using information found in
the /etc/modules.conf file.

%package initramfs
Summary: Scripts for initramfs images created by mkinitrd
Group: System/Kernel and hardware
AutoReq: no

%description initramfs
This package contains scripts for initramfs images created by mkinitrd.

%prep
%setup -q

%build
sed -i 's/@VERSION@/%version/g' -- %name

%install
install -pDm755 %name %buildroot/sbin/%name
install -pDm644 %name.8 %buildroot%_man8dir/%name.8

mkdir -p %buildroot/lib/mkinitrd/initramfs-base/scripts
install -pm755 init %buildroot/lib/mkinitrd/initramfs-base/
install -pm644 scripts/{functions,local,nfs} \
	%buildroot/lib/mkinitrd/initramfs-base/scripts/

mkdir -p %buildroot/lib/mkinitrd/initramfs-base/sbin
install -pm755 sbin/udevadm %buildroot/lib/mkinitrd/initramfs-base/sbin/

%files
/sbin/*
%_man8dir/*

%files initramfs
/lib/mkinitrd

%changelog
* Sat Jan 08 2011 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.11-alt1
- mkinitrd: Fix RAID level detection for mdadm >= 3.0 (ALT#24875).

* Tue May 19 2009 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.10-alt1
- mkinitrd: Add support for kernel-provided firmware (ALT#20103).

* Thu Dec 11 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.9-alt1
- mkinitrd: Removed non-initramfs image types support.

* Tue Sep 02 2008 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.8-alt1
- mkinitrd-initramfs: Add a fallback implementation of udevadm which uses
  udevtrigger and udevsettle (fixes compatibility with udev < 117).

* Tue Sep 02 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt1
- init: Use udevadm instead of udevtrigger and udevsettle
  (Valery Inozemtsev; closes: #15426, #16959).

* Fri Aug 29 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.6-alt1
- init: Set PATH to a sane value (Sergey Vlasov; closes: #15426).
- Fixed depmod failure when initramfs contains no modules (Sergey Vlasov).

* Sat Oct 20 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.5-alt1
- Add --extra=MODULES option to add modules to initramfs without loading
  (legion@).
- Do not use IGNORE_MODNAMES for modules specified on the command line
  (#11956).
- Fix IGNORE_MODNAMES check to avoid broken dependencies (now a module which
  is required by other modules cannot be ignored).
- initramfs init: Pass udev version from initramfs to the real system.
- Fix module load ordering issues:
   + load generic IDE module after all other IDE drivers;
   + load ahci before ata_piix if both were detected;
   + load ata_generic and pata_legacy last.
- Use "mdadm --examine --scan" in addition to "mdadm --detail --scan" in RAID
  detection; fixes missing RAID 0 modules when using EVMS if arrays were added
  to /etc/mdadm.conf (#11282).
- If ext3 root mount failed, try ext2 before giving up (#11174).
- Replace /usr/bin/realpath usage with /bin/readlink -ev.

* Fri Jun 01 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.4-alt1
- Fix NFS root problems (#11374, patch by led@altlinux):
   + create /tmp in initramfs;
   + use DEVICE=eth0 by default;
   + accept root path with explicit server address from DHCP server.

* Thu Mar 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.3-alt1
- Fix boot problems with root on /dev/md0 specified by UUID or LABEL
  (another part of bug #11190 - race between md_run opening /dev/md0 to
  invoke RAID_AUTORUN ioctl and vol_id invoked by udevd).

* Thu Mar 08 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.2-alt1
- Fix compatibility with mdadm >= 2.6.1-alt2: look for the mdadm binary in
  /sbin/mdadm before /usr/sbin/mdadm.

* Wed Feb 21 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.1-alt1
- Added firmware loading support for initramfs images (required at least by
  the qla2xxx module since kernel 2.6.18).  Firmware files listed by
  "modinfo -F firmware" are automatically copied to the generated initramfs
  image (works with kernels since 2.6.18-std-*-alt4; for older kernels the
  "-a" option can be used to add firmware files manually).  Fixes #10598.
- Enable RAID support if "mdadm --detail --scan" finds any arrays (fixes
  missing RAID support if /dev/md* devices are not listed in fstab
  explicitly).  Fixes #4997, partially fixes #5955.
- Added warning when RAID support is enabled without any RAID levels.
- Removed "N blocks" garbage output from cpio (added --quiet option).
- Removed garbage output from fbresolution if no framebuffer is present.
- Do not add bootsplash to initrd if the kernel does not support it.

* Thu Feb 08 2007 Sergey Vlasov <vsu@altlinux.ru> 1:3.0.0-alt1
- Added support for creating initramfs images.  Now using udevd inside
  initramfs; this adds support for mounting root by label or UUID and other
  useful features.
- Added mkinitrd-initramfs subpackage with scripts for initramfs.
- Added dependencies on klibc-utils-initramfs, module-init-tools-initramfs,
  udev-initramfs packages which contain binaries for initramfs.
- Added support for more software RAID levels: raid10, multipath, faulty.
- Added support for determining used RAID levels with mdadm instead of
  obsolete /etc/raidtab file from raidtools.
- Updated software RAID detection by fstab contents to handle partitionable
  arrays (/dev/md/dN[pN], /dev/md_dN[pN]).
- Added software RAID support for initramfs images (uses md_run utility from
  the klibc-utils-initramfs package, should be compatible with in-kernel
  RAID autorun support, but supports only old 0.90 RAID superblocks).
- Added "-a INITRAMFS_FILENAME=FILENAME" option to add extra files to the
  generated initramfs image.
- Made initramfs the default image type for kernels >= 2.6.15.

* Sun Jan 21 2007 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.12-alt1
- Always use /lib/mkinitrd for initrd binaries (previously /lib64/mkinitrd
  was used on x86_64).
- Require mkinitrd-busybox >= 1.3.0-alt2 due to the /lib/mkinitrd path change.

* Wed Jan 10 2007 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.11-alt1
- Added support for the module-init-tools implementation of modprobe.
  Requires ALT-specific modification to module-init-tools which adds the
  --ignore-all-commands option to modprobe (without this option module
  dependencies may be broken by "install" commands in the configuration).
- Changed autodetection of SCSI modules to use lspci instead of pciscan;
  removed dependency on libhw-tools.
- Added Packager: tag.
- Added BuildArch: noarch (the arch-dependent part is in mkinitrd-busybox
  for a long time, and this package contains just a shell script).
- Changed dependency on modutils >= 0:2.4.27-alt1 to module-init-tools >= 3.1
  (module-init-tools = 3.1 is provided by modutils since 2.4.27-alt3).

* Tue Dec 26 2006 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.10-alt1
- Fixed man page formatting and several typos.
- Added --type=TYPE option to specify initrd filesystem type (#8533).
- Added support for suspend2 2.2.7.2+ (/sys/power/suspend2/do_resume) to
  linuxrc (by Andrey Rahmatullin <wrar at altlinux>).
- Refactored root=... and resume=... parsing code in linuxrc in preparation for
  initramfs support.
- Added support for all forms of root=... parameter accepted by the kernel
  (root=MAJOR:MINOR, root=NUMBER (used by LILO), root=NAME without /dev/).
- Added explicit dependencies on libhw-tools >= 0.2.12-alt1 and pciutils.
- Added warnings about missing /proc and /sys to avoid silently creating an
  initrd image without proper drivers.

* Mon Jun 12 2006 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.9-alt1
- Fixed resume= option parser.
- Fixed ext2 size calculation (#8539).
- Fixed rpmbuild warnings due to broken '%%' usage in old changelog entries.
- Removed all %%__* macro abuse from spec.

* Thu Jun 01 2006 Anton Farygin <rider@altlinux.ru> 1:2.9.8-alt1
- Added resume= option parser for swsuspend

* Tue May 17 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.7-alt1
- Added '--kernel-version "$KERNEL"' to the 'modprobe -c' invocation (#6827).

* Fri May 06 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.6-alt1
- Fixed autodetection of SCSI modules:
  + find drivers for all PCI mass storage controllers (class 01) instead of
    limiting to 01:00 and 01:04 subclasses (fixes problems with Intel ICHx SATA
    controllers, which have IDE subclass, but the driver uses SCSI subsystem);
  + filter out IDE drivers which may be found by the search;
  + do not add sd_mod for other non-SCSI storage drivers which may be found.
- Added Conflicts for old libhw-tools versions (not Requires, because this
  dependency is optional - if scsi_hostadapter is specified expicitly in the
  configuration file, libhw-tools is not needed).

* Thu Apr 28 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.5-alt1
- Added autodetection of SCSI modules.  Autodetection is performed only if no
  (alias|probeall) scsi_hostadapter is specified in /etc/modules.conf.  Modules
  for all PCI devices with classes 01:00 (SCSI storage controller) and 01:04
  (RAID bus controller) are added to initrd; /usr/bin/pciscan is used to find
  modules in the driver database.

* Tue Mar 22 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.4-alt1
- Load IDE modules before SCSI to keep old configurations with ICH5/6 in
  combined mode working (IDE modules must be loaded before ata_piix, otherwise
  ata_piix grabs the whole device including legacy IDE ports, and parallel ATA
  does not work).
- Updated bootsplash support for new location of utilities (/sbin/splash) and
  theme files (/etc/bootsplash).

* Mon Feb 14 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.3-alt1
- Fixed bug in kernel version check.

* Tue Feb 08 2005 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.2-alt1
- Added modular IDE support for kernels >= 2.4.21 (with per-chipset modules).
  Both manual configuration with "probeall ide_hostadapter MODULE..." and
  automatic detection of required modules for the current system configuration
  are supported.
- Added "--with-raid" option to force software RAID autorun support even if
  there are no /dev/md* entries in /etc/fstab.
- Added software RAID level 6 support.
- Added /lib64 support for x86_64 (#4888).
- Added /sys to initrd (#5387).
- Fixed problems with unrecognized "root=/dev/..." on 2.6.x kernels: added root
  device searching in /proc/partition to the linuxrc script in generated
  initrd.  In 2.6.x the builtin "root=..." parser works only for drivers which
  are built into the kernel.

* Thu Mar 11 2004 Sergey Vlasov <vsu@altlinux.ru> 1:2.9.1-alt1
- Package busybox separately.
- Use "--kernel-release" and "--list-module-files" options from modutils >=
  2.4.26-alt1.
- Require modutils >= 2.4.27-alt1 because of bugs in previous versions.
- Removed module tree copying.
- Added module name normalization (y/-/_/) needed for 2.6.x kernels.

* Thu Feb 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.0-alt1
- Do not use full path for well-known utilities.
- Look for .ko/.ko.gz modules as well.

* Sun Nov 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.9-alt3
- busybox/insmod: backported GPLONLY_ prefix support.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.9-alt2
- busybox/insmod: set TAINT_FORCED_MODULE flag only when load is really forced.

* Thu Aug 28 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.9-alt1
- Updated software raid root support (Sergey Vlasov, #2082).
- Updated bootsplash support (fixes #2442).
- Updated busybox to stable-20030828.
- busybox/insmod: added more licenses to gpl compatibility list,
  to match modutils >= 2.4.15-alt1 behaviour.

* Tue Aug 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.8-alt1
- Added software raid root support (Sergey Vlasov).
- Enhanced modutils config parser (uses "modprobe -c").

* Fri May 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.7-alt2
- Updated busybox to 0.60.5, updated busybox patches.

* Mon Mar 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.7-alt1
- Updated mkinitrd(8).

* Wed Mar 12 2003 Peter Novodvorsky <nidd@altlinux.com> 1:2.8.6-alt2
- Increased extra initrd image size by 10%%.

* Mon Feb 10 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.6-alt1
- Added bootsplash support (rider).

* Mon Feb 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.5-alt1
- Added --pause option (Vladimir Kholmanov <fmfm@symmetron.msk.ru>).

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.4-alt2
- Rebuilt with new dietlibc.

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.4-alt1
- Added romfs image support (goldhead).

* Tue Jul 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.3-alt2
- Fixed build with new dietlibc.

* Mon Apr 08 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.3-alt1
- Corrected scsimodules/ataraidmodules calculation.

* Fri Feb 22 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.2-alt1
- Copy modules with full path.

* Sat Jan 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.1-alt1
- Added "--debug" option for debug messages.
- Cleaned up script to avoid using /usr. 
- Updated dependencies.

* Fri Jan 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.0-alt1
- Use busybox(echo,insmod,losetup,mount,msh) as linuxrc parser.

* Fri Jan 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt1
- Avoid "build" symlinks.

* Wed Jan 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.7-alt1
- Added more module namings for new master installer.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.6-alt1
- Fixed scsi autodetection for new master installer.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.5-alt1
- Use ash.static as linuxrc parser.

* Wed Jan 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.4-alt1
- Fixed pre_scsi_modules handling.

* Tue Dec 25 2001 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.3-alt1
- Fixed depmod generation for 2.4 kernels.

* Mon Dec 24 2001 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.2-alt1
- Regular mkinitrd cleanup.
- Forked completely due to patch size.

* Fri Dec 14 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.7.1-alt7
- Added ataraid patch

* Fri Nov 23 2001 Dmitry V. Levin <ldv@altlinux.org> 2.7.1-alt6
- Updates package requires.

* Thu Nov 22 2001 Dmitry V. Levin <ldv@altlinux.org> 2.7.1-alt5
- Added support for nested module dependencies.

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7.1-alt4
- Updated versioned dependence on mktemp package.

* Wed Aug 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7.1-alt3
- Removed versioned dependence on glibc package.
- Updated versioned dependence on mktemp package.

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7.1-alt2
- IMAGESIZE reservation increased from 2%% to 10%% (goldhead).

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7.1-alt1
- Implemented ramdisk size guessing.
- Rewritten command line options parsing.

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7-ipl3mdk
- Added --strict option.
- Changed IGNOREMODS list.

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7-ipl2mdk
- Do not load ide-cd module.

* Sun Dec 24 2000 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl1mdk
- 2.7 (added modular ide support).

* Tue Nov 28 2000 Dmitry V. Levin <ldv@fandra.org> 2.6-ipl1mdk
- 2.6
- Merged recent MDK changes into out patch.
- Added unobvious requires.

* Tue Nov 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.5-ipl2mdk
- RE adaptions.

* Wed Aug 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5-2mdk
- bug fix

* Mon Aug 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5-1mdk
- update for hackkernel (new modules layout)
- remove exclusiveos:linux (rms'll be happy)
- make it noarch

* Fri Jul 28 2000 Pixel <pixel@mandrakesoft.com> 2.4.3-3mdk
- modified the mdk patch: don't do "insmod the.o || insmod -f the.o" because
sash doesn't handle it :(

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 2.4.3-2mdk
- BM

* Sun Jun 25 2000 Pixel <pixel@mandrakesoft.com> 2.4.3-1mdk
- merge with redhat (mainly modules.conf by default)

* Thu Jun  1 2000 Bill Nottingham <notting@redhat.com>
- build on ia64
- bump up initrd size on ia64
- modules.confiscation, /usr/man -> /usr/share/man

* Thu May 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.2-16mdk
- Thanks my god initrd work on alpha !!!.

* Tue May  9 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-15mdk
- add possibility to modules to ignore via env var IGNOREMODS

* Wed May  3 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-14mdk
- patch for skipping usb-storage

* Tue Apr 18 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-13mdk
- add handling of non-ext2 root filesytems (again :()

* Mon Apr 17 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-12mdk
- insmod -f instead of insmod

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-11mdk
- new group

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 2.3.2-10mdk
- Added ppc and k7 arch
- Fixed bzipping of man pages

* Mon Mar 13 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-9mdk
- do not require ash.static but sash
- add requires sash >= 3.4

* Mon Mar 13 2000 Pixel <pixel@mandrakesoft.com> 2.3.2-8mdk
- add loopback handling

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- fix *buggy* grep scsi_hostadapter on conf.modules

* Mon Jan  3 2000 Pixel <pixel@mandrakesoft.com>
- fix to skip ide-scsi.o (overkill :)

* Tue Dec 28 1999 Pixel <pixel@mandrakesoft.com>
- fix to skip ppa.o and imm.o
- fix a typo

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.3.2.

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Upgrade to 2.0.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated description

* Mon Jan 11 1999 Matt Wilson <msw@redhat.com>
- Ignore the absence of scsi modules, include them if they are there, but
  don't complain if they are not.
- changed --no-scsi-modules to --omit-scsi-modules (as it should have been)

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Tue Oct 20 1998 Jakub Jelinek <jj@ultra.linux.cz>
- fix for combined sparc/sparc64 insmod, also pluto module is really
  fc4:soc:pluto and we don't look at deps, so special case it.

* Sat Aug 29 1998 Erik Troan <ewt@redhat.com>
- replaced --needs-scsi-mods (which is now the default) with
  --omit-scsi-mods

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- correct obscure regex/shell interaction (hardwires tabs on line 232)

* Mon Jan 12 1998 Erik Troan <ewt@redhat.com>
- added 'make archive' rule to Makefile
- rewrote install procedure for more robust version handling
- be smarter about grabbing options from /etc/conf.modules

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made it use /bin/ash.static

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Only use '-s' to install binaries if /usr/bin/strip is present.
- Use an image size of 2500 if binaries can't be stripped (1500 otherwise)
- Don't use "mount -o loop" anymore -- losetup the proper devices manually
- Requires losetup, e2fsprogs

* Wed Mar 12 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed a bug in parsing options.
- Changed to use a build tree, then copy the finished tree into the
  image after it is built.
- Added patches derived from ones written by Christian Hechelmann which
  add an option to put the kernel version number at the end of the module
  name and use install -s to strip binaries on the fly.
