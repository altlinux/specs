Name: installer
Version: 1.5.1
Release: alt1

Summary: Installer common parts
License: GPLv2+
Group: System/Configuration/Other

Source: %name-%version.tar

BuildRequires: glibc-devel-static

%description
This package contains common installer parts.

%package common-stage2
Summary: Installer common stage2
Group: System/Configuration/Other
Provides: %name-stage2 = %version-%release
Obsoletes: %name-stage2 < %version-%release
# installer-preinstall.desktop
Requires: alterator-preinstall
# scripts/install2
Requires: alterator-wizardface alterator-backend-x11 >= 0.21-alt2 xinit xinitrc xorg-x11-server xorg-x11-drv-video
# scripts/postinstall
Requires: eject
# initinstall.d/10-vt.sh
Requires: bash console-vt-tools
# initinstall.d/30-hal.sh initinstall.d/50-removable preinstall.d/01-hal.sh
# Requires: dbus hal

Requires: xorg-xvfb

Conflicts: alterator-pkg < 1.2-alt1, alterator-sysconfig < 0.6-alt1, alterator-datetime < 2.0-alt1
# stage2 and stage3 are mutually exclusive
Conflicts: %name-common-stage3

%description common-stage2
This package contains common installer stage2 files and dependencies.

%package common-stage3
Summary: Installer common stage3
Group: System/Configuration/Other
BuildArch: noarch
Provides: %name-stage3 = %version-%release
Obsoletes: %name-stage3 < %version-%release
Requires: alterator-wizardface alterator-notes
# stage2 and stage3 are mutually exclusive
Conflicts: %name-common-stage2

%description common-stage3
This package contains common installer stage3 files and dependencies.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files common-stage2
%_bindir/*
%_sbindir/*
%_datadir/install2

%files common-stage3

%changelog
* Fri Mar 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1
- dont't copy xorg.conf to destdir

* Sun Mar 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.0-alt1
- don't set DPI to 80 if 800x600 failed

* Wed Sep 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.14-alt2
- btrfs added to expert-only FS

* Thu Sep 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.14-alt1
- 15-expert.sh fixed

* Tue Aug 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.13-alt1
- new cp-mwtadata from stanv@

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt4
- Unset no globbing parameter -f to copy my mask

* Fri Aug 12 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt3
- Fix path to alteratord.log

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt2
- Set exception on copy of non existed log file

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt1
- Copy pkg-install.log and alteratord.log to installed system

* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.11-alt1
- added nodesign command line option for automatic testing

* Tue May 31 2011 Michael Shigorin <mike@altlinux.org> 1.4.10-alt1
- terminate countdown at a key press (closes: #17338)

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.9-alt1
- ignore return code of get_local_metadata when nfs

* Wed Feb 23 2011 Anton Farygin <rider@altlinux.ru> 1.4.8-alt1
- add workaround for aufs /etc/hosts bug
- Go away from HAL (Andrey Stepanov)

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 1.4.7-alt1
- remove plymouth requires

* Tue Dec 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt5
- fixes from stanv@

* Fri Dec 03 2010 Anton Farygin <rider@altlinux.ru> 1.4.6-alt4
- ignore plymouth errors (fixed work without plymouth theme)

* Fri Dec 03 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt3
- stop plymouth before start X

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt2
- nfs installation fixed

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt1
- plymouth support

* Tue Nov 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.5-alt1
- fix for cp-metadata from stanv@

* Fri Oct 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt3
- direct vnc installation fixed

* Mon Oct 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt2
- step file for vm-ortodox added

* Thu Sep 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt1
- mounting /dev/pts added for -el kernel

* Tue Sep 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.3-alt1
- LVM / installation fixed by aspsk@

* Tue Jun 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.2-alt1
- next curl call improvements from stanv@

* Thu Jun 10 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.1-alt1
- curl call improvements from stanv@

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt2
- wait for network in VNC install

* Mon Mar 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt1
- installation via VNC support (boot parameters are similar with fedora)

* Wed Mar 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.4-alt1
- step file for alterator-grub added

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.3-alt1
- fix nfs installation

* Sun Dec 27 2009 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- add --omit-ide-modules to installkernel hook

* Mon Dec 07 2009 Stanislav Ievlev <inger@altlinux.org> 1.3.1-alt1
- add support for noeject parameter (don't eject media)
- add cmdline_has_arg() function (check for existance of some parameter in kernel args)
- sbolshakov@:
    ensure that etc X11 exists;
    introduce new cmdline parameter for remote metadata.

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- expand data paths to avoid chroot operation

* Thu Nov 05 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.14-alt2
- explicitly require alterator-wizardface at stage2 and stage3

* Wed Oct 21 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.14-alt1
- removed -e from /usr/sbin/alterator-install2, wrong killall or 
  'service stop' exit status should not break installation

* Thu Oct 15 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.13-alt2
- fix false alarms

* Wed Sep 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.13-alt1
- check for already run scripts added to postinstall

* Wed Sep 09 2009 Anton Farygin <rider@altlinux.ru> 1.2.12-alt1
- remove hal and dbus from stage3 requires
- run haldaemon and message bus if theirs was installed to stage3

* Thu Aug 27 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.11-alt1
- run postinstall.d hooks only if system was marked as a new

* Thu Aug 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.10-alt1
- added handling 'expertmode' in command line

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.9-alt2
- Cleaned up manual dependencies.
- install2-action-functions: Append timestamp if not in color mode.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.9-alt1
- scripts/alterator-install2: Updated from image-scripts.d/01xorg.
- scripts/install2: Parametrized xserver args, added -nolisten tcp by default.

* Mon Mar 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt2
- Added conflicts for mutually exclusive subpackages.

* Thu Mar 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt1
- Updated steps.

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.7-alt1
- 50-removable reverted

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.6-alt1
- fixed initrd generation in installer/preinstall.d/50-initrd.sh

* Tue Mar 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Removed obsolete hooks:
  initinstall.d/50-removable
  preinstall.d/60-nfs.sh
  preinstall.d/99-ldconfig.sh

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.4-alt1
- Moved preinstall stage into separate package alterator-preinstall.
- Moved firsttime script from preinstall into postinstall.

* Mon Mar 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.3-alt1
- Fix from ldv@ for 99-cdrom.sh

* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- install2-init-functions (exec_chroot): Forward DURING_INSTALL variable.
- install2-init-functions: Deprecated run_chroot(), made it an alias to exec_chroot().
- preinstall.d/*: Replaced run_chroot() with exec_chroot().

* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Removed obsolete backend2/deadline (Stanislav Ievlev).
- Updated BuildRequires.
- Added "common-" prefix to subpackages.
- Cleaned up makefiles and scripts/*.
- install2-init: Changed to list filesystems which remains mounted only once.

* Wed Mar 11 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- install2-init: Fixed loop_change_fd (Michail Yakushin).

* Fri Feb 06 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt2
- switch to aufs usage. You should resurrect fs/exportfs.ko in your
  profiles/install2/image-scripts.d/999system

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- join datetime and tzone steps

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- run postinstall scripts from $destdir/$postinstall_dir and $postinstall_dir

* Wed Jan 21 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- move basesystem installation to alterator-pkg package

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- add step for sysconfig-base

* Thu Nov 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- fix build with gcc-4.3
- add new native backend

* Thu Oct 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- use alterator-sh-functions instead of backend3.sh

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt30
- add XORG_CONF definition to install2

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt29
- fix Requires: alterator-backend-x11

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt28
- add fallback to all drivers returned by vcscan

* Wed Sep 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt27
- preinstall.d/10-xorg.sh: fix breackage of InputDevice section

* Fri Sep 19 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt26
- fixed creating xorg.conf for nvidia

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt25
- change fbdev and vesa fallbacks in install2

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt24
- fixed remove-if-removable scripts with mike@

* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt23
- add steps/sysconfig.desktop

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt22
- fixed error from grep when CDROM installation

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt21
- update step files translations

* Thu Sep 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt20
- starting HAL after basesystem installation

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt19
- starting hal before x11_autosetup

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt18
- use new x11_autosetup options for setting xdriver and xres

* Wed Sep 03 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt17
- added sources.installer list when installing from removable devices

* Tue Sep 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt16
- really skip devices ;)

* Fri Aug 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt15
- fix bug in previous feature

* Thu Aug 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt14
- skip removable devices  from destination fstab

* Wed Aug 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt13
- fixed excluding usb media

* Fri Aug 15 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt12
- changeble fonts in stage2

* Thu Aug 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt11
- move icons to steps subdir

* Tue Jul 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt10
- move creation of xorg.conf from install2 to initinstall.d/30-xorg.sh
- fix problem with xdriver=auto

* Tue Jul 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt9
- add sleep 1 at the end of alterator-install2 (see #16450)

* Fri Jul 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt8
- add Requires: hal dbus to stage2

* Tue Jul 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt7
- modify preinstall.d/10-xorg.sh: create new xorg.conf for system,
  do not copy installer's xorg.conf

* Tue Jul 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt6
- kill console-kit-daemon too (by rider)

* Tue Jul 01 2008 Anton Farygin <rider@altlinux.ru> 0.7-alt5
- stop hal and dbus before alterator-wizard

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt4
- set 800x600 resolution for X

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt3
- fix scripts/install2, modify Requires

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- fix scripts/install2

* Fri Jun 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- remove initinstall.d/30-xorg.sh (configuration of xorg.conf)
- configure xorg.conf in scripts/install2 using x11_autosetup from new alterator-x11
- add preinstall.d/10-xorg.sh for copying xorg.conf to destination system

* Thu Jun 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5
- modify for new alterator-x11 (require hal, dbus)

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- update documentation

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3
- document:replace -> frame:replace

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- first run preinstall scripts from installed system

* Wed May 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- drop unionfs usage by sbolshakov@

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- remove rest of dependencies on alterator-autoinstall package

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- move logfile copying to postinstall scripts
- improve splash support

* Thu May 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- step files: use help files from modules
- remove autoinstall backend usage
- basesystem,preinstall: use colspan, remove inmplicit text attributes for labels, add help
- remove unused .scm files

* Wed May 14 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt17
- splash support
- exclude SCSI cdrom devices

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt16
- move preinstall.d to new alterator-net-eth
- update url of the installer-network step

* Thu Apr 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt15
- updated for new alterator-net-eth

* Wed Apr 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt14
- yet another merge (ldv@, sin@)
- fix reexec

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt13
- merge code improvements from @ldv and @sin
- move preinstall.d/pkg-groups to alterator-pkg

* Wed Apr 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt12
- add support for nonanonymous ftp servers (#14697)
- fix work with empty DNS_SERVER (#14966)

* Tue Apr 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt11
- @ldv: install2-init.c (killall): Do some sleep after sending SIGKILL

* Mon Apr 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt10
- fix install2-init abnormal exit (by ldv@, sin@)
- use control to switch portmap status

* Thu Mar 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt9
- use ALTERATOR_DATADIR

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt8
- added kernels sorting
- run installkernel in normal mode (without DURING_INSTALL)

* Mon Mar 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt7
- replace installer-finish with release-notes

* Fri Feb 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt6
- build to Sisyphus

* Thu Feb 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt5.1
- exclude a whole boot device

* Wed Feb 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- fix typo

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- kill before loop_change_fd

* Thu Feb 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- move last loop_change_fd into init

* Tue Feb 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- ignore eject failure
- improve sources layout
- improve install2-init:
  sleep between sigterm and sigkill
  more messages during kill process
  fix typo in messages

* Tue Feb 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- fix /mnt/destination umount in multidisk installation

* Wed Jan 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt9
- fix help refs in users-root and users-add steps

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- global DURING_INSTALL export

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- update docs
- patch from boyarsh: added -f option to openvt to avoid 'vt is already in use' bug

* Fri Dec 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- xorg tuning: add mouse_autosetup call (need to use serial mices)

* Mon Nov 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- common find-free-partition utility
- common CDROMDEV variable
- new preinstall script: try to free cdrom device

* Mon Nov 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- build system improvements (split C-sources and shell scripts)
- move main global variables to install2-sh-functions
- move unionfs code to common place
- add losetup-mv utility

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- add missing requires to stage3
- add support for multiple xdriver= (to allow xdriver defaults tuning)

* Tue Oct 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- fix firsttime script
- move openvt start to initinstall.d script

* Fri Oct 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update documentation

* Wed Oct 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- replace get-manifest with common cp-metadata utility
- add support for pkg-groups profile
- move old apt-profile.scm copying into preinstall script
- add initinstall.d feature (tuning before installator start)

* Thu Oct 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- fix icon names

* Mon Oct 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- backports from desktop branch
- turn off splash at the end of install

* Fri Oct 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add default finish step (installer-finish)

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- new profile system

* Mon Sep 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- improve nfs support
- move finish step to distribution specific package

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- move language step and i18n preinstall hack into common sysconfig package

* Wed Sep 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- move license step into separate package

* Fri Sep 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- remove conflict between stages

* Tue Aug 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- rename to installer

* Thu Mar 08 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt7
- Rewrite Date/Time step.

* Wed Feb 21 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt6
- Fix network settings.

* Mon Feb 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt5
- UI optimazations.
- Change bootloader stage.
- Broke autoinstall.
- Remove net-tcp stage.

* Thu Feb 08 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt4
- Add 'ai' parameter.
- Fix package for new udev-105.
- Fix autoinstall.
- Fix cdrom method.

* Fri Jan 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt3
- Add autoinstall.
- Add ftp/http install methods.
- Avoid using libhw-tools.
- Use swap.
- UI optimizations.

* Wed Jan 10 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt2
- Marge install2 and install3 stages.
- Remove useless UI step.
- UI optimizations.

* Fri Nov 17 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt4
- Initial revision.
