Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Safe-Isa
Version:        1.000010
Release:        alt1_6
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Safe-Isa
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(UNIVERSAL.pm)
Source44: import.info
# Dependencies

%description
This module allows you to call isa, can, does and DOES safely on things that
may not be objects, without the risk of crashing.

%prep
%setup -q -n Safe-Isa-%{version}

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
%{perl_vendor_privlib}/Safe/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.000010-alt1_6
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.000010-alt1_2
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.000010-alt1_1
- update to new release by fcimport

* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.000010-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.000009-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.000008-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.000007-alt1_1
- update to new release by fcimport

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.000007-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1_2
- update to new release by fcimport

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

