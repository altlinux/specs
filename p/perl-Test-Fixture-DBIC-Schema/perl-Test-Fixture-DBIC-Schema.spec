# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(DBIx/Class/Schema.pm) perl(Exporter.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBD/SQLite.pm)
%define upstream_name    Test-Fixture-DBIC-Schema
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Load fixture data to storage
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Filter/Util/Call.pm)
BuildRequires: perl(Kwalify.pm)
BuildRequires: perl(Params/Validate.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Requires.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildArch: noarch
Source44: import.info

%description
Test::Fixture::DBIC::Schema is fixture data loader for DBIx::Class::Schema.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- mageia import by cas@ requiest

