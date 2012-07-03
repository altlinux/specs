Name: tar
Version: 1.23
Release: alt5

Summary: A GNU file archiving program
License: GPLv3+
Group: Archiving/Backup
Url: http://www.gnu.org/software/tar/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.gnu.org/gnu/tar/tar-%version.tar.bz2
Source: tar-%version.tar
Source1: tar.1
Patch: tar-%version-%release.patch

Summary(ru_RU.UTF-8): Утилита проекта GNU для архивации файлов

%description
The GNU tar program saves many files together into one archive and
can restore individual files (or all of the files) from the archive.
tar can also be used to add supplemental files to an archive and to
update or list files in the archive.  tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives and the ability to perform incremental and full backups.

%prep
%setup -q
%patch -p1
bzip2 -9fk ChangeLog

%build
export tar_cv_path_RSH=no
%configure --bindir=/bin --with-rmt=/sbin/rmt --disable-silent-rules
sed -i '/HAVE_CLOCK_GETTIME/d' config.h
%make_build LIB_CLOCK_GETTIME=

%check
%make_build -k check LIB_CLOCK_GETTIME=

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall bindir=%buildroot/bin LIB_CLOCK_GETTIME=
ln -s ../../bin/tar %buildroot%_bindir/gtar
install -pm644 %_sourcedir/tar.1 %buildroot%_man1dir/
%find_lang %name

%files -f %name.lang
/bin/tar
%_bindir/gtar
%_mandir/man?/*
%_infodir/tar.info*
%doc AUTHORS ChangeLog.bz2 NEWS README THANKS TODO

%changelog
* Tue Jul 06 2010 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt5
- Updated to git://git.sv.gnu.org/tar release_1_23-18-g9c194c9.
- Backported workaround for ovz kernel bug #970 from coreutils.

* Sun Mar 21 2010 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt4
- Synced with 1.23-owl3: updated the documentation on --rsh-command.

* Sat Mar 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt3
- Updated to release_1_23-7-g340dbf5 (closes: #23187).
- Changed --rsh-command to have no default.

* Thu Mar 11 2010 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt2
- Fixed use of uninitialized variables.

* Wed Mar 10 2010 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt1
- Updated to 1.23 (fixes CVE-2010-0624).

* Sat Dec 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.22.90-alt3
- Corrected highly non-optimal memory allocation by
  canonicalize_filename_mode(), which got exposed with an
  unrelated change made shortly before the 1.22.90 release.
  Reported by Solar Designer, patch by Eric Blake.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.22.90-alt2
- Moved "make check" to %%check section.

* Tue Aug 25 2009 Dmitry V. Levin <ldv@altlinux.org> 1.22.90-alt1
- Updated to 1.22.90.

* Mon Jul 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt2
- Fixed build with fresh gcc.

* Tue Jul 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt1
- Updated to release_1_22-12-g01c4475.
- Updated FC patches.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Thu Apr 17 2008 Alexey Gladkov <legion@altlinux.ru> 1.20-alt1
- Updated to 1.20.

* Thu Aug 30 2007 Dmitry V. Levin <ldv@altlinux.org> 1.18-alt3
- Use fchown/fchmod instead of chown/chmod to set permissions
  of just created regular files.
- Use gl_futimens instead of utimens to set timestamps
  of just created regular files.
- Use lstat instead of stat in extract mode to avoid directory
  traversal attack when extracting into untrusted directory.

* Fri Aug 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1.18-alt2
- Fixed crash bug in list and extract modes.
- Changed license to GPLv3+.

* Sun Aug 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.18-alt1
- Updated to 1.18.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt8
- Reduced macro abuse in specfile.

* Tue Nov 28 2006 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt7
- Disabled GNUTYPE_NAMES handling by default and
  added --allow-name-mangling option to re-enable it.
  (CVE-2006-6097, patch from Kees Cook).

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt6
- Fixed build with gcc-4.1.0.

* Sat Feb 18 2006 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt5
- Backported upstream fix for potential heap buffer overrun
  in handling extended headers (CVE-2006-0300).

* Wed Nov 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt4
- Backported savedir() fix from gnulib CVS.

* Sun Nov 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt3
- Backported a few fixes from tar CVS.

* Sun May 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1.15.1-alt2
- Reviewed patches.
- Replaced broken mdk-doubleslash.patch with
  alt-contains_dot_dot.patch
- Applied fixes from Debian's tar package.
- Renamed patched according to our conventions, rediffed
  and renumbered them.
- Added missing tests/append.at and enabled test suit by default.
- Do not even build rmt.

* Fri Jan 14 2005 Ilya Evseev <evseev@altlinux.ru> 1.15.1-alt1
- Updated to 1.15.1
- specfile: added russian summary/description, changed URL's
- patchset changes:
   + rediff P1,P3,P21
   + remove P2,P11,P12,P22,P23,P31,P32 since they are in upstream now
   + replace P13 from 1.13.25-rh to 1.14-mdk, add P33 from Mdk
- Replaced pre-written manual page with help2man-generated one.
- /sbin/rmt is explicitly excluded from packaging
  because dump package provides better rmt implementation.

* Mon Sep 29 2003 Dmitry V. Levin <ldv@altlinux.org> 1.13.25-alt3
- Fixed symlink extraction bug (deb #149532).
- Fixed archive corruption in special cases (deb #126274).
- Updated package dependencies.

* Mon Jun 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1.13.25-alt2.1
- fix build in bte. no hard-compiled aclocal-1.6

* Sat Sep 28 2002 Dmitry V. Levin <ldv@altlinux.org> 1.13.25-alt2
- Replaced our dot-dot patch with better one from Owl.
- Fixed build with autoconf >= 2.53 (rh).
- Fixed argv NULL termination (rh).
- Don't include hardlinks to sockets and doors in a tar file (rh).
- Updated without_librt patch.

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.13.25-alt1
- 1.13.25, updated patches to new version.

* Sat Sep 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.13.22-alt1
- 1.13.22, updated patches to new version.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.13.19-ipl2mdk
- Merged RH and Owl patches.

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 1.13.18-ipl1mdk
- Merged RH and MDK patches.
- Fixed texinfo documentation.

* Tue Sep 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.13.17-ipl6mdk
- Fix exit code (RH).

* Sun Apr  2 2000 Dmitry V. Levin <ldv@fandra.org>
- Merged RH patches.

* Sun Feb 20 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Thu Feb 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.13.17-1mdk
- Make -y alias to -I and document it as obsoltes.
- 1.13.17.

* Tue Jan 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.13.11-3mdk
- call configure with LINGUAS unset.

* Mon Nov  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Reinserting -y support patchs.

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Split: back to the tar stable version for cassini.

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.13.13.

* Thu Oct 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.13.12.

* Fri Sep 03 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.13.11

* Fri Aug 20 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.13.10

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.3.6

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.13.5

* Thu Jul 15 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.13.2
- french description

* Tue Jul 12 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
- 1.13.1

* Fri Jul 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.
- Patch to handle bzip2.

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update to 1.2.64011.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- add de locale
- some spec tweaks
- bzip2 man/info pages
- Mandrake adaptions
- update to 1.12.64010 to get the -y (--bzip2) option

* Mon Mar 08 1999 Michael Maher <mike@redhat.com>
- added patch for bad name cache.
- FIXES BUG 320

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- add /usr/bin/gtar symlink (change #421)

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- Fiddle bindir/libexecdir to get RH install correct.
- Don't include /sbin/rmt -- use the rmt from dump.
- Turn on nls.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.11.8 to 1.12
- various spec file cleanups
- /sbin/install-info support

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu May 29 1997 Michael Fulbright <msf@redhat.com>
- Fixed to include rmt
