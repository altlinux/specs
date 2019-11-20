Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Test-Vars
Version:	0.014
Release:	alt1_13
Summary:	Detects unused variables
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-Vars
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Vars-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	perl-devel >= 5.10.0
BuildRequires:	rpm-build-perl
BuildRequires:	perl(Module/Build/Tiny.pm)
BuildRequires:	sed
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(B.pm)
BuildRequires:	perl(constant.pm)
BuildRequires:	perl(ExtUtils/Manifest.pm)
BuildRequires:	perl(IO/Pipe.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(Storable.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Symbol.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
BuildRequires:	perl(warnings.pm)
# ===================================================================
# Test suite requirements
# ===================================================================
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
# ===================================================================
# Optional test requirements
# ===================================================================
%if !0%{?rhel:1} && !0%{?perl_bootstrap:1}
BuildRequires:	perl(Moose/Role.pm)
%endif
BuildRequires:	perl(Test/Output.pm)
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
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} -c %{buildroot}

%check
./Build test
prove -Ilib $(echo $(find xt/ -name '*.t'))

%files
%if 0%{?_licensedir:1}
%doc --no-dereference LICENSE
%else
%doc LICENSE
%endif
%doc Changes README.md example/
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_13
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_3
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_2
- update to new release by fcimport

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_5
- update to new release by fcimport

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

