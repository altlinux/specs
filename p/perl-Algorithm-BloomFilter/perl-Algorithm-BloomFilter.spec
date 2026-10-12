%define real_name Algorithm-BloomFilter

Name: perl-%real_name
Version: 0.03
Release: alt1

Summary: A simple bloom filter data structure

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/%real_name-%version.tar.gz
Source: %real_name-%version.tar

# t/02_security.t: n_bits overflow checks fail on 32-bit x86
ExcludeArch: %ix86

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
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- new version 0.03
- disable build on %%ix86

* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for Sisyphus

