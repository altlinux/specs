## SPEC file for Perl module Ref::Util

%define real_name Ref-Util

Name: perl-Ref-Util
Version: 0.101
Release: alt2

Summary: Perl utility functions for checking references

License: %mit
Group: Development/Perl

URL: http://search.cpan.org/dist/Ref-Util/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Sep 17 2016
# optimized out: perl python-base python-modules python3
BuildRequires: perl-Encode perl-Readonly perl-devel

%description
Perl module Ref::Util provides several functions to help identify
references in a faster and smarter way.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Ref/Util*
%perl_vendor_autolib/Ref/Util*

%changelog
* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.101-alt2
- Initial build for ALT Linux Sisyphus
