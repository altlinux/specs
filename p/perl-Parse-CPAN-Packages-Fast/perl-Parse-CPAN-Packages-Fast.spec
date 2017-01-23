## SPEC file for Perl module Parse::CPAN::Packages::Fast

%define real_name Parse-CPAN-Packages-Fast

Name: perl-Parse-CPAN-Packages-Fast
Version: 0.09
Release: alt2

Summary: Perl module to parse CPAN's package index

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Parse-CPAN-Packages-Fast/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-Compress-Raw-Zlib perl-Encode perl-IO-Compress perl-devel perl-parent python-base python-modules python3-base
BuildRequires: perl-CPAN perl-CPAN-DistnameInfo

%description
Perl module Parse::CPAN::Packages::Fast provides an API to
parse CPAN's package index.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Parse/CPAN/Packages/Fast*

%changelog
* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.09-alt2
- Initial build for ALT Linux Sisyphus
