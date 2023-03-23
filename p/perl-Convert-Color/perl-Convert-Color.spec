%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(List/Util.pm) perl(Test2/V0.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Convert-Color
Version:        0.16
Release:        alt1
Summary:        Color space conversions and named lookups
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Convert-Color
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/Convert-Color-%{version}.tar.gz
# Workaround to a source-code trick, which break rpm's perl-module deptracking
Patch0:         Convert-Color-0.09.patch
BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(List/UtilsBy.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Number/Delta.pm)
# For improved testing
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  xorg-rgb
Source44: import.info


%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and HSV,
and it provides ways to look up colors by a name.

%prep
%setup -q -n Convert-Color-%{version}
%patch0 -p1

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples README
%{perl_vendor_privlib}/*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.16-alt1
- automated CPAN update

* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.14-alt1
- automated CPAN update

* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 0.13-alt1
- automated CPAN update

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_17
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_9
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_6
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_5
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_3
- fc import

