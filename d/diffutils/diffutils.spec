Name: diffutils
Version: 3.2
Release: alt1

Summary: A GNU collection of diff utilities
License: GPLv3+
Group: File tools
Url: http://www.gnu.org/software/diffutils/
# http://git.altlinux.org/people/ldv/packages/?p=gnulib.git refs/heads/diffutils
# git://git.sv.gnu.org/diffutils refs/heads/master
Source0: diffutils-%version-%release.tar
# git://git.sv.gnu.org/gnulib refs/heads/master
Source1: gnulib-%version-%release.tar
# translationproject.org::tp/latest/%name/
Source2: po-%version-%release.tar

Conflicts: man-pages <= 1.52-alt1

BuildRequires: gperf help2man

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff:
+ The diff command compares two files and shows the differences,
  line by line.
+ The cmp command compares two files, and if they differ, tells the
  first byte and line number where they differ or reports that one file
  is a prefix of the other.
+ The diff3 command compares three files and outputs descriptions of
  their differences.
+ The sdiff command merges two files and interactively outputs the
  results.

%prep
%setup -n %name-%version-%release -a1 -a2
echo -n %version > .tarball-version
# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap.conf
# Generate LINGUAS file.
ls po/*.po | sed 's|.*/||; s|\.po$||' > po/LINGUAS

%build
./bootstrap --skip-po --gnulib-srcdir=gnulib-%version-%release
# Predefine location of the pr utility.
export PR_PROGRAM=%_bindir/pr
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_infodir/*.info*
%_mandir/man?/*
%doc AUTHORS NEWS README THANKS

%changelog
* Sun Sep 04 2011 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt1
- Updated to v3.2.

* Tue Aug 16 2011 Dmitry V. Levin <ldv@altlinux.org> 3.1-alt1
- Updated to v3.1-7-g320355d.

* Tue May 18 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt1
- Updated to 3.0.

* Fri Feb 12 2010 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt1
- Updated to 2.9.
- Dropped "diff -k" patch.

* Tue Jun 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2.8.7-alt4
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.8.7-alt3
- Uncompressed tarball, reduced macro abuse in specfile,
  updated package description.

* Thu Jun 23 2005 Dmitry V. Levin <ldv@altlinux.org> 2.8.7-alt2
- Updated Russian translation.

* Tue May 17 2005 Dmitry V. Levin <ldv@altlinux.org> 2.8.7-alt1
- Updated to 2.8.7.
- Updated patches.

* Wed Feb 09 2005 Dmitry V. Levin <ldv@altlinux.org> 2.8.4-alt4
- Updated package dependencies.

* Tue Feb 08 2005 Kachalov Anton <mouse@altlinux.ru> 2.8.4-alt3.1
- fix bad C expression

* Wed Jul 14 2004 Stanislav Ievlev <inger@altlinux.org> 2.8.4-alt3
- fix buildreqs

* Wed Jul 07 2004 Stanislav Ievlev <inger@altlinux.org> 2.8.4-alt2
- fixed typo in russian translation

* Mon May 19 2003 Stanislav Ievlev <inger@altlinux.ru> 2.8.4-alt1
- 2.8.4

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.1-alt3
- fix typo in the URL.
- rebuild with gcc3.

* Wed Aug 07 2002 Stanislav Ievlev <inger@altlinux.ru> 2.8.1-alt2
- package now has it's own manpages, it's better then manual from 
  RH/MDK and man-pages

* Mon Jun 03 2002 Dmitry V. Levin <ldv@altlinux.org> 2.8.1-alt1
- 2.8.1 (a lot of changes since 2.7), updated patches.
- Don't print nanoseconds in timestamps
  (reverted to previous behaviour).

* Wed Mar 13 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7-ipl23mdk
- Rebuilt.

* Sun Jan 14 2001 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl22mdk
- Create tmpfiles in more secure way.

* Tue Nov 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl21mdk
- Added -k option to get a default suffix
  (from Peter Samuelson <peter@cadcamlab.org>).
- Fixed texinfo documentation.

* Thu Jul 27 2000 Dmitry V. Levin <ldv@fandra.org> 2.7-ipl20mdk
- Moved manpages to it's package.
- RE adaptions.

* Wed Jul 26 2000 David BAUDENS <baudens@mandrakesoft.com> 2.7-20mdk
- Human readable description

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.7-19mdk
- BM
- major spec simplification

* Thu Apr 4 2000 Denis Havlik <denis@mandrakesoft.com> 2.7-18mdk
- new group: Development/Other
- spechelper conform

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add defattr.

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- listing man-pages in %files.

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Sun Mar 14 1999 Jeff Johnson <jbj@redhat.com>
- add man pages (#831).
- add %configure and Prefix.

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Jul 14 1998 Bill Kawakami <billk@home.com>
- included the four man pages stolen from Slackware

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun May 03 1998 Cristian Gafton <gafton@redhat.com>
- fixed spec file to reference/use the $RPM_BUILD_ROOT always

* Wed Dec 31 1997 Otto Hammersmith <otto@redhat.com>
- fixed where it looks for 'pr' (/usr/bin, rather than /bin)

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
