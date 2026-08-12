%define real_name Linux-Smaps-Tiny

# Tests read /proc/self/smaps, unavailable in hasher's restricted /proc
%define _disable_test 1

Name: perl-%real_name
Version: 0.10
Release: alt1

Summary: A minimal and fast alternative to Linux::Smaps

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/A/AV/AVAR/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel

%description
Linux::Smaps::Tiny is a minimal and fast alternative to Linux::Smaps.
It provides a tiny XS interface to /proc/PID/smaps files with a
pure-Perl fallback.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Linux/Smaps
%perl_vendor_archlib/auto/Linux/Smaps

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for Sisyphus

