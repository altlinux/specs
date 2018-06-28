%define _unpackaged_files_terminate_build 1
%define sname sql-tokenizer

Name: perl-SQL-Tokenizer
Version: 0.24
Release: alt1
Summary: Simple SQL tokenizer
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/SQL-Tokenizer/
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)

%description
SQL::Tokenizer is a simple tokenizer for SQL queries. It does not claim to
be a parser or query verifier. It just creates sane tokens from a valid
SQL query.

%prep
%setup -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorlib/SQL*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.24-alt1
- initial build for ALT
