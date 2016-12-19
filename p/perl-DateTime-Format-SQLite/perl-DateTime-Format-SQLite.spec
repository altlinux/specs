Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/SQLite.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-SQLite 
Summary:        Parse and format SQLite dates and times 
Version:        0.11
Release:        alt2_19
License:        GPL+ or Artistic 
Source0:        http://search.cpan.org/CPAN/authors/id/C/CF/CFAERBER/DateTime-Format-SQLite-%{version}.tar.gz
URL:            http://search.cpan.org/dist/DateTime-Format-SQLite/
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime/Format/Builder.pm) >= 0.6


Source44: import.info
%filter_from_requires /^perl\\(DateTime.Format.Builder.pm\\)$/d

%description
This module understands the formats used by SQLite for its 'date',
'datetime' and 'time' functions. It can be used to parse these formats
in order to create the DateTime manpage objects, and it can take a
DateTime object and produce a timestring accepted by SQLite.*NOTE:*
SQLite does not have real date/time types but stores everything as
strings. This module deals with the date/time strings as
understood/returned by SQLite's 'date', 'time', 'datetime', 'julianday'
and 'strftime' SQL functions. You will usually want to store your dates
in one of these formats.

%prep
%setup -q -n DateTime-Format-SQLite-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_19
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_16
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_10
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_9
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_9
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- fc import

