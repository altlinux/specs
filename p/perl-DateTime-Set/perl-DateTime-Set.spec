# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Set
Version:        0.33
Release:        alt1
Summary:        Datetime sets and set math
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Set/
Source:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Set-%{version}.tar.gz
Patch0:         DateTime-Set-0.32-version.patch
BuildArch:      noarch
# Build
BuildRequires:  perl(Module/Build.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime/Duration.pm)
BuildRequires:  perl(DateTime/Infinite.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Set/Infinite.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Test Suite
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
# Optional Tests
# DateTime::Event::Recurrence requires DateTime::Set itself
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(DateTime/Event/Recurrence.pm)
%endif
Source44: import.info
# Runtime

%description
DateTime::Set is a module for datetime sets. It can be used to handle two
different types of sets. The first is a fixed set of predefined datetime
objects. For example, if we wanted to create a set of datetimes containing
the birthdays of people in our family. The second type of set that it can
handle is one based on the idea of a recurrence, such as "every Wednesday",
or "noon on the 15th day of every month". This type of set can have fixed
starting and ending datetimes, but neither is required. So our "every
Wednesday set" could be "every Wednesday from the beginning of time until
the end of time", or "every Wednesday after 2003-03-05 until the end of
time", or "every Wednesday between 2003-03-05 and 2004-01-07".

%prep
%setup -q -n DateTime-Set-%{version}

# Make perl/rpm version comparisons work the same way
%patch0

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes LICENSE README TODO
%{perl_vendor_privlib}/DateTime/
%{perl_vendor_privlib}/Set/

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1_1
- update to new release by fcimport

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_12
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_11
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_11
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_9
- fc import

