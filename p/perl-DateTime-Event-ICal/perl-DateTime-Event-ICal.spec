# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Event-ICal
Version:        0.11
Release:        alt1_1
Summary:        Perl DateTime extension for computing rfc2445 recurrences
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Event-ICal/
Source0:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Event/Recurrence.pm)
BuildRequires:  perl(DateTime/Set.pm)
BuildRequires:  perl(DateTime/Span.pm)
BuildRequires:  perl(DateTime/SpanSet.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Test suite
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Runtime

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for rfc2445 style recurrences.

%prep
%setup -q -n DateTime-Event-ICal-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes LICENSE README TODO
%{perl_vendor_privlib}/DateTime/

%changelog
* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_10
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_9
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_9
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7
- fc import

