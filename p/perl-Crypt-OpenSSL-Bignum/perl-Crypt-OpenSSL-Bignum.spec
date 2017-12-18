%define _unpackaged_files_terminate_build 1
%define module Crypt-OpenSSL-Bignum

Name: perl-%module
Version: 0.09
Release: alt1

Summary: Perl module for OpenSSL's multiprecision integer arithmetic
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/K/KM/KMX/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libssl-devel perl-devel

%description
Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision integer
arithmetic libraries.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.26.1

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- rebuild with new perl 5.24.1

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.22.0

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- rebuilt for perl-5.16

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
