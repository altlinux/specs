%define real_name Crypt-JWT

Name: perl-%real_name
Version: 0.038
Release: alt1

Summary: JSON Web Token (JWT, JWS, JWE, JWK)

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/M/MI/MIK/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-CryptX perl-JSON perl-Compress-Raw-Zlib

%description
Crypt::JWT - JSON Web Token (JWT), JSON Web Signature (JWS), JSON Web
Encryption (JWE) and JSON Web Key (JWK) implementation for Perl, built on top
of CryptX. Supports HS256/384/512, RS256/384/512, PS256/384/512, ES256/384,
EdDSA and A128/192/256KW key wrapping plus the standard compression and content
encryption algorithms.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Crypt/JWT*
%perl_vendor_privlib/Crypt/KeyWrap*

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.038-alt1
- initial build for Sisyphus
