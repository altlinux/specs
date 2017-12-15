%define module Crypt-OpenSSL-RSA

Name: perl-%module
Version: 0.28
Release: alt4.1.1.1.1

Summary: RSA encoding and decoding, using the openSSL libraries
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: %module-%version.tar.gz

# Not autodetectable (required inside eval)
Requires: perl-Crypt-OpenSSL-Bignum

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libssl-devel perl-Crypt-OpenSSL-Bignum perl-Crypt-OpenSSL-Random perl-devel

%description
Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which
are somewhat shorter than the block size of a key. It also allows for
decryption, signatures and signature verification.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.28-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.28-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 0.27-alt1
- 0.27

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.26-alt1.1
- rebuilt with perl 5.12

* Fri Dec 11 2009 Victor Forsyuk <force@altlinux.org> 0.26-alt1
- 0.26

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.25-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Wed Jul 25 2007 Victor Forsyuk <force@altlinux.org> 0.25-alt1
- 0.25

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.23-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Jun 13 2006 Victor Forsyuk <force@altlinux.ru> 0.23-alt1
- 0.23

* Wed Nov 16 2005 Victor Forsyuk <force@altlinux.ru> 0.22-alt1
- Initial build.
