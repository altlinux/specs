Name: perl-CSS-Compressor
Version: 0.02
Release: alt1

Summary: Perl extension for CSS minification
Group: Development/Perl
License: Perl

Url: %CPAN CSS-Compressor
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Test-Differences perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CSS/Compressor*
%doc README

%changelog
* Tue Jan 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux

