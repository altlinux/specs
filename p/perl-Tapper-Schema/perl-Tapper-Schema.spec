%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(JSON/XS.pm) perl(Tapper/Model.pm) perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl-podlators perl(File/Slurp.pm)
# END SourceDeps(oneline)
BuildRequires: perl(DBD/SQLite.pm) perl(Hash/Merge/Simple.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-Schema
%define upstream_version 5.0.9

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Database schemas for Tapper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Compress/Bzip2.pm)
BuildRequires: perl(DBD/Pg.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(DBD/mysql.pm)
BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(DBIx/Class/Core.pm)
BuildRequires: perl(DBIx/Class/InflateColumn/DateTime.pm)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm)
BuildRequires: perl(DBIx/Class/ResultSet.pm)
BuildRequires: perl(DBIx/Class/Schema.pm)
BuildRequires: perl(DBIx/Class/TimeStamp.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Duration.pm)
BuildRequires: perl(DateTime/Format/MySQL.pm)
BuildRequires: perl(DateTime/Format/Pg.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(DateTime/Format/Strptime.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Module/Pluggable.pm)
BuildRequires: perl(SQL/Translator.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/TAP/Harness.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Variable/Magic.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(YAML/XS.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(namespace/clean.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Database schemas for Tapper.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.9-alt1_1
- update by mgaimport

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.9-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.8-alt1
- automated CPAN update

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.6-alt1_1
- update by mgaimport

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.6-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_4.1
- NMU: fixed build

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_1
- mageia import by cas@ requiest

