%define dist Net-IDN-Encode
Name: perl-%dist
Version: 1.100
Release: alt1.2

Summary: Encoding and decoding of Internationalized Domain Names
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Module-Build perl-Net-IDN-Nameprep perl-Test-NoWarnings

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
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.100-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.100-alt1.1
- rebuilt with perl 5.12

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.100-alt1
- New version

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- Initial build for ALT Linux Sisyphus
