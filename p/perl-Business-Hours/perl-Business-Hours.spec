# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: 	Calculate business hours in a time period
Name: 		perl-Business-Hours
Version: 	0.12
Release: 	alt2_10
License: 	GPL+ or Artistic
Group: 		Development/Other
URL: 		http://search.cpan.org/dist/Business-Hours/

Source0: http://search.cpan.org/CPAN/authors/id/R/RU/RUZ/Business-Hours-%{version}.tar.gz
BuildArch: 	noarch

Requires:  perl(Set/IntSpan.pm) >= 1.120

BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:	perl(Set/IntSpan.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Time/Local.pm)
BuildRequires:	perl(warnings.pm)
# Required by the tests
BuildRequires:	perl(Test/More.pm)
# Optional tests:
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
%filter_from_requires /^perl\\(Set.IntSpan.pm\\)$/d

# Filter under-specified dependencies


%description
A simple tool for calculating business hours in a time period. Over time, 
additional functionality will be added to make it easy to calculate the 
number of business hours between arbitrary dates.

%prep
%setup -q -n Business-Hours-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
%make_build


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes
%{perl_vendor_privlib}/Business

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_10
- update to new release by fcimport

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_9
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_9
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_8
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_6
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- fc import

