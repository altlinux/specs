# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Data-YAML
%define upstream_version 0.0.6

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Easy YAML serialisation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(version.pm)
BuildArch: noarch
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
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README SIGNATURE
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.0.6-alt1_1
- mageia import by cas@ requiest

