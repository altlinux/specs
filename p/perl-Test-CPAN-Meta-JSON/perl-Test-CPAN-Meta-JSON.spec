# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-CPAN-Meta-JSON
Version:	0.16
Release:	alt1_5
Summary:	Validate a META.json file within a CPAN distribution
Group:		Development/Other
License:	Artistic 2.0
URL:		http://search.cpan.org/dist/Test-CPAN-Meta-YAML/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BA/BARBIE/Test-CPAN-Meta-JSON-%{version}.tar.gz
Patch0:		Test-CPAN-Meta-JSON-0.16-utf8.patch
BuildArch:	noarch
# Module Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(IO/File.pm)
BuildRequires:	perl(JSON.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(vars.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/More.pm)
# Optional Tests
BuildRequires:	perl(Test/CPAN/Meta.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
This module was written to ensure that a META.json file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%prep
%setup -q -n Test-CPAN-Meta-JSON-%{version}

# Recode LICENSE as UTF-8
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
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_3
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_2
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- fc import

