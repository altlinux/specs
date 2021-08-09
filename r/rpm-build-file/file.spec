%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: rpm-build-file
Version: 4.26
Release: alt18

Summary: A utility for determining file types (for rpm-build)
License: BSD-style
Group: File tools
Url: http://www.darwinsys.com/file/

Summary(ru_RU.UTF-8): Утилита для определения типов файлов
BuildPreReq: zlib-devel

# ftp://ftp.astron.com/pub/file/file-%version.tar.gz
Source: file-%version.tar
Source1: magic.local

Patch: file-%version-%release.patch

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  file can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

%prep
%setup -n file-%version
%patch -p1
sed -i 's!/etc/magic:!!' src/Makefile.am
sed -i 's/lib_LTLIBRARIES/noinst_LTLIBRARIES/' src/Makefile.am
sed -i 's/include_HEADERS/noinst_HEADERS/' src/Makefile.am
sed -i 's/man_MANS/noinst_MANS/' doc/Makefile.am
sed -i '/pkgdata_DATA/s/magic.mgc magic/magic.mgc/' magic/Makefile.am
sed -i '/AC_INIT/s/file/file4/' configure.ac

%build
%autoreconf
%configure --program-suffix=4
grep -FZl sparc magic/Magdir/* |
	xargs -r0 sed -i 's/sparc/SPARC/g' --
# SMP-incompatible build.
make

%install
%makeinstall_std

# Test for correct identification of Perl modules
find /usr/*/perl5 -type f -name '*.p[lmh]' |
%buildroot%_bindir/file4 \
	-m %buildroot%_datadir/file4/magic -f - >test.out
grep -q ' [Pp]erl.* text' test.out
grep -v ' text' test.out && exit 1

%check
make -k check

%files
%_bindir/file4
%_datadir/file4
%doc COPYING

%changelog
* Sun Aug 01 2021 Vitaly Chikunov <vt@altlinux.org> 4.26-alt18
- Rename package to rpm-build-file, binary to file4 (closes #40619).
- Make binary statically linked with libmagic.
- Do not package documentation, libraries, uncompiled magic.

* Wed Feb 10 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.26-alt17
- Removed weak magic for Infocom game data (to fix detection of
  zstd-compressed files).

* Wed Dec 02 2020 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt16
- Fixed build with gcc 10.x.

* Sun Nov 08 2020 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt15
- Dropped python-module-magic subpackage (closes: #39228).

* Fri Aug 28 2020 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt14
- Removed (by Vitaly Chikunov) weak magic for:
  - Sun disk label (to fix generation of debuginfo for kernel modules);
  - CLIPPER instruction on VAX (to fix misdetection of manpages).

* Wed Mar 22 2017 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt13
- Backported readelf fix (by sem@; fixes: CVE-2014-9653).
- Backported magic for lrzip, lz4, zstd, and snappy.
- Backported -z support for lrzip, lz4, and zstd.

* Tue Dec 08 2015 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt12
- Added magic for GNU M4 frozen state files.

* Fri Apr 05 2013 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt11
- libmagic: fixed &-prefixed offsets support in magic that uses string flags.
- Enhanced #!/usr/bin/env magic, removed "a " prefix from its output.
- Enhanced python magic and its output.
- Commented out weak sendmail magic (closes: #28310).

* Sun Mar 10 2013 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt10
- Commented out weak palm magic (closes: #28261).

* Sat Dec 22 2012 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt9
- Commented out weak doom packfile magic (closes: #28261).

* Tue Nov 29 2011 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt8
- Updated python magic.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.26-alt7.1
- Rebuild with Python-2.7

* Fri Apr 22 2011 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt7
- python-module-magic: fixed package dependencies.
- Backported a GRUB magic fix.

* Wed Nov 03 2010 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt6
- Rebuilt for soname set-versions.

* Wed Aug 11 2010 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt5
- Fixed one more false positive (by kas@; closes: #23866).

* Tue Feb 16 2010 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt4
- Packaged python-module-magic (by aris@).

* Wed Sep 23 2009 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt3
- Moved "make check" to %%check section.
- Backported lzip and xz compression from file-5.01.
- Backported fixes for compilation warnings from file-5.01.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Imported two fixes from FC package.

* Sat Sep 13 2008 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt1
- Updated to 4.26 (closes: #12597, #13059).
- Update magic entries (closes: #12966, #17119).
- Apply magic updates from Debian file-4.26-1 package.
- Reverted weak and fixed broken magic introduced upstream.

* Tue May 22 2007 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt5
- Fixed integer overflow check (CVE-2007-1536), reported by Colin Percival.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt4
- Commented out "OS/2 REXX batch file text" magix (CVE-2007-2026).

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt3
- Fixed memory leak in file_reset().

* Thu Mar 15 2007 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt2
- Fixed new --exclude option (introduced in file-4.20).
- Fixed troff support (broken in file-4.20).

* Thu Mar 15 2007 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt1
- Updated to 4.20 (CVE-2007-1536).
- Resurrected msdos magix (was removed in 4.19-alt1; fixes #11088).

* Wed Feb 28 2007 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt3
- Fixed Debian exit code change introduced in 4.19-alt1.
- Commented out "Bio-Rad .PIC Image File" magix.
- Moved rpm magix up (#7903).
- Fixed "Audio file with ID3" (#10858).

* Sun Jan 21 2007 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt2
- Commented out new "Perl POD documents" magix.

* Mon Jan 15 2007 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt1
- Updated to 4.19.
- Merged patches from Debian 4.17-5 and FC 4.19-1 packages.
- Commented out new weak magix.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt1
- Updated to 4.13.
- Updated patches.
- Enabled static magick library packaging (closes #6084).

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 4.12-alt1
- Updated to 4.12.
- Reviewed and updated patches.

* Sun Oct 17 2004 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt1
- Updated to 4.10 (fixes: #5168, #5198, #5326).
- Reviewed and updated patches.

* Thu Mar 11 2004 Dmitry V. Levin <ldv@altlinux.org> 4.07-alt4
- Removed "Maple help file, old style" magic (at@ request).

* Mon Mar 08 2004 Dmitry V. Levin <ldv@altlinux.org> 4.07-alt3
- Reviewed perl module source text detection (#2348).
- Plugged memory leak in regex matcher.
- Fixed uninitialized read in matcher.
- Fixed memory leak in magic loader.

* Tue Mar 02 2004 Dmitry V. Levin <ldv@altlinux.org> 4.07-alt2
- Provide %_datadir/magic/ for compatibility.

* Mon Mar 01 2004 Dmitry V. Levin <ldv@altlinux.org> 4.07-alt1
- Updated to 4.07
- Updated patches.
- Packaged libmagic and libmagic-devel subpackages.
- Merged fixes from Debian and RH.

* Mon Mar 03 2003 Dmitry V. Levin <ldv@altlinux.org> 3.41-alt2
- Fixed commands detection order (#0001680).

* Fri Feb 28 2003 Dmitry V. Levin <ldv@altlinux.org> 3.41-alt1
- Updated to 3.41
- Removed alt-mysql patch (merged upstream).

* Mon Feb 17 2003 Dmitry V. Levin <ldv@altlinux.org> 3.40-alt1
- Updated to 3.40

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 3.39-alt2
- Rebuilt in new environment.

* Thu Aug 01 2002 Dmitry V. Levin <ldv@altlinux.org> 3.39-alt1
- 3.39
- Added #!/bin/zsh and #!/usr/bin/zsh recognition (mdk).
- Fixed magic2mime perl path (mdk).

* Mon May 20 2002 Dmitry V. Levin <ldv@altlinux.org> 3.38-alt1
- 3.38

* Tue Dec 25 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.37-alt1
- 3.37
- Fixed text/html detection via DOCTYPE (#0000249).
- Fixed perl scripts detection typo (rh).
- Moved magic manpage from (4) to (5).

* Thu Oct 11 2001 Mikhail Zabaluev <mhz@altlinux.ru> 3.36-alt2
- Removed weird macintosh partition types that use to misclassify Perl scripts
  and, potentially, other text files.
- Added a test for all Perl scripts to be identified as text
  (important for Perl build).

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.36-alt1
- 3.36

* Wed Apr 25 2001 Rider <rider@altlinux.ru> 3.35-alt1
- 3.35

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.33-ipl5mdk
- Added MySQL magic.

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.33-ipl4mdk
- Added MNG magic.
- Updated mcrypt magic.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 3.33-ipl3mdk
- Moved magic files to their own directory.

* Tue Nov 28 2000 Dmitry V. Levin <ldv@fandra.org> 3.33-ipl2mdk
- fixed Newton PDA package formats detection
  (by Mikhail Zabaluev <mookid@sigent.ru>).

* Tue Nov 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.33-ipl1mdk
- 3.33

* Wed Aug  8 2000 Dmitry V. Levin <ldv@fandra.org> 3.32-ipl1mdk
- RE adaptions.

* Mon Aug 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.32-1mdk
- new release

* Sun Jul 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.31-3mdk
- BM

* Mon Jul 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.31-2mdk
- remove old commented commands.
- Stefan van der Eijk <s.vandereijk@chello.nl> did :
	- makeinstall macro
	- macroszifications

* Mon May 15 2000 DindinX <odin@mandrakesoft.com> 3.31-1mdk
- new version 3.31
- removed all unnecessary patches

* Tue Apr 11 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 3.30-1mdk
- new version 3.30
- fix license to BSD

* Thu Mar 23 2000 DindinX <odin@mandrakesoft.com> 3.28-2mdk
- Specs updates, new Group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- enable SMP build/check
- 3.28 :
	- Remove strip/realmedia patch (is there)
	- Remove sparc patch (perl does better, not need updateing)

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with redhat changes.
- identify ELF stripped files correctly (r).
- use SPARC (not sparc) consistently throughout (r).
- add entries for MS Office files (r).

* Tue Aug 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Redhat merge:
	- Thu Aug 12 1999 Jeff Johnson <jbj@redhat.com>
	- diddle magic so that *.tfm files are identified correctly.

* Thu Jul 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Reinserting po translations from MDK5.3.
- Bzip2 patch.
- 3.27.
- Removing unused stuff.

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch for realmedia support.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Fri Nov 27 1998 Jakub Jelinek <jj@ultra.linux.cz>
- add SPARC V9 magic.

* Tue Nov 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.26.

* Mon Aug 24 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.25.
- detect gimp XCF versions.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.24
- buildrooted

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Erik Troan <ewt@redhat.com>
- Fixed problems caused by 64 bit time_t.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Improved recognition of Linux kernel images.
