Name: spt
Version: 0.6.0
Release: alt12

Summary: Tools for creating based on Sisyphus solutions
License: GPL
Group: Development/Other

Url: http://www.altlinux.org/Spt
Source: %name-%version.tar
Packager: L.A. Kostis <lakostis@altlinux.org>
BuildArch: noarch

# Due to hsh-fakedev(1)
Requires: hasher >= 1.2.1
# Added by hand
Requires: bzip2 coreutils findutils gzip rsync
AutoReq: yes, noshell

Summary(ru_RU.KOI8-R): Утилиты для создания основанных на Sisyphus решений

%description
spt is a tool for making Sisyphus-based solution
like custom install ISO, LiveCD, OpenVZ container.
By default, spt is able to make LiveCD and rescue
image. Additional profiles could be found
at spt-profiles-* packages.

spt is considered deprecated due to mkimage.

%prep
%set_findreq_skiplist %_datadir/%name/*
%set_findprov_skiplist %_datadir/%name/*
%setup -c

%install
%makeinstall DESTDIR=%buildroot

%files
%dir %_datadir/%name
%doc docs/spt.txt
%_datadir/%name/*
%_bindir/*

%changelog
* Sun Mar 22 2009 Michael Shigorin <mike@altlinux.org> 0.6.0-alt12
- applied spec patch by Yury Yurevich <the.pythy@gmail.com>
  for better package description (#18851)
- added an Url:
- well, *minor* spec cleanup

* Wed Apr 09 2008 Michael Shigorin <mike@altlinux.org> 0.6.0-alt11
- pulled one-line fix from sbolshakov@

* Wed Mar 12 2008 Michael Shigorin <mike@altlinux.org> 0.6.0-alt10.3.1
- rebuild

* Fri Mar  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt10.3
- adapted for both mkmodpack and mkmar

* Tue Jan 29 2008 Michael Shigorin <mike@altlinux.org> 0.6.0-alt10.2.1
- make tgz compression level adjustable (#14235)
- minor spec cleanup (see alt-packaging)

* Wed Oct 24 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt10.2
- add missing requires due disabled findreq.

* Tue Oct 23 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt10.1
- add kludge for buggy findreq (fix #12928).

* Wed Sep 26 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt10
- scripts/spt: add .tar image support (patch by inger@).

* Sun Sep 16 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt9
- merge inger@ changes:
  + spt/scripts/spt: move "FILES" to chroot/.in (not to outdir)

* Mon Aug 20 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt8
- merge inger:
  + spt/scripts/spt-sh-functions: fix spt work with cdrom: method (fix #11739).

* Fri Jul 20 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt7
- merge boyarsh@ changes:
  + spt/scripts/spt: added xargs into install.

* Wed Jul 04 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt6
- merge lost legion@ changes:
  + spt/scripts/spt: Add optional files in isoimage.

* Thu Jun 21 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt5.1
- spt: add packages.$CDFILENAME support (by boyarsh@).

* Wed May 23 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt5
- fix root rw remount (ALT #11867).

* Mon May 21 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.6.0-alt4
- remove bootsplash fifo from /dev (alt workaround exists).
- remove /dev/fb0 (again).

* Fri May 18 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.6.0-alt3
- add new features:
  + no-compress switch: prevent squashfs image compression
  + create bootsplash initrd for stage1 (and add nobootsplash switch)

* Mon Apr 23 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt2
- more correct fix for #11266 (tnx to ldv@).

* Sun Apr 15 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt1.1
- fix chroot_mkdev (#11266).

* Wed Mar 14 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt1
- fixes:
  + remove unused /dev/fb0
  + remove ahci.ko from modules (pci id overlap) (TODO for propagator)
  ldv@:
  + spt.spec: Bump hasher version requirement to ensure working hsh-fakedev(1)
  + spt/scripts/spt, spt/scripts/spt-sh-functions: Remove deprecated --save-fakeroot usage
  + spt/scripts/spt-sh-functions (chroot_mkdev): Fix hsh-fakedev invocation

* Tue Feb 27 2007 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt0.1
- new release:
  + remove /dev/pts,/proc addiction and ugly triggers
  + remove internal hasher hacks like makedev_console=1
  + remove obsoleted profile-ovz (moved to separate package)
  + strict hasher requires (due hsh-fakedev).

* Fri Feb 16 2007 LAKostis <lakostis at altlinux.org> 0.5.3-alt1
- 0.5.3 release:
  + remove unused mkiso option
  legion changes:
  + Add missing variable THEME in hooks
  + Code cleanup
  + Remove COMPONENTS_ID variable
  + Add support of remote repositories
  + Remove obsolete gfxboot/memtest code
  + Add new hooks to make gfx bootlogo and memtest

* Tue Feb 06 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5.2-alt1
- merge with legion:
  + Add new options to able redefine $tmpdir and $outdir
  + remove deprecated REPO
  + remove unused directories

* Wed Jan 31 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5.1-alt1
- add forcedeth.ko to stage1 modules
- unset mkboot when mkiso=
- cleanup ovz profile
- update profiles (add symlinks to common hooks)
- update rescue profile (add mdadm to packages)
- hotfixes:
  + fix ovz profiles creation
  + add ata_piix.ko to modules
- update copyrights (add legion@)
- bump version in sh-functions

* Sat Jan 20 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt1
- Major update.
  + remove deprecated CLASS
  + add new rescue profile
  + update docs for LiveCD creation
  + allow symlinks in hooks
  + update profiles to new scheme (see spt.txt for details)
  + rewrite setup.d/postinstall to hooks.d
  + move common hooks.d to hooks-common (mostly it root useradd and resolv modification)
  + update modules list for live (add ahci/jmicron and pata_marvell)
  + remove gfxboot from syslinux/isolinux.cfg in livecd (it's for installer)
  + add more advanced hooks for livecd (locale/console config)
  + update packages for livecd
  + replace KERNEL var to KERNEL_ADD (for adding modules and kernel to initrd)
  + remove skip-root switch (don't work due mktemp use).
- sync changes from legion:
  + Move code for bootlogo in standalone function.
  + COPYONLY image may have empty 'packages' file.
  + Make imgdir and isodir for COPYONLY images:
    + isodir used for final iso-image generation.
    + imgdir used for per-stage image generation.
  + Add IMGDIR and ISODIR to hooks environment. Hooks in
    COPYONLY image should move needful data from IMGDIR to
    ISODIR.
  + Update installer profile.
  + spt-sh-functions: Fix print_uris for new scheme.
  + spt:
       - Move workdir/{out,tmp} into temprary directory.
       - Add new option --no-cleanup to not remove temprary directory.
       - Fix bug in packages installation in make_image(). Packages
         from $IDENT/packages could not be installed at all.
       - Code cleanup.
  + Large achitecture modifications.
    spt:
       - Split main loop in to several functions.
       - Split image creation loop and copyonly loop.
    spt-sh-functions:
       - postinstall: Add IMGDIR variable.
       - postinstall: Fix hooks loop.
  + Move configs for images in subdirs and update installer profile
  + Fix hooks and add new option
  + spt, spt-sh-functions:
       - Add new option --number=NUM.
       - Rewrite hooks.
       - Hooks moved to PROFILE_DIR/IDENT/hooks.d directory.
       - Remove obsolete variable.
       - Remove DIRS config variable. Packages list defined by PROFILE_DIR/IDENT/packages file.
       - Remove gen_repo. Use hooks for it.

* Sun Dec 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4.0-alt3
- Apply fixes from legion:
  + move iso creation to chroot;
  + code cleanup;
  + speedup build.

* Wed Dec 06 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4.0-alt2.1
- maintenance release w/ fixes from legion@:
  + spt-sh-functions: Fix to make in chroot /dev/{ptmx,tty,console}. WARNING!
    Now you need special hasher setup for spt! You must set allow_ttydev=YES
    parameter in hasher-priv.conf. See hasher-priv.conf(5) for details.

* Sun Dec 03 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4.0-alt2
- move all boot actions to chroot (making it more independed from host arch).
- remove requires to hasher-priv and syslinux.
- update initfs for new propagator.
- cleanup mkmar invocation.
- move syslinux in chroot (legion).
- code cleanup (legion).
- Use getconf to define LIB and LIBDIR (legion).

* Tue Nov 28 2006 L.A. Kostis <lakostis@altlinux.ru> 0.4.0-alt1.3
- Small fixes:
  + fix typo in print_uris;

* Wed Nov 08 2006 L.A. Kostis <lakostis@altlinux.org> 0.4.0-alt1.2
- Small fixes & cleanups:
  + rework isolinux actions.

* Tue Oct 31 2006 L.A. Kostis <lakostis@altlinux.org> 0.4.0-alt1.1
- Small fixes & cleanups:
  + fix tgz typos;
  + fix isolinux dir;
  + cleanup code in mkfs.

* Mon Oct 30 2006 L.A. Kostis <lakostis@altlinux.org> 0.4.0-alt1
- New version:
  + fixes for installer build (update profile, rework INSTALL2HASH);
  + remove unwanted code (like kernel version autoguessing);
  + rework image creation process, now it's fully separate from build
    host (fix for #10069);
  + new switch --no-boot (skip boot procedures);
  + always do --noiso for --no-boot;
  + remove deps on hasher internals (like chrootuid1).
  Fixes from Alexey Gladkov (legion@altlinux):
  + totally remove deps on hasher internals (now we require only hsh* utils);
  + fix bashizm in spt script;
  + code cleanup;
  + always do ptmx entries in /dev (remove --maketty switch and makedev hacks);
  + fix spt-install (remove deps on hasher internals).

* Wed Oct 04 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt5
- always do --noiso for tgz2/tgz images;
- remove cpio image (it really useless) and comment out untested
  (like ext2/cramfs/cloop);
- sync changes from rider@ git repository;
- fix #10016 (tnx to raorn@);
- fix #10069 (a bit hacky - just add squashfsprogs to packages list);
- fix #9954 (remove man from packages list for ovz);
- remove squashfsprogs from Requires (due #10069);
- fix rights for /;
- fix resolv.conf and hosts generation (don't use host version).

* Thu Aug 17 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt4.1
- fix --excludedocs switch.

* Thu Aug 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt4
- improve ovz class:
  + replace mtab by /proc/mounts symlink;
  + replace /dev/tty12 by /var/log/syslog/console.

* Sun Aug 06 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt3
- fix typo in tbz2;
- fix ovz profile (add missing modules file);
- fix package list for ovz profile (add iptables as needed by kernel).

* Fri Jul 14 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt2
- Fixed tgz/tbz2 image creation.

* Sun Jul 09 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.1-alt1.1
- update profiles and post scripts for install.
- prepare for git.

* Thu Jul 06 2006 LAKostis <lakostis at altlinux.ru> 0.3.1-alt1
- update for cross builds (--arch parameter).
- add in-chroot operation support (this helps cleanup buildrequires).

* Sun Jul 02 2006 LAKostis <lakostis at altlinux.ru> 0.3-alt1
- update, added some useful abilities:
  + OpenVZ support (use class ovz)
  + tar + gzip/bzip2 image creation support
  + update module list for live/install

* Fri Jan 27 2006 Kachalov Anton <mouse@altlinux.ru> 0.2-alt1
- update, bugfixes

* Thu Sep 22 2005 Kachalov Anton <mouse@altlinux.ru> 0.1-alt1
- first build
