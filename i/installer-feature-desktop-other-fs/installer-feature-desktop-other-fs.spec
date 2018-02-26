Name: installer-feature-desktop-other-fs
Version: 0.6
Release: alt3

Summary: Mount existing filesystems too
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Mount existing filesystems too
License: GPL
Group: System/Configuration/Other
Provides: installer-feature-other-fs
Conflicts: installer-ltsp-school-stage2

%description stage2
%summary

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%changelog
* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt3
- stage2: Drop depend on installer-stage2.

* Mon Jun 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- crypto_LUKS exclusion added

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- don't mount filesystems in installer as os-prober can't work
  correctly with evms

* Tue Oct 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- added linux_raid_member skip
- mounting system fixed

* Tue Apr 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- really mount ALL availible filesystems for os-probe

* Wed Apr 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- fixed LVM2_member skip

* Mon Apr 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- mount filesystems after adding to fstab for os-probe

* Tue Sep 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt5
- fix to conform new installer

* Fri Aug 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- fixed work when no removable

* Thu Aug 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- removable devices skip added

* Thu Jul 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- fixed bug with appending partitions, already listed in fstab

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- based on 40-add-partitions from installer-ltsp-school,
  heavily cleaned up and fixed (NB: no longer used there
  since autopartitioning would destroy the rest anyways)

