# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Data-YAML
%define upstream_version 0.0.7

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Easy YAML serialisation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(version.pm)
BuildArch:  noarch
Source44: import.info

%description
In the spirit of YAML::Tiny, Data::YAML::Reader and
Data::YAML::Writer provide lightweight, dependency-free YAML
handling. While 'YAML::Tiny' is designed principally for working with
configuration files, 'Data::YAML' concentrates on the transparent round-
tripping of YAML serialized Perl data structures.

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
%doc Changes META.json META.yml  README SIGNATURE
%perl_vendor_privlib/*

%changelog
* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_3
- update by mgaimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_2
- update by mgaimport

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.0.6-alt1_1
- mageia import by cas@ requiest

