%define dist Math-BigInt
Name: perl-%dist
Version: 1.997
Release: alt3

Summary: Arbitrary size integer math package
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Math-BigInt-1.997-alt-FastCalc.patch

# enable XS routines for more speed
Requires: perl-Math-BigInt-FastCalc

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Math-BigInt-FastCalc perl-Test-Pod perl-Test-Pod-Coverage

%description
This package contains the following perl modules:
Math::BigInt - Arbitrary size integer math package
Math::BigFloat - Arbitrary size floating point math package

%prep
%setup -q -n %dist-%version
%patch -p1
chmod -x -c CHANGES HISTORY

# do not check for older versions
sed -i- 's/eval " require/eval " die/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS CHANGES CREDITS HISTORY README
%perl_vendor_privlib/Math

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.997-alt3
- re-enabled dependency on perl-Math-BigInt-FastCalc
- disabled build dependency on perl-Module-Install

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.997-alt2
- bootstrap for perl-5.14
- rebuilt as plain src.rpm

* Sat Sep 17 2011 Alexey Tourbin <at@altlinux.ru> 1.997-alt1
- 1.992 -> 1.997
- changed default backend back to Math::BigInt::FastCalc

* Fri Aug 05 2011 Alexey Tourbin <at@altlinux.ru> 1.992-alt1
- 1.99 -> 1.992

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.99-alt1
- 1.95 -> 1.99
- re-enabled dependency on perl-Math-BigInt-FastCalc

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.95-alt1
- 1.89 -> 1.95
- built with perl-5.12
- disabled dependency on perl-Math-BigInt-FastCalc, for bootstrap

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.89-alt1
- 1.87 -> 1.89

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 1.87-alt1
- 1.86 -> 1.87

* Fri Jun 08 2007 Alexey Tourbin <at@altlinux.ru> 1.86-alt1
- 1.82 -> 1.86

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 1.82-alt1
- 1.81 -> 1.82

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 1.81-alt1
- 1.77 -> 1.81
- %name-Fastcalc packaged separately

* Fri May 20 2005 Alexey Tourbin <at@altlinux.ru> 1.77-alt1
- 1.76 -> 1.77

* Tue Apr 12 2005 Alexey Tourbin <at@altlinux.ru> 1.76-alt1
- 1.75 -> 1.76
- packaged %dist-FastCalc-0.10 here

* Sun Mar 20 2005 Alexey Tourbin <at@altlinux.ru> 1.75-alt1
- 1.74 -> 1.75

* Thu Jan 06 2005 Alexey Tourbin <at@altlinux.ru> 1.74-alt1
- 1.73 -> 1.74

* Thu Dec 09 2004 Alexey Tourbin <at@altlinux.ru> 1.73-alt1
- initial revision (split off from perl-base)
