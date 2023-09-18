Name: tar
Version: 1.35.0.20.1cdad4cc
Release: alt1

Summary: A GNU file archiving program
License: GPLv3+
Group: Archiving/Backup
Url: https://www.gnu.org/software/tar/

%define srcname %name-%version-%release
# git://git.altlinux.org/gears/t/tar.git
Source: %srcname.tar

%def_enable selinux
BuildRequires: libacl-devel libattr-devel makeinfo
%{?_enable_selinux:BuildRequires: libselinux-devel}
BuildRequires: gnulib >= 0.1.6321.a97e2
BuildRequires: paxutils >= 0.0.1.150.6fba

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: /dev/pts}}

%description
The GNU tar program saves many files together into one archive and
can restore individual files (or all of the files) from the archive.
tar can also be used to add supplemental files to an archive and to
update or list files in the archive.  tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives and the ability to perform incremental and full backups.

%prep
%setup -n %srcname

# Build scripts expect to find package version in this file.
echo -n %version-%release > .tarball-version

# Generate LINGUAS file.
ls po | sed -n 's/^\([^.]\+\)\.po$/\1/p' > po/LINGUAS

rmdir paxutils
ln -s %_datadir/paxutils .

%build
./bootstrap \
	--force \
	--no-git \
	--skip-po \
	--gnulib-srcdir=%_datadir/gnulib \
	#

export tar_cv_path_RSH=no
%configure --bindir=/bin --with-rmt=/sbin/rmt --disable-silent-rules
%make_build -C po update-po
%make_build AM_MAKEINFOFLAGS=--no-split

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall_std bindir=/bin
ln -s ../../bin/tar %buildroot%_bindir/gtar
install -pm644 doc/tar.1 %buildroot%_man1dir/
%find_lang %name

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
%make_build -k check

%files -f %name.lang
/bin/tar
%_bindir/gtar
%_mandir/man?/*
%_infodir/tar.info*
%doc AUTHORS NEWS README THANKS TODO

%changelog
* Fri Sep 08 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.35.0.20.1cdad4cc-alt1
- tar: release_1_34-16-g12d67f44 -> v1.35-20-g1cdad4cc.
- gnulib BR: v0.1-5208-gc8b8f3bbcd -> v0.1-6321-ga97e2d66a8.
- paxutils BR: v0.0.1-139-g2f7d215 -> v0.0.1-150-g6fba6e9.
- Updated translations from translationproject.org.

* Tue Jun 01 2021 Dmitry V. Levin <ldv@altlinux.org> 1.34.0.16.12d67f44-alt1
- tar: release_1_34-13-g66b59fcc -> release_1_34-16-g12d67f44.

* Tue Apr 13 2021 Dmitry V. Levin <ldv@altlinux.org> 1.34.0.13.66b59fcc-alt1
- tar: release_1_32 -> release_1_34-13-g66b59fcc.
- gnulib BR: v0.1-2313-g4652c7baf -> v0.1-4460-g783f2967e.
- paxutils BR: v0.0.1-125-g5693984 -> v0.0.1-139-g2f7d215.
- Updated translations from translationproject.org.

* Sat Feb 23 2019 Dmitry V. Levin <ldv@altlinux.org> 1.32-alt1
- release_1_31 -> release_1_32.

* Wed Jan 02 2019 Dmitry V. Levin <ldv@altlinux.org> 1.31-alt1
- tar: release_1_30-38-g3c2a2cd -> release_1_31 (fixes: CVE-2018-20482).
- gnulib: v0.1-2305-g95c96b6dd -> v0.1-2313-g4652c7baf.

* Wed Dec 26 2018 Dmitry V. Levin <ldv@altlinux.org> 1.30.0.38.3c2a-alt1
- tar: release_1_29-19-gd06126f -> release_1_30-38-g3c2a2cd.
- gnulib: v0.1-1209-g24b3216 -> v0.1-2305-g95c96b6dd.
- Updated translations from translationproject.org.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 1.29.0.19.d061-alt1
- tar: release_1_28-39-gd02c81d -> release_1_29-19-gd06126f
  (fixes: CVE-2016-6321).
- tar: added --lz4 and --zstd options.
- gnulib: v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Tue Dec 01 2015 Dmitry V. Levin <ldv@altlinux.org> 1.28.0.39.d02c-alt1
- Updated to release_1_28-39-gd02c81d.

* Thu Sep 24 2015 Dmitry V. Levin <ldv@altlinux.org> 1.28.0.32.cdf41c-alt1
- Updated to release_1_28-32-gcdf41c (closes: #26781).
- Imported some patches by Pavel Raiskup from Fedora tar-1.28-6 package.
- Built with gnulib v0.1-585-g2fda85e.

* Sun Nov 17 2013 Dmitry V. Levin <ldv@altlinux.org> 1.27.1-alt1
- Updated to 1.27.1.

* Tue Oct 22 2013 Dmitry V. Levin <ldv@altlinux.org> 1.27-alt1
- Updated to 1.27.
- Built with gnulib v0.0-8061-g5191b35.

* Tue Jan 15 2013 Dmitry V. Levin <ldv@altlinux.org> 1.26.90-alt1
- Updated to git://git.sv.gnu.org/tar release_1_26-55-gcd7bdd4.
- Enabled xattr, acl and selinux support.

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

* Thu Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.13.5

* Thu Jul 15 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.13.2
- french description

* Mon Jul 12 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
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
