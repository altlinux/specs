# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper
%define upstream_version 4.1

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_7

Summary:    Automated OS testing, also virtualized
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Tapper is a modular, flexible and open test infrastructure.

Its only primary assumption is the ubiquitous use of the Test Anything
Protocol (TAP). Internally it is based on technology known from the CPAN
testing infrastructure, extending it with automation and advanced querying.

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
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_7
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_5
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_4
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_3
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  4.1-alt1_2
- mageia import by cas@ requiest

