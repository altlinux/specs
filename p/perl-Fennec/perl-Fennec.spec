Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Fennec
Version:	2.018
Release:	alt3_14
Summary:	A tester's toolbox, and best friend
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Fennec
Source0:	http://cpan.metacpan.org/authors/id/E/EX/EXODIST/Fennec-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(Module/Build.pm)
# Module Runtime
BuildRequires:	perl(B.pm)
BuildRequires:	perl(base.pm)
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Child.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Exporter/Declare.pm)
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(Mock/Quick.pm)
BuildRequires:	perl(Parallel/Runner.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/Exception.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Simple.pm)
BuildRequires:	perl(Test/Warn.pm)
BuildRequires:	perl(utf8.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(Data/Dumper.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(Test/Pod.pm)
# Runtime
Requires:	perl(Child.pm) >= 0.010
Requires:	perl(Mock/Quick.pm) >= 1.106
Requires:	perl(Test/Exception.pm) >= 0.290
Requires:	perl(Test/More.pm) >= 0.880
Requires:	perl(Test/Warn.pm)
Requires:	perl(utf8.pm)
Source44: import.info

%description
Fennec ties together several testing-related modules and enhances their
functionality in ways you don't get loading them individually. Fennec
makes testing easier, and more useful.

This module is deprecated in favor of Test2::Suite, specifically
Test2::Tools::Spec and Test2::Bundle::SpecDeclare.

%prep
%setup -q -n Fennec-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc CHANGES README
%{perl_vendor_privlib}/Fennec.pm
%dir %{perl_vendor_privlib}/Fennec/
%{perl_vendor_privlib}/Fennec/Collector.pm
%{perl_vendor_privlib}/Fennec/Collector/
%{perl_vendor_privlib}/Fennec/EndRunner.pm
%{perl_vendor_privlib}/Fennec/Finder.pm
%doc %{perl_vendor_privlib}/Fennec/Manual.pod
%dir %{perl_vendor_privlib}/Fennec/Manual/
%doc %{perl_vendor_privlib}/Fennec/Manual/CustomFennec.pod
%{perl_vendor_privlib}/Fennec/Meta.pm
%{perl_vendor_privlib}/Fennec/Runner.pm
%{perl_vendor_privlib}/Fennec/Test.pm
%{perl_vendor_privlib}/Fennec/Util.pm
%{perl_vendor_privlib}/Test/

%changelog
* Tue Jul 12 2022 Igor Vlasenko <viy@altlinux.org> 2.018-alt3_14
- to Sisyphus as perl-Sub-HandlesVia build dep

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 2.018-alt2_14
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 2.018-alt2_13
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 2.018-alt2_12
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 2.018-alt2_11
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 2.018-alt2_10
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 2.018-alt2_9
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_9
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_8
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_7
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_6
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_5
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_4
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_3
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_2
- update to new release by fcimport

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.018-alt1_1
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_10
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_9
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_8
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_7
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_6
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_3
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.017-alt1_2
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.016-alt1_1
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.013-alt1_1
- update to new release by fcimport

* Tue Dec 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.012-alt1_1
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.011-alt1_1
- update to new release by fcimport

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 2.010-alt1_3
- fc import

