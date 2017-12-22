%define _unpackaged_files_terminate_build 1
%define dist Crypt-Curve25519

Name: perl-%dist
Version: 0.06
Release: alt2

Summary: Generate shared secret using elliptic-curve Diffie-Hellman function
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AJ/AJGB/%{dist}-%{version}.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
# optimized out: perl-parent
BuildRequires: perl-Encode perl-devel

%description
Generate shared secret using elliptic-curve Diffie-Hellman function

%prep
%setup -n %{dist}-%{version}
%ifarch e2k
# see mcst#1802; check with lcc >= 1.24; s/uint128_t/uintmax_t/g fails tests
sed -i 's,=\$x64,=0,;' Makefile.PL
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README curve25519-donna-license.md
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 22 2017 Michael Shigorin <mike@altlinux.org> 0.06-alt2
- E2K: avoid uint128_t use for now

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- rebuild with new perl 5.24.1

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.04-alt1
- initial build
