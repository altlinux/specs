%define dist Net-IDN-Encode
Name: perl-%dist
Version: 2.100
Release: alt1

Summary: Encoding and decoding of Internationalized Domain Names
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-%{version}.tar.gz

# uses unicode properties
Requires: perl-unicore

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Module-Build perl-Test-NoWarnings perl-unicore

%description
Net::IDN::Encode - high-level interface for encoding and decoding of domain
names (implements toASCII and toUNICODE as defined in RFC 3490).

Net::IDN::Punycode - ASCII-compatible encoding of Unicode (Punycode, RFC 3492)

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Net
%perl_vendor_archlib/Net

%changelog
* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 2.100-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.004-alt1
- 2.003 -> 2.004

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.003-alt2
- added dependency on perl-unicore

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 2.003-alt1
- 1.100 -> 2.003
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.100-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.100-alt1.1
- rebuilt with perl 5.12

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.100-alt1
- New version

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- Initial build for ALT Linux Sisyphus
