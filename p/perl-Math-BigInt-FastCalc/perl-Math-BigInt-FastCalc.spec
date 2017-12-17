%define _unpackaged_files_terminate_build 1
%def_with bootstrap
%define dist Math-BigInt-FastCalc
Name: perl-%dist
Version: 0.5006
Release: alt1.1.1.1

Summary: XS implementation of arbitrary size integer math
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PJ/PJACKLAM/%{dist}-%{version}.tar.gz

BuildRequires: perl-devel

%if_with bootstrap
%define _without_test 1
%add_findreq_skiplist %perl_vendor_archlib/Math/BigInt*
%else
BuildRequires: perl-Math-BigInt
%endif


%description
This is a replacement library for Math::BigInt::Calc that reimplements
some of the Calc functions in XS.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES CREDITS README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.5006-alt1.1.1.1
- rebuild with new perl 5.26.1

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.5006-alt1.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.5006-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.5006-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.5005-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.5002-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.5000-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1.1
- dropped Pod/Pod-Coverage tests (closes: #31760)

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1.2
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Sat Dec 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2.2
- unbootstrap

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2.1
- rebuild with new perl 5.20.1

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- support for bootstrap

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 0.30-alt5
- built for perl 5.18

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 0.30-alt4
- rebuilt for perl-5.16

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.30-alt3
- disabled build dependency on perl-Module-Install

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.30-alt2
- rebuilt for perl-5.14

* Sat Sep 17 2011 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.29 -> 0.30

* Fri Aug 05 2011 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- 0.24 -> 0.29

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.24-alt1
- 0.22 -> 0.24

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.19 -> 0.22
- built for perl-5.12

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.15 -> 0.19

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.15-alt2
- fixed integer overflow in FastCalc.xs:_new() "shortcut for
  integer argument" check (rt.cpan.org #29720)

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- 0.14 -> 0.15

* Fri Jun 08 2007 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.12 -> 0.13

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision (detached from perl-Math-BigInt)
