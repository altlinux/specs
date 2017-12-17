%define dist Crypt-OpenBSD-Blowfish

Name: perl-%dist
Version: 0.01
Release: alt1.1.1

Summary: This module provides an interface to the OpenBSD Blowfish cipher implementation
License: %perl_license
Group: Development/Perl

URL: http://github.com/lkinley/Crypt-OpenBSD-Blowfish
Source: %dist-%version.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
BuildRequires: perl-Encode perl-devel

%description
This module provides an interface to the OpenBSD Blowfish cipher implementation

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1.1
- rebuild with new perl 5.24.1

* Sat Feb 20 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.01-alt1
- initial build
