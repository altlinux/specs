## SPEC file for Perl module File::TreeCreate

%define real_name File-TreeCreate

%define _unpackaged_files_terminate_build 1

Name: perl-File-TreeCreate
Version: 0.0.1
Release: alt2

Summary: recursively create a directory tree.

License: %mit
Group: Development/Perl

URL: https://metacpan.org/release/File-TreeCreate

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Nov 07 2021
# optimized out: libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Tie-RefHash perl-devel perl-parent perl-podlators python3-base sh4
BuildRequires: perl-HTML-Parser perl-Module-Build perl-autodie

%description
Perl module File::TreeCreate recursively create a directory tree.
This module primary intended to be used in the tests of some of
File::Find::* CPAN distributions.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/TreeCreate*

%changelog
* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.0.1-alt2
- Rise release to override package from Autoimports/Sisyphus repository

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
