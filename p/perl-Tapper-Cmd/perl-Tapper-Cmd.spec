# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
%define upstream_name    Tapper-Cmd
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper - Backend functions for CLI and Web
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(Kwalify.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Net/OpenSSH.pm)
BuildRequires: perl(Perl6/Junction.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Tapper backend functions for the command line and the Web.

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
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

