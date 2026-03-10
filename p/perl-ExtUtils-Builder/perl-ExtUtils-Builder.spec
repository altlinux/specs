## SPEC file for Perl module ExtUtils::Builder

%define real_name ExtUtils-Builder

%define _unpackaged_files_terminate_build 1

Name: perl-ExtUtils-Builder
Version: 0.020
Release: alt1

Summary: Perl module to make an abstract representation of build processes

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/ExtUtils-Builder

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 10 2026
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python3 python3-base sh5
BuildRequires: perl-CPAN-Meta perl-ExtUtils-Config perl-ExtUtils-Helpers perl-Perl-OSType

%description
Perl module ExtUtils::Builder tries to abstract steps of Perl extensions build
processes into reusable building blocks for creating platform and build system
agnostic executable descriptions of work. This allows producing and consuming
sides to be completely independent from each other.

These build steps can be used directly (e.g. Dist::Build) or be converted
into Makefile.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/ExtUtils/Builder*

%changelog
* Mon Mar 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.020-alt1
- Initial build for ALT Linux Sisyphus
