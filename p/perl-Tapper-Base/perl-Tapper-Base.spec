%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Devel/AssertOS.pm) perl(Devel/CheckOS.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Find/Rule.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-Base
%define upstream_version 5.0.0

Name:       perl-%{upstream_name}
Version:    5.0.0
Release:    alt1

Summary:    Require that we are running on a particular OS
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-Base-%{version}.tar.gz

BuildRequires: perl(English.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(LockFile/Simple.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Module/Find.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
A learned sage once wrote on IRC:

   $^O is stupid and ugly, it wears its pants as a hat

Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

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
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.4-alt1_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.4-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.4-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  4.1.4-alt1_1
- mageia import by cas@ requiest

