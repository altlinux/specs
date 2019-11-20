Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Test-NoTabs
Version:	2.02
Release:	alt1_7
Summary:	Check the presence of tabs in your project
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-NoTabs
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-NoTabs-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(FindBin.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
# Optional Tests
%if "%{?rhel}" != "6"
BuildRequires:	perl(CPAN/Meta.pm)
%endif
Source44: import.info
# Runtime

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) for the presence of tabs.

%prep
%setup -q -n Test-NoTabs-%{version}

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
%if 0%{?_licensedir:1}
%doc --no-dereference LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_7
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_2
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_1
- update to new release by fcimport

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_2
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_6
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_7
- update to new release by fcimport

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_5
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- moved to Sisyphus (Tapper dep)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- fc import

