# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-XSD
Version:        0.2
Release:        alt2_12
Summary:        Format DateTime according to xsd:dateTime
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-XSD/
Source0:        http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-XSD-%{version}.tar.gz
BuildArch:      noarch
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
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

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

