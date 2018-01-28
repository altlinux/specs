## SPEC file for Perl module Consul

%define real_name Consul

Name: perl-Consul
Version: 0.023
Release: alt1

Summary:  Perl client library for Consul

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Consul/
#URL: https://github.com/robn/Consul

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 28 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-MaybeXS perl-JSON-PP perl-Moo perl-Parse-CPAN-Meta perl-Try-Tiny perl-URI perl-devel perl-parent python-base python-modules python3 python3-base
BuildRequires: perl-CPAN-Meta perl-Convert-Base64 perl-HTTP-Tiny perl-Hash-MultiValue perl-Test-Exception perl-Test-TCP perl-Type-Tiny perl-namespace-autoclean

%description
Perl module Consul provides a client library for accessing and
manipulating data in a Consul cluster. It targets the
Consul v1 HTTP API.

This module is quite low-level. You're expected to have a good
understanding of Consul and its API to understand the methods
this module provides.

# TO FIX: there are no Test::Consul module in Sisyphus,
# nor Consul itself - we can't test this module
%def_without test

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Consul*

%changelog
* Sun Jan 28 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.023-alt1
- New version

* Wed Aug 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.022-alt1
- New version

* Sun Jul 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.021-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.020-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.019-alt1
- New version

* Mon Jul 04 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.016-alt2
- Fix build (updating BuildRequires)

* Sat Apr 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.016-alt1
- Initial build for ALT Linux Sisyphus
