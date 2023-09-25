# BEGIN SourceDeps(oneline):
BuildRequires: perl(Crypt/CBC.pm) perl(Crypt/Mode/CBC.pm) perl(Crypt/Mode/CFB.pm) perl(Crypt/Mode/CTR.pm) perl(Crypt/Mode/ECB.pm) perl(Crypt/Mode/OFB.pm) perl(Crypt/OpenSSL/Guess.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define dist Crypt-OpenSSL-AES

Name: perl-%dist
Version: 0.10
Release: alt1

Summary: XS-wrapper around OpenSSL's AES library
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/T/TI/TIMLEGGE/%{dist}-%{version}.tar.gz

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
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 0.10-alt1
- automated CPAN update

* Fri Sep 15 2023 Igor Vlasenko <viy@altlinux.org> 0.07-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.2
- rebuild with new perl 5.28.1

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.02-alt1.1.2
- NMU: Rebuild with new openssl 1.1.0.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.24.1

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.02-alt1
- initial build
