Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-App-Cache
Summary:        Easy application-level caching
Version:        0.37
Release:        alt2_27
License:        GPL+ or Artistic

Source0:        https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/App-Cache-%{version}.tar.gz
URL:            https://metacpan.org/release/App-Cache

BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(Class/Accessor/Chained/Fast.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/stat.pm)
BuildRequires:  perl(HTTP/Cookies.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Path/Class.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)

Requires:       perl(Class/Accessor/Chained/Fast.pm)
Requires:       perl(File/Find/Rule.pm)
Requires:       perl(File/HomeDir.pm)
Requires:       perl(File/stat.pm)
Requires:       perl(HTTP/Cookies.pm)
Requires:       perl(LWP/UserAgent.pm)
Requires:       perl(Path/Class.pm)
Requires:       perl(Storable.pm)



%{?perl_default_subpackage_tests}
Source44: import.info

%description
The App::Cache module lets an application cache data locally. There are a
few times an application would need to cache data: when it is retrieving
information from the network or when it has to complete a large calculation.
For example, the Parse::BACKPAN::Packages module downloads a file off the
net and parses it, creating a data structure. Only then can it actually
provide any useful information for the programmer. Parse::BACKPAN::Packages
uses App::Cache to cache both the file download and data structures,
providing much faster use when the data is cached. This module stores data
in the home directory of the user, in a dot directory. For example, the
Parse::BACKPAN::Packages cache is actually stored underneath
"~/.parse_backpan_packages/cache/". This is so that permissions are not a
problem -- it is a per-user, per-application cache.

%prep
%setup -q -n App-Cache-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2_27
- update to new release by fcimport

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2_25
- to Sisyphus as dependency

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_25
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_24
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_23
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_21
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_20
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_19
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_18
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_17
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_16
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_13
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_11
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_10
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_8
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1_6
- fc import

