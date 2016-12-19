# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-ConsistentVersion
Version:        0.3.0
Release:        alt1_5
Summary:        Ensures a CPAN distribution has consistent versioning
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-ConsistentVersion/
Source0:        http://www.cpan.org/authors/id/C/CE/CEBJYRE/Test-ConsistentVersion-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(autodie.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Pod/Content.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(English.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
# Needed for TEST_AUTHOR tests
BuildRequires:  perl(Test/Perl/Critic.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(Test/Pod/Content.pm)
Source44: import.info

%description
The purpose of this module is to make it easy for other distribution
authors to have consistent version numbers within the modules (as well as
readme file and changelog) of the distribution.

%prep
%setup -q -n Test-ConsistentVersion-v%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_AUTHOR=1 ./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/Test*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_1
- update to new release by fcimport

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_10
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_9
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt2_8
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_6
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_5
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_3
- fc import

