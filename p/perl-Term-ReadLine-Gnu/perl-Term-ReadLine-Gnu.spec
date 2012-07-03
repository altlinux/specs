%define dist Term-ReadLine-Gnu
Name: perl-%dist
Version: 1.20
Release: alt1.2

Summary: Perl interface to the GNU Readline library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libncurses-devel libreadline-devel perl-devel

%description
Term::ReadLine::Gnu is an implementation of the interface to the GNU
Readline library.  This module gives you input line editing facility,
input history management facility, word completion facility, etc.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build
#PERL_RL_TEST_TK=1 perl -Mblib t/callback.t

%install
%perl_vendor_install

%files
%doc README eg
%perl_vendor_archlib/Term
%perl_vendor_autolib/Term

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt1.2
- rebuilt for perl-5.14

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.20-alt1.1
- rebuilt for perl-5.12

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.19 -> 1.20

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 1.19-alt1
- 1.17a -> 1.19

* Wed Feb 20 2008 Alexey Tourbin <at@altlinux.ru> 1.17a-alt1
- 1.16 -> 1.17a

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 1.16-alt2
- changed src.rpm packaging to keep upstream tarball unchanged

* Wed Oct 25 2006 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.15 -> 1.16
- imported sources into git and built with gear
- made quite a few minor changes, including the following:
  + Gnu.pm: use XSLoader
  + Gnu/XS.pm: remove AutoLoader
  + Gnu/XS.pm: pass syntax check
  + Gnu.XS: include <curses.h> and <term.h> for tputs() and tgetstr();
    Makefile.PL: link with -ltinfo
- applied patches from debian's libterm-readline-gnu-perl_1.16-2.diff.gz,
  including a fix for SEGV in the perl debugger

* Sat Dec 31 2005 Dmitry V. Levin <ldv@altlinux.org> 1.15-alt2
- Fixed build with new readline (aka avoid private symbols).

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.15-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Oct 24 2004 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.14 -> 1.15
- rewrote Makefile.PL and build section
- revised patches

* Fri Jul 04 2003 Alexey Tourbin <at@altlinux.ru> 1.14-alt3
- findConsole.patch: fixed /dev/tty stuff a bit

* Fri Jun 13 2003 Alexey Tourbin <at@altlinux.ru> 1.14-alt2
- package renamed: s/Readline/ReadLine/
- fixed tinfo build
- Term/ReadLine.pm moved here from perl bundle (5.8.1)
- no-static.patch: don't look for .a libraries
- syntax.patch: make Gnu/XS.pm pass syntax check

* Tue Mar 25 2003 Grigory Milev <week@altlinux.ru> 1.14-alt1
- new version released

* Tue Dec  3 2002 Grigory Milev <week@altlinux.ru> 1.13-alt2
- rebuild with tinfo

* Fri Nov 15 2002 Grigory Milev <week@altlinux.ru> 1.13-alt1
- rebuild with new perl
- new version released

* Wed Apr 10 2002 Grigory Milev <week@altlinux.ru> 1.12-alt1
- new version released

* Thu Jan 24 2002 Grigory Milev <week@altlinux.ru> 1.11-alt1
- new version released

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 1.10-alt1
- New version released.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.09-ipl7mdk
- Specfile minor cleanup (corrected arch subdirs).
- Corrected summary.

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.09-ipl6mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Fri Jun 19 2001 Grigory Milev <week@altlinux.ru> 1.09-ipl5mdk
- Spec rewritten for compatibility with new policy.

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation
- path patch

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.09-3mdk
- build release.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 1.09-2mdk
- macroszifications.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 1.09-1mdk
- 1.09.
- removed patch for compilation with perl 5.6.0.

* Mon Apr 04 2000 François Pons <fpons@mandrakesoft.com> 1.08-2mdk
- added patch for compilation with perl 5.6.0.
- updated spec file and Group.

* Tue Jan  4 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First package needed for perl-debug.

