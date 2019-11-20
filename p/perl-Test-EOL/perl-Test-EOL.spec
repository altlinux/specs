Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Test-EOL
Version:	2.00
Release:	alt1_10
Summary:	Check the correct line endings in your project
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-EOL
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-EOL-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
# Optional Tests
%if "%{?rhel}" != "6"
BuildRequires:	perl(CPAN/Meta.pm)
%endif
Source44: import.info
# Dependencies

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) with Windows line endings. It can also check for trailing
whitespace.

%prep
%setup -q -n Test-EOL-%{version}

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
%doc --no-dereference LICENCE
%else
%doc LICENCE
%endif
%doc Changes CONTRIBUTING README
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_10
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_7
- fixed build

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_5
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_2
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_2
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_1
- moved to Sisyphus (Tapper dep)

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_6
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- fc import

