# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Check/ISA.pm) perl(DBD/SQLite.pm) perl(DBD/mysql.pm) perl(DBI.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.04
%define module_name DBIx-Abstract
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.04
Release: alt2
Summary: DBI SQL abstraction
Group: Development/Perl
License: perl
URL: https://github.com/iarna/DBIx-Abstract

Source0: http://cpan.org.ua/authors/id/W/WI/WINTER/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/D*

%changelog
* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2
- to Sisyphus as colorer dependency

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- initial import by package builder

