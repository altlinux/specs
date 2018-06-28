%define _unpackaged_files_terminate_build 1
%define sname sql-splitstatement

Name: perl-SQL-SplitStatement
Version: 1.00020
Release: alt1
Summary: Split any SQL code into atomic statements
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/SQL-SplitStatement/
Source: %sname-%version.tar
Patch0: getopt-long-compat.patch
BuildArch: noarch
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Class/Accessor/Fast.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(List/MoreUtils.pm)
BuildRequires: perl(Pod/Usage.pm)
BuildRequires: perl(Regexp/Common.pm)
BuildRequires: perl(SQL/Tokenizer.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Script/Run.pm)
BuildRequires: perl(base.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)

%description
This is a simple module which tries to split any SQL code, even including
non-standard extensions (for the details see the "SUPPORTED DBMSs" section
of the module documentation), into the atomic statements it is composed of.

%prep
%setup -n %sname-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
# The LICENSE file is outdated and contains the wrong address for the FSF
# https://rt.cpan.org/Ticket/Display.html?id=107996
%_bindir/sql-split
%perl_vendorlib/SQL
%_man1dir/sql-split.1*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.00020-alt1
- initial build for ALT
