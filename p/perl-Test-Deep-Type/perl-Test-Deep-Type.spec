%define real_name Test-Deep-Type

Name: perl-%real_name
Version: 0.008
Release: alt1

Summary: A Test::Deep plugin for validating type constraints

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Test-Deep perl-Try-Tiny perl-Test-Needs perl-Test-Tester perl-Test-Fatal

%description
Test::Deep::Type is a Test::Deep plugin that lets you compare a value
against a type constraint (e.g. from Moose, Specio, or Type::Tiny),
descending into the structure and checking each element against the
constraint.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENCE
%perl_vendor_privlib/Test/Deep/*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.008-alt1
- initial build for Sisyphus
