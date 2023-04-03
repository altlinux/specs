%define _unpackaged_files_terminate_build 1
%define dist Math-BigInt
Name: perl-%dist
Version: 1.999838
Release: alt1

Summary: Arbitrary size integer math package
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PJ/PJACKLAM/%{dist}-%{version}.tar.gz
Patch: perl-Math-BigInt-1.997-alt-FastCalc.patch

# enable XS routines for more speed
Requires: perl-Math-BigInt-FastCalc

BuildArch: noarch

BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-Math-BigInt-FastCalc perl(Math/Complex.pm)

%description
This package contains the following perl modules:
Math::BigInt - Arbitrary size integer math package
Math::BigFloat - Arbitrary size floating point math package

%prep
%setup -q -n %{dist}-%{version}
#patch -p1
chmod -x -c CHANGES HISTORY

# do not check for older versions
sed -i- 's/eval " require/eval " die/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS CHANGES CREDITS HISTORY README examples README.md
%perl_vendor_privlib/Math

%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 1.999838-alt1
- automated CPAN update

* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 1.999837-alt1
- automated CPAN update

* Mon Jun 27 2022 Igor Vlasenko <viy@altlinux.org> 1.999836-alt1
- automated CPAN update

* Wed May 25 2022 Igor Vlasenko <viy@altlinux.org> 1.999835-alt1
- automated CPAN update

* Tue May 24 2022 Igor Vlasenko <viy@altlinux.org> 1.999834-alt1
- automated CPAN update

* Mon May 23 2022 Igor Vlasenko <viy@altlinux.org> 1.999832-alt1
- automated CPAN update

* Fri May 20 2022 Igor Vlasenko <viy@altlinux.org> 1.999831-alt1
- automated CPAN update

* Tue Apr 12 2022 Igor Vlasenko <viy@altlinux.org> 1.999830-alt1
- automated CPAN update

* Sat Jan 01 2022 Igor Vlasenko <viy@altlinux.org> 1.999829-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 1.999828-alt1
- automated CPAN update

* Tue Oct 05 2021 Igor Vlasenko <viy@altlinux.org> 1.999827-alt1
- automated CPAN update

* Fri Sep 24 2021 Igor Vlasenko <viy@altlinux.org> 1.999824-alt1
- automated CPAN update

* Thu Jul 15 2021 Igor Vlasenko <viy@altlinux.org> 1.999823-alt1
- automated CPAN update

* Sun Jul 11 2021 Igor Vlasenko <viy@altlinux.org> 1.999822-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.999818-alt1
- automated CPAN update

* Sun Oct 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.999817-alt1
- automated CPAN update

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.999816-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.999815-alt1
- automated CPAN update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.999813-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.999811-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.999810-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.999809-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.999808-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.999807-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.999806-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.999802-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.999800-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.999726-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.999724-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.999723-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.999722-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.999717-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.999716-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.999715-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.999714-alt1
- automated CPAN update

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.999710-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.999709-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.999707-alt1
- automated CPAN update

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.999706-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.999704-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.9993-alt1
- automated CPAN update

* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 1.997-alt7
- re-enabled dependency on perl-Math-BigInt-FastCalc

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 1.997-alt6
- bootstrap for perl-5.18

* Sun Sep 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.997-alt5
- re-enabled dependency on perl-Math-BigInt-FastCalc

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 1.997-alt4
- bootstrap for perl-5.16

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
