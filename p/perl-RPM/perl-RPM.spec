%define dist Perl-RPM
Name: perl-RPM
Version: 1.51
Release: alt5.1

Summary: Native bindings to the RPM Package Manager API
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version-%release.tar

# google "assert.h breaks perl.h"
BuildConflicts: perl-devel = 1:5.8.1

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: librpm-devel perl-Devel-Leak perl-devel

%description
The Perl-RPM package is an attempt to provide Perl-level access to the
complete application programming interface that is a part of the RPM
Package Manager (RPM). Rather than have scripts rely on executing RPM
commands and parse the resultant output, this modules aims to provide
Perl programmers the ability to do anything that would otherwise have
been done in C or C++.

%prep
%setup -q -n %dist-%version-%release

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%_bindir/rpmprune
%perl_vendor_archlib/RPM*
%perl_vendor_autolib/RPM*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt5.1
- rebuild with new perl 5.26.1

* Sat Apr 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt5
- no error when opening RPM header with MISSING KEYS

* Fri Mar 24 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt4
- rpm413 full support (including db)

* Thu Mar 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt3
- rpm413 base support (constants and headers)

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2.1
- rebuild with new perl 5.24.1

* Fri Jan 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt2
- fixed build to not hinder perl upgrade

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1.1
- rebuild with new perl 5.20.1

* Fri Dec 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- updated from cpan
- c code cleanup in preparation for perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.49-alt3
- built for perl 5.18

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.49-alt2
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.49-alt1.3
- rebuilt for perl-5.14

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1.2
- added perl-RPM-1.49-fix-warning-use-once.patch

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.49-alt1.1
- rebuilt with perl 5.12

* Sun Apr 22 2007 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- major revision, see ChangeLog for details
- released on CPAN as Perl-RPM-1.49_01

* Sat Mar 18 2006 Alexey Tourbin <at@altlinux.ru> 0.40.0-alt9
- implemented RPM::evrcmp($$) to facilitate [Epoch:]Version[-Release]
  comparison; fixed a number of bugs in RPM/Header.xs that made it
  possible; TODO: fix memory leaks in rpmhdr_STORE()
- fixed rpmdb_init() and rpmdb_rebuild()
- fixed License tag (Artistic, not GPL)

* Thu Jan 19 2006 Dmitry V. Levin <ldv@altlinux.org> 0.40.0-alt8
- Fixed tests for x86_64.

* Wed Sep 07 2005 Alexey Tourbin <at@altlinux.ru> 0.40.0-alt7
- fixed SEGV in rpmhdr_FETCH (cpan #14489)

* Sat Apr 02 2005 Alexey Tourbin <at@altlinux.ru> 0.40.0-alt6
- fixed some memory leaks (cpan #12120)

* Sat Mar 12 2005 Alexey Tourbin <at@altlinux.ru> 0.40.0-alt5
- dropped unnecessary linking with libpopt
- applied Mandrake 64-bit fixes
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.40.0-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jun 11 2004 Alexey Tourbin <at@altlinux.ru> 0.40.0-alt4
- dropped altrpm.patch as it was perl-5.8.1 fault
- revamped specfile

* Wed Oct  1 2003 Grigory Milev <week@altlinux.ru> 0.40.0-alt3
- patching for build with new perl

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.40.0-alt2
- rebuild with new perl

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 0.40.0-alt1
- new version released
- minor spec cleanup

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.32.0-alt8
- Rebuilt with new rpm

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.32.0-alt7
- Fixed linkage.

* Thu Nov 08 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.32.0-alt6
- Initial build with rpm4.

* Thu Oct 25 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.32.0-alt5
- Specfile cleanup.

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 0.32.0-alt4
- Rebuilt with new perl again.

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.32-alt3
- Rebuilt with perl-5.6.1
- Some spec cleanup
- Fixed version bug

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 0.32-alt2
- Rewrite spec for compatible with new police

* Tue May 15 2001 Grigory Milev <week@altlinux.ru> 0.32.0-alt1
- new version (0.32)

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Nov 16 2000 Pixel <pixel@mandrakesoft.com> 0.29.2-1mdk
- new version

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.29.1-2mdk
- rpmv4 aware.

* Sat Oct 14 2000 Pixel <pixel@mandrakesoft.com> 0.29.1-1mdk
- new version (0.291 that is)

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 0.28-2mdk
- use %%perl_sitearch

* Sun Aug 20 2000 Pixel <pixel@mandrakesoft.com> 0.28-1mdk
- new version

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 0.27-2mdk
- rebuild with new clean_perl in spec-helper

* Tue Aug  8 2000 Pixel <pixel@mandrakesoft.com> 0.27-1mdk
- new version

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.26-2mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Pixel <pixel@mandrakesoft.com> 0.26-1mdk
- new version, BM

* Sun Jul  9 2000 Pixel <pixel@mandrakesoft.com> 0.25-1mdk
- new version

* Tue Jul  4 2000 Pixel <pixel@mandrakesoft.com> 0.2-2mdk
- and RPM.pm to %files (chmousux)

* Fri Jun 09 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2-1mdk
- First Mandrake version.
