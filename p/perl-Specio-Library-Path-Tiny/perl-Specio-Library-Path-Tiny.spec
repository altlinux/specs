%define _unpackaged_files_terminate_build 1

Name: perl-Specio-Library-Path-Tiny
Version: 0.04
Release: alt1
Summary: Path::Tiny types and coercions for Specio
License: ASL-2.0
Group: Development/Perl
Url: https://metacpan.org/release/Specio-Library-Path-Tiny
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/Fatal.pm) perl(Specio.pm) perl-devel perl(File/pushd.pm) perl(Path/Tiny.pm) perl(Test/More.pm)

%description
This library provides a set of Path::Tiny types and coercions for Specio.
These types can be used with Moose, Moo, Params::ValidationCompiler, and
other modules.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*

%changelog
* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 0.04-alt1
- initial build for ALT

