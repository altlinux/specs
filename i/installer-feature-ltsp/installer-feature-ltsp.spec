Name: installer-feature-ltsp
Version: 0.7.3
Release: alt1

Summary: Linux Terminal Server Project
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/LTSP
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%add_findreq_skiplist %_datadir/install2/postinstall.d/*

%description
%summary

%package stage2
Summary: Linux Terminal Server Project
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Requires: dhcpcd
Conflicts: installer-ltsp-school-stage2 < 0.4-alt4.12

%description stage2
%summary

%package stage3
Summary: %summary
Group: System/Configuration/Other
Requires: installer-feature-pxeboot-stage3
Requires: installer-feature-eth-by-mac-stage3
Requires: coreutils libshell sed

%description stage3
This package contains installer stage3 hooks for ALTSP

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/preinstall.d/*

%files stage3
%_datadir/install2/postinstall.d/*

%changelog
* Sat Mar 10 2012 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- fixed silly option omission

* Fri Mar 09 2012 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- added lightdm support

* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- inialize chroot's root password to that of the main system

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- rewrote to employ heuristics for better eth preconfiguration:
  + the fastest DHCP-configurable interface will be "inet" one;
  + the fastest one lacking DHCP replies will be "ltsp" one

* Tue Mar 06 2012 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- enable remote syslog

* Sat Nov 26 2011 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- adapt for t6/branch

* Thu Dec 30 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt2
- bump release

* Sun Nov 07 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- use installer-feature-pxeboot-stage3, not -stage2

* Sun Mar 14 2010 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- ltsp-nxclient renamed to ltsp-client-nxsession

* Sun Mar 14 2010 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- install ltsp-nxclient by default
- updated Url:

* Thu Mar 11 2010 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- introduced rc.sysinit optimization in a crude way
  (hopefully our startup will handle diskless
  r/o netbooting clients even better some day)

* Wed Mar 10 2010 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- added drm to KERNEL_MODULES (closes: #23103)

* Tue Feb 09 2010 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- added mc to default client chroot on amike's request

* Mon Dec 28 2009 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- reintroduced compcache

* Wed Dec 09 2009 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- added gdm support, thanks ktirf@ for control file (#17047)
- added kde4*kdm support

* Fri Jun 12 2009 Michael Shigorin <mike@altlinux.org> 0.2.9-alt1
- workaround unexpected -stage3 dependency on installer-common-stage2

* Thu Jun 11 2009 Michael Shigorin <mike@altlinux.org> 0.2.8-alt1
- use installer-feature-eth-by-mac-stage3 instead of -stage2

* Thu Jun 11 2009 Michael Shigorin <mike@altlinux.org> 0.2.7-alt1
- temporary hack: revert nfs setup breakage (see also #20421)

* Thu Jun 11 2009 Michael Shigorin <mike@altlinux.org> 0.2.6-alt1
- temporary hack: override led-tc

* Thu Jun 11 2009 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- s/led-tc/tmc-tc/

* Wed Apr 01 2009 Michael Shigorin <mike@altlinux.org> 0.2.4-alt1
- explicitly deny NetworkMangler's right to muck around
  with our precious interfacess
- reintroduced $cdrom_stage3 (hope it's temporary)

* Thu Mar 05 2009 Michael Shigorin <mike@altlinux.org> 0.2.3-alt1
- explicitly chkconfig dhcpd on

* Wed Mar 04 2009 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- create /media/cdrom in chroot just in case

* Wed Mar 04 2009 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- mv 99-ltsp 98-ltsp: thanks new and shiny 99-cdrom :(

* Fri Feb 27 2009 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- adapt for M50

* Thu May 08 2008 Michael Shigorin <mike@altlinux.org> 0.1.2-alt1
- require installer-feature-eth-by-mac

* Tue May 06 2008 Michael Shigorin <mike@altlinux.org> 0.1.1-alt2
- require installer-feature-pxeboot

* Mon Apr 21 2008 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- generate bootable ISO image for PXE-less thin clients (/opt/ltsp-boot.iso)

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk
- let's start with 98-eth0.sh, 99-ltsp.sh from installer-ltsp-school

