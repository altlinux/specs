%def_without floppyd

Name: mtools
Version: 4.0.43
Release: alt1
Epoch: 1

Summary: Programs for accessing FAT formatted media without mounting it
License: GPLv3
Group: File tools

Url: https://www.gnu.org/software/mtools/
Source0: https://ftp.gnu.org/gnu/mtools/%name-%version.tar.gz
Source1: floppyd.xinetd
Source100: mtools.watch
Packager: Michael Shigorin <mike@altlinux.org>

Patch0: mtools-3.9.6-config.patch
Patch2: mtools-3.9.6-atari.patch
Patch3: mtools-3.9.7-texinfo.patch
Patch4: mtools-3.9.10-alt-no-x.patch
Patch5: mtools-4.0.10-alt-buffer.patch

# for check
BuildRequires: dosfstools

Requires: glibc-gconv-modules

%if_with floppyd
# Automatically added by buildreq on Tue Apr 07 2009 (-bi)
BuildRequires: imake libSM-devel libX11-devel libXau-devel xorg-cf-files
%endif

%define inetd_dir     %_sysconfdir/xinetd.d
%define inetd_floppyd %inetd_dir/floppyd

Summary(ru_RU.UTF-8): Утилиты для работы с дисками MS-DOS
# explicitly added texinfo for info files
BuildRequires: texinfo

%package floppyd
Group: File tools
Requires: xinetd
Summary: Daemon for remote access to floppy drive
Summary(ru_RU.UTF-8): Демон для доступа к дисководам через сеть и X-терминал

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 Xdf disks, and 2m disks.

Mtools should be installed if you need to use MS-DOS disks without
mounting them.

%description -l ru_RU.UTF-8
Mtools содержит набор утилит для работы с дисками MS-DOS:
форматирования, чтения/записи, управления атрибутами,
проверки на сбойные блоки и т.д.

Mtools работает с дискетами напрямую, минуя драйверы файловых систем Линукса,
то есть монтировать дискету утилитой mount при использовании Mtools не нужно.
Это означает, что поддержка FAT в ядре операционной системы не требуется
(хотя её отсутствие сейчас - случай уникальный).

Mtools поддерживает длинные имена в стиле Windows95, Xdf-диски OS/2,
а также дискеты большой ёмкости, созданные с помощью утилиты 2m.

%description floppyd
Floppyd is used as a server to grant access to the floppy drive to clients
running on a remote machine, just as an X server grants access to the display
to remote clients. floppyd is always associated with an X server.
It runs on the same machine as its X server, and listens on port 5703 and above.

%description floppyd -l ru_RU.UTF-8
Floppyd является сервером, предоставляющим доступ к дискетам для клиентов,
работающих на других компьютерах подобно тому, как X-сервер предоставляет им
доступ к монитору. Floppyd выполняет привязку к X-серверу, запущенному
на том же компьютере, и пользуется его системой авторизации.

%prep
%setup
%patch0 -p1
#patch2 -p1
#patch3 -p1
%if_without floppyd
#patch4 -p1
%endif
#patch5 -p1

find -type f -print0 |
	xargs -r0 grep -FZl -- /usr/local/etc |
	xargs -r0 sed -i -- 's,/usr/local/etc,%_sysconfdir,g'

%build
%autoreconf
%configure
%make_build all info

%install
%makeinstall install-info
install -pDm644 %name.conf %buildroot%_sysconfdir/%name.conf

%if_with floppyd
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/floppyd* %buildroot%_sbindir
install -pD %SOURCE1 %buildroot%inetd_floppyd
%else
find %buildroot -name floppyd\* -print0 | xargs -r0 rm -fv --
%endif

%check
dd if=/dev/zero of=.efiboot.img bs=32k count=227
/sbin/mkfs.fat -v -n 'El Torito' .efiboot.img
mkdir -p EFI/BOOT EFI/enroll
touch EFI/BOOT/bootia32.efi EFI/enroll/cert
%buildroot%_bindir/mcopy -v -i .efiboot.img -s EFI ::

%files
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc NEWS README mkdosboot *.tex

%if_with floppyd

%exclude %_man1dir/floppyd*

%files floppyd
%inetd_floppyd
%_sbindir/floppyd*
%_man1dir/floppyd*

%endif

# TODO:
# - revisit mtools-3.9.10-alt-no-x.patch?
# - review, rediff and send upstream patch1, patch2

%changelog
* Wed Mar 22 2023 Anton Midyukov <antohami@altlinux.org> 1:4.0.43-alt1
- new version 4.0.43

* Fri Nov 18 2022 Anton Midyukov <antohami@altlinux.org> 1:4.0.42-alt1
- new version (4.0.42) with rpmgs script via gear-uupdate

* Mon Jul 19 2021 Anton Midyukov <antohami@altlinux.org> 1:4.0.32-alt3
- add check mcopy to image with FAT12

* Mon Jul 19 2021 Michael Shigorin <mike@altlinux.org> 1:4.0.32-alt2
- reverting to 4.0.32 due to mcopy breakage (ALT#40532)

* Sun Jul 18 2021 Michael Shigorin <mike@altlinux.org> 4.0.33-alt1
- new version (watch file uupdate)

* Wed Jul 14 2021 Michael Shigorin <mike@altlinux.org> 4.0.32-alt1
- new version (watch file uupdate)

* Sun Jun 20 2021 Michael Shigorin <mike@altlinux.org> 4.0.31-alt1
- new version (watch file uupdate)

* Fri Jun 18 2021 Michael Shigorin <mike@altlinux.org> 4.0.30-alt1
- new version (watch file uupdate)

* Tue Jun 01 2021 Michael Shigorin <mike@altlinux.org> 4.0.29-alt1
- new version (watch file uupdate)

* Mon May 31 2021 Michael Shigorin <mike@altlinux.org> 4.0.28-alt1
- new version (watch file uupdate)

* Sat Apr 17 2021 Michael Shigorin <mike@altlinux.org> 4.0.27-alt1
- new version (watch file uupdate)

* Mon Nov 30 2020 Michael Shigorin <mike@altlinux.org> 4.0.26-alt1
- new version (watch file uupdate)

* Sun Oct 25 2020 Michael Shigorin <mike@altlinux.org> 4.0.25-alt1
- new version (watch file uupdate)

* Sun Mar 22 2020 Michael Shigorin <mike@altlinux.org> 4.0.24-alt1
- new version (watch file uupdate)

* Mon Dec 10 2018 Michael Shigorin <mike@altlinux.org> 4.0.23-alt1
- new version (watch file uupdate)

* Mon Dec 03 2018 Michael Shigorin <mike@altlinux.org> 4.0.22-alt1
- new version (watch file uupdate)

* Sat Nov 24 2018 Michael Shigorin <mike@altlinux.org> 4.0.21-alt1
- new version (watch file uupdate)
- dropped gentoo patches (merged upstream)

* Mon Nov 12 2018 Michael Shigorin <mike@altlinux.org> 4.0.20-alt1
- new version (watch file uupdate)

* Fri Oct 05 2018 Michael Shigorin <mike@altlinux.org> 4.0.19-alt1
- new version (watch file uupdate)

* Mon Nov 06 2017 Michael Shigorin <mike@altlinux.org> 4.0.18-alt2
- added gentoo patches

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.18-alt1.1
- NMU: added BR: texinfo

* Wed Feb 20 2013 Michael Shigorin <mike@altlinux.org> 4.0.18-alt1
- new version (watch file uupdate)

* Tue Jul 10 2012 Michael Shigorin <mike@altlinux.org> 4.0.17-alt3
- added Requires: glibc-gconv-modules (closes: #27525)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 4.0.17-alt2
- added watch file

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 4.0.17-alt1
- 4.0.17

* Thu Jun 16 2011 Michael Shigorin <mike@altlinux.org> 4.0.16-alt1
- 4.0.16

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 4.0.14-alt1
- 4.0.14
- cooking a goose! :)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 4.0.13-alt1
- 4.0.13
- disabled patch2
- disabled patch5 (redone slightly differently upstream)

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 4.0.12-alt1
- 4.0.12

* Mon Jul 20 2009 Michael Shigorin <mike@altlinux.org> 4.0.10-alt3
- replaced my broken patch with vsu@'s one; mine fixed build
  while breaking filename handling fundamentally, shame on me...
- clarified License: along the way

* Mon Jul 20 2009 Michael Shigorin <mike@altlinux.org> 4.0.10-alt2
- fixed sloppy DOS filename buffer handling

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 4.0.10-alt1
- 4.0.10:
  + Unicode support
  + translit support
  + LSEEK64 support
- v20071226 also fixed security issue with doctored file names
- disabled patch3, patch4
- updated an Url:
- spec cleanup
- buildreq
- NB: this package would benefit from proper maintainer

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 3.9.11.20070601-alt2
- fixed build: buildreq and calling sed properly
- spec cleanup
- me as a Packager:
- description translation converted to utf-8

* Mon Jun  4 2007 Ilya Evseev <evseev@altlinux.ru> 3.9.11.20070601-alt1
- Updated to 3.9.11, with the latest patchset

* Tue Jul 25 2006 Ilya Evseev <evseev@altlinux.ru> 3.9.10.20060626-alt1
- Updated by latest patchset 3.9.10.20060626

* Tue May  2 2006 Ilya Evseev <evseev@altlinux.ru> 3.9.10.20060228-alt1
- Updated by latest patchset, updated patch #4
- New version scheme including patchset timestamp

* Mon Feb 20 2006 Ilya Evseev <evseev@altlinux.ru> 3.9.10-alt2
- Updated to 3.9.10-20051011

* Mon Apr  4 2005 Ilya Evseev <evseev@altlinux.ru> 3.9.10-alt1
- Updated to 3.9.10-20050317
- Floppy daemon is back, packaged optionally via 'rpmbuild --with floppyd'
- Specfile:
   + added russian summary/description
   + changed docfiles list

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 3.9.9-alt2
- Updated build dependencies.

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 3.9.9-alt1
- Updated to 3.9.9

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 3.9.8-alt3
- rebuild with gcc3

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.9.8-alt2
- Fixed build.

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.9.8-alt1
- 3.9.8

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.9.7-ipl2mdk
- Fixed texinfo documentation.
- Fixed wrong references to /usr/local.

* Tue Jul 04 2000 Dmitry V. Levin <ldv@fandra.org> 3.9.7-ipl1mdk
- RE and Fandra adaptions.

* Mon Jun 19 2000 DindinX <odin@mandrakesoft.com> 3.9.7-1mdk
- 3.9.7
- use of %configure and %makeinstall
- updated patches

* Fri Mar 24 2000 DindinX <odin@mandrakesoft.com> 3.9.6-5mdk
- Group and spec fixes

* Fri Jan 28 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.9.6-4mdk
- added a defattr

* Fri Nov 12 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Sat Aug 07 1999 Bernhard RosenkrДnzer <bero@linux-mandrake.com>
- 19990729 bugfix
- add patch to allow reading Atari ST disks (am I the only person
  trying to use STonX occasionally???)

* Thu Jul  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.9.6
- Prefixing the .spec.

* Sat May 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove the 1.44m in mtools.conf (reported by Jacques).

* Wed May 05 1999 Bernhard RosenkrДnzer <bero@linux-mandrake.com>
- Mandrake adaptions
- 3.9.5

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- patch to make the texi sources compile
- fix the spec file group and description
- fixed floppy drive sizes

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- fixed invalid SAMPLE_FILE configuration file

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- Built package for 5.2.
- Updated Source to 3.9.1.
- Cleaned up spec file.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 3.8

* Tue Oct 21 1997 Otto Hammersmith
- changed buildroot to /var/tmp, rather than /tmp
- use install-info

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Apr 17 1997 Erik Troan <ewt@redhat.com>
- Changed sysconfdir to be /etc

* Mon Apr 14 1997 Michael Fulbright <msf@redhat.com>
- Updated to 3.6
