%define real_name Algorithm-BloomFilter

Name: perl-%real_name
Version: 0.02
Release: alt1

Summary: A simple bloom filter data structure

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel

%description
Algorithm::BloomFilter implements a simple bloom filter data structure in C/XS.
It uses SipHash internally for hashing.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Algorithm*
%perl_vendor_archlib/auto/Algorithm

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for Sisyphus

