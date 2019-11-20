Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Manifest/Skip.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Module-Install-ManifestSkip
Version:        0.24
Release:        alt2_15
Summary:        Generate a MANIFEST.SKIP file
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Install-ManifestSkip
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Install-ManifestSkip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Module/Install/Base.pm)
# Module::Manifest::Skip 0.18 not used at test-time
# Tests:
# inc::Module::Install not used, the t/sample1 is used by xt tests only
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Module/Manifest/Skip.pm) >= 0.180
Requires:       perl(warnings.pm)
Source44: import.info

%description
This module generates a MANIFEST.SKIP file for you (using
Module::Manifest::Skip) that contains the common files that people do not
want in their MANIFEST files. The SKIP file is generated each time that you
(the module author) run Makefile.PL.

%prep
%setup -q -n Module-Install-ManifestSkip-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2_11
- update to new release by fcimport

* Fri Apr 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2_10
- to Sisyphus as perl-Dancer2 dep

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_9
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_8
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_7
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_6
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_5
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_4
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_2
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_3
- update to new release by fcimport

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_1
- fc import

