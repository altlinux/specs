%define dist Math-BigRat
Name: perl-%dist
Version: 0.2602
Release: alt1

Summary: Arbitrarily big rational numbers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Math-BigInt perl-Test-Pod perl-Test-Pod-Coverage

%description
Math::BigRat complements Math::BigInt and Math::BigFloat
by providing support for arbitrarily big rational numbers.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS CHANGES README TODO
%perl_vendor_privlib/Math

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.2602-alt1
- 0.26 -> 0.2602

* Sun Aug 07 2011 Alexey Tourbin <at@altlinux.ru> 0.26-alt2
- t/bigratpm.inc: update test data from 0.2602

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.26-alt1
- 0.24 -> 0.26

* Fri Sep 11 2009 Alexey Tourbin <at@altlinux.ru> 0.24-alt1
- 0.22 -> 0.24

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.20 -> 0.22

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.19 -> 0.20

* Fri Jun 08 2007 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.18 -> 0.19

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 0.17 -> 0.18

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- 0.15 -> 0.17

* Tue Apr 12 2005 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- 0.14 -> 0.15

* Thu Jan 06 2005 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- initial revision (split off from perl-base)
