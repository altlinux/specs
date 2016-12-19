# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Safe-Isa
Version:        1.000006
Release:        alt1_1
Summary:        Call isa, can, does and DOES safely on things that may not be objects
Group:          Development/Other
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Safe-Isa/
Source0:        http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Dependencies

%description
This module allows you to call isa, can, does and DOES safely on things that
may not be objects, without the risk of crashing.

%prep
%setup -q -n Safe-Isa-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Safe/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1_1
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1_1
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.000005-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_2
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.000003-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1_2
- update to new release by fcimport

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1_1
- new version

