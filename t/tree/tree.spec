Name: tree
Version: 1.0.0
Release: alt4
Epoch: 1

Summary: A utility which displays a tree view of the contents of directories
Group: File tools
License: GPL
URL: www.altlinux.org
Source: %name-%version.tar.bz2

Packager: Stanislav Ievlev <inger@altlinux.ru>

# Automatically added by buildreq on Tue Mar 30 2004
BuildRequires: help2man

%description
The %name utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the %name DOS
utility.

Install %name if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep
%setup -q

%build
%make_build

%install
%make_install DESTDIR=$RPM_BUILD_ROOT install

%files
%_bindir/*
%_mandir/man?/*

%changelog
* Fri Jul 04 2008 Alex V. Myltsev <avm@altlinux.ru> 1:1.0.0-alt4
- fix: always return to the starting directory (closes #16263)

* Sun Mar 2 2008 Alex V. Myltsev <avm@altlinux.ru> 1:1.0.0-alt3
- fixing #12468 (incorrect handling of multibyte file names)
- minor cleanups

* Wed Oct 03 2007 Alex V. Myltsev <avm@altlinux.ru> 1:1.0.0-alt2
- fixing #10352 (lstat error with large files)

* Tue Mar 30 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.0.0-alt1
- 1.0.0

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2.1-alt2
- fix building in hasher

* Mon Jun 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2.1-alt1
- 0.2.1 (minor improvements)

* Tue Feb 18 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2.0-alt2
- fix max_level filter

* Thu Feb 06 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2.0-alt1
- rewrite fs walking, was bug in fts usage

* Tue Sep 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1.4-alt1
- new options

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1.3-alt2
- minor improvements in Makefile
- fixes in signal handlers

* Mon Jul 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1.3-alt1
- cleanups in code
- added vt100 and UTF graphics
- added plain mode (works like find ;))

* Fri Jun 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1.2-alt1
- added colorification for pipes and sockets
- added cool filtering

* Mon Jun 17 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1.1-alt1
- bugfixes
- max-level option

* Tue May 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1-alt3
- small improvements

* Fri May 24 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1-alt2
- Added patch from Alexey Voinov <vns@altlinux.ru> to return
  --force-colorize/--force-no-colorize option.

* Tue May 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1:0.1-alt1
- rewritten

* Wed Mar 20 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3-ipl4mdk
- Rebuilt

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl3mdk
- RE adaptions.
- Corrected License tag.

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-3mdk
- macros, BM
- let spechelper compress man-pages

* Sat Jun 03 2000 Etienne Faure <etienne@mandrakesoft.com> 1.3-2mdk
- removed unused patch from sources
- Updated Source URL

* Tue Mar 14 2000 Daouda LO <daouda@mandrakesoft.com> 1.3-1mdk
- Adjust Group
- 1.3

* Tue Nov 23 1999 Pixel <pixel@linux-mandrake.com>
- build release

* Fri Nov 12 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- installing in %_bindir

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
