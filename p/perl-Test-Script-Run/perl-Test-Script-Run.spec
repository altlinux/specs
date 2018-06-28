%define _unpackaged_files_terminate_build 1
%define sname test-script-run

Name: perl-Test-Script-Run
Version: 0.08
Release: alt1
Summary: Test the script with run
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Test-Script-Run/
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(base.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(CPAN.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IPC/Run3.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(String/ShellQuote.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)

%description
This module exports some subs to help test and run scripts in your
distribution's bin/ directory, if the script path is not absolute.

%prep
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendorlib/Test/Script*
%perl_vendorlib/Test/Script/Run.pm

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.08-alt1
- initial build for ALT
