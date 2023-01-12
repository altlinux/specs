%define _unpackaged_files_terminate_build 1
%define module Crypt-X509
%define m_distro Crypt-X509
%define m_name Crypt::X509
%define m_author_id unknown
%define _enable_test 1

Name: perl-Crypt-X509
Version: 0.55
Release: alt1

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Source0: http://www.cpan.org/authors/id/M/MR/MRSCOTTY/%{module}-%{version}.tar.gz

Summary: Parse a X.509 certificate

BuildArch: noarch
BuildPreReq: rpm-build-perl
BuildRequires: perl-devel perl-Math-BigInt perl-Convert-ASN1

%description
Crypt::X509 parses X.509 certificates. Methods are provided for
accessing most certificate elements.

It is based on the generic ASN.1 module by Graham Barr, on the
x509decode example by Norbert Klasen and contributions on the
perl-ldap-dev-Mailinglist by Chriss Ridd.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.55-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 0.54-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Sat Nov 09 2013 Afanasov Dmitry <ender@altlinux.org> 0.51-alt1
- initial build

