%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_enable snapshot
%set_verify_elf_method unresolved=relaxed

%def_enable static
%def_enable shared
%def_disable rpath
%def_disable mtrace
%def_disable debug
%def_disable ro
%def_disable discover_only
%def_enable dynamic_loading
%def_disable pc98
%def_enable largefile
%def_enable nls
%def_with readline
%def_with pic
%def_enable selinux
%def_enable device_mapper
%def_without usermode
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%define Name Parted
Name: parted
%define lname lib%name
Version: 3.6
%define prerel %nil
%define git_version %{version}.46-e4ae
Release: alt1

Summary: Flexible partitioning tool
Summary(uk_UA.UTF-8): Универсальний інструмент для роботи з разділами диску
Summary(ru_RU.UTF-8): Универсальный инструмент для работы с разделами диска
License: GPLv3
Group: System/Configuration/Hardware
URL: http://www.gnu.org/software/%name

%if_disabled snapshot
Source: ftp://ftp.gnu.org/gnu/%name/%name-%version%prerel.tar.xz
%else
Source: %name-%git_version.tar.xz
%endif
Source1: %name-pam
Source2: %name-security

Patch0: parted-3.4-fix-segfault-on-exit.patch

Requires: %lname = %version-%release

BuildRequires: gcc-c++ libtinfo-devel libreadline-devel
BuildRequires: libe2fs-devel libuuid-devel libblkid-devel
BuildRequires: libcheck-devel
%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_enable_device_mapper:BuildRequires: libdevmapper-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel libsepol-devel}
# for check
BuildRequires: e2fsprogs xfsprogs dosfstools perl-Digest-CRC bc
# explicitly added texinfo for info files
BuildRequires: texinfo

# configure.ac has such requirements:
BuildPreReq: autoconf >= 2.63 automake >= 1.11.6

%description
GNU %Name is a program that allows you to create, destroy, resize,
move and copy hard disk partitions. This is useful for creating space
for new operating systems, reorganising disk usage, and copying data to
new hard disks.

%description -l uk_UA.UTF-8
GNU %Name - програма для створення, знищення, зміни розміру,
переміщення та копіювання розділів диску. Це може бути корисним при
створенні місця для нових операційних систем, реорганізації
використання диску та копіювання даних на новий жорсткий диск.

%description -l ru_RU.UTF-8
GNU %Name - программа для создания, уничтожения, изменения размера,
перемещения и копирования разделов диска. Это может быть полезно при
создании места для новых операционных систем, реорганизации
использования диска и копировании данных на новый жесткий диск.


%if_enabled shared
%package -n %lname
Summary: Shared library for flexible partitioning tool
Group: System/Libraries

%description -n %lname
This package includes the shared library needed to run
%lname-based software.

%description -n %lname -l uk_UA.UTF-8
Цей пакет включає в себе роздільні бібліотеки, необхідні для запуску
програм, що використовують %lname.

%description -n %lname -l ru_RU.UTF-8
Этот пакет включает в себя разделяемые библиотеки, необходимые для
запуска программ, которые используют %lname.
%endif

%package -n %lname-devel
Summary: Files required to compile software that uses %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%description -n %lname-devel
This package includes the header files.

%description -n %lname-devel -l uk_UA.UTF-8
Цей пакет включає в себе файли заголовків.

%description -n %lname-devel -l ru_RU.UTF-8
Этот пакет включает в себя файлы заголовков.

%if_enabled static
%package -n %lname-devel-static
Summary: Files required to compile statically linked software that uses %lname
Group: Development/C
Requires: %lname-devel = %version-%release
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static

%description -n %lname-devel-static
This package includes the libraries needed to statically link software
with %lname.

%description -n %lname-devel-static -l uk_UA.UTF-8
Цей пакет включає в себе бібліотеки, необхідні для статичного
лінкування з %lname.

%description -n %lname-devel-static -l ru_RU.UTF-8
Этот пакет включает в себя библиотеки, необходимые для статической
линковки с %lname.
%endif


%prep
%if_disabled snapshot
%setup -n %name-%version%prerel
%else
%setup -n %name-%git_version
%endif

%patch0 -p1

%build
%configure \
    %{subst_enable rpath} \
    %{subst_with pic} \
    %{subst_enable mtrace} \
    %{subst_enable debug} \
    %{subst_enable_to ro read-only} \
    %{subst_enable_to discover_only discover-only} \
    %{subst_enable_to dynamic_loading dynamic-loading} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable pc98} \
    %{subst_enable largefile} \
    %{subst_enable nls} \
    %{subst_with readline} \
    %{subst_enable_to device_mapper device-mapper} \
    %{subst_enable selinux}

%make_build

bzip2 --best --keep --force ChangeLog

%install
%makeinstall_std

%if_with usermode
#usermode
install -D -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -D -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
install -d %buildroot%_bindir
ln -s %_bindir/consolehelper %buildroot%_bindir/%name

#menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Encoding=UTF-8
Exec=%name
Name=%Name
Icon=
Terminal=true
Type=Application
Comment=Flexible partitioning tool
Comment[uk]=Универсальний інструмент для роботи з разділами диску
Comment[ru]=Универсальный инструмент для работы с разделами диска
Categories=Application;System;Filesystem;ConsoleOnly;
__MENU__
%endif

%find_lang --output=%name.lang %name

# some tests require root priviledges
#%check
#export LD_LIBRARY_PATH=$(pwd)/libparted/.libs
#%make check

%post
%{?_with_usermode:}

%files -f %name.lang
%doc AUTHORS BUGS NEWS README THANKS TODO
%_sbindir/%name
%_sbindir/partprobe
%_infodir/*
%_man8dir/%name.*
%_man8dir/partprobe.*
%if_with usermode
%_bindir/%name
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_desktopdir/*
%endif

%if_enabled shared
%files -n %lname
%_libdir/%lname.so.*
%_libdir/%lname-fs-resize.so.*
%endif

%files -n %lname-devel
%doc doc/API doc/FAT ChangeLog.*
%{?_enable_shared:%_libdir/*.so}
%_includedir/%name/
%_pkgconfigdir/%lname.pc
%_pkgconfigdir/%lname-fs-resize.pc

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Tue Nov 07 2023 Leontiy Volodin <lvol@altlinux.org> 3.6-alt1
- 3.4 -> 3.6

* Thu Sep 09 2021 Anton Farygin <rider@altlinux.ru> 3.4-alt1
- 3.2 -> 3.4 (closes: #40175)

* Mon Mar 30 2020 Nikita Ermakov <arei@altlinux.org> 3.2-alt6
- Fix building with glibc >= 2.27.

* Mon Nov 19 2018 Anton Farygin <rider@altlinux.ru> 3.2-alt5
- fixed charset in package summary and description (closes: #33045)

* Mon Jul 03 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.2-alt4
- (.spec) BuildPreReq: autoconf >= 2.63 automake >= 1.11.6
  (due to configure.ac).

* Thu Aug 04 2016 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt3
- updated to v3.2-46-ge4ae433

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.2-alt2.1
- NMU: added BR: texinfo

* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 3.2-alt2
- added patch to fix crash on FAT16 resize (bgo#735669)

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2

* Sun Dec 09 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt3
- Fixed interpackage dependencies.
- Really fixed build.

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2.1
- Fixed build with glibc 2.16

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
- 1.8.6: changed %lname soname

* Mon Mar 19 2007 Led <led@altlinux.ru> 1.8.4-alt1
- 1.8.4: changed %lname soname
- removed %name-1.7.0-configure.patch (fixed in upstream)
- fixed BuildRequires
- added %lname.pc

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
