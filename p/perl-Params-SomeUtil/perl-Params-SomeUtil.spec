%define _unpackaged_files_terminate_build 1
%define dist Params-SomeUtil
Name: perl-%dist
Version: 1.12
Release: alt1

Summary: Simple, compact and correct param-checking functions

License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl

URL: %CPAN %dist
Source0: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{dist}-%{version}.tar.gz

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl(ExtUtils/CBuilder.pm) perl(File/Spec.pm) perl(Test/More.pm)

%description
Params::SomeUtil provides a basic set of importable functions that makes
checking parameters much easier. This module is a fork of version 1.07 of
Params::Util with some additional bug fixes.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%check
unset PERL_PARAMS_UTIL_PP PERL_PARAMS_SOMEUTIL_PP PUREPERL_ONLY
make test

%files
%doc Changes README LICENSE
%perl_vendor_archlib/Params/SomeUtil*
%perl_vendor_autolib/Params/SomeUtil*

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- initial build for Sisyphus

