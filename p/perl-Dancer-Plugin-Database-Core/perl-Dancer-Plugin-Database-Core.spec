%define module_version 0.04
%define module_name Dancer-Plugin-Database-Core
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBD/Sponge.pm) perl(DBI.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: Shared core for D1 and D2 Database plugins
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AM/AMBS/Dancer/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/D*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- build for Sisyphus (required for perl update)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

