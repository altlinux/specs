Name: perl-Math-FFT
Version: 1.34
Release: alt1.1

Summary: Perl extension for Fast Fourier Transforms
Group: Development/Perl
License: Perl and Public Domain

Url: %CPAN Math-FFT
Source: %name-%version.tar

BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Math/FFT*
%perl_vendor_archlib/Math/FFT*
%doc Changes README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1.1
- rebuild with new perl 5.26.1

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2.1
- rebuild with new perl 5.20.1

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt2
- built for perl 5.18

* Sun Nov 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt1
- initial build for ALTLinux

