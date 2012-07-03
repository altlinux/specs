Name: ipmiutil
Version: 2.8.3
Release: alt1

Summary: IPMI server management utilities
License: BSD
Group: System/Kernel and hardware

Url: http://ipmiutil.sf.net
Source: http://prdownloads.sf.net/ipmiutil/%name-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ libssl-devel

%description
The ipmiutil component package provides utilities to view the SEL
(showsel), perform a hardware reset (hwreset), set up the BMC LAN
and Platform Event Filter entry to allow SNMP alerts (pefconfig),
and other IPMI tasks.  These can be invoked with the metacommand,
ipmiutil, as well.  Man pages are provided.

An IPMI driver can be provided by either the Intel IPMI driver
(/dev/imb) or the OpenIPMI driver (/dev/ipmi0).  If used locally
and no driver is detected, ipmiutil will use user-space register
I/Os instead.

%package cronjob
Summary: A periodic job to syslog and clear SEL records
Group: Monitoring
BuildArch: noarch

%description cronjob
This package contains a daily cron script which runs ipmiutil sel,
writing any new records to syslog, and will then clear the SEL
if free space is low.

The IPMI SEL should not normally be cleared, because the history
of the events is important, but if the IPMI SEL fills up, no new
events are logged, so saving the previous SEL events and clearing
the SEL must be done occasionally, as needed.

%prep
%setup

%build
%configure
#make_build
# SMP incompatible build, see #27254
make

%install
%makeinstall_std
install -pDm755 scripts/checksel %buildroot%_sysconfdir/cron.daily/checksel

%files
%_bindir/*
%_sbindir/*
%_datadir/%name/
%_man8dir/*

%files cronjob
%_sysconfdir/cron.daily/checksel

%changelog
* Sun May 06 2012 Michael Shigorin <mike@altlinux.org> 2.8.3-alt1
- 2.8.3
- single-threaded build (closes: #27254)
- despammed Summary:

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 2.8.2-alt1
- 2.8.2
  + install checksel cronjob by hand (stupid RH#752319)
  + NB: some utils moved from %_sbindir to %_bindir

* Sun Oct 09 2011 Michael Shigorin <mike@altlinux.org> 2.7.9-alt2
- cronjob subpackage made noarch

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 2.7.9-alt1
- 2.7.9
- introduced cronjob subpackage
- spec cleanup

* Wed May 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.3.7-alt1
- 2.3.7 release.
- Remove libraries subpackages as they don't exist anymore.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.3-alt1
- 2.0.3 release.

* Fri Jul 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.8-alt2
- Fix %%files, added libraries subpackages.

* Wed Jul 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.8-alt1
- Initial build for ALT Linux.

* Fri Jun 08 2007 Andrew Cress <arcress@users.sourceforge.net>
  rpmlint tweaks for ipmiutil-1.9.8
* Mon May 21 2007 Andrew Cress <arcress@users.sourceforge.net>
  added isroot flag for chroot cases
* Mon May 18 2007 Andrew Cress <arcress@users.sourceforge.net>
  added ipmi_port init handling
* Mon Jul 10 2006 Andrew Cress <arcress@users.sourceforge.net>
  changed to libfreeipmi.so.2, include & run ipmi_if.sh
* Tue Aug 02 2005 Andrew Cress <arcress@users.sourceforge.net> 
  changed not to run pefconfig if already configured
* Wed Feb 03 2005 Andrew Cress <arcress@users.sourceforge.net> 
  changed /usr/man to /usr/share/man,
  fixed postun to recognize rpm -U via $1 
* Mon Nov 1 2004 Andrew Cress <arcress@users.sourceforge.net> 
  added freeipmi install files and logic
* Tue Aug 23 2004 Andrew Cress <arcress@users.sourceforge.net> 
- added MIB links to /usr/share/snmp/mibs
* Tue Aug 10 2004 Andrew Cress <arcress@users.sourceforge.net> 
- added icmd utility to the rpm
* Thu Aug 05 2004 Andrew Cress <arcress@users.sourceforge.net> 
- added special logic for SuSE snmpd.conf
* Fri Apr 02 2004 Andrew Cress <arcress@users.sourceforge.net> 
- added checksel cron job
* Tue Jan 28 2003 Andrew Cress <arcress@users.sourceforge.net> 
- added sensor & fruconfig for ipmiutil 1.2.8
* Tue Aug  2 2002 Andrew Cress <arcress@users.sourceforge.net> 
- fixed bug 793 (dont need Require:ipmidrvr) for ipmiutil 1.2.2
* Tue Jul  2 2002 Andrew Cress <arcress@users.sourceforge.net> 
- fixed bug 555 in showsel for ipmiutil 1.2.1
* Fri May 10 2002 Andrew Cress <arcress@users.sourceforge.net> 
- fixed bug 504 in pefconfig for ipmiutil 1.1.5
* Thu Apr 11 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated pathnames for ipmiutil 1.1.4, some cleanup
* Mon Mar 18 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.1.3-2, added checking for grub vs. lilo to .spec
* Tue Mar 12 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.1.3, added source rpm, changed license, etc.
* Thu Jan 31 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.1.0-2, changed selpef to pefconfig
* Thu Jan 25 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.1.0, changed to ipmidrvr rather than isc dependency
* Thu Jan 16 2002 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.1.0, added hwreset utility
* Thu Dec 14 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 1.0.0, man page updates
* Thu Nov 19 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 0.9.0, uses new OSS bmc_panic, so don't install module.
* Thu Nov 13 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 0.8.5, add "Requires: isc" (#32), hide selpef output (#38)
* Thu Nov  8 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 0.8.4, eliminate "file exists" messages by fixing removal
* Thu Oct 25 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 0.8.2, run selpef (objdump:applypatch gives bogus warning)
* Thu Oct 25 2001 Andrew Cress <arcress@users.sourceforge.net> 
- updated for 0.8.2, run selpef (objdump:applypatch gives bogus warning)
* Wed Oct 24 2001 Andrew Cress <arcress@users.sourceforge.net> 
- created ipmiutil package 0.8.1 without kbuild
* Tue Oct 23 2001 Andrew Cress <arcress@users.sourceforge.net> 
- created ipmiutil package 0.8.0
