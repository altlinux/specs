# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-DateManip
Version:        0.04
Release:        alt2_22
Summary:        Convert Date::Manip to DateTime and vice versa
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/DateTime-Format-DateManip/
Source0:        http://www.cpan.org/authors/id/B/BB/BBENNETT/dt-fmt-datemanip/DateTime-Format-DateManip-%{version}.tar.gz
# Use full time zone name instead of an ambiguous abbreviation, CPAN RT#55771
Patch0:         DateTime-Format-DateManip-01conversion.patch
# Pass test with Date-Manip-6.49, bug #1199969, CPAN RT#102670
Patch1:         DateTime-Format-DateManip-0.04-Set-system-time-zone-in-test.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
# Run-time
BuildRequires:  perl(bytes.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Date/Manip.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Duration.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
DateTime::Format::DateManip is a class that knows how to convert between
Date::Manip dates and durations and DateTime and DateTime::Duration
objects. Recurrences are note yet supported.

%prep
%setup -q -n DateTime-Format-DateManip-%{version}
%patch0 -p1
%patch1 -p1

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
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_22
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_20
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_13
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_10
- fc import

