## SPEC file for Perl module Ref::Util

%define real_name Ref-Util

Name: perl-Ref-Util
Version: 0.113
Release: alt1.1

Summary: Perl utility functions for checking references

License: %mit
Group: Development/Perl

URL: http://search.cpan.org/dist/Ref-Util/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jan 21 2017
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-Parse-CPAN-Meta python-base python-modules python3
BuildRequires: perl-Encode perl-CPAN-Meta perl-Readonly perl-devel

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
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.113-alt1
- New version

* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.101-alt2
- Initial build for ALT Linux Sisyphus
