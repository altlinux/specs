%define module Crypt-X509
%define m_distro Crypt-X509
%define m_name Crypt::X509
%define m_author_id unknown
%define _enable_test 1

Name: perl-Crypt-X509
Version: 0.51
Release: alt1

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Source: %m_distro-%version.tar.gz

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
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Sat Nov 09 2013 Afanasov Dmitry <ender@altlinux.org> 0.51-alt1
- initial build

