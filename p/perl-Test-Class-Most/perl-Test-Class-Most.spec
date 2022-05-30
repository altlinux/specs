%define _unpackaged_files_terminate_build 1

Name: perl-Test-Class-Most
Version: 0.08
Release: alt1
Summary: Test::Class::Most - Test Classes the easy way
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/pod/Test::Class::Most
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(Module/Build.pm) perl(Test/Class/Load.pm) perl(Test/Most.pm)

%description
Using the module helps to reduce boilerplate when writing tests based on
Test::Class.

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
* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 0.08-alt1
- initial build for ALT

