Name: eject
Version: 2.1.5
Release: alt3

Summary: A program that ejects removable media using software control
Group: System/Kernel and hardware
License: GPL
Url: http://www.pobox.com/~tranter/eject.html
Packager: Sergey V Turchin <zerg at altlinux dot org>

# http://ca.geocities.com/jefftranter@rogers.com/eject-%version.tar.gz
Source: eject-%version.tar
Source1: ru.po

Patch1: eject-2.1.5-alt-fixes.patch
Patch2: eject-2.1.5-alt-mntent.patch
Patch3: eject-2.1.5-alt-supersubmount.patch
Patch4: eject-2.1.5-alt-i18n.patch
Patch5: eject-2.1.5-alt-usage-stdout.patch

%description
Eject allows removable media (typically a CD-ROM, floppy disk, tape,
or JAZ or ZIP disk) to be ejected under software control.  The command
can also control some multi-disc CD-ROM changers, the auto-eject feature
supported by some devices, and close the disc tray of some CD-ROM drives.

%prep
%setup -q -n %name
install -pm644 %_sourcedir/ru.po po/

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -fisv
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_bindir/*
%_mandir/man?/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Thu Jun 28 2007 Sergey V Turchin <zerg at altlinux dot org> 2.1.5-alt3
- update Russian translation
- fix return code and proper output of usage()

* Tue Apr 24 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1.5-alt2
- Added Packager tag.
- Uncompressed tarball.
- Moved autoreconf from %%prep to %%build.
- Cleaned up specfile a bit.
- Changed -alt patch to use program_invocation_short_name.
- Rediffed patches and renamed them according to the policy.
- Fixed unchecked fgets() and fd leak in ReadSpeedCdrom().
- Fixed unchecked realpath() in SymLink().

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 2.1.5-alt1
- new version

* Wed Aug 03 2005 Sergey V Turchin <zerg at altlinux dot org> 2.1.0-alt1
- new version
- add Russian translation

* Tue May 11 2004 Sergey V Turchin <zerg at altlinux dot org> 2.0.13-alt4
- improve supermount patch for subfs

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 2.0.13-alt3
- fix mntent && supermount patches
  thanx ldv

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 2.0.13-alt1.1
- added mntent patch
- don't umount when supermount, but only if device presented
  in /etc/fstab in traditional place too

* Fri Feb 21 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.13-alt1
- 2.0.13
- added autoclose patch from RH.

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.12-alt2
- rebuild with gcc3

* Mon Oct 08 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.12-alt1
- 2.0.12

* Mon Jul 09 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.10-alt1
- 2.0.10. Removed error()'s from alt patch (internationalization added in this version).

* Wed May 30 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.9-alt1
- 2.0.9 .
* Tue May 22 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.8-alt1
- 2.0.8 . Added patch that allow using of /proc/mounts instead /etc/mtab.

* Fri May 04 2001 Rider <rider@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Wed Apr 25 2001 Rider <rider@altlinux.ru> 2.0.3-alt1
- 2.0.3
- new program "volname"

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.2-ipl8mdk
- RE adaptions.

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.2-8mdk
- BM
- specfile cleanup
- macrozashions

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0.2-7mdk
- fix group

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build Release.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- solved a lot of problems by finding eject 2.0.2. :)

* Tue Feb 09 1999 Preston Brown <pbrown@redhat.com>
- patch to improve symlink handling folded into linux-2.2 patch

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jul 15 1998 Donnie Barnes <djb@redhat.com>
- added small patch to 1.5 for longer device names

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 1.5
- various spec file clean ups
- eject rocks!

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
