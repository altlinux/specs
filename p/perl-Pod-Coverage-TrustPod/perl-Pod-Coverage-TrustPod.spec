Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-Coverage-TrustPod
Version:        0.100003
Release:        alt1_5
Summary:        Allow a module's pod to contain Pod::Coverage hints
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Pod-Coverage-TrustPod/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Pod-Coverage-TrustPod-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Pod/Coverage/CountParents.pm)
BuildRequires:  perl(Pod/Eventual/Simple.pm)
BuildRequires:  perl(Pod/Find.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Carp/Heavy.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Explicit dependencies:

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

%prep
%setup -q -n Pod-Coverage-TrustPod-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/Pod/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_1
- update to new release by fcimport

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt2_5
- update to new release by fcimport

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt2_4
- sisyphus release

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_1
- fc import

