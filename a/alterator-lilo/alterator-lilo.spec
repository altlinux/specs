Name: alterator-lilo
Version: 1.8.2
Release: alt2

Summary: alterator module for lilo setup
License: GPL
Group: System/Configuration/Other

Source:%name-%version.tar

Requires: alterator >= 4.10-alt6
Requires: alterator-sh-functions >= 0.6-alt1
Requires: alterator-hw-functions >= 0.4-alt1
Requires: libshell
Requires: lilo e2fsprogs sfdisk fdisk sed grep sysfsutils

BuildPreReq: alterator >= 4.10-alt6
BuildRequires: libdevmapper-devel

%description
alterator module for lilo setup

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_datadir/alterator/applications/*
%_datadir/alterator/steps/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/%name

%changelog
* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt2
- rebuild with new libdevmapper versioning

* Fri Feb 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.2-alt1
- quiet* added to list of options got from /proc/cmdline

* Wed Feb 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.1-alt1
- set 1 second wait by default if there is only one system

* Fri Dec 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt14
- lilo-other-system.sh/add_kernels():
 -  avoid non-zero return value
 -  fix regexp

* Thu Dec 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt13
- backend: add all installed kernels to new lilo.conf

* Wed Dec 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt12
- qt ui: fix type checking in (round-timeout t)
- update alterator-lc-functions; add tests for it

* Mon Sep 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt11
- backend: protect boot= parameter if user don't want to install
  bootloader (closes: #18679)

* Thu Aug 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt10
- lilo-disk.sh/find_others(): don't look for windows on extended
  partitions with 0xf type

* Wed Aug 12 2009 Stanislav Ievlev <inger@altlinux.org> 1.8-alt9
- little ui improvements
- remove some unused code from backend

* Thu Aug 06 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt8.2
- NMU: offer mdX if root is on software raid
  conflict between device name and boot parameter format, forbidden ':' symbol in device name
  (regression, was #17613)

* Wed Aug 05 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt8.1
- NMU: fix raid install

* Tue Jun 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt8
- lilo-disk.sh: fix get_part_with_mntpt to find correct 
  devices by uuid (closes: #20634)

* Fri Jun 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt7
- fix adding -b parameter
- localize some messages from lilo

* Wed Jun 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt6
- lilo-disk.sh: don't show unexisting mountpoints

* Tue Jun 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt5
- helpers/lilo-{parser,raid-boot}.sh: Fixed raidboot (closes: #20469).

* Thu Jun 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt4
- fix root device search in installer

* Fri Jun 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt3
- fix evms_protection()

* Thu Jun 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt2
- use /mnt/destination/etc/fstab in installer's environment

* Wed Jun 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- lilo-disk.sh: use /etc/fstab instead of /proc/mounts for
  finding device mountpoints
- lilo-conf.sh: use "UUID=..." instead of "/dev/disk/by-uuid/..."
  for root parameter (closes: #20292)
- avoid more error messages

* Tue Jun 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- avoid error messages about broken pipes

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt2
- add step file

* Thu May 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- backend: add udevadm trigger/settle on startup
- allow using in installer's stage2

* Fri May 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- add LILO_LITE, LILO_STAGE2 controls

* Wed Apr 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- use alterator-hw-functions

* Thu Feb 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt6
- fix lilo-disk.sh helper

* Tue Feb 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt5
- fix lilo-disk.sh helper

* Mon Feb 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt4
- fix lilo-disk.sh helper

* Thu Feb 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt3
- fix get_part_with_mntpt() for lvm partitions

* Thu Feb 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- don't show empty bootloader place

* Wed Feb 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- add list_bootloader_places() instead of
  list_hard_drives() + get_boot_part()
- change bootloader places list (fix qemu installation)

* Tue Feb 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt5
- get_part_with_mntpt: use ID_FS_USAGE from evms device

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt4
- fix typo in get_part_with_mntpt() (by mithraen@)

* Fri Feb 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt3
- fix get_part_with_mntpt()

* Wed Feb 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt2
- lilo-disk.sh helper: fix disk sizes and root device

* Tue Feb 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- HAL-free version. Use udevadm+sysfs+sfdisk+lilo to collect system information.
- Search for default place for bootloader in bios.

* Thu Jan 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt7
- fix translation in desktop-file

* Thu Jan 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt6
- use translations and help from alterator-l10n

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt5
- helpers/lilo-hal.sh: fix problem with volumes which can not be found by hal (lvm)

* Mon Dec 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt4
- fix helpers/lilo-parser.sh
- fix expert UI
- add master-boot settins for autodetected Windows sections
- replace expert boot-as setting by master-boot

* Mon Dec 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt3
- fix alignements in expert UI
- fix expert UI
- remove po-domain from backend

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt2
- don't install help

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- use help from alterator-l10n
- rewrite expert UI
- show apply and reset buttons in edit lilo.conf UI in installer
- some tests on new sections in lilo-parser.sh
- lilo testing dryrun with real command line options
- fix read dev action in backend
- use -efu in backend

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt33
- fix helpers/lilo-conf.sh

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt32
- broken evms workaround (install bootloader to evms device)

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt31
- rebuild with new alterator-l10n

* Wed Dec 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt30
- don't convert boot dev to UUID=... on lilo.conf writing

* Wed Nov 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt29
- protect current boot device from being lost by simple interface
- move write_enum_item functions from helpers to backend

* Thu Nov 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt28
- remove update_menus from spec (thanks to repocop)

* Sat Nov 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt27
- update help

* Wed Oct 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt26
- fix backend for working with devices with - in names
- fix lilo-other-system.sh

* Wed Oct 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt25
- 2 digits after point in disk sizes
- fix problem with translation of other systems labels

* Tue Oct 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt24
- fix template lilo.conf

* Mon Oct 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt23
- hack get_part_with_mntpt for raid+evms

* Fri Oct 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt22
- fix bootable flags setting
- fix raid capabilities

* Thu Oct 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt21
- fix label for failsafe section
- rewrite lilo-bootable-flag.sh
- show raids as partitions, not as disks
- get_default_boot_dev returns raidboot if it exists

* Thu Oct 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt20
- debug -> verbose in lilo-fix-cdrom.sh
- fix error with labels for other systems
- move dev2sym tests from lilo-hal to dev2sym
- sort partitions numerically
- change hal property info.product to storage.model in disk labels
- skip raid members in partition list

* Wed Oct 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt19
- fix labels for other systems
- prevent default boot disk to be removable

* Mon Oct 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt18
- write globals when change mode from the expert one
- ui/lilo/index.scm: remove nested (woo-catch/message
- protect device names by symlinks /dev/disks/by-id/*
- misc fixes

* Fri Oct 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt17
- skip removables in disk list
- fix error with leading zeros in arithmetics (we dont want oct values!)

* Thu Oct 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt16
- remove (with-translation), remove implicit attribute in (label)

* Fri Sep 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt15
- fix makefile - 2

* Fri Sep 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt14
- fix makefile

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt13
- rebuild with new alterator-l10n

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt12
- tune ui

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt11
- rebuild with alterator-l10n

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt10
- turn backend debug messages off
- change label in desktop-file (Bootloader (lilo) -> Bootloader)

* Tue Sep 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt9
- fix helpers/lilo-hal.sh (mountpoints)

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt8
- fix helpers/lilo-hal.sh (hal does not understand devices /dev/evms/sda1)

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt7
- fix helpers/lilo-hal.sh (hal can't get mount_point in installer's chroot...)

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt6
- fix helpers/lilo-hal.sh

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt5
- remove woo-write/constraints

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt4
- fix helpers/lilo-hal.sh

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt3
- install tests

* Mon Sep 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- fix helpers/lilo-hal.sh

* Thu Sep 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- use hal

* Mon Sep 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt8
- show /boot partition name in simple interface "Linux partition (hda5)"

* Fri Sep 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt7
- fix work with new enumref (explicitly print label)

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt6
- improve timeout round function
- improve help (cas@)

* Fri Jul 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt5
- if install=="text" remove message parameter,
  else message=/boot/splash/message (fix #16217)

* Mon Jul 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt4
- use decimal point from LC_NUMERIC in hard drive labels

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt3
- fix labels

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt2
- rebuild with new alterator-l10n

* Tue Jul 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt1
- add some controls in simple mode

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt10
- rebuild

* Thu Jun 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt9
- fix bug with confonly setting in expert mode

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt8
- change labels for interface types

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt7
- add commiting lilo.conf in expert mode interface (fix #16162)

* Tue Jun 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt6
- fix adding default current device

* Tue Jun 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt5
- fix translations for disk sizes

* Tue Jun 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt4
- add default current device
- add translations for disk sizes (Gb/Mb/Kb)

* Tue Jun 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt3
- remove help message from installer
- remove bootable flag check in other system search
- change label for other OS (partition types: 81|83|85|88|8e|f0|fd) Other->Linux

* Mon Jun 23 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt1
- add other sections to simple-mode interface

* Fri Jun 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- simple interface with radiobuttons only
- fix parameters with "-" (raid-extra-boot, read-only and others)

* Fri Jun 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- Interface: new simple mode + expert mode from 0.4-alt13 + edit-source

* Wed Jun 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- use install-module rule, remove translation from desktop file

* Mon Jun 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- remove expert mode interface
- new simple mode interface

* Mon Jun 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- rewrite backend output to fit alterator_api_version=1

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- rewrite read action in backend

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- remove constrains action

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- use alterator_api_version=1
  Requires: alterator-sh-functions >= 0.3-alt4

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- remove in_part usage from backend

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt13
- rearrange expert interface to fit to installer

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt12
- rearrange expert interface to fit it to 800x600

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt11
- rebuild with new alterator-l10n

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt10
- remove "map" parameter writing from backend.
  (fix bug with bad lilo.conf with map="")

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt9
- add "don't install bootloader" checkbox to "edit lilo.conf" dialog"

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt8
- use enumrefs

* Fri Jun 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt7
- remove pot-file

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt6
- rewrite new/update-section functions
  fix problem with modifying existing sections
- modify write_params to write empty values!

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt5
- simplification of "edit lilo.conf" dialog

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt4
- fix bug with duplication of global "append" parameter
  (use /proc/cmdline params only when lilo.conf is initially created)

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- fix append/addappend confusion in section parameters

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- change parameter boot-as -> boot_as for use with new alterator-sh-functions

* Thu Jun 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- join extra-global and extra-sections interfaces
- fix labels
- remove "skip bootloader installation" checkbox

* Tue May 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt10
- remove duplicated "Set Default" button

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt9
- remove alterator-autoinstall usage
- fix package dependencies
- remove po files

* Thu May 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt8
- change labels in QT UI

* Thu May 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt7
- fix bug with "skip bootloader" checkbox

* Tue May 13 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt6
- use quote_sed_regexp() and quote_shell() from libshell
- use ui/*/index.scm catalog structure
- fix qt ui

* Mon May 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt5
- fix labels

* Mon May 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt4
- move ":" back to (_ )
- simple_quote -> string_quote, error -> write_error in backend
- use alterator-l10n

* Mon May 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt3
- change label "Install" (menu/text) to "Interface"
- remove "Map" parameter from interface
- move ":" from the (_ )

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2
- fix labels and translations

* Tue May 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- autodetect other systems only if lilo.conf does non exists
- join dialogs for linux and other sections:
  - lilo-parser.sh/show_sections_list - returns all sections with "type" field
  - lilo.in/list - returns all sections with "type" field
  - modify extra-sections.scm
- change labels:
  - View source -> Edit source
  - Other -> Device

- Remove section existance test in lilo-parser.sh/create_section()
  Now update_section rewrites all the existing section

* Wed Apr 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt6
- remove radiolists
- add /sbin/ paths to fdisk, sfdisk and lilo

* Wed Apr 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt5
- change Name in desktop-file
- changes in QT UI:
  - remove Quit button 
  - change ru translation for Apply button
  - remove password settings (qt only, not backend)
  - rearrange gridboxes with text fields
  - rearrange Apply/Reset buttons

* Sun Mar 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4.1
- fix typo

* Sun Mar 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- remove ALTLinux from labels

* Fri Mar 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- fix translation
- use alterator-sh-functions

* Thu Feb 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2.3
- add internal help
- build for Sisyphus and 4.0

* Mon Feb 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2.2
- quick fix for extra options
- added X-Alterator-UI=qt

* Wed Dec 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt2
- Fix 'activity' in installer mode.

* Tue Dec 11 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt1
- Add 'compact' option in default lilo.conf .
- Add 'View source' mode to change lilo.conf directly.
- Add workaround for free cdrom.
- Ignore comments in the lilo.conf .
- Allow write lilo.conf without boot loader installation.
- Optimize image rename.

* Thu Oct 04 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt5
- Add packager.

* Thu Sep 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt4
- russian & ukrainian translations resurrected

* Wed Aug 22 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt3
- Fix reset global params.
- Add gfxboot support.
- Add kernel bootsplash support.

* Wed Aug 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2.1
- port fixes for automatic boot device recognition

* Tue Aug 21 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt2
- Fix temp files.

* Fri May 25 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial release
