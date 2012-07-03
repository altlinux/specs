Name: cpio
Version: 2.11
Release: alt1

Summary: A GNU archiving program
License: GPLv3+
Group: Archiving/Backup
Url: http://www.gnu.org/software/cpio/

# ftp://ftp.gnu.org/gnu/cpio/cpio-%version.tar.bz2
Source: cpio-%version.tar
Patch: cpio-%version-%release.patch

# Due to static subpackage.
BuildPreReq: glibc-devel-static

Summary(ru_RU.UTF-8): Утилита архивации и копирования данных GNU cpio

%package static
Summary: Static version of the GNU cpio
Group: Archiving/Backup
Requires: %name = %version-%release
Summary(ru_RU.UTF-8): Статически скомпонованная версия архиватора GNU cpio

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

%description -l ru_RU.UTF-8
GNU cpio помещает и извлекает файлы из архивов формата TAR и CPIO.
Архивами в Юниксе принято называть файлы, хранящие коллекции других файлов
(необязательно сжатую - этим отдельно занимаются программы компрессии),
плюс некоторую дополнительную информацию о них: имена, идентификаторы
владельца и группы, время создания и изменения, права доступа и т.д.
Архив может храниться в файле на диске, на магнитной ленте, или записан
в канал (pipe) для обработки другой программой. GNU cpio поддерживает
следующие форматы архивов: двоичный, старый ASCII, новый ASCII, crc,
двоичный HPUX, старый ASCII HPUX, старый TAR и TAR стандарта POSIX.1.
По умолчанию GNU cpio создаёт архивы в двоичном формате, совместимые
со старыми реализациями программы cpio. При извлечении cpio определяет
формат архива автоматически, в частности, правильно восстанавливает
порядок байтов, даже если архив был создан на машине с другой архитектурой.

%description -l uk_UA.KOI8-U
cpio коп╕ю╓ файли в або з арх╕ву cpio або tar, який явля╓ собою файл,
що м╕стить ╕нш╕ файли та ╕нформац╕ю про них, таку як ╕м'я файлу, його
власника, час створення, права доступу ╕ т.╕. Арх╕вом може бути файл,
стр╕чка або пайп.

%description static
This package contains statically linked version of the GNU cpio program.

%description -l ru_RU.UTF-8 static
Статически скомпонованная версия GNU cpio. Занимает больше места,
чем основной, динамически скомпонованный вариант, используемый
по умолчанию, но меньше зависит от общесистемных библиотек
и может пригодиться для аварийных работ.

%prep
%setup
%patch -p1

# Outdated by fresh autoconf.
rm m4/extensions.m4
find -type f -print0 |
	xargs -r0 fgrep -lZ gl_USE_SYSTEM_EXTENSIONS -- |
	xargs -r0 sed -i 's/gl_USE_SYSTEM_EXTENSIONS/AC_USE_SYSTEM_EXTENSIONS/g' --

%build
# Several changes modify configure.ac and Makefile.am
%autoreconf
%configure --disable-mt --with-rmt=/sbin/rmt --disable-silent-rules
%make_build

%check
%make_build -k check

%install
%makeinstall bindir=%buildroot%_bindir mandir=%buildroot%_mandir
mkdir -p %buildroot/bin
mv %buildroot%_bindir/cpio %buildroot/bin/
mv %buildroot%_bindir/cpio{,.}static

%find_lang %name

%files -f %name.lang
/bin/cpio
%_infodir/cpio.info*
%_mandir/man?/cpio.*
%doc AUTHORS NEWS README THANKS TODO
%exclude %_man1dir/mt.*

%files static
%_bindir/cpio.static

%changelog
* Sun Mar 14 2010 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt1
- Updated to 2.11.

* Thu Nov 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt3
- Fixed creation of newc/crc archives with files containing multiple hard links.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt2
- Moved "make check" to %%check section.

* Mon Jul 06 2009 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt1
- Updated to 2.10.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Tue Oct 21 2008 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt3
- Fixed build with fresh autotools.
- Fixed build with gcc-4.3.x.
- Dropped ChangeLog.bz2.

* Thu Aug 30 2007 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt2
- Ignore age of existing file when creating directory in copyin mode.

* Wed Aug 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt1
- Updated to 2.9.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt17
- Reduced macro abuse in specfile.

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt16
- Fixed build with gcc-4.1.0.

* Wed Nov 16 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt15
- Backported fixes for write_out_header() and read_for_checksum()
  from cpio CVS.
- Backported savedir() fix from gnulib CVS.

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt14
- Fixed dircategory entry in texinfo documentation.

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt13
- Configure with proper rmt(8) location: /sbin/rmt.
- Do not even build rmt.

* Fri May 13 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.6-alt12.1
- Rebuilt with glibc-devel-static-2.3.5-alt2.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt12
- Fixed race condition while setting permissions
  in copy-in and copy-pass modes:
  + corrected directory creation algorithm to chmod existing
    directory using safe mode before chown, for each directory
    which is going to be reused by cpio.

* Tue May 10 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt11
- Rebuilt with glibc-2.3.5-alt1.

* Fri May 06 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt10
- Fixed two race condition issues while setting permissions
  in copy-in and copy-pass modes:
  + corrected open(2) calls to use O_EXCL;
  + corrected mkdir(2) and mknod(2) calls to use safe permissions.

* Thu May 05 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt9
- Applied find_inode_file fix from Debian's cpio package.

* Tue May 03 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt8
- Fixed several race condition issues while setting permissions
  in copy-in and copy-pass modes (CAN-2005-1111).
- Removed patches:
  mtime: obsolete;
  stdout: invalid;
  errorcode: broken;
- Renamed patched according to our conventions, rediffed
  and renumbered them.
- Deal with compilation warnings generated by compiler.

* Tue Apr 26 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt7
- Fixed directory traversal issue in copy-in and copy-pass
  modes (CAN-2005-1229).

* Tue Feb 01 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt6
- Updated lfs patch.
- Fixed umask issue (CAN-1999-1572).

* Tue Feb 01 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt5
- Fixed lstat support.

* Tue Feb 01 2005 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt4
- Build with fresh automake.
- Fixed i18n patch.
- Reenabled "--extract --sparse".

* Thu Jan 27 2005 Ilya Evseev <evseev@altlinux.ru> 2.6-alt3
- autoreconf is called between patching and calling configure script
- added EXPERIMENTAL unfinished building of static version
  using diet-libc instead of glibc-static for reducing size
- few docfiles additionally placed to packaging

* Sun Jan  9 2005 Ilya Evseev <evseev@altlinux.ru> 2.6-alt2
- specfile: change (un)install_info dependency to modern style

* Tue Jan  7 2005 Ilya Evseev <evseev@altlinux.ru> 2.6-alt1
- version 2.6
- patchset changes:
   + commented obsoleted patches #1 (no more glibc problems)
     and #6 (superceded by patch #3)
   + reapplied patches 4,5,9,10
   + patch #3 is upgraded from old incomplete ALT to actual full MDK
   + added patches 2,7(replacing old RH/ALT patches),21,22 from PLD
   + todo's: patch #8 still unapplied; compile warnings still not fixed
- other specfile changes:
   + added russian summary and description
   + added ukrainian description, taken from PLD
   + completely ignore mt/rmt stuff
   + use find_lang for processing message files

* Fri Apr 11 2003 Dmitry V. Levin <ldv@altlinux.org> 2.5-alt4
- Updated buildrequires.

* Thu Mar 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.5-alt3
- Build static version of the GNU cpio program.
- Added more verbosity to error messages.

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5-alt2
- Rebuilt in new environment.

* Thu Aug 01 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5-alt1
- 2.5, 5 patches merged upstream.

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.2-ipl18mdk
- Merged patches (redhat, debian).

* Wed Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.2-ipl17mdk
- Fixed texinfo documentation.

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.2-ipl16mdk
- RE adaptions.

* Tue Jul 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.4.2-16mdk
- clean a lot the spec (macros, install fix by Stefan van der Eijk
  <s.vandereijk@chello.nl>)
- use spechelper

* Sat Jul 08 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 2.4.2-16mdk
- fixed makeinstall problem
- some hassle getting the manpage in the right dir

* Thu Apr 4 2000 Denis Havlik <denis@mandrakesoft.com> 2.4.2-15mdk
- new Group: Archiving/Backup

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Specs files tweaks.
- Merge with rh patchs.
- fix infinite loop unpacking empty files with hard links (r).
- stdout chould contain progress information (r).

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- longlong dev wrong with "-o -H odc" headers (formerly "-oc").

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to compile on glibc 2.1, where strdup is a macro

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- Fiddle bindir/libexecdir to get RH install correct.
- Don't include /sbin/rmt -- use the rmt from dump package.
- Don't include /bin/mt -- use the mt from mt-st package.
- Add prereq's

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- fix '-c' to duplicate svr4 behavior (problem #438)
- install support programs & info pages

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot
- removed "(used by RPM)" comment in Summary

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- no longer statically linked as RPM doesn't use cpio for unpacking packages
