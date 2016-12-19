# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(YAML.pm) perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-CPAN-Meta-YAML
Version:	0.25
Release:	alt1_5
Summary:	Validate a META.yml file within a CPAN distribution
Group:		Development/Other
License:	Artistic 2.0
URL:		http://search.cpan.org/dist/Test-CPAN-Meta-YAML/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BA/BARBIE/Test-CPAN-Meta-YAML-%{version}.tar.gz
Patch0:		Test-CPAN-Meta-YAML-0.25-utf8.patch
BuildArch:	noarch
# Module Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/YAML/Valid.pm)
BuildRequires:	perl(vars.pm)
BuildRequires:	perl(warnings.pm)
BuildRequires:	perl(YAML/Syck.pm)
# Test Suite
BuildRequires:	perl(IO/File.pm)
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/More.pm)
# Optional Tests
BuildRequires:	perl(Test/CPAN/Meta/JSON.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
# Runtime
# Explicitly requests the YAML::Syck backend for Test::YAML::Valid
Requires:	perl(YAML/Syck.pm)
Source44: import.info

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of ExtUtils::MakeMaker,
Module::Build and Module::Install.

See CPAN::Meta for further details of the CPAN Meta Specification.

%prep
%setup -q -n Test-CPAN-Meta-YAML-%{version}

# Recode documentation as UTF-8
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
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_3
- update to new release by fcimport

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2_3
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_3
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_1
- fc import

