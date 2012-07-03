Name: mpt-status
Version: 1.2.0
Release: alt2

Summary: MPT Fusion based RAID inquiry tool for LSI Logic HBAs
License: GPL v2+
Group: Monitoring

Url: http://www.drugphish.ch/~ratz/mpt-status/
Source0: %name-%version.tar.bz2
Source1: %name.sysconfig
Source2: %name.cron
Source3: %name-check.sh
Source4: %name-install.sh
Patch0: %name-headers.patch
Patch1: %name-no_compiler.h.patch
Patch2: %name-sync_info.patch
Packager: Michael Shigorin <mike@altlinux.org>

%description
mpt-status requests information about RAID status for LSI Logic
SCSI/SAS controllers.  Currently supported and tested HBAs are:

LSI 1030 SCSI RAID storage controller
LSI SAS1064 SCSI RAID storage controller
LSI SAS1068 SCSI RAID storage controller
LSI SAS 3442-R SCSI RAID storage controller

Since the tool is using the MPI (message passing interface)
changes are high that the basic information regarding RAID status
will be available for all LSI based controllers. Just give it
a try and report back.

You might want to install %name-monitoring package either.

%package monitoring
Summary: %name setup for automated RAID monitoring
License: GPL
Group: Monitoring
Requires: %name = %version-%release

%description monitoring
Install this package if you want your LSI MPT-based RAID
status monitoring automatically configured for you

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make CFLAGS="%optflags -Wall -W -Iincl -Iinclude"

%install
install -pD -m755 mpt-status %buildroot%_sbindir/%name
install -pD -m644 man/mpt-status.8 %buildroot%_man8dir/%name.8
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/cron.d/%name
install -pD -m755 %SOURCE3 %buildroot%_sbindir/%name-check
install -pD -m755 %SOURCE4 %buildroot%_sbindir/%name-install

%post monitoring
%_sbindir/%name-install ||:

%files
%doc doc/*
%_sbindir/%name
%_man8dir/%name.8*

%files monitoring
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/cron.d/%name
%_sbindir/%name-check
%_sbindir/%name-install

%changelog
* Mon Mar 24 2008 Michael Shigorin <mike@altlinux.org> 1.2.0-alt2
- don't break monitoring subpackage installation if there's 
  no controller present: just leave a message

* Sun Mar 23 2008 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- built for ALT Linux
  + based on generic spec in tarball
  + added PLD patches from 1.2.0-2 package
- spec cleanup
- added monitoring subpackage (cron script based on 
  http://prefetch.net/reference/mpt-status.spec)

* Fri Jun 30 2006 Roberto Nibali (ratz@drugphish.ch)
- Changed release version

* Fri Jun 30 2006 Rich Edelman (rich.edelman@openwave.com)
- Upgraded to version 1.2.0-RC7
- Changed Makefile to use /lib/modules/`uname -r`/build as the KERNEL_PATH
  directory, instead of /usr/src/linux. This should make building this package
  across different distributions easier. (Patch mpt-status-fix-kernel-path.diff)

* Thu Jul 14 2005 Jean-Philippe CIVADE <jp.civade@100p100.net> - 1.1.3-0
- Initial package.
