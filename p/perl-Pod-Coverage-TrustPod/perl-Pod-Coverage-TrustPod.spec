%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Pod-Coverage-TrustPod
Version:        0.100006
Release:        alt1
Summary:        Allow a module's pod to contain Pod::Coverage hints
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Coverage-TrustPod
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Pod-Coverage-TrustPod-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
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
BuildRequires:  perl(File/Spec.pm)
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
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Pod/

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.100006-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.100005-alt1_7
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.100005-alt1_2
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.100005-alt1_1
- update to new release by fcimport

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.100005-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.100004-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.100003-alt1_6
- update to new release by fcimport

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

