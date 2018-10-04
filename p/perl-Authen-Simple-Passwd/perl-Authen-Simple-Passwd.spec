Name:           perl-Authen-Simple-Passwd
Version:        0.6
Release:        alt2
Summary:        Simple Passwd authentication
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/Authen-Simple-Passwd
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-Passwd-%{version}.tar.gz
BuildArch:      noarch

BuildRequires(pre): rpm-build-perl
BuildRequires:  perl(Authen/Simple.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Params/Validate.pm)

# Required by the tests
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)

# For improved tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)

%description
Authenticate against a passwd file.

%prep
%setup -q -n Authen-Simple-Passwd-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%check
TEST_POD=1 ./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.6-alt2
- Initial build for Sisyphus.

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_22
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_21
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_20
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_19
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_18
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_17
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_16
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_15
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_13
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_10
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_6
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4
- fc import

