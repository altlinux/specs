## SPEC file for Perl module Test::Filename

%define real_name Test-Filename

Name: perl-Test-Filename
Version: 0.03
Release: alt2

Summary: Perl module for portable filename comparison

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Filename/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-IPC-Run3 perl-Probe-Perl perl-devel perl-parent perl-threads python-base python-modules python3-base
BuildRequires: perl-Encode perl-Path-Tiny perl-Test-Script

%description
Perl module Test::Filename provides provides some handy
functions to convert all those path separators
automatically so filename tests will just DWIM.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Filename*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt2
- Initial build for ALT Linux Sisyphus
