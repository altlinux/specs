Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-Identity
Version:        0.01
Release:        alt2_21
Summary:        Assert the referential identity of a reference
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Identity
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-Identity-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module provides a single testing function, identical. It asserts that
a given reference is as expected; that is, it either refers to the same
object or is undef. It is similar to Test::More::is except that it uses
refaddr, ensuring that it behaves correctly even if the references under
test are objects that overload stringification or numification.

%prep
%setup -q -n Test-Identity-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE 
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_21
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_13
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_7
- update to new release by fcimport

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_6
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_1
- fc import

