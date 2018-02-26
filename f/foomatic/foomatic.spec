%define snapshot 20040828

Name: foomatic
Version: 3.0.1
Release: alt2.%snapshot

Summary: Foomatic printer database
License: GPL
Group: Publishing
Url: http://www.linuxprinting.org

Requires: mpage netcat ghostscript enscript
Conflicts: cups-drivers

Requires: foomatic-db foomatic-db-engine foomatic-filters

%description
Foomatic is a comprehensive, spooler-independent database of printers,
printer drivers, and driver descriptions. It contains utilities to
generate driver description files and printer queues for CUPS, LPD,
LPRng, and PDQ using the database. There is also the possibility to
read the PJL options out of PJL-capable laser printers and take them
into account at the driver description file generation.

There are spooler-independent command line interfaces to manipulate
queues (foomatic-configure) and to print files/manipulate jobs
(foomatic printjob).

The site http://www.linuxprinting.org/ is based in this database.

This is a virtual package for compatibility

%files

%changelog
* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt2.20040828
- latest snapshot

* Wed Feb 11 2004 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20040128
- new foomatic snapshot

* Thu Dec 25 2003 Stanislav Ievlev <inger@altlinux.org> 3.0.1-alt1.20031219
- 3.0.1

* Wed Feb 26 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt1.20030213
- now virtual package for compatibility

* Tue Jan 21 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt2.20021220
- added hack from  Anton V. Boyarshinov (boyarsh@ru.echo.fr) for lexmarkinstall

* Thu Jan 09 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt1.20021220
- update to latest MDK version

* Wed Dec 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt1.20021030
- added dep on enscript

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt0.20021030
- update

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt0.20021023
- 2.0.2

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-alt0.20020913
- new snapshot

* Fri Aug 16 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-alt0.1
- 2.0 + snapshot

* Wed Jun 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1.9-alt0.3
- new snapshot

* Mon May 20 2002 Stanislav Ievlev <inger@altlinux.ru> 1.9-alt0.2
- Added missing man-pages

* Tue Apr 02 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.17
- new snapshot (20020322)

* Mon Mar 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.16
- fixed bug in foomatic-printjob (izvrat support)

* Tue Feb 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.15
- new snapshot
- fixed some bugs in izvrat patch
- rewritten encoding patch

* Wed Feb 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.14
- added izvrat support

* Fri Jan 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.13
- latest snapshot 20020111.

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.12
- Latest snapshot 20020101
- Fixed Group tag ( #0000365).
- Turn off imagearea patch

* Mon Dec 17 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.11
- try to fix resolutions for some HP LaserJet 4 printers (bug #0000224)
- try to fix ppd file generation (DefaultImageableArea, DefaultPaperDimension)

* Fri Dec 07 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.10
- snapshot 20011130.
- turn of precomiling. I think we don't need it.

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.9
- new snapshot

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.8
- new snapshot

* Tue Sep 18 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.7
- MDK merges.

* Mon Sep 10 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.6
- Fixed buildreqs.

* Thu Sep 06 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.5
- New snapshot. foomatic is more faster now.

* Mon Sep 03 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.4
- New snapshot.

* Wed Aug 15 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.3
- Added locale hack.

* Mon Aug 13 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.2
- New snapshot (serveral bugfixes).
- Added lexmark-cups-kit.
- Install now using update-alternatives.

* Fri Aug 10 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt0.1
- Initial release for ALT Linux.
- It's a great database, but compiles 5 hours on 2 processor machine.

* Mon Jul 23 2001 Crutcher Dunnavant <crutcher@redhat.com> 1.1-0.20010717.2
- made foomatic pre-compute its db

* Thu Jul 18 2001 Crutcher Dunnavant <crutcher@redhat.com> 1.1-0.20010717.1
- imported from mandrake.

* Tue Jul 17 2001 Till Kamppeter <till@mandrakesoft.com> 1.1-0.20010717mdk
- Added job listing/removal/manipulation and queue control to
  foomatic-printjob
- Support for printing multiple copies with PDQ

* Fri Jul 14 2001 Till Kamppeter <till@mandrakesoft.com> 1.1-0.20010714mdk
- Included the cupsomatic filter script
- When a queue is set up, default options can be set now
- Help messages of foomatic-configure and foomatic-printjob cleaned up.

* Fri Jul 13 2001 Till Kamppeter <till@mandrakesoft.com> 1.1-0.20010713mdk
- Many bugfixes in "foomatic-printjob".
- "foomatic-configure" adds the Foomatic config file directory automatically
  to the search paths of PDQ.
- Printing a help page under PDQ was broken.

* Thu Jul 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.1-0.20010712mdk
- BuildRequires:	perl-devel

* Wed Jul 11 2001 Till Kamppeter <till@mandrakesoft.com> 1.1-0.20010711mdk
- initial release.
- Deleted the obsolete drivers "stp", "cZ11", and "hpdj".
- Patch applied which flushes the memory cache regularly, otherwise
  foomatic-configure would hang when the Foomatic data of GIMP-Print is
  installed.
