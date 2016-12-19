Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-ICal
Version:        0.09
Release:        alt2_22
Summary:        Parse and format iCal datetime and duration strings
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DateTime-Format-ICal/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ICal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
# Runtime
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Event/ICal.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(DateTime/Span.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DateTime.pm) >= 0.17
Requires:       perl(DateTime/Event/ICal.pm) >= 0.03
Requires:       perl(DateTime/Set.pm) >= 0.1
Requires:       perl(DateTime/TimeZone.pm) >= 0.22
Requires:       perl(Params/Validate.pm) >= 0.59




Source44: import.info
%filter_from_requires /^perl\\(DateTime.pm\\)$/d
%filter_from_requires /^perl\\(DateTime.Event.ICal.pm\\)$/d
%filter_from_requires /^perl\\(Params.Validate.pm\\)$/d

%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep
%setup -q -n DateTime-Format-ICal-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc LICENSE
%doc Changes TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_22
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_13
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_12
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_10
- fc import

