# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
%define upstream_name    Tapper-Reports-Receiver
%define upstream_version 4.1.1

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Receive test reports
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(AnyEvent.pm)
BuildRequires: perl(AnyEvent/Handle.pm)
BuildRequires: perl(AnyEvent/Socket.pm)
BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Data/DPath.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime/Format/Mail.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(Devel/Backtrace.pm)
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
BuildArch: noarch
Source44: import.info

%description
Tapper Distribution for Recevining Test Reports.

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
%doc META.json META.yml Changes LICENSE README SPEC
%perl_vendor_privlib/*
/usr/bin/tapper-reports-receiver
/usr/bin/tapper-reports-receiver-daemon
/usr/share/man/man1/tapper-reports-receiver-daemon.1.*
/usr/share/man/man1/tapper-reports-receiver.1.*



%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_1
- mageia import by cas@ requiest

