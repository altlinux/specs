%define dist Crypt-Twofish
Name: perl-%dist
Version: 2.17
Release: alt2.1.1.1.1

Summary: The Twofish Encryption Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AM/AMS/Crypt-Twofish-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Crypt-CBC perl-devel

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128,
192, or 256-bit) key, developed by Counterpane Labs. It is unpatented
and free for all uses, as described at
<URL:http://www.counterpane.com/twofish.html>.

This module implements Twofish encryption. It supports the Crypt::CBC
interface, with the functions described below. It also provides an
interface that is call-compatible with Crypt::Twofish 1.0, but its use
in new code is strongly discouraged.

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.17-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.17-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.17-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.17-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.17-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 2.14-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.14-alt1.2
- rebuitl for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.14-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- first build for ALT Linux Sisyphus
