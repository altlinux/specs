%define module Crypt-OpenSSL-Bignum

Name: perl-%module
Version: 0.04
Release: alt2

Summary: Perl module for OpenSSL's multiprecision integer arithmetic
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Crypt/%module-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libssl-devel perl-devel

%description
Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision integer
arithmetic libraries.

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
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.1.1
- rebuilt with perl 5.12

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.04-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Wed Jul 25 2007 Victor Forsyuk <force@altlinux.org> 0.04-alt1
- 0.04

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.03-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Nov 16 2005 Victor Forsyuk <force@altlinux.ru> 0.03-alt1
- Initial build.
