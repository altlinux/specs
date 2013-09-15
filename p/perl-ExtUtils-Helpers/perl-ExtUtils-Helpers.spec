# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# We don't really need Text::ParseWords a.. 3.24
%global old_tpw %(perl -MText::ParseWords -e 'print (($Text::ParseWords::VERSION) < 3.24 ? 1 : 0);' 2>/dev/null || echo 0)

# Test suite needs patching if we have Test::More < 0.88
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION) < 0.88 ? 1 : 0);' 2>/dev/null || echo 0)

Name:		perl-ExtUtils-Helpers
Version:	0.021
Release:	alt2_4
Summary:	Various portability utilities for module builders
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/ExtUtils-Helpers
Source0:	http://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Helpers-%{version}.tar.gz
Patch2:		ExtUtils-Helpers-0.016-old-Text::ParseWords.patch
Patch3:		ExtUtils-Helpers-0.021-old-Test::More.patch
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Copy.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(Module/Load.pm)
BuildRequires:	perl(Text/ParseWords.pm)
# Test Suite
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
# Release Tests
# perl-Pod-Coverage-TrustPod -> perl-Pod-Eventual -> perl-Mixin-Linewise ->
#   perl-YAML-Tiny -> perl-Module-Build-Tiny -> perl-ExtUtils-Helpers
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
%endif
Source44: import.info
# Runtime

%description
This module provides various portable helper functions for module building
modules.

%prep
%setup -q -n ExtUtils-Helpers-%{version}

# We don't really need Text::ParseWords ≥ 3.24
%if %{old_tpw}
%patch2
%endif

# Test suite needs patching if we have Test::More < 0.88
%if %{old_test_more}
%patch3
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test AUTHOR_TESTING=1 RELEASE_TESTING=1

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/ExtUtils/

%changelog
* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_2
- update to new release by fcimport

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_1
- build for Sisyphus

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_1
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1_1
- initial fc import

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1_1
- initial fc import

