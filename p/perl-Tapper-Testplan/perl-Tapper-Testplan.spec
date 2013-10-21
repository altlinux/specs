# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm) perl(Tapper/Base.pm)
%define upstream_name    Tapper-Testplan
%define upstream_version 4.1.2

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Main module for testplan reporting
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CHI.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Format/DateParse.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(DateTime/Format/Strptime.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(Email/Sender/Simple.pm)
BuildRequires: perl(Email/Sender/Transport/SMTP.pm)
BuildRequires: perl(Email/Simple.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(HTTP/Daemon.pm)
BuildRequires: perl(HTTP/Status.pm)
BuildRequires: perl(Hash/Merge.pm)
BuildRequires: perl(Module/Find.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Tapper/Cmd/Testplan.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Test/Differences.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/CSV/Slurp.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: rsync
Requires:   rsync
BuildArch:  noarch
Source44: import.info

%description
This distribution provides a main module for testplan reporting, for Tapper.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*


%changelog
* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

