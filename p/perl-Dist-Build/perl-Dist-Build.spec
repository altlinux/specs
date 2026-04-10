## SPEC file for Perl module Dist::Build

%define real_name Dist-Build

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Build
Version: 0.025
Release: alt1

Summary: SOME PERL MODULE

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Build

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Apr 09 2026
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Encode perl-ExtUtils-Builder perl-ExtUtils-Config perl-ExtUtils-Helpers perl-JSON-PP perl-Parse-CPAN-Meta perl-Perl-OSType perl-devel perl-parent python3 python3-base sh5
BuildRequires: perl-ExtUtils-Builder-Compiler perl-ExtUtils-InstallPaths perl-Term-ANSIColor

%description
Perl module Dist::Build provides SOMETHING

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Build*
#%%perl_vendor_archlib/Dist/Build*
#%%perl_vendor_autolib/Dist/Build*

%changelog
* Thu Apr 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.025-alt1
- Initial build for ALT Linux Sisyphus
