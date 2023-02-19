Name: dos2unix
Version: 7.4.4
Release: alt1

Summary: Text file format converter
License: BSD
Group: Text tools

Url: http://waterlan.home.xs4all.nl/dos2unix.html
Source: http://waterlan.home.xs4all.nl/dos2unix/%name-%version.tar.gz
Source100: %name.watch

Obsoletes: unix2dos
Provides: unix2dos = %version-%release

# Automatically added by buildreq on Mon Feb 15 2016
# optimized out: perl-Encode perl-Locale-gettext perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Pod-Usage perl-parent perl-podlators
BuildRequires: perl-Pod-Checker po4a gettext gcc perl-Padre

%description
%name - DOS/Mac to Unix and vice versa text file format converter.

%prep
%setup
# podchecker reports Non-ASCII characters
rm -rf man/{es,nl}

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE $(getconf LFS_CFLAGS)"

%install
%makeinstall_std

%find_lang --with-man --output=%name.lang %name mac2unix unix2dos unix2mac

%files -f %name.lang
%_bindir/%name
%_bindir/mac2unix
%_bindir/unix2dos
%_bindir/unix2mac
%_man1dir/*
%doc *.txt

%changelog
* Sun Feb 19 2023 Ilya Mashkin <oddity@altlinux.ru> 7.4.4-alt1
- 7.4.4

* Mon Jun 06 2022 Ilya Mashkin <oddity@altlinux.ru> 7.4.3-alt1
- 7.4.3

* Sat Jun 12 2021 Ilya Mashkin <oddity@altlinux.ru> 7.4.2-alt1
- 7.4.2
- Update License to BSD

* Mon Jul 10 2017 Michael Shigorin <mike@altlinux.org> 7.3.5-alt1
- new version (watch file uupdate)

* Wed May 25 2016 Michael Shigorin <mike@altlinux.org> 7.3.4-alt1
- new version (watch file uupdate)

* Sun Feb 14 2016 Michael Shigorin <mike@altlinux.org> 7.3.3-alt1
- new version (watch file uupdate)
- buildreq

* Mon Nov 23 2015 Michael Shigorin <mike@altlinux.org> 7.3.2-alt1
- new version (watch file uupdate)

* Thu Oct 01 2015 Michael Shigorin <mike@altlinux.org> 7.3.1-alt1
- new version (watch file uupdate)

* Mon Aug 24 2015 Michael Shigorin <mike@altlinux.org> 7.3-alt1
- new version (watch file uupdate)

* Thu Jul 02 2015 Michael Shigorin <mike@altlinux.org> 7.2.3-alt1
- new version (watch file uupdate)

* Sat May 23 2015 Michael Shigorin <mike@altlinux.org> 7.2.2-alt1
- added watch file
- new version (watch file uupdate)

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 6.0.5-alt1
- 6.0.5

* Tue Dec 31 2013 Yuri N. Sedunov <aris@altlinux.org> 6.0.4-alt1
- 6.0.4

* Sat Dec 14 2013 Yuri N. Sedunov <aris@altlinux.org> 6.0.3-alt1
- 6.0.3
- removed obsolete patches

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr 27 2007 Serhii Hlodin <hlodin@altlinux.ru> 3.1-alt1
- Initial build

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1-27.1
- rebuild

* Mon Jul 10 2006 Tim Waugh <twaugh@redhat.com> 3.1-27
- Re-encoded spec file in UTF-8 (bug #197817).

* Mon Jun  5 2006 Tim Waugh <twaugh@redhat.com> 3.1-26
- Rebuilt.

* Thu Jun  1 2006 Tim Waugh <twaugh@redhat.com> 3.1-25
- Build with large file support.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.1-24.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.1-24.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Apr 13 2005 Tim Waugh <twaugh@redhat.com> 3.1-24
- Fixed tmppath patch (bug #150277).

* Thu Mar  3 2005 Mike A. Harris <mharris@redhat.com> 3.1-23
- Bump and rebuild for FC4, using gcc 4.

* Tue Feb  8 2005 Mike A. Harris <mharris@redhat.com> 3.1-22
- Bump and rebuild for FC4

* Wed Oct 20 2004 Miloslav Trmac <mitr@redhat.com> - 3.1-21
- Don't just delete the original file when destination and current directory
  are on different filesystems (#65548, #123069, patch by James Antill)
- Fix return type of StripDelimiter in dos2unix-3.1-safeconv.patch (#136148)

* Wed Oct  6 2004 Mike A. Harris <mharris@redhat.com> 3.1-20
- Added dos2unix-3.1-manpage-update-57507.patch to fix manpage (#57507)
- Added dos2unix-3.1-preserve-file-modes.patch to properly preserve file
  permissions (#91331,55183,112710,132145)

* Sun Sep 26 2004 Rik van Riel <riel@redhat.com> 3.1-19
- safer conversion w/ mac2unix (fix from bz #57508)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 05 2003 Elliot Lee <sopwith@redhat.com> 3.1-15
- Remove build dependency on perl, since perl BuildRequires: dos2unix,
  and there's no good reason not to just use sed here.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 3.1-13
- All-arch rebuild
- Added BuildRequires: perl

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.1-10
- Build in new environment

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix bug #57700 (segfault)
- Add the mac2unix symlink recommended in README
- Fix compiler warnings

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jan 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- shut up rpmlint

* Fri Nov 17 2000 Tim Powers <timp@redhat.com>
- use mkstemp instead of mktemp. Not much needed to change.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- cleaned up specfile a bit
- built for 7.1

* Tue Jul 07 1999 Peter Soos <sp@osb.hu> 
- Added Hungarian "Summary:" and "%description" 
- Corrected the file and directory attributes to rebuild the package 
  under RedHat Linux 6.0
