Name: patch
Version: 2.6.1
Release: alt6

Summary: The GNU patch command, for modifying/upgrading files
License: GPLv3+
Group: Text tools
Url: http://www.gnu.org/software/patch/

# git://git.altlinux.org/gears/p/patch.git
Source: %name-%version-%release.tar

BuildRequires: gnulib >= 0.0.7312.7995834

# for extended attribute copying support
BuildRequires: libattr-devel

%description
The patch program applies diff files to originals.  The diff command
is used to compare an original to a changed file.  Diff lists the
changes made to the file.  A person who has the original file can then
use the patch command with the diff file to add the changes to their
original file (patching the file).

%prep
%setup -n %name-%version-%release
echo -n %version > .tarball-version

%build
./bootstrap --skip-po --gnulib-srcdir=%_datadir/gnulib
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README

%changelog
* Tue Apr 24 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt6
- Updated patch to v2.6.1-170-g90d4e1f.

* Fri Apr 20 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt5
- Updated patch to v2.6.1-169-g709688a.
- Built with gnulib v0.0-7312-g7995834.

* Thu Oct 13 2011 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt4
- Updated patch to v2.6.1-148-g17086c5.
- Updated gnulib to v0.0-6453-g6a4c64c.
- Enabled extended attribute copying support.

* Sat Feb 12 2011 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt3
- Updated patch to v2.6.1-112-g3fc5b24.
- Updated gnulib to v0.0-4800-ga036b76.
- Applied fixes from Jim Meyering, including fixes for regressions
  introduced in previous release.

* Fri Feb 04 2011 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt2
- Updated to v2.6.1-110-g4c3004c (fixes CVE-2010-4651).

* Fri Jun 18 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt1
- Updated to v2.6.1-85-g423d17d (closes: #23463).
- Rnabled test suite.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.5.9-alt3
- Uncompressed tarball.

* Wed Oct 26 2005 Dmitry V. Levin <ldv@altlinux.org> 2.5.9-alt2
- Corrected URLs.
- Reviewed and rediffed patches.
- Applied upstream fix for CR handling bug.
- Applied SuSE patch to prevent previously created
  backup files from being overwritten.
- Additional convention enforcement on patch file names.

* Sun Aug 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.9-alt1
- Updated to 2.5.9 (taken from Mandrake)
- Updated some patches, retired others
- Retired the ifdef patch because the bug it fixed is gone

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.4-ipl10mdk
- rebuild with gcc3
- added alt-noerror and rh-ifdef patches

* Mon Mar 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.4-ipl9mdk
- Rebuilt

* Sat Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 2.5.4-ipl8mdk
- Merged RH patches:
  + fflush(stderr) before asking quiestions;
  + use .orig as default suffix.

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 2.5.4-ipl7mdk
- RE adaptions.

* Tue Jul 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.5.4-7mdk
- Fix possible sigsev (deb).
- By default create empty backup files as readable.

* Tue Jul 25 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.5.4-6mdk
- really move the strip (titiscks)
- BM

* Tue Jul 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>  2.5.4-5mdk
- add alpha for largefile
- remove binaries stripping & {info,man}-pages compression because of
  spec-helper
- Stefan van der Eijk <s.vandereijk@chello.nl> :
	* makeinstall macro
	* macroszifications

* Sun Apr 02 2000 Adam Lebsack <adam@mandrakesoft.com> 2.5.4-4mdk
- Fixed powerpc by adding -D_GNU_SOURCE flag.

* Mon Jan 17 2000 Francis Galiegue <francis@mandrakesoft.com>

- No large file support for sparc - now done from ./configure

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- build release.

* Wed Sep 08 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.5.4

* Fri Aug 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 2.5.3

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Mar 22 1999 Jeff Johnson <jbj@redhat.com>
- (ultra?) sparc was getting large file system support.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Tue Sep  1 1998 Jeff Johnson <jbj@redhat.com>
- bump release to preserve newer than back-ported 4.2.

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- Fix for problem #682 segfault.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- added buildroot

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 2.5

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
