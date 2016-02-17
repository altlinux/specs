# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name	 Clone-PP
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_4

Summary:    Recursively copy Perl datatypes
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Clone/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Benchmark.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

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
%doc Changes META.json META.yml  README
%{perl_vendor_privlib}/Clone

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_2
- update by mgaimport

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update by mgaimport

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_1
- update by mgaimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_3
- Sisyphus build

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- converted for ALT Linux by srpmconvert tools

