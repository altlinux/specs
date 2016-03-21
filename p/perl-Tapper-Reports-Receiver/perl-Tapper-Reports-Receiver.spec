%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm) perl(DateTime/Format/SQLite.pm)
%define upstream_name    Tapper-Reports-Receiver
%define upstream_version 5.0.0

Name:       perl-%{upstream_name}
Version:    5.0.0
Release:    alt1

Summary:    Receive test reports
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-Reports-Receiver-%{version}.tar.gz

BuildRequires: perl(AnyEvent.pm)
BuildRequires: perl(AnyEvent/Handle.pm)
BuildRequires: perl(AnyEvent/Socket.pm)
BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Data/DPath.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime/Format/Mail.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(Devel/Backtrace.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/MimeInfo/Magic.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(HTTP/Daemon.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(LockFile/Simple.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Module/Find.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Daemonize.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Sys/Syslog.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Schema.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Tapper/TAP/Harness.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper Distribution for Recevining Test Reports.

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
%doc Changes LICENSE META.json META.yml  README SPEC
%perl_vendor_privlib/*
/usr/bin/tapper-reports-receiver
/usr/bin/tapper-reports-receiver-daemon
/usr/share/man/man1/tapper-reports-receiver-daemon.1*
/usr/share/man/man1/tapper-reports-receiver.1*


%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_4
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1
- automated CPAN update

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt2_1
- fixed build

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_1
- mageia import by cas@ requiest

