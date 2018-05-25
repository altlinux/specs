# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(parent.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_MockModule_enables_optional_test
%else
%bcond_with perl_Test_MockModule_enables_optional_test
%endif

Name:           perl-Test-MockModule
Version:        0.15
Release:        alt1_1
Summary:        Override subroutines in a module for unit testing
Group:          Development/Other
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-MockModule/
Source0:        http://search.cpan.org/CPAN/authors/id/G/GF/GFRANKS/Test-MockModule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(SUPER.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:	perl(Test/Warnings.pm)
%if %{with perl_Test_MockModule_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n Test-MockModule-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/Test

%changelog
* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- new version

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_19
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_18
- update to new release by fcimport

* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- picked up by robot, thanks to enp@

* Fri Oct 26 2012 Eugene Prokopiev <enp@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

