# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-YAML-Meta
Version:        0.22
Release:        alt1_5
Summary:        Validation of the META.yml file in a distribution
License:        Artistic 2.0
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-YAML-Meta/
Source0:        http://www.cpan.org/modules/by-module/Test/Test-YAML-Meta-%{version}.tar.gz
Patch0:         Test-YAML-Meta-0.21-utf8.patch
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/CPAN/Meta/YAML.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Test/CPAN/Meta/JSON.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of
ExtUtils::MakeMaker, Module::Build and Module::Install.

%prep
%setup -q -n Test-YAML-Meta-%{version}

# Re-code LICENSE as UTF-8
%patch0

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test AUTOMATED_TESTING=1

%files
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes README examples/
%{perl_vendor_privlib}/Test/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_1
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_2
- fc import

