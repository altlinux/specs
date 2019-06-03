Name: lha
Version: 1.14i
Release: alt3
Serial: 2

%define addver -ac20050924p1
%define fullname %name-%version%addver

Summary: An archiving and compression utility for LHarc format archives
License: freeware
Group: Archiving/Compression

Url: http://www2m.biglobe.ne.jp/~dolphin/lha/lha-unix.htm
Source: http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%fullname.tar.gz
Patch: %name-1.14i-fix-includes.patch.bz2
Packager: Stanislav Ievlev <inger@altlinux.ru>

%description
LhA is an archiving and compression utility for LHarc format archive.
LhA is mostly used in the Amiga and in the DOS world, but can be used
under Linux to extract files from .lha and .lzh archives.

Install the LhA package if you need to extract files from .lha or .lzh
Amiga or DOS archives, or if you have to build LhA archives to
be read on the Amiga or DOS.

%prep
%setup -n %fullname
%patch -p1

%build
%define _optlevel 3
%add_optflags %optflags_notraceback
%configure
%make_build OPTIMIZE="%optflags"

%install
install -pDm755 src/%name %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Mon Jun 03 2019 Michael Shigorin <mike@altlinux.org> 2:1.14i-alt3
- E2K: fix build via lowering superfluous optimization level
- minor spec cleanup

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2:1.14i-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Apr 15 2007 Michael Shigorin <mike@altlinux.org> 2:1.14i-alt2
- ac20050924p1: security fixes for CVE-2006-4335, CVE-2006-4337,
  CVE-2006-4338 (DoS, system access)
- removed patch1, patch2, patch4, patch5 (didn't apply)

* Sat May 08 2004 Michael Shigorin <mike@altlinux.ru> 2:1.14i-alt1
- security fixes for CAN-2004-0234, CAN-2004-0235 (patch taken from RH)
- symlink patch from the same source
- spec cleanup
  (little modification by inger)

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 1:1.14i-ipl3mdk
- rebuild with gcc3
- added real 114i (instead 114f) tarball ;)

* Wed Mar 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1:1.14i-ipl2mdk
- Rebuilt

* Tue Jan 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.14i-ipl1mdk
- 1.14i

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.14f-ipl4mdk
- RE adaptions (beware: whole code is written insecure).

* Wed Aug 30 2000 Etienne Faure <etienne@mandrakesoft.com> 1.14f-4mdk
- rebuilt with _mandir macro

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 1.14f-3mdk
- fix group

* Wed Jan 12 2000 Pixel <pixel@mandrakesoft.com>
- fix build as nonroot (owner of the man page)

* Wed Nov 03 1999 Pablo Saratxaga <pablo@mandrakesoft.comW
- added japanese man page
- upgraded to 1.14f

* Mon Jul 28 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added patch to handle .lha extensions.
- fixed make patch.
- upgraded to version 1.14e.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 11)

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- this package will never change.
- changed groups

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- add english doco.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- removed man page, wasn't ASCII and caused more harm than good
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
