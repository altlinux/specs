# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-CPAN-Meta-JSON
Version:	0.15
Release:	alt2_2
Summary:	Validate a META.json file within a CPAN distribution
Group:		Development/Perl
License:	Artistic 2.0
URL:		http://search.cpan.org/dist/Test-CPAN-Meta-YAML/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BA/BARBIE/Test-CPAN-Meta-JSON-%{version}.tar.gz
Patch0:		Test-CPAN-Meta-JSON-0.15-utf8.patch
BuildArch:	noarch
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(IO/File.pm)
BuildRequires:	perl(JSON.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/CPAN/Meta.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info

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
%doc Changes LICENSE README examples/
%{perl_vendor_privlib}/Test/

%changelog
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

