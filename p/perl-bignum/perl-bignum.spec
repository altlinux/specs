%define dist bignum
Name: perl-%dist
Version: 0.29
Release: alt1

Summary: Transparent BigNumber support for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Math-BigRat perl-Test-Pod

%description
This package attempts to make it easier to write perl scripts that
use big numbers.  Math::BigInt, Math::BigFloat, and Math::BigRat
modules are used in a transparent way.

bigint - Transparent BigInteger support
bignum - Transparent BigNumber support
bigrat - Transparent BigNumber/BigRational support

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS CHANGES README
%perl_vendor_privlib/Math
%perl_vendor_privlib/big*

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- 0.28 -> 0.29

* Fri Aug 05 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.25 -> 0.28

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.23 -> 0.25

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.23-alt1
- 0.22 -> 0.23

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.21 -> 0.22

* Fri Jun 08 2007 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.20 -> 0.21

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.19 -> 0.20

* Wed Apr 04 2007 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.17 -> 0.19

* Tue Apr 12 2005 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- 0.16 -> 0.17

* Thu Jan 06 2005 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- 0.15 -> 0.16

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision (split from perl-base)
