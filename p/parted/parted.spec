Name: parted
Version: 2.4
Release: alt2
Summary: Flexible partitioning tool
License: GPLv3
Group: System/Configuration/Hardware
URL: http://www.gnu.org/software/%name
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release

Source: http://ftp.gnu.org/gnu/parted/%name-%version.tar.gz
Patch0: parted-2.3-gpt-labels.patch
Patch1: parted-2.4-alt-headers-regression.patch

BuildRequires: libblkid-devel libdevmapper-devel libreadline-devel libtinfo-devel libuuid-devel

%description
GNU %name is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data to
new hard disks

%package -n lib%name
Summary: Shared library for flexible partitioning tool
Group: System/Libraries

%description -n lib%name
This package includes the shared library needed to run
lib%name-based software

%package -n lib%name-devel
Summary: Files required to compile software that uses lib%name
Group: Development/C
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%description -n lib%name-devel
This package includes the header files

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-rpath \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --output=%name.lang %name

%files -f %name.lang
%doc AUTHORS BUGS NEWS THANKS TODO
%_sbindir/*
%_infodir/%name.info*
%_man8dir/*.8*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/API doc/FAT
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Jun 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt2
- fixed headers regression

* Thu May 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt1
- 2.4

* Tue Apr 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt4
- GPT: fixed pte handling (closes: #25517)

* Wed Feb 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt3
- rebuild

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt2
- rebuild

* Thu Jun 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- 2.3

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.2-alt1
- 2.2

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.8.8-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libparted
  * postun_ldconfig for libparted
  * obsolete-call-in-post-install-info for parted
  * postclean-05-filetriggers for spec file

* Mon May 05 2008 Led <led@altlinux.ru> 1.8.8-alt3
- without usermode (#15535)
- fixed Provides

* Tue Mar 04 2008 Led <led@altlinux.ru> 1.8.8-alt2
- fixed %name.desktop

* Wed Aug 15 2007 Led <led@altlinux.ru> 1.8.8-alt1
- 1.8.8:
  + Read an msdos partition table from a device with 2K sectors
  + Add detection support for Xen virtual block devices (/dev/xvd*)
  + Add the --dry-run option to the partprobe command
  + Support testing with tmpfs filesystems on Linux
- removed %name-1.8.7-linux_swap.patch due to "evert the implementation
  of linux-swap(old) and linux-swap(new) types" in upstream
- changed license from GPLv2+ to GPLv3+

* Sun Jul 22 2007 Led <led@altlinux.ru> 1.8.7-alt4
- fixed requires

* Thu Jul 19 2007 Led <led@altlinux.ru> 1.8.7-alt3
- cleaned up and fixed %name-1.8.7-linux_swap.patch

* Sat Jun 23 2007 Led <led@altlinux.ru> 1.8.7-alt2
- added %name-1.8.7-linux_swap.patch

* Sat May 15 2007 Led <led@altlinux.ru> 1.8.7-alt1
- 1.8.7
- updated BuildRequires
- cleaned up spec

* Sun Mar 25 2007 Led <led@altlinux.ru> 1.8.6-alt1
- 1.8.6: changed lib%name soname

* Mon Mar 19 2007 Led <led@altlinux.ru> 1.8.4-alt1
- 1.8.4: changed lib%name soname
- removed %name-1.7.0-configure.patch (fixed in upstream)
- fixed BuildRequires
- added lib%name.pc

* Tue Jan 16 2007 Led <led@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Mon Dec 04 2006 Led <led@altlinux.ru> 1.8.1-alt1
- 1.8.1
- enabled device-mapper

* Thu Nov 23 2006 Led <led@altlinux.ru> 1.8.0-alt1
- 1.8.0 release

* Wed Nov 08 2006 Led <led@altlinux.ru> 1.8.0-alt0.3
- 1.8.0rc3

* Thu Oct 12 2006 Led <led@altlinux.ru> 1.8.0-alt0.2
- 1.8.0rc2

* Thu Sep 21 2006 Led <led@altlinux.ru> 1.8.0-alt0.1
- 1.8.0rc1
- cleaned up and fixed spec

* Tue May 30 2006 Led <led@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Mon May 29 2006 Led <led@altlinux.ru> 1.7.0-alt2
- fixed spec

* Mon May 22 2006 Led <led@altlinux.ru> 1.7.0-alt1
- 1.7.0
- removed %name-1.6.24-alt-gcc-err.patch
- updated %name-1.7.0-configure.patch
- fixed spec

* Mon May 22 2006 Led <led@altlinux.ru> 1.6.25.1-alt1
- fixed spec

* Tue Mar 28 2006 Led <led@altlinux.ru> 1.6.25.1-alt0.4
- added %name-1.6.25.1-configure.patch

* Wed Jan 25 2006 Led <led@altlinux.ru> 1.6.25.1-alt0.3
- fix /etc/security/console.apps/%name
- fix spec

* Mon Jan 23 2006 Led <led@altlinux.ru> 1.6.25.1-alt0.2
- enabled static libs
- removed empty NEWS from docs
- added %name.desktop
- uk and ru Summary and description
- added usermode starting

* Thu Jan 19 2006 Led <led@altlinux.ru> 1.6.25.1-alt0.1
- 1.6.25.1

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.24-alt1.1
- Rebuilt with libreadline.so.5.

* Sun Sep 11 2005 Kachalov Anton <mouse@altlinux.ru> 1.6.24-alt1
- 1.6.24

* Sat Jan 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.21-alt1
- 1.6.21

* Wed Dec 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.19-alt1
- 1.6.19

* Wed Sep 01 2004 Kachalov Anton <mouse@altlinux.ru> 1.6.12-alt1
- new version
- busy_check patch by author of gparted.
- use %%subst_enable static
- use %%find_lang --with-man
- use %%post{,un}_ldconfig macros in post{,un} for libparted
- use {un,}install_info macros in post{,un} for parted
- enable SMP build.
- fix source URL.

* Wed Apr 28 2004 Kachalov Anton <mouse@altlinux.ru> 1.6.10-alt2
- moved info-files from libparted-devel to parted

* Mon Apr 19 2004 Kachalov Anton <mouse@altlinux.ru> 1.6.10-alt1
- 1.6.10

* Fri Dec 26 2003 Michael Shigorin <mike@altlinux.ru> 1.6.6-alt1
- 1.6.6
- removed *.la
- don't package static library by default
- added missing aclocal and info files

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Tue Oct 29 2002 Michael Shigorin <mike@altlinux.ru> 1.6.3-alt0.1
- 1.6.3
- changed configure options as per Yura Umanets' advice
- test/use with attention, I've not actually tested this build!

* Mon Jan 21 2002 Yury V. Umanets <umka@altlinux.ru> 1.5.6-alt2
- Fix some problems with compilling with gcc-2.96
- Some code cleanups

* Sat Jan 19 2002 Yury V. Umanets <umka@altlinux.ru> 1.5.6-alt1
- 1.5.6
- Added full ReiserFS support
- Fix a problem with --disable-nls option

* Fri Aug 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.18-alt1
- 1.4.18

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.17-alt1
- 1.4.17

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.16-alt1
- 1.4.16

* Thu Jul 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.15-alt1
- 1.4.15

* Mon May 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Wed May 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.11-alt2
- Fixed GROUP tag.

* Wed Apr 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.11-alt1
- 1.4.11

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.10-ipl1mdk
- 1.4.10

* Mon Feb 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.9-ipl1mdk
- 1.4.9

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.8-ipl1mdk
- 1.4.8
- Split into three subpackages.

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.6-ipl1mdk
- 1.4.6

* Sun Dec 31 2000 Dmitry V. Levin <ldv@fandra.org> 1.4.5-ipl1mdk
- 1.4.5

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.4.4-ipl1mdk
- 1.4.4

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 1.4.1-ipl1mdk
- 1.4.1

* Mon Nov 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.4.0-ipl1mdk
- 1.4.0

* Fri Nov 03 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.12-ipl1mdk
- 1.2.12

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.11-ipl1mdk
- 1.2.11

* Mon Oct 16 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.10-ipl1mdk
- 1.2.10

* Sat Sep 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.9-ipl1mdk
- 1.2.9

* Fri Aug 25 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.8-ipl1mdk
- 1.2.8

* Sun Aug 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.7-ipl1mdk
- 1.2.7

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.6-ipl1mdk
- RE adaptions.

* Mon Jul 31 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.6-1mdk
- new release

* Tue Jul 25 2000 Pixel <pixel@mandrakesoft.com> 1.2.5-3mdk
- move .so to -devel

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 1.2.5-2mdk
- use *all* new macros
- BM

* Tue Jul 18 2000 Pixel <pixel@mandrakesoft.com> 1.2.5-1mdk
- new version

* Sat Jul 15 2000 Pixel <pixel@mandrakesoft.com> 1.2.4-1mdk
- new version

* Wed Jun 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.3-1mdk
- new release
- use new macros
- add postun ldconfig (pixel sucks)

* Wed Jun 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2 (bug fixes release)
- add ldconfig in postinst (pxlscks)
- move libparted.so link to parted since parted need it (only keep lib*.a in
  parted-devel package) (pxlscks)

* Thu Jun 15 2000 Pixel <pixel@mandrakesoft.com> 1.2.1-1mdk
- new version

* Thu Jun  8 2000 Pixel <pixel@mandrakesoft.com> 1.0.17-4mdk
- new version (and add missing changelog, sorry for not resetting release, too late)

* Tue May 16 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.0.13-3mdk
- requires parted for parted-devel or you can't link anything!

* Thu Apr 13 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.13-2mdk

- Changed group for parted-devel
- Removed .po instal hack, looks like the Makefile is up to the task again -
  good.

* Mon Apr 10 2000 Pixel <pixel@mandrakesoft.com> 1.0.13-1mdk
- new version

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 1.0.12-1mdk
- new version

* Fri Mar 24 2000 Pixel <pixel@mandrakesoft.com> 1.0.11-1mdk
- new version

* Thu Mar 16 2000 Francis Galiegue <francis@mandrakesoft.com> 1.0.10-3mdk
- Don't use prefix, too many headaches
- Some spec file changes
- Changed group according to 7.1 hierarchy (the package wasn't in the list)
- Let spec-helper do its job

* Tue Feb 29 2000 Pixel <pixel@mandrakesoft.com> 1.0.10-1mdk
- new version

* Tue Feb 15 2000 Pixel <pixel@mandrakesoft.com> 1.0.9-2mdk
- bzip man page
- remove vendor tag

* Tue Feb 15 2000 Pixel <pixel@mandrakesoft.com> 1.0.9-1mdk
- new version

* Mon Feb 07 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used a great srpm provided by Geoffrey Lee <snailtalk@linux-mandrake.com>

* Mon Feb 07 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- Rebuilt for Mandrake
- 1.0.8

* Mon Jan 20 2000 Ryan Weaver <ryanw@infohwy.com>
  [parted-1.0.7-2]
- made ped_device_seek() a bit more portable
- changed type of PedDevice's heads, sector, cyl fields to int's.
- added a man page, contributed by Timshel Knoll <timshel@pobox.com>

* Thu Jan 20 2000 Ryan Weaver <ryanw@infohwy.com>
  [parted-1.0.6-2]
- fixed >16gig bug in libparted/disk_dos.c  (need LE32, not LE16!!!)

* Tue Jan 18 2000 Ryan Weaver <ryanw@infohwy.com>
  [parted-1.0.5-2]
- applied patch from Tim Waugh <twaugh@redhat.com>
- added autoconfuse checks up-to-date linux/ext2_fs.h
- imported new ext2_fs.h
- imported changes from ext2resize, to add support the ext2 "filetype"
  feature
- removed -Wno-sign-compare, because it breaks older gcc
- moved checks for termcap up before readline check, and get readline check
  to use the result of the termcap check.
- the "termcap" library can be now be one of: -ltermcap, -ltermlib, -lcurses,
  -lncurses.
- fixed buglet for FAT16 cluster entries
- fixed (hopefully) str_list_print_wrap()
- use static for do_* in parted/parted.c
- cleaned up parted.spec.in

  [parted-1.0.4-2]
- Fixed a silly bug in ped_partition_set_system() for extended partitions

* Tue Jan  4 2000 Ryan Weaver <ryanw@infohwy.com>
  [parted-1.0.3-2]
- Arrghh!  Found (and fixed) a VERY nasty bug during partition table writes.

  [parted-1.0.2-1]
- Arrghh!  Found (and fixed) a nasty bug in the string printing code.

  [parted-1.0.1-1]
- added some documentation about --without-readline and --disable-nls
