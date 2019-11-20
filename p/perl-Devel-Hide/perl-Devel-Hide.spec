Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/CoreList.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_Devel_Hide_enables_optional_test
%else
%bcond_with perl_Devel_Hide_enables_optional_test
%endif

Name:           perl-Devel-Hide
Version:        0.0010
Release:        alt1_6
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-Hide
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Devel-Hide-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module Runtime
# File::Temp not used on perl >= 5.008
BuildRequires:  perl(lib.pm)
# Module::CoreList is used from a private subroutine that is never called
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
%if %{with perl_Devel_Hide_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Source44: import.info
# Dependencies

%description
Given a list of Perl modules/filenames, this module makes require and use
statements fail (regardless of whether the specified files/modules are
installed or not).

%prep
%setup -q -n Devel-Hide-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Devel/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.0010-alt1_6
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.0010-alt1_2
- update to new release by fcimport

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.0010-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_10
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_9
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_2
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_13
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt1_9
- fc import

