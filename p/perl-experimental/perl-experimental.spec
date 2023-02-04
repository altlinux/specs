%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-experimental
Version:        0.031
Release:        alt1
Summary:        Experimental features made easy
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/experimental
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/experimental-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
# feature is highly recommended on perl >= 5.10
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
# feature is highly recommended on perl >= 5.10
Requires:       perl(feature.pm)
Source44: import.info

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

%prep
%setup -q -n experimental-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sat Feb 04 2023 Igor Vlasenko <viy@altlinux.org> 0.031-alt1
- automated CPAN update

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.030-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.030-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 0.029-alt1
- automated CPAN update

* Tue Apr 26 2022 Igor Vlasenko <viy@altlinux.org> 0.028-alt1
- automated CPAN update

* Tue Feb 08 2022 Igor Vlasenko <viy@altlinux.org> 0.027-alt1
- automated CPAN update

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.025-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 0.024-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1_439
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1_2
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1_1
- update to new release by fcimport

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1_2
- update to new release by fcimport

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_394
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_393
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_366
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_365
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1_1
- update to new release by fcimport

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_1
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_2
- perl dependency for Language-Expr

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_2
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_1
- fc import

