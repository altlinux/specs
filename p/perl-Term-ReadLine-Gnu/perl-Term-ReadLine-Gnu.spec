%define dist Term-ReadLine-Gnu
Name: perl-%dist
Version: 1.35
Release: alt1

Summary: Perl interface to the GNU Readline library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: %dist-%version.tar
Source1: Term-ReadLine.tar
Source2: Makefile.PL

Patch1: perl-Term-ReadLine-Gnu-at-Gnu.pm-use-XSLoader.patch
# two merged in one Patch3 file
# hist/perl-Term-ReadLine-Gnu-at-Gnu.xs-use-curses.patch
# hist/perl-Term-ReadLine-Gnu-at-dont-use-xmalloc.patch
Patch3: perl-Term-ReadLine-Gnu-1.35-at-xmalloc-at-curses.patch
Patch6: perl-Term-ReadLine-Gnu-at-Gnu_XS.pm-pass-syntax-check.patch
Patch7: perl-Term-ReadLine-Gnu-at-Gnu_XS.pm-debian-10term.patch
Patch8: perl-Term-ReadLine-Gnu-at-add-Term-Readline-to-MANIFEST.patch
Patch9: perl-Term-ReadLine-Gnu-at-perlsh-dont-import-POSIX.patch
Patch10: perl-Term-ReadLine-Gnu-at-disable-Tk-test.patch
Patch11: Term-ReadLine-1.15-at.patch


# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libncurses-devel libreadline-devel perl-devel perl-Encode

%description
Term::ReadLine::Gnu is an implementation of the interface to the GNU
Readline library.  This module gives you input line editing facility,
input history management facility, word completion facility, etc.

%prep
%setup -q -n %dist-%version -a1
mv Makefile.PL Makefile.PL.orig
cp -f %{SOURCE2} Makefile.PL

%patch1 -p1
%patch3 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p0

%build
%perl_vendor_build
#PERL_RL_TEST_TK=1 perl -Mblib t/callback.t

%install
%perl_vendor_install

%files
%doc README eg Changes
%perl_vendor_archlib/Term
%perl_vendor_autolib/Term

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1.1
- rebuild with new perl 5.24.1

* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Tue Mar 01 2016 Vladimir Lettiev <crux@altlinux.ru> 1.30-alt1
- 1.30

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- new version 1.25

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- new version 1.24

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.22-alt2
- updated Term-ReadLine to 1.15 from perl 5.22
- switched to patches (commits still are in history)

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- new version 1.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt3
- built for perl 5.18

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.16

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

