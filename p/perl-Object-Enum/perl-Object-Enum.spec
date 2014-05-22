# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Object-Enum
%define upstream_version 0.073

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Perl Enum Replacement
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/Accessor/Fast.pm)
BuildRequires: perl(Class/Data/Inheritable.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Sub/Install.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
Implements enums in Perl in a robust manner.

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
%doc Changes LICENSE META.yml  README
%perl_vendor_privlib/*

%changelog
* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.073-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.072-alt1_4
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.072-alt1_3
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.072-alt1_2
- mageia import by cas@ requiest

