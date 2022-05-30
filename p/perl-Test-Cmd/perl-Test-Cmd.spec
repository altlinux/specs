%define _unpackaged_files_terminate_build 1
%define sname Test-Cmd

Name:  perl-Test-Cmd
Version: 1.09
Release: alt1
Summary: Perl module for portable testing of commands and scripts
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Test-Cmd
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)

%description
The Test::Cmd module provides a framework for portable automated testing
of executable commands and scripts (in any language, not just Perl),
especially commands and scripts that interace with the file system.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*

%changelog
* Thu May 26 2022 Alexandr Antonov <aas@altlinux.org> 1.09-alt1
- initial build for ALT

