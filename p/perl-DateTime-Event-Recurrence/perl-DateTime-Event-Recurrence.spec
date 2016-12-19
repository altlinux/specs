# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Event-Recurrence
Version:        0.18
Release:        alt1_3
Summary:        DateTime::Set extension for create basic recurrence sets
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/DateTime-Event-Recurrence/
Source0:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-Recurrence-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
# Runtimea
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(DateTime/Span.pm)
BuildRequires:  perl(integer.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(DateTime/SpanSet.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(DateTime.pm) >= 0.27
Requires:       perl(DateTime/Set.pm) >= 0.360.0



Source44: import.info
%filter_from_requires /^perl\\(DateTime.pm\\)$/d
%filter_from_requires /^perl\\(DateTime.Set.pm\\)$/d

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep
%setup -q -n DateTime-Event-Recurrence-%{version}

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
%doc Changes CREDITS README TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_3
- update to new release by fcimport

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_24
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_18
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_17
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_17
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_15
- fc import

