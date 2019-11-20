Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: 	Calculate business hours in a time period
Name: 		perl-Business-Hours
Version: 	0.13
Release: 	alt1_4
License: 	GPL+ or Artistic
URL: 		https://metacpan.org/release/Business-Hours

Source0: https://cpan.metacpan.org/authors/id/B/BP/BPS/Business-Hours-%{version}.tar.gz
BuildArch: 	noarch

Requires:  perl(Set/IntSpan.pm) >= 1.120

BuildRequires:	%{__perl}

BuildRequires:	perl-devel
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

# Filter under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(Set.IntSpan.pm)/d

%description
A simple tool for calculating business hours in a time period. Over time, 
additional functionality will be added to make it easy to calculate the 
number of business hours between arbitrary dates.

%prep
%setup -q -n Business-Hours-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc --no-dereference LICENSE
%doc Changes
%{perl_vendor_privlib}/Business

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_4
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update to new release by fcimport

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_14
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_11
- update to new release by fcimport

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

