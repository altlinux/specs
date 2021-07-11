Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/XML/XPathEngine.pm
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform optional tests
%bcond_without perl_XML_XPathEngine_enables_optional_test

Name:           perl-XML-XPathEngine
Version:        0.14
Release:        alt3_22
Summary:        Re-usable XPath engine for DOM-like trees
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XML-XPathEngine
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-XPathEngine-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(overload.pm)
# POSIX not used in tests
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
%if %{with perl_XML_XPathEngine_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Requires:       perl(POSIX.pm)
Source44: import.info

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

%prep
%setup -q -n XML-XPathEngine-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt3_22
- to Sisyphus as perl-Finance-Quote dep

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt2_22
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt2_21
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_20
- update to new release by fcimport

* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_20
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_19
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_18
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_17
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_16
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_15
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_14
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_13
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_10
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_9
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_8
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_6
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_3
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_12
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_10
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_8
- fc import

