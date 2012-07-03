%define dist Crypt-DES
Name: perl-Crypt-DES
Version: 2.05
Release: alt1.2

Summary: Perl DES encryption module
License: BSD
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Crypt-CBC perl-devel

%description
Crypt::DES - an XS-based DES implimentation for Perl.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README COPYRIGHT
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.05-alt1.1
- rebuilt with perl 5.12

* Fri Jan 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.05-alt1
- 2.05

* Fri Dec 24 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 2.03-alt3
- rebuild with perl-5.8.6

* Sun Sep 07 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.03-alt2
- rebuild with hasher
- add 'URL:' tag into spec-file

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.03-alt1
- Initial package for ALT Linux
