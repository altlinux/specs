%define dist Math-BigInt-FastCalc
Name: perl-%dist
Version: 0.30
Release: alt3

Summary: XS implementation of arbitrary size integer math
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Math-BigInt perl-Test-Pod perl-Test-Pod-Coverage

%description
This is a replacement library for Math::BigInt::Calc that reimplements
some of the Calc functions in XS.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES CREDITS README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
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
