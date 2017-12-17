%define dist Crypt-OpenSSL-AES

Name: perl-%dist
Version: 0.02
Release: alt1.1.1

Summary: XS-wrapper around OpenSSL's AES library
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
BuildRequires: libssl-devel perl-devel

%description
This is XS-wrapper around OpenSSL's AES (Advanced Encryption
Standard) library.

This module is an alternative to the implementation provided by
Crypt::Rijndael which implements AES itself. In contrast, this
module is simply a wrapper around the OpenSSL library.

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.24.1

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.02-alt1
- initial build
