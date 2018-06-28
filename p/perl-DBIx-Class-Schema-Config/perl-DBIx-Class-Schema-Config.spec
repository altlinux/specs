%define _unpackaged_files_terminate_build 1

Name: perl-DBIx-Class-Schema-Config
Version: 0.001011
Release: alt1
Summary: Credential Management for DBIx::Class
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/DBIx-Class-Schema-Config/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(inc/Module/Install.pm)
BuildRequires: perl(Module/Install/Metadata.pm)
BuildRequires: perl(Module/Install/WriteAll.pm)
# Run-time
BuildRequires: perl(base.pm)
BuildRequires: perl(Config/Any.pm)
BuildRequires: perl(DBIx/Class/Schema.pm)
BuildRequires: perl(File/HomeDir.pm)
BuildRequires: perl(Hash/Merge.pm)
BuildRequires: perl(namespace/clean.pm)
BuildRequires: perl(Storable.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
# Tests
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(DBI.pm)
BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(Test/More.pm)
Requires: perl(DBIx/Class.pm)

%description
DBIx::Class::Schema::Config is a subclass of DBIx::Class::Schema that
allows the loading of credentials & configuration from a file. The actual
code itself would only need to know about the name used in the
configuration file. This aims to make it simpler for operations teams to
manage database credentials.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/DBIx/Class/Schema*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.001011-alt1
- initial build for ALT
