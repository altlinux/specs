Name: installer-distro-workbench
Version: 5.0
Release: alt2

Summary: Installer common files
License: GPL
Group: System/Configuration/Other

Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: alterator rpm-devel

%define feature installer-feature-desktop

%description
Installer common files

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-license
Requires: alterator-datetime openntpd
Requires: alterator-vm
Requires: alterator-pkg
Requires: x-cursor-theme-jimmac
#features
Requires: %{feature}-disable-mktemp-stage2
Requires: %{feature}-other-fs-stage2
Requires: %{feature}-suspend-stage2
Requires: %{feature}-disable-remote-stage2
Requires: installer-feature-hwtweaks-stage2
Requires: installer-feature-runlevel5-stage2
Requires: installer-feature-eth-by-mac-stage2
Requires: installer-feature-set-tz

Provides: installer-lite-stage2
Provides: installer-workbench-stage2
Obsoletes: installer-workbench-stage2

%description stage2
Installer stage2

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage3
#modules
Requires: alterator-lilo
Requires: alterator-pkcs11
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: alterator-x11
Requires: installer-feature-nfs-client-stage3

Provides: installer-lite-stage3
Provides: installer-workbench-stage3
Obsoletes: installer-workbench-stage3
%description stage3
Installer stage3

%prep
%setup -q

%install
%makeinstall

%find_lang alterator-workbench

%files -f alterator-workbench.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu

%files stage3
%_datadir/alterator/ui/workbench

%changelog
* Tue Sep 29 2009 Alexey I. Froloff <raorn@altlinux.org> 5.0-alt2
- Fixed icon placement and names (cherry-picked from installer-desktop)

* Sun Sep 27 2009 Alexey I. Froloff <raorn@altlinux.org> 5.0-alt1
- Workbench installer based on Desktop

* Wed Aug 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- icon for Auth step fixed

* Thu Aug 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- vm-profile setting now smarter on small disks when package size > 2G

* Wed Jun 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- / size for minimal disks fixed in vm-profile 

* Wed Jun 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- vm-profile setting now smarter on small disks 

* Mon Jun 08 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- running sync every 30 sec removed

* Thu Jun 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- fix alterator-menu copying 

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- running sync every 30 sec added 

* Wed May 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- requires to alterator-root added 

* Wed Apr 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- added requires to alterator-datetime 

* Wed Apr 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- datetime step reverted
- setting timezone from kernel command line added

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- added autentification setup step 

* Thu Apr 02 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- renamed to installer-distro-desktop
- installer-feature-nfs-client-stage2 added
- added sorting for acc modules

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- fixed typo in vm-profile 

* Wed Mar 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- setting vm-profile fixed 

* Wed Mar 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- datetime step removed: time should be set via ntdp 

* Mon Feb 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- dnsmasq off by default 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- tzone joined with datetime 

* Thu Jan 22 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- fixed conflict with new installer 

* Tue Dec 16 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- possibility to use pae kernel for highmem installations 

* Thu Nov 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt3.M41.1
- port to M41 

* Thu Nov 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt4
- fixed color scheme setting for kdm 

* Thu Nov 13 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- fixed 60-pkg-groups in normal desktop 

* Tue Nov 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- fixed removimg emulators group when wine installed

* Mon Nov 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt19
- removimg emulators group when wine installed 

* Mon Nov 10 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt18
- dynamic selecting color scheme for kdm 

* Thu Oct 30 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt17
- fixed / size tuning 

* Fri Oct 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt15
- more size for / by default 

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt14
- run depmod after install, not at first boot 

* Tue Sep 30 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt13
- virtualbox service on by default 

* Mon Sep 29 2008 Michael Shigorin <mike@altlinux.org> 0.3-alt12
- disabled these most often unneeded services:
  anacron, smartd, evms, rawdevices

* Mon Sep 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt11
- added depmod into postinstall 

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt10
- added control calls for virtualbox and klaptop  

* Wed Sep 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt9
- kdm color scheme tuning 

* Fri Sep 05 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt8
- network step reverted, openvpn switched off 

* Wed Sep 03 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt7
- network step deleted 

* Fri Aug 08 2008 Michael Shigorin <mike@altlinux.org> 0.3-alt6
- merged with boyarsh@; changelog: renamed my
  0.3-alt5 -> 0.3-alt3.2,
  0.3-alt4 -> 0.3-alt3.1

* Wed Aug 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt4
- deleted hotplug tuning
- xdm tuning changed to gdm tuning

* Sat May 31 2008 Michael Shigorin <mike@altlinux.org> 0.3-alt3.2
- added "bind ethernet interfaces by MAC" feature

* Thu May 29 2008 Michael Shigorin <mike@altlinux.org> 0.3-alt3.1
- moved default runlevel setting to separate installer-feature

* Thu May 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- added setting default runlevel 
- changed last step

* Wed May 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- removed multydisks install support 

* Tue Apr 22 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- used installer-feature-* packages 

* Tue Apr 15 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt5
- do not remove alterator-autoinstall 

* Tue Apr 01 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt4
- do not remove alterator-lilo 

* Wed Feb 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt3
- fixed installation of desktop personal with <=128M RAM 

* Thu Feb 07 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- try to fix xdm crash 

* Mon Jan 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- fixed deleting installer packages  

* Mon Jan 14 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4.1
- fixed ntfs mounting 

* Mon Dec 24 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- fixed install without clamav 
- fixed first page setting
- xdm look changed

* Fri Dec 14 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- added hook to gemove gnumeric from menu 

* Fri Nov 30 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.5
- added list of groups for first user
- added multydisc install support

* Wed Nov 28 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.4
- fixed 60-*profile* 

* Mon Nov 12 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.3
- added vm-profile customization 

* Thu Nov 08 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.2
- added hook for inserting resume= into lilo.conf. template 

* Wed Oct 31 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2.1
- changed alterator-apt to alterator-pkg 

* Tue Oct 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- fix firefox homepage setup
- add russian manpages charset setup

* Wed Oct 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
