%define _libexecdir %_prefix/libexec/hal
%define _haldocdir  %_docdir/lib%name-devel-%version

Name: hal
Version: 0.5.14
Release: alt8
Summary: Hardware Abstraction Layer
Group: System/Servers
License: AFL/GPL
Url: http://www.freedesktop.org/wiki/Software/hal

PreReq: shadow-utils dbus udev
Requires: lib%name = %version-%release dmidecode hal-info >= 20081022-alt5
Conflicts: hal-fstab-sync < 0.0.1-alt7

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: hal-0.5.14-alt-ntfs-options.patch

AutoReq: yes, noshell
BuildPreReq: libblkid-devel >= 1.43
BuildRequires: docbook-utils gcc-c++ gtk-doc intltool libdbus-glib-devel libexpat-devel libusb-compat-devel perl-XML-Parser
BuildRequires: python-devel gperf python-modules-compiler python-modules-encodings xmlto libConsoleKit-devel
%ifarch %ix86 x86_64
BuildRequires: libpci-devel zlib-devel
%endif

%description
HAL is daemon for collection and maintaining information from several
sources about the hardware on the system. It provdes a live device
list through D-BUS

%package -n lib%name
Summary: Shared libraries for HAL
Group: System/Libraries
Requires: pciids usbids

%description -n lib%name
This package provides shared libraries for HAL

%package -n lib%name-devel
Summary: Libraries and headers for HAL
Group: Development/C
Requires: lib%name = %version-%release
Obsoletes: %name-devel < %version-%release lib%name-devel-doc < %version-%release
Provides: %name-devel = %version-%release lib%name-devel-doc = %version-%release

%description -n lib%name-devel
Headers for HAL

%prep
%setup -q
%patch -p1
%patch1 -p1

rm -f gtk-doc.make acinclude.m4

%build
%autoreconf
%configure \
	--disable-static \
	--without-usb-csr \
	--with-cpufreq \
	--disable-docbook-docs \
	--disable-gtk-doc \
	--with-doc-dir=%_haldocdir \
	--with-html-dir=%_haldocdir/api \
	--disable-pmu \
	--disable-policy-kit \
	--with-hal-user=haldaemon \
	--with-hal-group=haldaemon \
	--with-udev-prefix=/lib \
	--with-hwdata=%_datadir/misc \
	--with-pid-file=%_var/run/hal.pid \
	--localstatedir=%_var
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_var/{run,cache}/hald
mkdir -p %buildroot%_sysconfdir/hal/fdi/{information,policy,preprobe}

%pre
%_sbindir/groupadd -r -f haldaemon >/dev/null 2>&1 || :
%_sbindir/useradd -r -g haldaemon -d '/' -s /sbin/nologin -c "HAL daemon" haldaemon >/dev/null 2>&1 ||:

%post
%post_service haldaemon

%preun
%preun_service haldaemon

%files
%doc AUTHORS NEWS README doc/TODO
%_sysconfdir/dbus*/system.d/hal.conf
/lib/udev/rules.d/90-hal.rules
%_initdir/haldaemon
%dir %_sysconfdir/hal
%dir %_sysconfdir/hal/fdi
%dir %_sysconfdir/hal/fdi/information
%dir %_sysconfdir/hal/fdi/policy
%dir %_sysconfdir/hal/fdi/preprobe
%_sbindir/*
%_bindir/*
%_libexecdir
%dir %_datadir/hal
%_datadir/hal/fdi
%_datadir/hal/scripts
%_man1dir/*.1*
%_man8dir/*.8*
%attr(0775,root,haldaemon) %_var/*/hald

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Oct 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.14-alt8
- fix ntfs mount options (ALT#26513)

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.14-alt7
- don't build docs

* Wed Mar 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.14-alt6
- revert 0.5.14-alt5 changes

* Sun Mar 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.5.14-alt5
- libhal: added conflicts to libudev
- libhal-devel is not packed. not be used to build!

* Sat Sep 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.5.14-alt4
- required pciids, usbids

* Mon Mar 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.5.14-alt3
- reenabled cpufreq (closes: #23048)

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.14-alt2
- fixed build gtk doc

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.14-alt1
- 0.5.14

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.13-alt5
- allow gdm access to org.freedesktop.Hal.Device.LaptopPanel

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.13-alt4
- moved from libvolume_id to libblkid

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.13-alt3
- moved from libblkid to libvolume_id
- versioning conflict to hal-fstab-sync (closes: #20776)

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.13-alt2
- don't compiled with csr, ibm or cpufreq options, this functionality is obsolete (closes: #21465)
- disabled ACL management, this is now handled by udev-extras
- disabled ConsoleKit/PolicyKit support and lock down most interfaces with at_console

* Fri Jul 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.13-alt1
- 0.5.13

* Mon Jun 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt19
- removed Dell killswitches support

* Sun Jun 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt18
- merged fixes from hal-0_5_12-branch

* Sat Jun 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt17
- fixed crash when assembling certain MD devices (closes: #20470)

* Sat Apr 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt16
- fixed volume label parsing

* Wed Mar 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt15
- changed chkconfig 345 34 91 -> 345 11 91

* Sun Feb 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt14
- fixed previous commits

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt13
- fixed some memory leaks

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt11.M50.1
- build for branch 5.0

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt12
- added org.freedesktop.DBus.Peer standard iterface

* Wed Jan 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt11
- fixed HAL D-Bus config due to D-Bus changes caused by CVE-2008-4311

* Thu Jan 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt10
- droped EeePC specific, used new eeepc-laptop

* Tue Dec 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt9
- corrected EeePC check

* Tue Dec 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt8
- addon-eeepc-killswitch: added support eeepc-laptop kernel driver

* Tue Dec 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt7
- added EeePC wlan killswitch addon

* Mon Dec 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt6
- added forward EeePC ACPI events

* Sat Dec 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt5
- hal.conf: added interface "org.freedesktop.Hal.Device.Storage",
  "org.freedesktop.Hal.Device.WakeOnLan", "org.freedesktop.Hal.Device.DockStation"

* Sat Dec 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt4
- hal.conf: added interface "org.freedesktop.Hal.Device.KillSwitch", "org.freedesktop.Hal.Device.Alsa"
- enabled proc acpi event

* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt3
- hal.conf: added interface "org.freedesktop.Hal.Device.CPUFreq"

* Thu Dec 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt2
- libhal: introduced HAL_0.5.11 ABI for new functions

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.12-alt1
- git snapshot 2008-11-26 (c3cf2b8b252dd593c4058b9688b5978e3e7ee7cc)

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt21.M41.1
- build for branch 4.1

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt22
- added new addons for the iwl killswitch interface

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt20.M41.1
- build for branch 4.1

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt21
- hald-addon-ipw-killswitch: fixed get/set status

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt19.M41.1
- build for branch 4.1

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt20
- hald-addon-ipw-killswitch: ignored 80211control iface

* Thu Nov 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt19
- libhal: droped ldconfig call in post
- initscrips: added condstop

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt18
- hald-addon-ipw-killswitch: fix potential segfault

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt17
- fixed ipw killswith sysfs path

* Mon Nov 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt16
- added new addons for the ipw killswitch interface
  and the generic sysfs backlight interface

* Sat Nov 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt15
- added quiet,fmask=117 mount options for vfat

* Wed Sep 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt14
- use udevadm instead of (deprecated) udevinfo

* Tue Sep 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt13
- allow gid=/uid= for removable media volumes with ntfs-3g

* Mon Sep 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt12
- rebuild with libvolume_id.so.1

* Thu Aug 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt11
- volume.num_blocks can become larger than 2G
- make hal start a lot faster

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt10
- API fixed in CK 0.3

* Mon Jun 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt9
- 10-x11-input.fdi: added XkbRules & XkbModel

* Sat Jun 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt8
- install 10-x11-input.fdi

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt7
- skip "Macintosh mouse button emulation" from capability input.mouse

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt6
- 0.5.11 release

* Mon May 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt5
- hal-0_5_11-branch from 2008-04-29
- drop deprecated input.xkb.{rules,model,layout,variant}

* Tue Apr 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt4
- hal-0_5_11-branch from 2008-04-21
- allow gid=/uid= for removable media volumes with subfs
- removed "Conflicts: submount", "Sometimes They Come Back"

* Sun Apr 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt3
- hal-0_5_11-branch from 2008-04-18
- always enabled ConsoleKit/PolicyKit
- added conflicts: submount, rest in peace (close #15340)
- spec cleanup

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt2.rc2
- added info.capabilities key for VGA capabilities controllers
- allow gid=/uid= for removable media volumes with hfsplus/ntfs filesystems
- drop 10-x11-input.fdi

* Mon Mar 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt1.rc2
- 0.5.11 RC2

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.11-alt1.rc1
- 0.5.11 RC1

* Fri Feb 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt11.1
- rebuild for udev-118
- drop hal-0.5.9.1-alt-vfat-flush.patch, requires kernel > 2.6.20

* Tue Jan 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt11
- close fd-leaks in hald-addon-input
- fix percentage for empty batteries
- don't set percentag if chargelevel is 0

* Thu Jan 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt10
- fixes hal aborting on Fujitsu laptops because the fujitsu fdi contains an
  empty <match /> rule. (close #13959)

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt8.M40.1
- build for branch 4.0

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt9
- fix addon exiting on system bus restart
- returned hal-0.5.10-git-disc-type-detection.patch

* Tue Dec 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt8
- drop hal-0.5.10-git-disc-type-detection.patch

* Fri Dec 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt7
- add drm subsystem
- don't Eject() on dm-devices
- fix possible segfault on fdi-cache recreation
- prevent flood syslog if battery remaining time is above 60 hours
- fix normalised_rate if dis-/charging state is unknown
- fix the keyboard addon to not ignore key repeat events
- when initial disc type detection fails fall back to a alternate detection method

* Wed Nov 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt6
- libhal: fixed  memory leaks after out of memory conditions

* Thu Nov 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt4.M40.1
- build for branch 4.0

* Mon Nov 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt5
- fix int_outof handling

* Wed Oct 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt4
- add support for Wake On LAN
- drop hal-0.5.8-SuSE-hal-fix-storage-policy-fixed-drives.patch

* Thu Oct 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt3
- enabled Macbook backlight support and Macbook Pro utils

* Wed Oct 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt2
- hal-0.5.10-git-GSList-related-memleaks.patch: fixes several memory leaks
  caused by not free'd GSList objects.

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.10-alt1
- 0.5.10

* Tue Oct 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt6
- fixed build for ARM

* Mon Oct 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt5
- change chkconfig 345 34 91 -> 345 35 91 (after acpid)

* Sun Sep 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt4
- change chkconfig 345 48 02 -> 345 34 91

* Fri Sep 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt3
- update hal-0.5.9.1-alt-crypt.patch

* Mon Jul 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt2
- separate hal-info to hal-info package

* Mon Jun 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9.1-alt1
- 0.5.9.1
- hal-info-20070618

* Sun Jun 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt14
- added conflicts: hal-fstab-sync

* Thu May 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt13
- fixed luks-encrypted devices support, broken other stuff. thanks Sergey Bolshakov

* Mon May 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt12
- hal-info-20070516
- added hal-0.5.9-git-property-changed.patch: fix problem with repeated
  property-changed signals

* Wed Apr 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt11
- added create group haldaemon (close #11349)

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt10
- hal-0.5.9 release
- hal-info-20070402

* Mon Apr 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt9
- hal-0.5.9 GIT snapshot 2007-04-02 (9e04dee76ae5f46c1292dcea094b6fdcc38c68a5)
- fixed a bug with unauthorized reboot/shutdown. Now only privileged or console
   users can perform these operations. thanks Alexey Morozov

* Sun Apr 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt8
- hal-0.5.9 GIT snapshot 2007-04-01 (e0d3327b68fc043e6ac8a1b0bdf97249476a3968)
- hal-info-20070328

* Thu Mar 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt7
- hal-0.5.9 GIT snapshot 2007-03-22 (0cd8dccc8382f26d3b3f68f6131aefd08b134232)
- hal-info GIT snapshot 2007-03-22 (58917de0ae967c0fb7c52513521090de18599c24)

* Wed Mar 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt6
- hal-0.5.9 GIT snapshot 2007-03-13 (c9cde9a767168fe9151695142baaae06d5e0827b)
- hal-info-20070313
- drop hal-0.5.3-alt-libhal-storage-mopts_collect-allow-string-options.patch

* Sat Mar 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt5
- hal-0.5.9 GIT snapshot 2007-03-07 (b53fd153f48c55ac9fcb677f1ecaea47b6f9ca3a)
  + libhal: validate parameter to be != NULL
  + fix scsi_host parent relationship
  + make the fdi cache test stricter by not allowing skipped fdi files
- hal-info GIT snapshot 2007-03-07 (98b34973933fc6db1735ae94053ed369826226f7)
  + fix up vbestate_restore for display resuming
  + added iRiver T20 to USB musicplayers list

* Tue Mar 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt4
- moved addon and policy for Dell backlight support to subpackge %name-dell-backlight

* Tue Mar 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt3
- hal-0.5.9 GIT snapshot 2007-03-06 (c31c32b8b7c0fed9c871da947f35922e03ad6ed3)
- hal-info-20070304
- build with Dell backlight support
- disabled Macbook Pro utils
- disabled PMU support

* Mon Mar 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt2
- hal-0.5.9 GIT snapshot 2007-03-05 (0c16761e61064979daa7b39ce0083f064676e578)
- added iocharset=utf8 to mount options for ntfs
- moved API doc to lib%name-devel

* Thu Mar 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.9-alt1
- hal-0.5.9 GIT snapshot 2007-03-01 (f5b862f5690106bb3d5500b1091d12f089bae070)
- hal-info GIT snapshot 2007-02-28 (302840ec67441f55ba07cae9991538e6c91f7fdc)
- fixed requires for lib%name-devel

* Wed Feb 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8.1-alt4
- added to hide fixed storage devices
- added IBM Hotkey support
- fix syntax error in configure script

* Tue Feb 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8.1-alt3
- fixed requires for %name-gnome

* Tue Feb 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8.1-alt2
- fixed hibernate support

* Sun Feb 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.8.1-alt1
- 0.5.8.1
- spec cleanup
- updated build dependencies
- drop lib%name-devel-doc subpackage
- renamed subpackage %name-manager to %name-gnome

* Wed Jan 03 2007 Igor Zubkov <icesik@altlinux.org> 0.5.7-alt4.1.1.1.1
- NMU
- add python-module-pygnome-bonobo to requires of hal-manager subpackage (#8230)

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.5.7-alt4.1.1.1
- NMU
- rebuild
- bump buildrequires libdbus-devel >= 0.94

* Mon Dec 11 2006 Igor Zubkov <icesik@altlinux.org> 0.5.7-alt4.1.1
- NMU
- fix build with new dbus

* Mon Jun 19 2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.5.7-alt4.1
- Add patch that makes hald not stat nfs and autofs mounts

* Fri May 26 2006 Anton Farygin <rider@altlinux.ru> 0.5.7-alt4
- fixed trigger

* Mon Apr 17 2006 Anton Farygin <rider@altlinux.ru> 0.5.7-alt3
- service hal renamed to haldaemon
- removed obsoleted policy for charsets
- updated requires to new udev and dbus

* Fri Apr 14 2006 Anton Farygin <rider@altlinux.ru> 0.5.7-alt2
- updated to new version

* Wed Nov 16 2005 Anton Farygin <rider@altlinux.ru> 0.5.5.1-alt1
- updated to new version
- disabled shell requires searching
- added PalmOne Tungsten|T3 support (#8478)
- added Explay SD/MMC Carder (Realtek 2.0 Card Reader) supporrt (#8477)
- fixed ntfs mount options (#8494)

* Thu Oct 20 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt6
- added patches from HEAD and SuSE:
    hal-0.5.4-acpi_reconnect.patch
    hal-fix-seqfault_if_addon_missing.diff
- disabled acpi-proc by default (always use acpid socket)
- todo() function renamed to _todo() in hal-system-power-set-power-save 
    (workarond for rpm-build bug #8211)

* Mon Oct 10 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt5
- typo in storagepolicy fixed

* Fri Sep 30 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt4
- policy for floppy fixed
- charset for cdrom devices fixed (#8067)
- mount option "sync" removed for usb devices

* Tue Sep 13 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt3
- storage policy for floppy devices fixed (#7551)
- libhal-devel added requires to libdbus-devel (#7863)

* Fri Sep 02 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt2.1
- fix for previos fix

* Wed Aug 31 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt2
- requires fixed

* Mon Aug 29 2005 Anton Farygin <rider@altlinux.ru> 0.5.4-alt1
- new version

* Wed Aug 17 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt9
- umask for iso9660 removed

* Wed Aug 17 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt8
- initscript priority changed from 98 to 47 (for running after dm)
- added default (for UTF-8) charset policy for fat filesystems

* Mon Aug 08 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt7
- more options for vfat and ntfs (#7551)
- fixed filelist (#7576)

* Wed Aug 03 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt6
- postun scriptlet removed (#7454)

* Fri Jul 22 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt5
- added key disable_force_umount for storage

* Thu Jul 21 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt4
- storage-policy: fixed managed key 
- storage-policy: revert back changes for subfs (moved to submountd package)

* Sun Jul 17 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- added policy and scripts for mounting subfs
- renamed mountpoint for cd devices to cdrom

* Thu Jul 14 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- --retain-privileges added to initscript (#7362)

* Wed Jul 13 2005 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- new version
- added patch for allowed sting type options for mount (like fs=cdfss)

* Wed Mar 23 2005 Anton Farygin <rider@altlinux.ru> 0.4.7-alt3
- initscript stop/start fixed

* Tue Feb 08 2005 Anton Farygin <rider@altlinux.ru> 0.4.7-alt2
- storage-policy: added comment=managed mount option

* Wed Jan 26 2005 Anton Farygin <rider@altlinux.ru> 0.4.7-alt1
- 0.4.7
- added noexec, nosuid, nodev to default mount options
- don't use volume label for mount point names
- fixed pci.ids location (#6011)
- service haldaemon renamed to hal (#5995)

* Wed Jan 26 2005 Anton Farygin <rider@altlinux.ru> 0.4.4-alt5
- added patch for build with kernel-headers-std26-up
- removed requires to gnome-common

* Sun Jan 23 2005 Alexey Morozov <morozov@altlinux.org> 0.4.4-alt4
- Removed several reduntant dependencies, build- and installtime,
  made hal-manager be less demanding regarding python
- Replaced kernel-headers-std26-up w/ linux-libc-headers (from PLD)

* Mon Jan 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.4-alt3
- new libhal{,-devel{,-doc}} subpackages.
- gnome-common, kernel-headers-std26 required for build.
- rewrited haldaemon.

* Mon Jan 10 2005 Vital Khilko <vk@altlinux.ru> 0.4.4-alt2
- minor changes

* Mon Jan 10 2005 Vital Khilko <vk@altlinux.ru> 0.4.4-alt1
- 0.4.4
- added belarusian package description

* Thu Jan 06 2005 Vital Khilko <vk@altlinux.ru> 0.4.2-alt1
- 0.4.2
- added *.desktop and icon file for hal-device-manager
- two specs merged
- added belarusian translation
- set textrel=relaxed

* Tue Dec 14 2004 Alexey Morozov <morozov@altlinux.org> 0.4.1-alt1
- Initial build for ALTLinux (taken from PLD)
