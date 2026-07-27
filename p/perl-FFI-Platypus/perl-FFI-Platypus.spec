%define real_name FFI-Platypus

Name: perl-%real_name
Version: 2.11
Release: alt1

Summary: Write Perl bindings to non-Perl libraries with FFI. No XS required.

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Alien-FFI perl-FFI-CheckLib perl-Capture-Tiny perl-ExtUtils-CBuilder
BuildRequires: perl-autodie
BuildRequires: libffi-devel pkg-config
BuildRequires: perl-Test2-Suite

%description
FFI::Platypus is a tool for writing Perl bindings to non-Perl libraries
using the Foreign Function Interface (libffi). No XS required.

%prep
%setup -q -n %real_name-%version

%build
export ALIEN_INSTALL_TYPE=system
%perl_vendor_build

%install
export ALIEN_INSTALL_TYPE=system
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/FFI*
%perl_vendor_archlib/auto/FFI
%perl_vendor_archlib/auto/share/dist/FFI-Platypus

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 2.11-alt1
- initial build for Sisyphus
