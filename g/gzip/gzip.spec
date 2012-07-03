Name: gzip
Version: 1.4
Release: alt3

Summary: The GNU data compression program
License: GPLv3+
Group: Archiving/Compression
Url: http://www.gnu.org/software/gzip/

# http://git.altlinux.org/people/ldv/packages/?p=gzip.git
Source0: gzip-%version-%release.tar
Source1: gnulib-%version-%release.tar
Source2: zme.sh
Source3: zme.1

Patch: gzip-%version-%release.patch

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: less}}

%package utils
Summary: Utilities for handy use of the GNU gzip
Group: Archiving/Compression
BuildArch: noarch
Requires: %name = %version-%release, mktemp >= 1:1.3.1
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Provides: bzip2-utils = 0:1.0.3-alt5
Obsoletes: bzip2-utils
Conflicts: lzma-utils < 0:4.32.9

%description
This package contains the popular GNU gzip data compression
program and its associated scripts to manage compressed files.

%description utils
This package contains additional utilities for the popular
GNU gzip, bzip2, lzma and xz data compression programs.

%prep
%setup -q -n gzip-%version-%release -a1
%patch -p1
echo -n %version >.tarball-version

# Unset the variable gl_printf_safe to indicate that we do not need
# a safe handling of non-IEEE-754 'long double' values.
sed -i 's/gl_printf_safe=yes/gl_printf_safe=/' \
	gnulib-%version-%release/modules/printf-safe

%build
%define _optlevel 3
%add_optflags -DGNU_STANDARD=0 %optflags_notraceback
./bootstrap --skip-po --gnulib-srcdir=gnulib-%version-%release
%configure --bindir=/bin --disable-silent-rules
%make_build
ln -snf zdiff zcmp
cp -p gzip.1 gzip.doc

%install
mkdir -p %buildroot%_bindir
%makeinstall bindir=%buildroot/bin

# uncompress is a part of ncompress package
rm %buildroot/bin/uncompress

for i in zcmp zegrep zforce znew gzexe zdiff zfgrep zgrep; do
	mv %buildroot/bin/$i %buildroot%_bindir/
done

# Replace wrappers with symlinks.
ln -sf gzip %buildroot/bin/gunzip
ln -sf gzip %buildroot/bin/zcat
ln -sf zdiff %buildroot%_bindir/zcmp
ln -sf zgrep %buildroot%_bindir/zegrep
ln -sf zgrep %buildroot%_bindir/zfgrep

# Add compatibility symlinks.
for i in gzip gunzip zcat; do
	ln -s ../../bin/gzip %buildroot%_bindir/$i
done

# Additional utilities.
for c in b l x; do
	ln -s zdiff %buildroot%_bindir/${c}zcmp
	ln -s zdiff %buildroot%_bindir/${c}zdiff
	ln -s zgrep %buildroot%_bindir/${c}zgrep
	ln -s zgrep %buildroot%_bindir/${c}zegrep
	ln -s zgrep %buildroot%_bindir/${c}zfgrep
done
install -pm755 %_sourcedir/zme.sh %buildroot%_bindir/zme
ln -s zme %buildroot%_bindir/bzme

# Additional manpages.
echo '.so man1/zgrep.1' >%buildroot%_man1dir/zegrep.1
echo '.so man1/zgrep.1' >%buildroot%_man1dir/zfgrep.1
for c in b l x; do
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}zgrep.1
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}zegrep.1
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}zfgrep.1
	echo '.so man1/zdiff.1' >%buildroot%_man1dir/${c}zcmp.1
	echo '.so man1/zdiff.1' >%buildroot%_man1dir/${c}zdiff.1
done
install -pm755 %_sourcedir/zme.1 %buildroot%_man1dir/
ln -s zme.1 %buildroot%_man1dir/bzme.1

# Our zless and zmore live in less package.
rm %buildroot{/bin/z{less,more},%_man1dir/z{less,more}.1}

%check
%make_build -k check

%files
/bin/*
%_bindir/g*zip
%_bindir/zcat
%_man1dir/g*zip.*
%_man1dir/zcat.*
%_infodir/*.info*
%doc AUTHORS NEWS README THANKS TODO

%files utils
%_bindir/*
%_man1dir/*
%exclude %_bindir/g*zip
%exclude %_bindir/zcat
%exclude %_man1dir/g*zip.*
%exclude %_man1dir/zcat.*

%changelog
* Fri Feb 04 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt3
- Updated gzip to v1.4-70-g70b7874.
- Updated gnulib to v0.0-4672-ga2e8447.

* Tue Mar 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt2
- Updated gzip to v1.4-24-gcad194d.
- Updated gnulib to v0.0-3591-geb2f221.

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Updated to 1.4.
- Reviewed and reworked patches.
- Enabled test suite.
- Packaged gzip-utils as noarch.

* Wed Jan 13 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt6
- Applied upstream fix for integer underflow bug (CVE-2010-0001).

* Fri Sep 25 2009 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt5
- gzip-utils: Added lzma/xz support to zdiff and zgrep.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt4
- Rebuilt.

* Mon Sep 18 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt3
- Fixed several bugs (CVE-2006-433[5678])
  based on patch from Tavis Ormandy.
- zgrep: Terminate when pipeline is interrupted by signal (#9998).

* Fri Jul 22 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt2
- Fixed a segfault on invalid compressed data (patch from Gentoo).

* Thu May 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- Updated to 1.3.5.
- Reviewed and reworked patches.
- Added zegrep(1) and zfgrep(1) manpage links.
- Changed zgrep and zdiff to handle also functionality of
  bz*grep, bzcmp and bzdiff utilities.
- Changed znew utility to avoid dependence on compress utility.
- Relocated zme utility from bzip2-utils to gzip-utils.
- Relocated zmore utility to less package.
- Fixed chmod/chown race condition in file permission handling
  code (CAN-2005-0988).
- Changed gunzip to ignore path in original file name stored
  in gzip archive when uncompressing with -N; this measure
  prohibits uncontrolled files creation in arbitrary filesystem
  locations. (CAN-2005-1228).
- Fixed zgrep to properly sanitize arguments, to avoid arbitrary
  commands execution via filenames injection into a sed script
  (CAN-2005-0758).

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3.3-alt3
- rebuild with gcc3

* Wed Jun 12 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt2
- Added "Provides: /bin/gzip, /bin/gunzip, /bin/zcat" to gzip subpackage.

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- 1.3.3 (nothing interesting).
- Additional convention enforcement on patch file names.

* Sat Jan 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt2
- Eliminated basename usage in gz* script utils.

* Wed Nov 21 2001 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- 1.3.2
- Renamed devel subpackage into %name-utils.

* Tue Nov 20 2001 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- 1.3.1
- Updated patches.
- Corrected mktemp dependence.

* Sat Sep 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3-ipl5mdk
- Synced with Owl:
  + Synced with Todd's latest fixes: re-create the temporary file in gzexe
    safely when run on multiple files, support GZIP="--suffix .suf" in znew.
  + Patched unsafe temporary file handling in gzexe, zdiff, and znew based
    on work by Todd Miller of OpenBSD.
  + Dropped Red Hat's patch which attempted to fix some of the same issues
    for gzexe but was far from sufficient.

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3-ipl4mdk
- Merged in RH patches:
  + Patch various uses of $$ in the bundled scripts
  + Fix the SIGPIPE patch to avoid blank lines (#43319)
  + Fixed buzilla bug #26680. Wrong skip value after mktemp patch and forced
    overwrite for output file during decompression.
  + trap SIGPIPE in zgrep, so "zgrep | less" gets a happy ending
    (#24104).

* Sat Dec 02 2000 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl3mdk
- Moved utilities to %name-devel subpackage.
- Removed PreReq: %%__install_info.

* Tue Aug 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl2mdk
- Move lesspipe.sh and zless to less package.

* Sat Jun 24 2000 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl1mdk
- 1.3

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.4a-ipl1mdk
* RE and Fandra adaptions.

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 1.2.4a-1mdk
- Updated sources to 1.2.4a (minor doc changes)
- Updated rpm group
- Cleanup to conform to spec-helper

* Wed Mar 08 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.4-19mdk
- added lesspipe.sh (allowing zless to handle arbitrary compressions
  methods, but also allows to use less command line parameters on zless,
  and use arrows keys to navigate between various files; that is a nice
  and useful zless not one only limited to "zcat $* | less" )

* Thu Dec 16 1999 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Added 4g patch, from www.gzip.org

* Thu Dec 16 1999 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed zforce.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix building as user.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- built against glibc 2.1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/bin/gzip and /usr/bin/gunzip symlinks as some programs are too
  brain dead to figure out they should be at least trying to use $PATH
- added BuildRoot

* Wed Jan 28 1998 Erik Troan <ewt@redhat.com>
- fix /tmp races

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info
- applied patch for gzexe

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Marc Ewing <marc@redhat.com>
- (Entry added for Marc by Erik) fixed gzexe to use /bin/gzip

