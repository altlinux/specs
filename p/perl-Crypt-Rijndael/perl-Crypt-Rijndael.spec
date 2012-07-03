%define dist Crypt-Rijndael
Name: perl-%dist
Version: 1.09
Release: alt1.2

Summary: Crypt::CBC compliant Rijndael encryption module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage

%description
This module implements the Rijndael cipher, which has just been selected
as the Advanced Encryption Standard.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.09-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.06-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.06-alt1
- new version 1.06 (with rpmrb script)

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt1
- new version (1.01)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus
