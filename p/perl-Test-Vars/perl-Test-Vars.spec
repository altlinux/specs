# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-Vars
Version:	0.005
Release:	alt2_4
Summary:	Detects unused variables
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-Vars/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Test-Vars-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Build requirements
# ===================================================================
BuildRequires:	perl(Module/Build.pm)
BuildRequires:	perl(CPAN/Meta.pm)
BuildRequires:	perl(CPAN/Meta/Prereqs.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(utf8.pm)
BuildRequires:	perl(warnings.pm)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl
BuildRequires:	perl(B.pm)
BuildRequires:	perl(constant.pm)
BuildRequires:	perl(ExtUtils/Manifest.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(Symbol.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
# ===================================================================
# Test suite requirements
# ===================================================================
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/More.pm)
# ===================================================================
# Author/Release test requirements
# ===================================================================
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Synopsis.pm)
Source44: import.info
# ===================================================================
# Runtime requirements
# ===================================================================

%description
Test::Vars finds unused variables in order to keep the source code tidy.

%prep
%setup -q -n Test-Vars-%{version}

# Placate rpmlint about script interpreters in examples
sed -i -e '1s|^#!perl|#!/usr/bin/perl|' example/*.t

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}

%check
./Build test
./Build test --test_files="xt/*.t"

%files
%doc Changes LICENSE README.md example/
%{perl_vendor_privlib}/Test/

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_4
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_3
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_1
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_3
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_2
- update to new release by fcimport

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2_3
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1_3
- fc import

