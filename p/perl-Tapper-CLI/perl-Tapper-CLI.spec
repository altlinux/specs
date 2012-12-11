# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Catalyst/Runtime.pm) perl(Data/DPath.pm) perl(DateTime.pm) perl(DateTime/Format/DateParse.pm) perl(File/Find/Rule.pm) perl(File/stat.pm) perl(FindBin.pm) perl(Hash/Merge.pm) perl(Moose/Role.pm) perl(Perl6/Junction.pm) perl(Pod/Usage.pm) perl(Test/WWW/Mechanize/Catalyst.pm) perl(XML/Feed.pm) perl(YAML.pm) perl(common/sense.pm) perl(namespace/autoclean.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
%define upstream_name    Tapper-CLI
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper-* command line tools
License:    BSD
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRequires: perl(Tapper/Testplan/Generator.pm)
BuildRequires: perl(Tapper/Testplan/Reporter.pm)
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
/usr/bin/tapper
/usr/bin/tapper-api
/usr/bin/tapper-db-deploy
/usr/bin/tapper-testrun
/usr/share/man/man1/tapper-api.1.*
/usr/share/man/man1/tapper-db-deploy.1.*
/usr/share/man/man1/tapper-testrun.1.*
/usr/share/man/man1/tapper.1.*



%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

