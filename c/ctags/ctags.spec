# vim: set ft=spec: -*- rpm-spec -*-

Name: ctags
Version: 5.8
Release: alt2

Summary: A C programming language indexing and/or cross-reference tool
License: GPLv2+
Group: Development/Other
Url: http://ctags.sourceforge.net/

# http://download.sourceforge.net/ctags/ctags-%version.tar.gz
Source: ctags-%version.tar
Patch1: ctags-5.8-alt-warnings.patch
Patch2: ctags-5.8-alt-buildroot.patch
Patch3: ctags-5.8-rh-segfault-fix.patch

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
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

