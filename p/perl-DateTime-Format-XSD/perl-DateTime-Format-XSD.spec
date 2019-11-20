Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Format-XSD
Version:        0.2
Release:        alt2_22
Summary:        Format DateTime according to xsd:dateTime
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Format-XSD
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-XSD-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(DateTime/Format/ISO8601.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime/Format/ISO8601.pm)

#Not autodetermined.
Provides:       perl(DateTime/Format/XSD.pm) = %{version}
Source44: import.info

%description
XML Schema defines a usage profile which is a subset of the ISO8601
profile. This profile defines that
  'YYYY-MM-DD"T"HH:MI:SS(Z|[+-]zh:zm)' 
is the only possible representation for a dateTime, despite 
all other options ISO provides.

%prep
%setup -q -n DateTime-Format-XSD-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_22
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_11
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_5
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_4
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_2
- fc import

