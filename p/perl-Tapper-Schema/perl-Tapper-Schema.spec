# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBD/SQLite.pm) perl(Hash/Merge/Simple.pm)
%define upstream_name    Tapper-Schema
%define upstream_version 4.1.1

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Database schemas for Tapper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Compress/Bzip2.pm)
BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(DBIx/Class/Core.pm)
BuildRequires: perl(DBIx/Class/InflateColumn/DateTime.pm)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm)
BuildRequires: perl(DBIx/Class/ResultSet.pm)
BuildRequires: perl(DBIx/Class/Schema.pm)
BuildRequires: perl(DBIx/Class/TimeStamp.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Format/MySQL.pm)
BuildRequires: perl(DateTime/Format/Pg.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(SQL/Translator.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/TAP/Harness.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Database schemas for Tapper.

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
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_1
- mageia import by cas@ requiest

