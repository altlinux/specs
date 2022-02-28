# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tree
Version: 2.0.2
Release: alt1
Epoch: 1

Summary: List contents of directories in a tree-like format
Group: File tools
License: GPL-2.0-or-later
URL: http://mama.indstate.edu/users/ice/tree/
Source: %name-%version.tar

%description
Tree is a recursive directory listing program that produces a depth
indented listing of files, which is colorized ala dircolors if the
LS_COLORS environment variable is set and output is to tty.

%prep
%setup

%build
# Upstream have LDFLAGS=-s causing binaries to be stripped.
%make_build CFLAGS="%optflags %(getconf LFS_CFLAGS)" LDFLAGS=

%install
install -Dpm755 -t %buildroot%_bindir  tree
install -Dpm644 -t %buildroot%_man1dir doc/tree.1

%files
%doc LICENSE CHANGES README
%_bindir/tree
%_man1dir/tree.1*

%changelog
* Fri Feb 25 2022 Vitaly Chikunov <vt@altlinux.org> 1:2.0.2-alt1
- Change upstream and update to 2.0.2 (02/16/2022).

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.0.0-alt5
- Fixed build with new toolchain.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:1.0.0-alt4.qa1
- NMU: rebuilt for debuginfo.

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
