Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Set-Scalar
Version:        1.29
Release:        alt1_15
Summary:        Basic set operations
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Set-Scalar
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Test Suite
BuildRequires:  perl(Carp.pm)
Source44: import.info
# Dependencies

%description
%{summary}.

%prep
%setup -q -n Set-Scalar-%{version}

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
%doc ChangeLog README README.old
%{perl_vendor_privlib}/Set/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_10
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1_1
- update to new release by fcimport

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Fri Feb 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Sat Nov 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt2_11
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_8
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_6
- fc import

