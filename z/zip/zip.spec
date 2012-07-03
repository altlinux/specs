%define origver 30

Name: zip
Version: 3.0
Release: alt1

Epoch: 30000000

Summary: A file compression and packaging utility compatible with PKZIP/WinZIP
License: BSD
Group: Archiving/Compression

Url: http://www.info-zip.org/Zip.html
Source0: http://downloads.sourceforge.net/infozip/%{name}%{origver}.tar.gz
Source1: ftp://ftp.uu.net/pub/archiving/zip/src/zcrypt29-exportable.tar.bz2
Patch0:	zip-3.0-umask-tmp.patch
Patch1: infozip-zip2.3-noninteractivepassword+testencrypedfile.patch
Patch3: zip-3.0-alt-natspec.patch
Patch4: zip-3.0-alt-asdos.patch
# This patch will probably be merged to zip 3.1
# http://www.info-zip.org/board/board.pl?m-1249408491/
Patch5: zip-3.0-exec-shield.patch
# Not upstreamed.
Patch6: zip-3.0-currdir.patch
# Not upstreamed.
Patch7: zip-3.0-time.patch


Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Утилита сжатия и упаковки файлов, совместимая с PKZIP/WinZIP
Summary(uk_UA.KOI8-U): Утил╕та стиснення та арх╕вування файл╕в, що сум╕сна з PKZIP/WinZIP

BuildRequires: libnatspec-devel

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and is
compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems) and WinZIP.

Install the %name package if you need to compress files using the zip program.

%description -l ru_RU.KOI8-R
Программа архивирования/сжатия zip, совместимая по формату с PKZIP и WinZIP.
Аналогична комбинации команд UNIX tar и compress.

%description -l uk_UA.KOI8-U
Програма арх╕вування/стиснення zip, що сум╕сна по формату ╕з PKZIP та WinZIP.
╢ аналогом комб╕нац╕╖ команд UNIX tar та compress.

%prep
%setup -q
#rm -f LICENSE WHERE crypt.c crypt.h
#%%setup -q -DT -a1
subst \
  "s|-O2|%optflags|;s|/usr/local/bin|%_bindir|g;s|/usr/local/man|%_mandir|g" \
  unix/configure

%patch0 -p2
#%%patch3 -p2
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch7 -p1

%define _optlevel 3

%build
make -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc  %{?_smp_mflags}

%install
mkdir -p %buildroot{%_bindir,%_mandir}
%makeinstall -f unix/Makefile \
	BINDIR=%buildroot%_bindir MANDIR=%buildroot%_man1dir
make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

%files
%doc README CHANGES TODO WHATSNEW WHERE LICENSE README.CR
%doc proginfo/algorith.txt
%_bindir/*
%_man1dir/*

%changelog
* Mon Mar 19 2012 Andrey Cherepanov <cas@altlinux.org> 30000000:3.0-alt1
- Version 3.0 (ALT #26954)
- Disable zcrypt29 encription and codepage detection by natspec

* Tue Jun 24 2008 Vitaly Lipatov <lav@altlinux.ru> 20060805:2.32-alt2
- build with natspec patch for correct name encoding (fix bug #14125)
- add fix for create DOS like archives (needed for WinRAR, FAR)

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 20060805:2.32-alt1.0
- Automated rebuild.

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 20060805:2.32-alt1
- 2.32 (security fixes done upstream)
- removed patch2 which broke 2.31-alt1; thanks Valery Inozemtsev (shrek@)
  for reporting that

* Thu Sep 22 2005 Michael Shigorin <mike@altlinux.org> 20050922:2.3-alt3
- rollback to 2.3+fixes, there was a report of 2.31 brokenness
  regarding filenames ("zip a aaaa ...") by <chernoff northstar ru>

* Mon Sep 19 2005 Michael Shigorin <mike@altlinux.org> 20050919:2.31-alt1
- security fixes merged upstream
- fixed Url:, thanks to Vitaly Lipatov (lav@)

* Tue Jun 28 2005 Anton D. Kachalov <mouse@altlinux.org> 20050628:2.3-alt2
- serial fixup

* Fri Jan 21 2005 Michael Shigorin <mike@altlinux.ru> 20050121:2.3-alt1
- updated patch dealing with CAN-2004-1010
- changed release to alt
- spec cleanup

* Sun Jan 09 2005 Anton Farygin <rider@altlinux.ru> 2.3-ipl8mdk
- buffer overflow fixed (CAN-2004-1010)
- noninteractivepassword+testencrypedfile patch added

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 2.3-ipl7mdk
- russian summary
- rebuild (gcc 3.2)

* Tue Dec 04 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.3-ipl6mdk
- Rebuild for Sisyphus

* Tue Nov 07 2000 Dmitry V. Levin <ldv@fandra.org> 2.3-ipl5mdk
- RE adaptions.

* Tue Aug 22 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.3-5mdk
- fix url
- add crypto stuff

* Sun Jul 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.3-4mdk
- use even more macros (titisucks)
- fix the url

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.3-3mdk
- use new macros
- BM

* Mon Apr 03 2000 Jerome Martin <jerome@mandrakesoft.com> 2.3-2mdk
- rpm group change
- spec-helper related cleanup 

* Wed Dec 08 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- upgrade to 2.3
- add URL
- remove zip archive source for the tarball (who put both the source tarball
  and the source zip ?)
- add LICENCE file

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix compilation with gcc2.95.

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.2
- handle optimizations

* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- bzip2 man-pages.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- updated text in the spec file

* Fri Jan 15 1999 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm

* Mon Dec 21 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
