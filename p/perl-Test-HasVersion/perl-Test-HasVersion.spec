Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-HasVersion
Version:        0.014
Release:        alt1_13
Summary:        Check Perl modules have version numbers
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-HasVersion
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-HasVersion-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
# Module Runtime
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
# Optional Tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
Do you want to check that every one of your Perl modules in a distribution has
a version number? You want to make sure you don't forget the brand new modules
you just added? Well, this is the module you have been looking for.

Do you want to check someone else's distribution to make sure the author has
not committed the sin of leaving Perl modules without a version that can be
used to tell if you have this or that feature? Test::HasVersion is also for
you.

%prep
%setup -q -n Test-HasVersion-%{version}

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
%doc --no-dereference LICENSE
%doc Changes README
%{_bindir}/test_version
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_13
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1_2
- update to new release by fcimport

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_10
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_9
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_4
- fc import

