Name: sdparm
Version: 1.07
Release: alt2

Summary: Utility for listing and changing SCSI disk parameters
License: BSD
Group: System/Kernel and hardware

Url: http://sg.danny.cz/sg/sdparm.html
Source0: %name-%version.tgz
Source1: %url
Source100: sdparm.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libsgutils-devel

%description
sdparm is a utility for listing and potentially changing SCSI disk
parameters. More generally it can be used on any device that uses
a SCSI command set. Apart form SCSI disks, examples of devices that
use SCSI command sets are ATAPI CD/DVD drives, SCSI and ATAPI tape
drives and SCSI enclosures.

SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use the
SCSI command set e.g. some SATA devices) such as CD/DVD and tape
drives may also find parts of sdparm useful. Requires the linux kernel
2.4 series or later. In the 2.6 series any device node the understands
a SCSI command set may be used (e.g. /dev/sda). In the 2.4 series SCSI
device node may be used.

Fetches Vital Product Data pages. Can send commands to start or stop
the media and load or unload removable media.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
cp -a %SOURCE1 .

%files
%_bindir/*
%_man8dir/*
%doc AUTHORS CREDITS ChangeLog README notes.txt sdparm.html

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.07-alt2
- added watch file

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.07-alt1
- 1.07

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.06-alt2
- rebuilt with current libsgutils just in case
- merged in package description from Fedora
- updated an Url:

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 1.06-alt1
- 1.06 (thanks force@)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 1.05-alt1
- 1.05
- built with libsgutils
- HTML page no longer included in tarball

* Tue Oct 16 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.02-alt2
- 1.02 [20071008]

* Sat May 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.02-alt1
- 1.02

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.01-alt1
- 1.01

* Sun Dec 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.00-alt1
- initial build
