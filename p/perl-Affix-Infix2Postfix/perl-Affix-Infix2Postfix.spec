## SPEC file for Perl module Affix::Infix2Postfix
## Used during tests of Imager

%define version    0.03
%define release    alt1

Name: perl-Affix-Infix2Postfix
Version: %version
Release: alt1.1

Summary: Perl module for converting from infix notation to postfix notation

License: Artistic
Group: Development/Perl

%define real_name Affix-Infix2Postfix
URL: http://search.cpan.org/~addi/%real_name/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: http://search.cpan.org/CPAN/authors/id/A/AD/ADDI/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel


%description
Perl module Infix2Postfix  as the name suggests converts from 
infix to postfix notation. For example it converts expression
like "a+b+c*d" to a string of operations: "a b + c d * +".

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Affix/Infix2Postfix.pm
%perl_vendor_privlib/auto/Affix/Infix2Postfix*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 25 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt1
- Initial build for ALT Linux

