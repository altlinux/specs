# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-MockTime
Version:        0.16
Release:        alt1
Summary:        Replaces actual time with simulated time
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-MockTime/
Source0:        http://www.cpan.org/authors/id/D/DD/DDICK/Test-MockTime-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Time/Local.pm)
BuildRequires:  perl(Time/Piece.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

# for improved tests
BuildRequires:  perl(Test/Pod.pm)

Requires:       perl(Time/Piece.pm) >= 1.080
Source44: import.info

%description
This module was created to enable test suites to test code at specific
points in time. Specifically it overrides localtime, gmtime and time at
compile time and then relies on the user supplying a mock time via
set_relative_time, set_absolute_time or set_fixed_time to alter future
calls to gmtime,time or localtime.

%prep
%setup -q -n Test-MockTime-%{version}

# fix up broken permissions
chmod -x lib/Test/MockTime.pm t/test.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_5
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_4
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3_11
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3_10
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_10
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_8
- fc import

