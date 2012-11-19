%define _altdata_dir %_datadir/alterator

Name: alterator-grub
Version: 0.8
Release: alt1

Summary: alterator module to setup grub bootloader
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

Requires: alterator >= 4.7-alt5
Requires: alterator-l10n >= 2.9-alt10
Requires: alterator-sh-functions >= 0.6-alt1
Requires: alterator-hw-functions >= 0.4-alt1
Requires: grub2 >= 2.00-alt4

BuildPreReq: alterator >= 4.7-alt5
BuildRequires: grub2 >= 2.00-alt4
BuildRequires: libdevmapper-devel

%description
alterator module to setup grub bootloader

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_altdata_dir/steps/*
%_alterator_backend3dir/*
%dir %_libexecdir/alterator/hooks/grub.d
%_bindir/*

%changelog
* Thu Nov 15 2012 Michael Shigorin <mike@altlinux.org> 0.8-alt1
- added initial EFI support

* Thu Nov 08 2012 Michael Shigorin <mike@altlinux.org> 0.7-alt5
- replace symlink with bindmount for grub 2.00

* Wed Nov 07 2012 Timur Aitov <timonbl4@altlinux.org> 0.7-alt4
- add hack for luks devices

* Thu Jun 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt3
- mike@: set default input focus to the combobox

* Mon Jun 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt2
- fix grub install into partition (ALT #25628)

* Mon May 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1
- add /dev/emvs/md hackaround

* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt2
- rebuild with new libdevmapper versioning

* Mon Jan 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- install into partition in installer fixed (ALT #24617)

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt4
- fisttime script moved to the grub2 package

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt3
- "one time system" effect fixed

* Tue Oct 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt2
- typo fixed

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- firttime script added

* Sun Oct 24 2010 Andrey Cherepanov <cas@altlinux.org> 0.4-alt2
- localize backend scripts

* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1
- allow grub install on partition using blocklists (ALT #24197)
- set GRUB_AUTOUPDATE_DEVICE and GRUB_AUTOUPDATE_FORCE options

* Tue Sep 21 2010 Anton Protopopov <aspsk@altlinux.org> 0.3-alt7
- Add dirty hack to install grub2 on lvm

* Mon Jun 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt6
- do not try to install bootloader on floppy (ALT #23687)

* Tue Jun 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt5
- do not try to install bootloader on cd/dvdrom

* Fri Apr 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt4
- include removable devices in proposed locations

* Mon Mar 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt3
- avoid conflict with alterator-lilo

* Fri Mar 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2
- reuse devmap_name from alterator-lilo

* Fri Mar 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1
- "skip bootloader install" added
- fix 'set bootable'
- fix typo

* Thu Mar 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt8
- simplify raid handling

* Wed Mar 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt7
- another fox for raid install
- more verbose error handling

* Wed Mar 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt6
- fix raid install

* Tue Mar 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt5
- fix grub-install fail on some devices

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt4
- just another possible installer fix

* Thu Mar 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt3
- possible installer fix

* Tue Mar 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2
- step file packaged

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- step file added

* Fri Mar 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial
