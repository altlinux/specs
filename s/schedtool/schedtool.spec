# vim:set ft=spec: -*- rpm-spec -*-
Name: schedtool
Version: 1.3.0
Release: alt1

Summary: Tool for setting and querying scheduling parameters
License: GPL
Group: System/Kernel and hardware
Url: http://freequaos.host.sk/schedtool/
Packager: Gleb Stiblo <ulfr@altlinux.ru>

Source0: %name-%version.tar.bz2
Patch01: Makefile.patch
Patch02: schedtool-1.2.4-for-SCHED_ISO3.patch

%description
schedtool can set all scheduling parameters Linux is capable of or dis-
play information for given processes.
													
Long-running, non-interactive tasks may  benefit  from  SCHED_BATCH  as
timeslices are longer, less system-time is wasted by computing the next
runnable process and the caches stay stable.
													
Audio/video or other near-realtime applications may run with less skip-
ping  if  set  to SCHED_RR.  Use the static priority-switch -p to fine-
tune inter-process-hierarchies.
													
schedtool now supports setting the  CPU-affinity  introduced  in  linux
2.5.8.

%prep
%setup -q
%patch01 -p1
#patch02 -p1

%build
%make_build affinity_hack
# CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install install DESTPREFIX=/usr DESTDIR=%buildroot MANDIR=/usr/share/man/man8

%files
#_docdir/%name-%version/*
%doc README INSTALL SCHED_DESIGN TUNING LICENSE CHANGES PACKAGERS TODO
%_man8dir/%name.*
%_bindir/*

%changelog
* Tue Nov 25 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.0-alt1
- new upstream version:
  bring schedtool to new glibc affinity api (cpu_set_t) & 
	make it work under new glibcs again
  bug-fix behaviour when 1 wrong PID was given - 
	all other (valid) PIDs would run into error

* Wed Sep 26 2007 Gleb Stiblo <ulfr@altlinux.ru> 1.2.10-alt1
- new version, small makefile fixes

* Fri Dec 15 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.2.9-alt1
- new version

* Tue Oct 03 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.2.7-alt1
- man update

* Tue May 23 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.2.6-alt1
- add support for SCHED_IDLEPRIO in 2.6.16-ck kernels
- update documentation accordingly; remove old stuff about SCHED_BATCH which is
  in mainline 2.6 now

* Tue Jul 12 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.2.5-alt1
- fix NULL pointer printing when policy is out-of-range of TAB[];
  instead, print numeric value + <UNKNOWN>
- behave more nicely with SCHED_ISO and newer -ck kernels 
  (inspired by cr7)

* Mon Apr 04 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.2.4-alt2
- ISO scheduler priority patch added.

* Tue Dec 21 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.2.4-alt1
- new release

* Wed Sep 29 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.2-alt1
- new version. From changelog:
- finally try to not break affinity-compiled binaries on non-affinity kernels
  (2nd FIXME fixed)
- use getpid() instead of PID 0 (== current process) when in execute mode

* Tue Jul 06 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.1.1-alt1
- new version

* Tue May 11 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.0-alt1
- email fixed
- updated to 1.0:
  support nice operations; 
  schedtool is now capable of setting ALL scheduling attributes;
  documentation update.

* Thu Feb 05 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.99-alt1
- Initial revision.

