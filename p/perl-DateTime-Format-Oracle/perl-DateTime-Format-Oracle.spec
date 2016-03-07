# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-Oracle
Version:        0.06
Release:        alt2_11
Summary:        Parse and format Oracle dates and timestamps
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-Oracle/
Source0:        http://www.cpan.org/authors/id/K/KO/KOLIBRIE/DateTime-Format-Oracle-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Convert/NLS_DATE_FORMAT.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module may be used to convert Oracle date and timestamp values into
DateTime objects. It also can take a DateTime object and produce a date
string matching the NLS_DATE_FORMAT.

%prep
%setup -q -n DateTime-Format-Oracle-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_4
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- fc import

