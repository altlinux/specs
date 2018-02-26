Name: ltsp-client-full
Version: 5.1
Release: alt0.12

Summary: ALTSP client package
License: Public domain
Group: Networking/Remote access

Url: http://www.altlinux.org/LTSP
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: ltsp-client >= 5.1
Requires: mingetty
Requires: passwd
Requires: udev
#Requires: x11setupdrv
#Requires: libhw-tools
Requires: syslinux
Requires: etcnet
Requires: openssh-clients
Requires: xorg-server
Requires: xorg-drv-video
Requires: xorg-drv-openchrome
Requires: xorg-dri-intel
Requires: xorg-drv-synaptics
Requires: xorg-drv-wacom
Requires: xorg-mesagl
Requires: xorg-utils
#Requires: ltsp-x11-autosetup ###
Requires: lbuscd
Requires: lp_server
Requires: ltspfsd
Requires: ltspinfod
Requires: nbd-client
#Requires: nbd-client-static
Requires: acpid
Requires: acpid-events-power
#Requires: nasd
#Requires: esound
Requires: pulseaudio-daemon pulseaudio-system
Requires: nfs-clients
Requires: dialog
Requires: Xdialog
#Requires: rdesktop
Requires: mkelfimage
Requires: ntfs-3g
#Requires: aumix-minimal
Requires: amixer
# for buggy udev's sound.agent
Requires: alsa-utils
Requires: firmware-linux
Requires: ltsp-sysreport

%ifarch %ix86
Requires: xorg-drv-geode
Requires: xorg-drv-i740
%endif

%description
ALTSP client package (it forms the client chroot).

%files

%changelog
* Fri Mar 09 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.12
- xorg-drv-geode, xorg-drv-i740 are i586-only

* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.11
- added xorg-drv-geode

* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.10
- added xorg-drv-i740

* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.9
- s/ethtool/ltsp-sysreport/

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.8
- (re-)added:
  + openchrome, wacom, synaptics xorg drivers
  + ethtool
- dropped:
  + aumix-minimal (no longer needed)
  + rdesktop (remmina should be reintegrated)

* Sun Feb 05 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.7
- added pulseaudio-system

* Sun Jan 29 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.6
- added xorg-dri-intel explicitly
- added firmware-linux

* Sat Jan 21 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.5
- added acpid-events-power (see also #25018)

* Fri Jan 20 2012 Michael Shigorin <mike@altlinux.org> 5.1-alt0.4
- dropped old Provides:/Obsoletes:/Exclusive*: (not really needed)
- whole package made noarch

* Mon Nov 28 2011 Michael Shigorin <mike@altlinux.org> 5.1-alt0.3
- deps cleaned up for t6+

* Tue Dec 22 2009 Michael Shigorin <mike@altlinux.org> 5.1-alt0.2
- dropped obsolete libhw-tools dependency

* Tue Feb 24 2009 Michael Shigorin <mike@altlinux.org> 5.1-alt0.1.1
- NMU: replaced alterator-backend-x11 dep with ltsp-x11-autosetup

* Sat Jun 21 2008 Led <led@altlinux.ru> 5.1-alt0.1
- ExlusiveArch: %%ix86 %%arm

* Sat Jun 07 2008 Led <led@altlinux.ru> 5.0-alt0.16
- Requires:
  + nbd-client-static
  + xorg-x11-extensions-xaudio

* Mon Mar 31 2008 Led <led@altlinux.ru> 5.0-alt0.15
- renamed ltsp5-client-full -> ltsp-client-full

* Tue Mar 18 2008 Led <led@altlinux.ru> 5.0-alt0.14
- Requires: xorg-x11-drv-openchrome

* Mon Mar 10 2008 Led <led@altlinux.ru> 5.0-alt0.13
- Requires: alterator-backend-x11 >= 0.13.1

* Sun Dec 23 2007 Led <led@altlinux.ru> 5.0-alt0.12
- added Requires:
  + lp_server
- fixed %%changelog

* Fri Dec 14 2007 Led <led@altlinux.ru> 5.0-alt0.11
- added Requires:
  + alsa-utils (for buggy udev's sound.agent)
  + aumix-minimal (for OSS)

* Sun Aug 19 2007 Led <led@altlinux.ru> 5.0-alt0.10
- removed Requires:
  + lp_server

* Tue Aug 07 2007 Led <led@altlinux.ru> 5.0-alt0.9
- replaced Requires:
  + alsa-utils with amixer

* Mon Aug 06 2007 Led <led@altlinux.ru> 5.0-alt0.8
- added Requires:
  + alsa-utils

* Sat Jul 28 2007 Led <led@altlinux.ru> 5.0-alt0.7
- added Requires:
  + mingetty
  + passwd
  + x11setupdrv

* Thu Jul 26 2007 Led <led@altlinux.ru> 5.0-alt0.6
- added Requires:
  + ntfs-3g
  + mkelfimage

* Thu Jul 12 2007 Led <led@altlinux.ru> 5.0-alt0.5
- added Requires:
  + pulseaudio-daemon

* Mon Jul 09 2007 Led <led@altlinux.ru> 5.0-alt0.4
- added Requires:
  + alterator-backend-x11

* Thu Jul 05 2007 Led <led@altlinux.ru> 5.0-alt0.3
- added to Requires:
  + acpid
  + xorg-x11-drv-synaptics

* Thu May 24 2007 Led <led@altlinux.ru> 5.0-alt0.2
- added Requires rdesktop dialog, Xdialog

* Tue May 15 2007 Led <led@altlinux.ru> 5.0-alt0.1
- initial build
