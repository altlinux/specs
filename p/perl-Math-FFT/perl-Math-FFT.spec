Name: perl-Math-FFT
Version: 1.28
Release: alt1

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
* Sun Nov 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt1
- initial build for ALTLinux

