%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Catalyst/Runtime.pm) perl(Data/DPath.pm) perl(DateTime.pm) perl(DateTime/Format/DateParse.pm) perl(File/Find/Rule.pm) perl(File/stat.pm) perl(FindBin.pm) perl(Hash/Merge.pm) perl(Moose/Role.pm) perl(Perl6/Junction.pm) perl(Pod/Usage.pm) perl(Test/WWW/Mechanize/Catalyst.pm) perl(XML/Feed.pm) perl(YAML.pm) perl(common/sense.pm) perl(namespace/autoclean.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm) perl(Tapper/Cmd/Init.pm) perl(Tapper/Base.pm)
%define upstream_name    Tapper-CLI
%define upstream_version 5.0.4

Name:       perl-%{upstream_name}
Version:    5.0.5
Release:    alt1
%if %release == alt3nt
%define _without_test 1
%endif
Summary:    Tapper-* command line tools
License:    BSD
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/T/TA/TAPPER/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(App/Cmd.pm)
BuildRequires: perl(App/Cmd/Command.pm)
BuildRequires: perl(App/Rad.pm)
BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Compress/Bzip2.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(IO/Socket.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Tapper/Cmd/Cobbler.pm)
BuildRequires: perl(Tapper/Cmd/Notification.pm)
BuildRequires: perl(Tapper/Cmd/Precondition.pm)
BuildRequires: perl(Tapper/Cmd/Queue.pm)
BuildRequires: perl(Tapper/Cmd/Requested.pm)
BuildRequires: perl(Tapper/Cmd/Scenario.pm)
BuildRequires: perl(Tapper/Cmd/Testplan.pm)
BuildRequires: perl(Tapper/Cmd/Testrun.pm)
BuildRequires: perl(Tapper/Cmd/User.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Reports/DPath/TT.pm)
BuildRequires: perl(Tapper/Schema.pm)
BuildRequires: perl(Tapper/Schema/ReportsDB.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Tapper/Schema/TestrunDB.pm)
#BuildRequires: perl(Tapper/Testplan/Generator.pm)
#BuildRequires: perl(Tapper/Testplan/Reporter.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(UNIVERSAL.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(YAML/XS.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Command line tools for Tapper.

%prep
%setup -q -n %{upstream_name}-%{version}

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
%_bindir/tapper*
%_man1dir/tapper*

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.5-alt1
- automated CPAN update

* Mon Apr 11 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.4-alt2
- build w/o Tapper-Testplan

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.4-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 4.1.7-alt1
- automated CPAN update

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt3nt
- disabled tests - waiting for the new release

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

