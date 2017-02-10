%define _unpackaged_files_terminate_build 1
%define dist Crypt-Curve25519

Name: perl-%dist
Version: 0.05
Release: alt1.1

Summary: Generate shared secret using elliptic-curve Diffie-Hellman function
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AJ/AJGB/Crypt-Curve25519-%{version}.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
# optimized out: perl-parent
BuildRequires: perl-Encode perl-devel

%description
Generate shared secret using elliptic-curve Diffie-Hellman function

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
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- rebuild with new perl 5.24.1

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.04-alt1
- initial build
