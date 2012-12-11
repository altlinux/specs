# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/Rad.pm) perl(Catalyst/Runtime.pm) perl(Compress/Bzip2.pm) perl(Data/DPath.pm) perl(DateTime.pm) perl(DateTime/Format/DateParse.pm) perl(DateTime/Format/Natural.pm) perl(File/Find/Rule.pm) perl(File/ShareDir.pm) perl(File/stat.pm) perl(FindBin.pm) perl(Hash/Merge.pm) perl(IO/Socket.pm) perl(Moose/Role.pm) perl(Perl6/Junction.pm) perl(Pod/Usage.pm) perl(Template.pm) perl(Test/WWW/Mechanize/Catalyst.pm) perl(Try/Tiny.pm) perl(UNIVERSAL.pm) perl(XML/Feed.pm) perl(YAML.pm) perl(YAML/Syck.pm) perl(YAML/XS.pm) perl(common/sense.pm) perl(namespace/autoclean.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
%define upstream_name    Tapper-Reports-API
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper - Remote network API for result evaluation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Daemonize.pm)
BuildRequires: perl(Net/Server/Fork.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Reports/DPath/Mason.pm)
BuildRequires: perl(Tapper/Reports/DPath/TT.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(subs.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This package provides Tapper's Remote network API for result evaluation.


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
/usr/bin/tapper-reports-api
/usr/bin/tapper-reports-api-daemon
/usr/share/man/man1/tapper-reports-api-daemon.1.*
/usr/share/man/man1/tapper-reports-api.1.*



%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

