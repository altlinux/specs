# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Set-Intersection
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Get intersection (of set theory) of arrays
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
This Perl distribution provides an API to get intersection (of set theory) of
arrays.

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
%doc Changes META.yml README
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- mageia import by cas@ requiest

