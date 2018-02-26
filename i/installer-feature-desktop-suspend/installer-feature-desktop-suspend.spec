Name: installer-feature-desktop-suspend
Version: 0.5
Release: alt3

Summary: Suspend/resume configuration
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
BuildArch: noarch

%description
%summary

%package stage2
Summary: Suspend/resume configuration
License: GPL
Group: System/Configuration/Other
Conflicts: installer-ltsp-school-stage2 <= 0.4-alt4.13

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

# TODO:
# - figure out whether lvm is suitable or detect/drop that too

%changelog
* Wed Sep 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt3
- zram swap skipping added

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt2
- stage2: Drop depend on installer-stage2.

* Mon Oct 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1
- switch to grub

* Tue Mar 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- rewritten without HAL

* Tue Oct 21 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- added lost chroots

* Fri Oct 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- rewrited to HAL usage and setting resume to /dev/disk/by-uuid

* Thu May 29 2008 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- shouldn't fail anyways (caught on swapless installation)

* Fri May 23 2008 Anton Farygin <rider@altlinux.ru> 0.2-alt1
- fix script for execution on system without swap

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- fix silly read-related thinko

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- script taken from installer-ltsp-school, fixed regarding
  swap on software raid (which isn't suitable for swsusp)
  and improved to accept some other swap device if there is one

