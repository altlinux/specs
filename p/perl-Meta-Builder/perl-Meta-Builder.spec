Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Meta-Builder
Version:        0.004
Release:        alt1_4
Summary:        Tools for creating Meta objects to track custom metrics
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Meta-Builder
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Meta-Builder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Fennec/Lite.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Meta programming is becoming more and more popular. The popularity of Meta
programming comes from the fact that many problems are made significantly
easier. There are a few specialized Meta tools out there, for instance
Class:MOP which is used by Moose to track class metadata.

%prep
%setup -q -n Meta-Builder-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_4
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_1
- update to new release by fcimport

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_10
- update to new release by fcimport

* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_9
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_9
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_8
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_7
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_4
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_1
- initial fc import

