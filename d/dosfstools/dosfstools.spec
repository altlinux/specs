Name: dosfstools
Version: 4.1
Release: alt1%ubt

Summary: Utilities to create and check MS-DOS FAT filesystems
License: GPL
Group: File tools
BuildRequires(pre):rpm-build-ubt
Url: http://daniel-baumann.ch/software/dosfstools/
Source: %name-%version.tar
Patch: %name-%version-alt.patch

Obsoletes: mkdosfs-ygg

Summary(ru_RU.UTF-8): Утилиты для создания и проверки файловых систем MS-DOS FAT

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%description -l ru_RU.UTF-8
В этом пакете содержатся две утилиты: mkdosfs для форматирования
дискет и разделов форматов FAT и FAT32, принятых в MS-DOS и Windows,
а также dosfsck для проверки таких дисков на логические ошибки.

%prep
%setup
%patch -p1

%build
autoreconf -fisv
%configure --prefix=/ --sbindir=/sbin
%make_build \
	CFLAGS="%optflags\
		-D_LARGEFILE_SOURCE \
		-D_FILE_OFFSET_BITS=64 \
		-fno-strict-aliasing"

%install
%makeinstall PREFIX=%buildroot MANDIR=%buildroot%_mandir sbindir=%buildroot/sbin

%files
/sbin/*
%_mandir/man?/*
%doc doc/*

%changelog
* Tue Feb 07 2017 Anton Farygin <rider@altlinux.ru> 4.1-alt1%ubt
- new version

* Thu Jun 09 2016 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- new version

* Thu Oct 22 2015 Anton Farygin <rider@altlinux.ru> 3.0.28-alt1
- new version

* Tue Nov 18 2014 Anton Farygin <rider@altlinux.ru> 3.0.27-alt1
- new version

* Fri Mar 21 2014 Anton Farygin <rider@altlinux.ru> 3.0.26-alt1
- new version

* Tue Feb 25 2014 Anton Farygin <rider@altlinux.ru> 3.0.25-alt1
- new version

* Fri Dec 20 2013 Michael Shigorin <mike@altlinux.org> 3.0.24-alt2
- synced build options with fedora (thx aen@)

* Fri Dec 20 2013 Anton Farygin <rider@altlinux.ru> 3.0.24-alt1
- new version

* Fri Oct 18 2013 Anton Farygin <rider@altlinux.ru> 3.0.23-alt1
- new version

* Tue Oct 15 2013 Michael Shigorin <mike@altlinux.org> 3.0.22-alt2
- fixed small FAT32 filesystem cluster size to avoid confusing
  UEFI firmware into ignoring the resulting ESP (closes: #29476)

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 3.0.22-alt1
- new version
- build from upstream git
- removed obsoleted and unused patched

* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 3.0.11-alt1
- new version

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 2.11-alt5
- fixed build
- spec cleanup
- me as Packager:

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.11-alt4
- Added patch #3 that fixes bug #10433:
  dosfsck fails on russian filenames in CP866 charset
- Added macro for building under ALC3.0 via 'rpmbuild --with kernel26 ...',
  not needed under ALM2.4 and modern Sisyphus/ALM3.1

* Wed Sep 14 2005 Kachalov Anton <mouse@altlinux.ru> 2.11-alt3
- Compiling with LFS support

* Thu Apr 14 2005 Anton D. Kachalov <mouse@altlinux.org> 2.11-alt2
- Compiling with kernel-headers-std26-up

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.ru> 2.11-alt1
- Updated to version 2.11
- Implemented mkdosfs feature: copy bootloader code from another file
- Specfile fixes:
   + added russian description
   + BuildPreReq: kernel-headers-std replaced to kernel-headers
   + disabled source #1, patch #0: no more needed?

* Tue Jul 20 2004 Anton Farygin <rider@altlinux.ru> 2.10-alt2
- fixed #4844

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 2.10-alt1
- new version

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt1
- Updated to 2.9
- Fixed build (mdk).
- Updated build dependencies.

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 2.8-alt2
- rebuild

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 2.8-alt1
- 2.8

* Thu Feb 15 2001 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl1mdk
- 2.7

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 2.6-ipl1mdk
- RE adaptions.

* Wed Nov 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.6-1mdk
- remove ExclusiveArch tag.
- new and shiny source.
- put in correct optimizations.

* Thu Jul 20 2000 FranГois Pons <fpons@mandrakesoft.com> 2.4-3mdk
- further spec cleaning.

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.4-2mdk
- remove man-pages compression and let spec-helper do the job
- Stefan van der Eijk <s.vandereijk@chello.nl>
	* makeinstall macro
	* macroszifications
	* added %clean

* Fri Mar 31 2000 FranГois Pons <fpons@mandrakesoft.com> 2.4-1mdk
- updated Group.
- 2.4.

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 2.2-7mdk
- Added PPC support

* Mon Jan 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2-6mdk
- ExclusiveArch x86.

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Thu Aug 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Stripping again (#60).
- Fix defatttr root,root.

* Mon Aug  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove fsck.* to don't have a fsck on vfat on boot (Maybe we can
  do a port of scandisk on linux ;) )

* Thu Jul  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rewriting the .spec files to obsoletes mkdosfs-ygg for new dosfstools.
- initialization of spec file.
- 2.2 :
 - Added dosfsck/COPYING, putting dosfsck officially under GPL (Werner
   and I agree that it should be GPL).
 - mkdosfs: Allow creation of a 16 bit FAT on filesystems that are too
   small for it if the user explicitly selected FAT16 (but a warning
   is printed). Formerly, you got the misleading error message "make
   the fs a bit smaller".
 - dosfsck: new option -y as synonym for -y; for compability with
   other fs checkers, which also accept this option.
 - dosfsck: Now prints messages similar to e2fsck: at start version
   and feature list; at end number of files (and directories) and
   number of used/total clusters. This makes the printouts of *fsck at
   boot time nicer.
 - dosfsck: -a (auto repair) now turns on -f (salvage files), too. -a
   should act as non-destructive as possible, so lost clusters should
   be assigned to files. Otherwise the data in them might be
   overwritten later.
 - dosfsck: Don't drop a directory with lots of bad entries in
   auto-repair mode for the same reason as above.
 - dosfsck: avoid deleting the whole FAT32 root dir if something is
   wrong with it (bad start cluster or the like).
 - general: also create symlinks {mkfs,fsck}.vfat.8 to the respective
   real man pages.
