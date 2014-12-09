Name: perl-Math-FFT
Version: 1.28
Release: alt2.1

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
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2.1
- rebuild with new perl 5.20.1

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt2
- built for perl 5.18

* Sun Nov 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt1
- initial build for ALTLinux

