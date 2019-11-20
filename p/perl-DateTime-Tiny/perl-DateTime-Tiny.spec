Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Tiny
Version:        1.07
Release:        alt1_6
Summary:        Date object, with as little code as possible
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/DateTime-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(overload.pm)
# Tests
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
Requires:       perl(Carp.pm)
Requires:       perl(DateTime.pm)
Source44: import.info

%description
DateTime::Tiny implements an extremely lightweight object that represents a
datetime.

%prep
%setup -q -n DateTime-Tiny-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README CONTRIBUTING.mkdn
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_6
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_2
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_1
- update to new release by fcimport

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_2
- update to new release by fcimport

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_1
- to Sisyphus

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_9
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_3
- initial fc import

