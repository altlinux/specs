%define _unpackaged_files_terminate_build 1

Name: perl-Specio-Library-Path-Tiny
Version: 0.05
Release: alt1
Summary: Path::Tiny types and coercions for Specio
License: ASL-2.0
Group: Development/Perl
Url: https://metacpan.org/release/Specio-Library-Path-Tiny
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/Specio-Library-Path-Tiny-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/Fatal.pm) perl(Specio.pm) perl-devel perl(File/pushd.pm) perl(Path/Tiny.pm) perl(Test/More.pm)

%description
This library provides a set of Path::Tiny types and coercions for Specio.
These types can be used with Moose, Moo, Params::ValidationCompiler, and
other modules.

%prep
%setup -q -n Specio-Library-Path-Tiny-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md README.md
%perl_vendorlib/*

%changelog
* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1
- automated CPAN update

* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 0.04-alt1
- initial build for ALT

