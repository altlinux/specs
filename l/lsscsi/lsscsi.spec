Name: lsscsi
Version: 0.26
Release: alt1

Summary: List SCSI devices (or hosts) and associated information
License: GPL
Group: System/Kernel and hardware

Url: http://sg.danny.cz/scsi/lsscsi.html
Source0: %{name}-%{version}.tgz
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

%description
Uses information provided by the sysfs pseudo file system in
Linux kernel 2.6 series to list SCSI devices or all SCSI hosts.
Includes a "classic" option to mimic the output of
"cat /proc/scsi/scsi" that has been widely used prior to
the Linux kernel 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert at interlog dot com>

%prep
%setup

%build
%configure

%install
%makeinstall_std

%files
%doc ChangeLog README CREDITS AUTHORS COPYING
%_bindir/*
%_man8dir/*

%changelog
* Tue May 08 2012 Michael Shigorin <mike@altlinux.org> 0.26-alt1
- new version (watch file uupdate)

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.25-alt1
- 0.25

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 0.24-alt1
- 0.24 (thanks force@)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 0.23-alt1
- built for ALT Linux

* Thu Dec 03 2009 - dgilbert at interlog dot com
- remove /proc/mounts scan for sysfs mount point, assume /sys
  * lsscsi-0.23
* Fri Dec 26 2008 - dgilbert at interlog dot com
- protection (T10-DIF) information, USB, ATA + SATA transports
  * lsscsi-0.22
* Tue Jul 29 2008 - dgilbert at interlog dot com
- more changes  for lk 2.6.26 (SCSI sysfs)
  * lsscsi-0.21
* Wed Jul 9 2008 - dgilbert at interlog dot com
- changes for lk 2.6.25/26 SCSI midlayer rework
  * lsscsi-0.20
* Thu Jan 25 2007 - dgilbert at interlog dot com
- add transport information (target+initiator)
  * lsscsi-0.19
* Fri Mar 24 2006 - dgilbert at interlog dot com
- cope with dropping of 'generic' symlink post lk 2.6.16
  * lsscsi-0.18
* Mon Feb 06 2006 - dgilbert at interlog dot com
- fix disappearance of block device names in lk 2.6.16-rc1
  * lsscsi-0.17
* Fri Dec 30 2005 - dgilbert at interlog dot com
- wlun naming, osst and changer devices
  * lsscsi-0.16
* Tue Jul 19 2005 - dgilbert at interlog dot com
- does not use libsysfs, add filter argument, /dev scanning
  * lsscsi-0.15
* Fri Aug 20 2004 - dgilbert at interlog dot com
- add 'timeout'
  * lsscsi-0.13
* Sun May 9 2004 - dgilbert at interlog dot com
- rework for lk 2.6.6, device state, host name, '-d' for major+minor
  * lsscsi-0.12
* Fri Jan 09 2004 - dgilbert at interlog dot com
- rework for lk 2.6.1
  * lsscsi-0.11
* Tue May 06 2003 - dgilbert at interlog dot com
- adjust HBA listing for lk > 2.5.69
  * lsscsi-0.10
* Fri Apr 04 2003 - dgilbert at interlog dot com
- fix up sorting, GPL + copyright notice
  * lsscsi-0.09
* Sun Mar 2 2003 - dgilbert at interlog dot com
- start to add host listing support (lk >= 2.5.63)
  * lsscsi-0.08
* Fri Feb 14 2003 - dgilbert at interlog dot com
- queue_depth name change in sysfs (lk 2.5.60)
  * lsscsi-0.07
* Mon Jan 20 2003 - dgilbert at interlog dot com
- osst device file names fix
  * lsscsi-0.06
* Sat Jan 18 2003 - dgilbert at interlog dot com
- output st and osst device file names (rather than "-")
  * lsscsi-0.05
* Thu Jan 14 2003 - dgilbert at interlog dot com
- fix multiple listings of st devices (needed for lk 2.5.57)
  * lsscsi-0.04
* Thu Jan 09 2003 - dgilbert at interlog dot com
- add --generic option (list sg devices), scsi_level output
  * lsscsi-0.03
* Wed Dec 18 2002 - dgilbert at interlog dot com
- add more options including classic mode
  * lsscsi-0.02
* Fri Dec 13 2002 - dgilbert at interlog dot com
- original
  * lsscsi-0.01
