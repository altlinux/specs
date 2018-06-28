%define _unpackaged_files_terminate_build 1
%define sname test-compile

Name: perl-Test-Compile
Version: 1.3.0
Release: alt1
Summary: Check whether Perl module files compile correctly
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Test-Compile/
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(ExtUtils/MakeMaker.pm)
# Run-time
# Devel::CheckOS is needed only on VMS. See Changes.
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(Test/Builder.pm)
BuildRequires: perl(UNIVERSAL/require.pm)
BuildRequires: perl(version.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Test/Warnings.pm)
BuildRequires: perl-Module-Build
BuildRequires: perl-Devel-CheckOS
# Tests
# Test::More version is described in Changes
BuildRequires: perl(Test/More.pm)

%description
Test::Compile lets you check the validity of a Perl module file or Perl script
file, and report its results in standard Test::Simple fashion.

%prep
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorlib/*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.3.0-alt1
- initial build for ALT
