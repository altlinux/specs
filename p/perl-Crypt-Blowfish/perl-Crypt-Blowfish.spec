%define dist Crypt-Blowfish
Name: perl-%dist
Version: 2.12
Release: alt1.2

Summary: Perl Blowfish encryption module
License: GPLR Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Crypt-CBC perl-devel

%description
Blowfish is capable of strong encryption and can use key sizes up
to 56 bytes (a 448 bit key).  You're encouraged to take advantage
of the full key size to ensure the strongest encryption possible
from this module.

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
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.12-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.12-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version 2.10 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt1
- first build for ALT Linux Sisyphus
