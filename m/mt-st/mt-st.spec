Name: mt-st
Version: 1.1
Release: alt1

Summary: Programs to control tape device operations
License: GPL
Group: Archiving/Backup
Url: http://www.ibiblio.org/pub/Linux/system/backup/
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

# ftp://ftp.ibiblio.org/pub/Linux/system/backup/mt-st-%version.tar.gz
Source: mt-st-%version.tar

%description
The mt-st package contains the mt and st tape drive management programs.
Mt (for magnetic tape drives) and st (for SCSI tape devices) can control
rewinding, ejecting, skipping files and blocks and more.

%prep
%setup

%build
%make_build

%install
%make_install install mandir=%_mandir

%files
/bin/mt
/sbin/stinit
%_mandir/man?/*
%doc README* *.lsm stinit.def.examples

%changelog
* Thu Sep 18 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.1-alt1
- 1.1
- Patches now integrated into source tree (see git repo)

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt2
- Uncompressed tarball.

* Fri May 06 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Updated to 0.8.
- Updated patches.
- Fixed license tag.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.7-alt2
- rebuild

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt1
- 0.7, redone patches.
- Add density code 0x48 for Quantum SDLT220 tape drive (rh).

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.6-alt1
- 0.6

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Thu Jul 20 2000 François Pons <fpons@mandrakesoft.com> 0.5b-8mdk
- macroszifications.

* Fri Mar 31 2000 François Pons <fpons@mandrakesoft.com> 0.5b-7mdk
- updated Group.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh changes.
- enable "datcompression" command(r).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Feb 10 1999 Preston Brown <pbrown@redhat.com>
- upgrade to .5b, which fixes some cmd. line arg issues (bugzilla #18)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- package for 5.2.

* Sun Jul 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated to version 0.5
- removed the touch to force the build: no binaries are included!
- added to the docs: README.stinit, stinit.def.examples
- made buildroot capable

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
