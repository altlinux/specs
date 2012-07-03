Name: perl-JavaScript-Beautifier
Version: 0.17
Release: alt1

Summary: JavaScript::Beautifier - Beautify Javascript (beautifier for javascript)
Group: Development/Perl
License: Perl

Url: %CPAN JavaScript-Beautifier
Source: %name-%version.tar

BuildRequires: perl-devel perl-Module-Build perl-Pod-Parser

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/js_beautify.pl
%perl_vendor_privlib/JavaScript/Beautifier*
%doc Changes README 

%changelog
* Fri Oct 21 2011 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- initial build
