Name: hwdatabase
Version: 0.3.31
Release: alt1
Summary: Hardware list for the detections tools
Summary(ru_RU.UTF-8): База данных оборудования для утилит определения
License: GPL
Group: System/Libraries
BuildArch: noarch
Conflicts: pciutils <=  2.1.11-alt6
Conflicts: libhw <=  0.2.5-alt1
BuildRequires: pciids usbids
Requires: pciids usbids

Source: %name-%version.tar

%description
The hardware device lists provided by this package are used as lookup
table to get hardware autodetection.

%prep
%setup -q

%build

%install
%makeinstall DESTDIR=%buildroot

%files
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/misc/*
%_datadir/pci.ids

%changelog
* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.31-alt1
- add pnp.ids from http://git.fedorahosted.org/git/hwdata.git
- delete old pnp.ids from pcmcia-cs
- rm pci.ids and usb.ids; use from pciids and usbids package
- update classes
- update bus
- update MonitorsDB from http://git.fedorahosted.org/git/hwdata.git

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 0.3.30-alt1
- updated pci.ids and usb.ids

* Sun Jul 04 2010 Anton Farygin <rider@altlinux.ru> 0.3.29-alt1
- updated pci.ids and usb.ids

* Mon Feb 15 2010 Anton Farygin <rider@altlinux.ru> 0.3.28-alt1
- updated pci.ids and usb.ids

* Sat Jul 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.3.27-alt1
- updated pci.ids and usb.ids

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.3.26-alt1
- updated pci.ids and usb.ids

* Thu Mar 13 2008 Denis Smirnov <mithraen@altlinux.ru> 0.3.25-alt2
- add Seiros TI24 support

* Thu Mar 13 2008 Anton Farygin <rider@altlinux.ru> 0.3.25-alt1
- remove unused pcitable and Cards+
- updated pci.ids and usb.ids

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.3.24-alt5
- update MonitorsDB
- automatic update of pci.ids and usb.ids

* Mon Jul 02 2007 L.A. Kostis <lakostis@altlinux.ru> 0.3.24-alt4
- automatic update of pci.ids and usb.ids

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.3.24-alt3
- update MonitorsDB
- automatic update of pci.ids and usb.ids

* Mon Dec 18 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.24-alt2
- Update fglrx pci ids (synced with 8.32.5):
- Added:
  + R430 XTP (R430 XTP 554C)
  + R430 GL XT (R430 GL XT 5554)
  + R430 GL PRO (R430 GL PRO 5555)
  + Radeon X700 Series (RV410 (5657) 5657)
  + RV370X (RV370X 5B66)
  + R480 Consumer 4P (R480 Consumer 4P 5D4C)
  + R480 GL 12P (R480 GL 12P 5D51)
  + ATI Mobility Radeon X1450 (M64M 718A)
  + Radeon X1300 Series (RV516LE PCI 718F)
  + Radeon X1650 Series (RV535 XT (71C1) 71C1)
  + Radeon X1300 Series (RV535 PRO (71C3)
  + Radeon X1650 Series (RV535 (71C7) 71C7)
  + Radeon X1600 Series (RV530 71CD 71CD)
  + ATI MOBILITY FireGL V5250 (M66 GL 71D4)
  + ATI Mobility Radeon X1700 (M66-P 71D5)
  + RV550 (RV550 7200 7200)
  + Radeon X1950 Series (RV570 XT 7280)
  + ATI Mobility Radeon X1900 (M68 7284)
  + Radeon X1650 Series (RV560 7293 7293)
- Add Marvell 6101/45 PATA driver support (FIXME!).

* Sun Nov 19 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.24-alt1.1
- Add NVidia Geforce 7900 GTX support

* Wed Nov 15 2006 Stanislav Ievlev <inger@altlinux.org> 0.3.24-alt1
- automatic update of pci.ids and usb.ids
- update MonitorsDB

* Tue Nov 07 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3.23-alt1
- Massive update from internal git:
  - add AHCI drivers support ( 7dcb46335767e29186a38a5d78935291cb240b81 ):
    + add Intel chips support (from ICH6R to ICH8R);
    + add JMicron chips support (JMB360/JMB363);
    + add ULi chips support (M5288).
  
  - update QLogic support (add qla2312, qla2400, qla6312);
  - remove obsoleted qlogicisp
    ( faf93038dfce654e4460d9d96da818a4d089b835 )
  
  - fix megaraid support: remove bogus drivers and id's, add new id's and drivers (like _sas)
    ( 80e70685cf401bbf7be402d2fa9358a79fa57674 )
  
  - fix support for Fusion-MPT devices ( f6ca1a8d65e995421f1e147d32da47fe86828e7e ) :
    + rename mptscsih to mpt{fc,spi} as suggested https://bugzilla.altlinux.org/show_bug.cgi?id=8672;
    + fix support for 1000:0040 - according
      http://www.lsilogic.com/files/docs/techdocs/storage_stand_prod/SCSIICs/1035_tm.pdf
      it's actually MPT device;
    + add mptsas devices.
  
  - Update Radeon pciids (sync w/ 8.30.3 version) ( bd36d3d527db7ca63048bf9fec87b516d33b4866 ) :
    Added:
    + FireMV 2400 (RV380 3151)
    + RADEON X1300 PRO (RV505 7143)
    + RADEON X1300 (RV505 7147)
    + RADEON X1300 Series (RV505 715F)
    Removed:
    - Radeon 8500 AIW BB (AGP)
    - Radeon Mobility 9000 (M9) Lf (AGP)
    - Radeon Mobility 9000 (M9) Lg (AGP)
    - Radeon 9000/PRO If (AGP/PCI)
    - Radeon 9000/PRO Ig (AGP/PCI)
    - FireGL Mobility 9000 (M9) Ld (AGP)
    - FireGL 8700/8800 QH (AGP)
    - Radeon 8500 QL (AGP)
    - Radeon 9100 QM (AGP)
    - Radeon 9100 IGP (A5) 5834
    - Radeon Mobility 9100 IGP (U3) 5835
    - Radeon 9250 5960 (AGP)
    - Radeon 9200 5961 (AGP)
    - Radeon 9200 5962 (AGP)
    - Radeon 9200SE 5964 (AGP)
    - Radeon RV280 5965 (AGP)
    - Radeon Mobility 9200 (M9+) 5C61 (AGP)
    - Radeon Mobility 9200 (M9+) 5C63 (AGP)
    - Radeon 9000 PRO/9100 PRO IGP (RS350 7834)
    - Radeon 9000 PRO/9100 PRO IGP (RS350 7835)
    - unknown ids: 71C1 71D4 71D5
  
  - Update ATI Radeons database (sync with fglrx 8.28.8)
    ( 14383746b02651735f6bdec3efa08c047d0d3f37 )
  - Update SiS and VIA (XGI) cards (sync with Xorg-7.1)
    ( 544b069596f10513969bed6649464ed03d91f21c) 
  - Update ATI Radeons cards (sync with Xorg-7.1 and fglrx 8.27.4)
    ( d2f025adb98ea25bd81a1a57ed5b7aa2abcfac48) 
  - Update i9xx cards (sync with Xorg-7.1)
    ( a2a8079d4ea88d1b0ab02681d8f4b96b5178d0cc )
  - Update Intel NIC's database (sync with 2.6.16+)
    ( bdcfefa0b38962df061d6ceb382a7167f49aa271 )
  
  - turion64 X2 added ( 410c47113a601b21a706f344fb32ded77c8bca3d ) 
  - updated pci and usb ids ( b8548c2983816c85df743cd5ca84095cc968f394 )

* Fri Apr 28 2006 Andriy Stepanov <stanv@altlinux.ru> 0.3.22-alt1
- updated ids database
- Display information about PowerNOW for AMD processors

* Tue Jan 31 2006 Anton Farygin <rider@altlinux.ru> 0.3.21-alt1
- more fglrx, sata_sil
- updated ids database
- use via for Unichrome PRO

* Tue Dec 13 2005 Anton Farygin <rider@altlinux.ru> 0.3.20-alt1
- use VESA for Unichrome PRO
- updated ids database

* Mon Oct 24 2005 Anton Farygin <rider@altlinux.ru> 0.3.19-alt1
- use s3virge xorg driver for S3 Inc. 86c368 (#8209)

* Fri Oct 14 2005 Anton Farygin <rider@altlinux.ru> 0.3.18-alt1
- added Geforce4 MX 4000 (#7798)
- added some ACER montors to monitorsdb

* Wed Oct 05 2005 Anton Farygin <rider@altlinux.ru> 0.3.17-alt1
- AlpsPS/2 ALPS GlidePoint added
- ATI X700, X200 added
- fixed driver for Radeon 9200SE

* Wed Aug 17 2005 Anton Farygin <rider@altlinux.ru> 0.3.16-alt1
- more sk98lin, forcedeth, tg3 cards
- updated nvidia data for last nvidia_glx drivers
- updated usb.ids and pci.ids
- rewrited config for "GenPS/2 Genius Wheel Mouse" (#7561)

* Thu Aug 04 2005 Anton Farygin <rider@altlinux.ru> 0.3.15-alt1
- more ide controllers added
- updated usb.ids

* Thu Jul 07 2005 Anton Farygin <rider@altlinux.ru> 0.3.14-alt1
- updated cpu database (greycat@)
- updated usb.ids

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 0.3.13-alt1
- added second i915 adapter, reported by raorn@

* Fri Jun 24 2005 Anton Farygin <rider@altlinux.ru> 0.3.12-alt1
- mouse: added default mice with wheel

* Thu Jun 16 2005 Anton Farygin <rider@altlinux.ru> 0.3.11-alt1
- added Generic Flat Panel 1280x768
- added fbdev to drivers list

* Tue Jun 07 2005 Anton Farygin <rider@altlinux.ru> 0.3.10-alt1
- added more i9xx, UniChrome and nVidia based video cards
- changed driver to 3w-9xxx for 13c1:1002 (#6535)

* Fri Jun 03 2005 Anton Farygin <rider@altlinux.ru> 0.3.9-alt1
- added depth parameter for video card drivers
- added more fglrx and UniChrome based video cards

* Thu Jun 02 2005 Anton Farygin <rider@altlinux.ru> 0.3.8-alt1
- use Card instead of xdriver into class
- added driver for mobile P4

* Tue May 24 2005 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- Cards+ and pcitable cleanup

* Wed Apr 06 2005 Anton Farygin <rider@altlinux.ru> 0.3.6-alt1
- added more tg3 devices to pcitable
- added driver definitions for storages to class

* Mon Apr 04 2005 Anton Farygin <rider@altlinux.ru> 0.3.5-alt1
- Cards+ cleanup
- added vesa driver for class 003:80
- added snd-intel8x0 for 10de:00ea (nVidia Corporation nForce3), #6395

* Wed Mar 09 2005 Anton Farygin <rider@altlinux.ru> 0.3.4-alt1
- some records for lt_modem (#3951)
- some records for hw_random
- fixed typo in class

* Fri Feb 18 2005 Anton Farygin <rider@altlinux.ru> 0.3.3-alt1
- added pnp.ids
- updated pci.ids, usb.ids
- added slamr driver to pcitable (#6181)

* Tue Feb 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.2-alt1
- updated pcitable with ide modules

* Tue Feb 08 2005 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- updated pci.ids, usb.ids (#6013)
- added driver for Radeon Mobility 9100IGP (#6036)

* Tue Dec 28 2004 Anton Farygin <rider@altlinux.ru> 0.3.0-alt1
- pcitable format changed

* Thu Dec 23 2004 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- added pci.ids from pciutils (updated)
- added usb.ids from usbutils (updated)
- all data moved to %_datadir/%name/

* Tue Dec 14 2004 Anton Farygin <rider@altlinux.ru> 0.1.9-alt1
- more mices
- added radeon driver for R300 based videocards

* Tue Dec 07 2004 Anton Farygin <rider@altlinux.ru> 0.1.8-alt1
- Cards+ config format changed
- added default X11 driver (vesa) for all display controllers

* Wed Nov 03 2004 Anton Farygin <rider@altlinux.ru> 0.1.7-alt1
- added sync options to mount
- added some sata controllers to pciid
- mountpoints for block devices moved to /media

* Fri Oct 15 2004 Anton Farygin <rider@altlinux.ru> 0.1.6-alt1
- added table with mount options for varios filesystems (fstype)

* Sun Oct 10 2004 Rider <rider@altlinux.ru> 0.1.5-alt1
- added table for detection acpi-specific devices (like buttons, ac adapter and more)
- added table for configuring detected mouses
- added new Intel cpu with core stepping E0

* Thu Sep 30 2004 Rider <rider@altlinux.ru> 0.1.4-alt1
- added table for cpu detection

* Mon Sep 06 2004 Anton Farygin <rider@altlinux.ru> 0.1.3.1-alt1
- typo fixed (#4259)

* Tue Aug 17 2004 Rider <rider@altlinux.ru> 0.1.3-alt1
- driver for 8086:24dd changed from uhci to ehci (#4259)
- added mountpoints descriptions for class 106 (Mass Storage Device)

* Fri Jul 02 2004 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- database cleanup
- fixed driver for EHCI usb controlers (#4307)

* Fri May 21 2004 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- sound cards: changed all drivers to alsa for kernel 2.6

* Wed May 19 2004 Anton Farygin <rider@altlinux.ru> 0.1-alt1
- first build
