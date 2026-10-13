%define _unpackaged_files_terminate_build 1
%define dist Crypt-DSA-GMP
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: DSA Signatures and Key Generation using GMP

License: %perl_license
Group: Development/Perl
Url: %CPAN %dist

# Source-url: http://www.cpan.org/authors/id/D/DA/DANAJ/%dist-%version.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl(Test/More.pm) perl(Convert/PEM.pm) perl(Crypt/DES_EDE3.pm) perl(Math/BigInt/GMP.pm) perl(Math/Prime/Util/GMP.pm) perl(Data/Buffer.pm) perl(Crypt/Random/Seed.pm) perl(Digest/SHA.pm)

%description
Crypt::DSA::GMP is an implementation of the DSA (Digital Signature
Algorithm) signature verification system. It is a fork of Crypt::DSA
using Math::BigInt::GMP and Math::Prime::Util::GMP for speed and
supporting FIPS 186-3/186-4 key generation.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Crypt/DSA/GMP*

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for Sisyphus
