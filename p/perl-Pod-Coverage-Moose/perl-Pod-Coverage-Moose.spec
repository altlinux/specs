Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Pod-Coverage-Moose
Version:        0.07
Release:        alt3
Summary:        Pod::Coverage extension for Moose
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Coverage-Moose
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Coverage-Moose-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Load.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(Pod/Coverage.pm)
# Tests:
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(if.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
# Optional Tests
BuildRequires:  perl(MooseX/AttributeHelpers.pm)
BuildRequires:  perl(MooseX/Role/WithOverloading.pm)
Source44: import.info
# Dependencies

%description
When using Pod::Coverage in combination with Moose, it will report any
method imported from a Role. This is especially bad when used in
combination with Test::Pod::Coverage, since it takes away its ease of use.

%prep
%setup -q -n Pod-Coverage-Moose-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc --no-dereference LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendor_privlib}/Pod/

%changelog
* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 0.07-alt3
- Rebuild by human.

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_23
- update to new release by fcimport

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_22
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_21
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_20
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_19
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_18
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_17
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2_16
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_16
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_15
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_14
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_13
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_12
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_11
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_10
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_9
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_7
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_5
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_13
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_11
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_10
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_9
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- fc import

