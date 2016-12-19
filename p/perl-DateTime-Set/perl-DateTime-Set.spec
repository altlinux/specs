# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Set
Version:        0.3900
Release:        alt1_1
Summary:        Datetime sets and set math
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/DateTime-Set/
Source0:        http://www.cpan.org/authors/id/F/FG/FGLOCK/DateTime-Set-%{version}.tar.gz
Patch0:         DateTime-Set-0.32-version.patch
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Duration.pm)
BuildRequires:  perl(DateTime/Infinite.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(Set/Infinite.pm)
BuildRequires:  perl(vars.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info

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
./Build install destdir="%{buildroot}" create_packlist=0
# %{_fixperms} %{buildroot}

%check
./Build test

%files
%doc LICENSE
%doc Changes README TODO
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.3900-alt1_1
- update to new release by fcimport

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.3900-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.3800-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3600-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.3600-alt1_1
- update to new release by fcimport

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.3600-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3400-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3400-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3400-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.3400-alt1_1
- update to new release by fcimport

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.3400-alt1
- automated CPAN update

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1_1
- update to new release by fcimport

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

