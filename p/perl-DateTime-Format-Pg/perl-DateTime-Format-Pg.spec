# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-Pg
Version:        0.16012
Release:        alt1_2
Summary:        Parse and format PostgreSQL dates and times
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-Pg/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/DateTime-Format-Pg-%{version}.tar.gz
# Support durations with fractional seconds again, bug #1377428,
# <https://github.com/lestrrat/DateTime-Format-Pg/issues/12>, in upstream
# after 0.16012
Patch0:         DateTime-Format-Pg-0.16012-Fix-parse_duration-handling.patch
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Duration.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(DateTime/TimeZone.pm)
BuildRequires:  perl(DateTime/TimeZone/Floating.pm)
BuildRequires:  perl(DateTime/TimeZone/UTC.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
# Optional tests only
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create DateTime or DateTime::Duration objects, and it can take
a DateTime or DateTime::Duration object and produce a string representing
it in a format accepted by PostgreSQL.

%prep
%setup -q -n DateTime-Format-Pg-%{version}
%patch0 -p1

%build
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc LICENSE
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.16012-alt1_2
- new version

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.16011-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16011-alt1_1
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.16010-alt1_6
- update to new release by fcimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.16010-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.16009-alt1
- regenerated from template by package builder

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_1
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_2
- fc import

