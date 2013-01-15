Name: perl-JavaScript-Minifier
Version: 1.05
Release: alt1

Summary: JavaScript::Minifier - Perl extension for minifying JavaScript code
Group: Development/Perl
License: Perl

Url: %CPAN JavaScript-Minifier
Source: %name-%version.tar

BuildArch: noarch
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
%perl_vendor_privlib/JavaScript/Minifier*
%doc Changes README

%changelog
* Tue Jan 15 2013 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1
- initial build for ALTLinux

