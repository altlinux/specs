# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBIx/Class.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    DBIx-Class-InflateColumn-Object-Enum
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_4

Summary:    Allows a DBIx::Class user to define a Object::Enum column
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBICx/TestDatabase.pm)
BuildRequires: perl(DBIx/Class/Schema.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Object/Enum.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
no description found

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
%doc Changes LICENSE META.yml 
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update by mgaimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update by mgaimport

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update by mgaimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.04-alt1_1
- mageia import by cas@ requiest

