Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Execute extra test
%bcond_with perl_DateTime_Format_Flexible_enables_extra_test

Name:       perl-DateTime-Format-Flexible
Version:    0.32
Release:    alt1_1
License:    GPL+ or Artistic
Summary:    Flexibly parse strings and turn them into DateTime objects
Source:     https://cpan.metacpan.org/authors/id/T/TH/THINC/DateTime-Format-Flexible-%{version}.tar.gz
Url:        https://metacpan.org/release/DateTime-Format-Flexible
BuildArch:  noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(DateTime/Infinite.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/MockTime.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
# Extra tests:
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Source44: import.info

%description
If you have ever had to use a program that made you type in the date a certain
way and thought "Why can't the computer just figure out what date I wanted?",
this module is for you.

DateTime::Format::Flexible attempts to take any string you give it and parse
it into a DateTime object.

%prep
%setup -q -n DateTime-Format-Flexible-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} %{buildroot}/*

%check
%if %{with perl_DateTime_Format_Flexible_enables_extra_test}
export TEST_POD=1
%else
export TEST_POD=0
%endif
make test

%files
%doc --no-dereference LICENSE
%doc Changes example/ README TODO
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1_1
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_1
- update to new release by fcimport

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_1
- update to new release by fcimport

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_2
- update to new release by fcimport

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_1
- update to new release by fcimport

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_2
- update to new release by fcimport

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2_2
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2_1
- moved to Sisyphus (Tapper dep)

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- fc import

