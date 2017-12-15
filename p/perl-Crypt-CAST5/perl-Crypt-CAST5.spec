%define dist Crypt-CAST5
Name: perl-%dist
Version: 0.05
Release: alt4.1.1.1.1

Summary: CAST5 block cipher
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Crypt-CBC perl-devel

%description
This module provides an implementation of the CAST5 block cipher using
compiled C code for increased speed. CAST5 is also known as CAST-128.
It is a product of the CAST design procedure developed by C. Adams and
S. Tavares.

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2.2
- rebuit for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- new version 0.05 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus
