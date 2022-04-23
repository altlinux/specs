# vim: set ft=spec: -*- rpm-spec -*-

Name: ctags
Version: 5.8
Release: alt5

Summary: A C programming language indexing and/or cross-reference tool
License: GPLv2+
Group: Development/Other
Url: http://ctags.sourceforge.net/

# http://download.sourceforge.net/ctags/ctags-%version.tar.gz
Source: ctags-%version.tar

# SUSE patches
Patch1: 0001-Mixing-with-anjuta-tags-https-git.gnome.org-browse-a.patch
Patch2: 0002-Making-inline-behave-like-an-attribute.-Fixes-1.patch
Patch3: 0003-Treat-typename-as-an-attribute.patch
Patch4: 0004-parseReturnType-should-start-from-the-first-non-brac.patch
Patch5: 0005-Ensuring-a-space-is-printed-in-return-type-AFTER-the.patch
Patch6: 0006-Prevent-C-static_assert-from-stopping-parsing.patch
Patch7: 0007-c-Handle-C-11-noexcept.patch
Patch8: 0008-c-Properly-parse-C-11-override-and-final-members.patch
Patch9: 0009-Parse-C-11-enums-with-type-specifier.patch
Patch10: 0010-Parse-C-11-classed-enums.patch
Patch11: 0011-Handle-template-expressions-that-may-use-the-or-oper.patch
Patch12: 0012-Make-sure-we-don-t-throw-things-away-while-collectin.patch
Patch13: 0013-C-mitigate-matching-error-on-generics-containing-an-.patch
Patch14: 0014-fix-wrongly-interpreted-in-template.patch
Patch15: 0015-Added-constexpr-as-keyword.patch
# Covered by ctags-5.8-r791-cve-2014-7204-fix.patch
# Patch16: 0016-CVE-2014-7204.patch
Patch17: 0017-Go-language-support.patch
# SUSE specific
# Patch18: 0018-SUSE-man-page-changes.patch
# Covered by SOURCE_DATE_EPOCH
# Patch19: 0019-Do-not-include-build-time-in-binary.patch
Patch20: ctags-gcc11.patch

# ALT patches
Patch101: ctags-5.8-alt-warnings.patch
Patch102: ctags-5.8-alt-buildroot.patch
Patch103: ctags-5.8-rh-segfault-fix.patch
Patch104: ctags-5.8-r791-cve-2014-7204-fix.patch
Patch105: ctags-5.8-alt-man.patch

%description
The ctags program generate an index (or "tag") file for C, C++, Eiffel,
Fortran, and Java language objects found in files.  This tag file allows
these items to be quickly and easily located by a text editor or other
utility.  A "tag" signifies a language object for which an index entry is
available (or, alternatively, the index entry created for that object).

Alternatively, ctags can generate a cross reference file which lists, in
human readable form, information about the various source objects found
in a set of language files.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure --disable-etags
%make_build

%install
%makeinstall

%files
%_bindir/*
%_mandir/man?/*
%doc EXTENDING.html FAQ NEWS README

%changelog
* Sat Apr 23 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.8-alt5
- Synced with SUSE devel:tools/ctags r36:
  + Included bugfixes and improvements;
  + Added returntype field to tag file format (disabled by default);
  + Added support for Go language.
- Rediffed and updated patches.
- Added patches for man page.

* Thu Apr 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.8-alt4
- Security release (fixed CVE-2014-7204).

* Mon Dec 06 2021 Igor Vlasenko <viy@altlinux.org> 5.8-alt3
- NMU: fixed build

* Wed Feb 02 2011 Dmitry V. Levin <ldv@altlinux.org> 5.8-alt2
- Import a fix for potential segfault from FC.

* Sun Feb 28 2010 Alexey I. Froloff <raorn@altlinux.org> 5.8-alt1
- Updated to 5.8.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 5.6-alt1
- Updated to 5.6.

* Thu Sep 22 2005 Sir Raorn <raorn@altlinux.ru> 5.5.4-alt1.1
- NMU
- Url changed from prdownloads.sf.net to download.sf.net
- Patch from Bram Moolenaar <Bram@moolenaar.net> that adds typename
  information for variables (closes: #7940)
- Patch for stripping file prefix in tags file (closes: #7954)

* Thu Apr 15 2004 Dmitry V. Levin <ldv@altlinux.org> 5.5.4-alt1
- Updated to 5.5.4

* Wed Apr 09 2003 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt1
- Updated to 5.5

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt1
- Updated to 5.4

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3.1-alt1
- Updated to 5.3.1

* Fri Mar 29 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.2.3-alt1
- 5.2.3

* Fri Feb 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.2.2-alt1
- 5.2.2

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.2-alt1
- 5.2

* Wed Nov 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 5.1-alt1
- 5.1

* Tue Jun 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.0.1-alt2
- Rebuilt.

* Tue Apr 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Tue Mar 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.0-ipl1mdk
- 5.0

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 4.0.3-ipl2mdk
- Updated Url.
- Removed etags* links.

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 4.0.3-ipl1mdk
- 4.0.3

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 4.0.2-ipl1
- 4.0.2

* Fri Jun 30 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.2-ipl1
- RE and Fandra adaptions.

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Mon May  8 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Update to 3.5.2
- minor cleanups to spec file

* Tue Feb 16 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Update to 3.4 to fix bug #9446

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- compress man page.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)
- version 3.2

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.0.3

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed etags.  Emacs provides its own; and needs to support
  more than just C.

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 1.5 to 1.6

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

