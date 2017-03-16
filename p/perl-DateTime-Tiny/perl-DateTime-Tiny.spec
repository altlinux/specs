# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DateTime.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Tiny
Version:        1.06
Release:        alt2_2
Summary:        Date object, with as little code as possible
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/DateTime-Tiny/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/DateTime-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime.pm)

%description
DateTime::Tiny implements an extremely lightweight object that represents a
datetime.

%prep
%setup -q -n DateTime-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README CONTRIBUTING.mkdn
%doc LICENSE
%{perl_vendor_privlib}/*

%changelog
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

