## SPEC file for Perl module ExtUtils::Builder::Compiler

%define real_name ExtUtils-Builder-Compiler

%define _unpackaged_files_terminate_build 1

Name: perl-ExtUtils-Builder-Compiler
Version: 0.036
Release: alt1

Summary: an interface around different compilers

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/ExtUtils-Builder-Compiler

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Apr 09 2026
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-JSON-PP perl-Parse-CPAN-Meta perl-Perl-OSType perl-devel perl-parent python3 python3-base sh5
BuildRequires: perl-ExtUtils-Builder

%description
Perl module ExtUtils::Builder::Compiler provides an interface
wrapping around different compilers. It's usually not used
directly but by a portability layer like
ExtUtils::Builder::Autodetect::C.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/ExtUtils/Builder/*

%changelog
* Thu Apr 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.036-alt1
- Initial build for ALT Linux Sisyphus
