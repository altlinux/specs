%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %_bindir/cpancover
%add_findreq_skiplist %perl_vendor_archlib/Devel/Cover/Collection.pm
%define dist Devel-Cover
Name: perl-%dist
Version: 1.29
Release: alt1.1

Summary: Code coverage metrics for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PJ/PJCJ/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Wed Oct 12 2011 (-bi)
BuildRequires: perl-B-Debug perl-JSON-PP perl-PPI-HTML perl-Parallel-Iterator perl-Perl-Tidy perl-Pod-Coverage perl-Template perl-Test-Differences perl-Test-Warn rpm-build-ruby perl(Sereal/Decoder.pm) perl(Sereal/Encoder.pm) perl(JSON/MaybeXS.pm)

%description
This module provides code coverage metrics for Perl. Code coverage
metrics describe how thoroughly tests exercise code. By using
Devel::Cover you can discover areas of code not exercised by your tests
and determine which tests to create to increase coverage. Code coverage
can be considered as an indirect measure of quality.

%prep
%setup -q -n %{dist}-%{version}

# fix expected output for test suite
#sed -i 's@!/bin/perl@!/usr/bin/perl@' test_output/cover/inc_sub.*

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

# Undefined subroutine &Devel::Cover::set_first_init_and_end called
echo 'sub Devel::Cover::set_first_init_and_end{}1' >%buildroot/hack.pm
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot -mhack'

%files
%doc Changes docs README.md
%_bindir/cover
%_bindir/cpancover
%_bindir/gcov2perl
%_man1dir/*
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel
%exclude /hack.pm

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1.1
- rebuild with new perl 5.24.1

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Mon Mar 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1
- 1.06 -> 1.08

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.93-alt1
- 0.79 -> 0.93
- built for perl-5.16

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- 0.72 -> 0.79
- built for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.67-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- automated CPAN update

* Tue Jan 19 2010 Vitaly Lipatov <lav@altlinux.ru> 0.65-alt1
- initial build for ALT Linux Sisyphus
