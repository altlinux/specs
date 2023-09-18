Name: gzip
Version: 1.13
Release: alt1

Summary: The GNU data compression program
License: GPLv3+
Group: Archiving/Compression
Url: https://www.gnu.org/software/gzip/

%define srcname %name-%version-%release
Source0: %srcname.tar

BuildRequires: gnulib >= 0.1.5474.f5ad0, makeinfo

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
%setup -n %srcname

# Use fresh bootstrap from gnulib
install -pm755 %_datadir/gnulib/build-aux/bootstrap .

# Build scripts expect to find the gzip version in this file.
echo -n %version > .tarball-version

%build
%define _optlevel 3
%add_optflags -DGNU_STANDARD=0 %optflags_notraceback
./bootstrap --skip-po --gnulib-srcdir=%_datadir/gnulib

# Unset the variable gl_printf_safe to indicate that we do not need
# a safe handling of non-IEEE-754 'long double' values.
sed -i 's/gl_printf_safe=yes/gl_printf_safe=/' m4/gnulib-comp.m4 configure

%configure --bindir=/bin --disable-silent-rules DEFS=-DNO_ASM
%make_build
ln -snf zdiff zcmp
cp -p gzip.1 gzip.doc

%install
mkdir -p %buildroot%_bindir
%makeinstall_std bindir=/bin

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
for c in bz lz lz4 lzi lzo xz zstd; do
	ln -s zdiff %buildroot%_bindir/${c}cmp
	ln -s zdiff %buildroot%_bindir/${c}diff
	ln -s zgrep %buildroot%_bindir/${c}grep
	ln -s zgrep %buildroot%_bindir/${c}egrep
	ln -s zgrep %buildroot%_bindir/${c}fgrep
done
install -pm755 zme.sh %buildroot%_bindir/zme
ln -s zme %buildroot%_bindir/bzme

# Additional manpages.
echo '.so man1/zgrep.1' >%buildroot%_man1dir/zegrep.1
echo '.so man1/zgrep.1' >%buildroot%_man1dir/zfgrep.1
for c in bz lz lz4 lzi lzo xz zstd; do
	echo '.so man1/zdiff.1' >%buildroot%_man1dir/${c}cmp.1
	echo '.so man1/zdiff.1' >%buildroot%_man1dir/${c}diff.1
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}grep.1
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}egrep.1
	echo '.so man1/zgrep.1' >%buildroot%_man1dir/${c}fgrep.1
done
install -pm755 zme.1 %buildroot%_man1dir/
ln -s zme.1 %buildroot%_man1dir/bzme.1

# Our zless and zmore live in less package.
rm %buildroot{/bin/z{less,more},%_man1dir/z{less,more}.1}

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

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
* Wed Sep 13 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.13-alt1
- gzip: v1.12-3-g83c65d1 -> v1.13.
- gnulib BR: v0.1-4279-gbb6ecf327 -> v0.1-5474-gf5ad0b6b38.

* Fri Apr 08 2022 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt1
- gzip: v1.10-31-g34db0a2 -> v1.12-3-g83c65d1 (fixes: CVE-2022-1271).

* Fri Apr 09 2021 Dmitry V. Levin <ldv@altlinux.org> 1.10.0.31.34db-alt1
- gzip: v1.10 -> v1.10-31-g34db0a2.
- gnulib BR: v0.1-2305-g95c96b6dd -> v0.1-4279-gbb6ecf327.

* Sun Dec 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt1
- gzip: v1.9-18-g9c2a2de -> v1.10.

* Mon Dec 24 2018 Dmitry V. Levin <ldv@altlinux.org> 1.9.0.18.9c2a-alt1
- gzip: v1.8-20-g82c62a3 -> v1.9-18-g9c2a2de.
- gnulib: v0.1-1209-g24b3216 -> v0.1-2305-g95c96b6dd.

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.8.0.20.82c6-alt1
- gzip: v1.6-33-g6bfbf81 -> v1.8-20-g82c62a3 (closes: #8184).
- gzip-utils: added support for lz4, lzip, lzop, and zstd.
- gnulib: v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Wed Dec 02 2015 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.33.6bfb-alt1
- Updated to v1.6-33-g6bfbf81.

* Tue Aug 25 2015 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.32.cf68-alt1
- Updated to v1.6-32-gcf688dd.
- Built with gnulib v0.1-585-g2fda85e.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt1
- Updated to v1.6-9-g8b112f2.
- Built with gnulib v0.0-8061-g5191b35.

* Mon Apr 08 2013 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt2
- Updated to v1.5-24-g6ea2e1b.
- Built with gnulib v0.0-7901-g076ac82.

* Fri Aug 03 2012 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- Updated gzip to v1.5-3-gc8ae982.
- Built with gnulib v0.0-7557-gee60576.

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
