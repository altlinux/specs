%define _unpackaged_files_terminate_build 1
%define dist Math-BigInt-GMP
Name: perl-%dist
Version: 1.6004
Release: alt1.1

Summary: Use the GMP library for Math::BigInt routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PJ/PJACKLAM/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libgmp-devel perl-Math-BigInt perl-Test-Pod perl-threads

%description
Provides support for big integer calculations via means of the GMP c-library.

Math::BigInt::GMP now no longer uses Math::GMP, but provides it's own XS layer
to access the GMP c-library. This cut's out another (perl sub routine) layer
and also reduces the memory footprint by not loading Math::GMP and Carp at
all.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README BUGS CREDITS
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.6004-alt1.1
- rebuild with new perl 5.26.1

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.6004-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.6003-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.6003-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.6002-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.6001-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.6000-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1.1
- rebuild with new perl 5.20.1

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.37-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.37-alt2
- rebuilt for perl-5.16

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.37-alt1.1
- Rebuilt with gmp 5.0.5

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.24 -> 1.37
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.24-alt1.1
- rebuilt with perl 5.12
- fixed test with Math::BigIng >= 1.90

* Mon Nov 23 2009 Mikhail Pokidko <pma@altlinux.org> 1.24-alt1
- Version up. Close: #22358

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 1.22-alt2
- sisyphus_checks fixes

* Wed Jun 06 2007 Mikhail Pokidko <pma@altlinux.org> 1.22-alt1
- first build for ALT Linux Sisyphus

