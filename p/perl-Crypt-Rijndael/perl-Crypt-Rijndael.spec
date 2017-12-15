%define _unpackaged_files_terminate_build 1
%define dist Crypt-Rijndael
Name: perl-%dist
Version: 1.13
Release: alt1.1.1.1

Summary: Crypt::CBC compliant Rijndael encryption module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-%{version}.tar.gz

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1.1
- rebuild with new perl 5.20.1

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt1
- 1.09 -> 1.11
- built for perl-5.16

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
