# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Test.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Math-Fibonacci
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_6

Summary:    Fibonacci numbers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch: noarch
Source44: import.info

%description
This module provides a few functions related to Fibonacci numbers.

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
%doc Changes ARTISTIC TODO
%perl_vendor_privlib/*




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_4
- update by mgaimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_3
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- converted for ALT Linux by srpmconvert tools

