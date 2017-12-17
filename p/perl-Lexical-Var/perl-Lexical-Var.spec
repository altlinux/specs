# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Lexical-Var
Version:        0.009
Release:        alt2_13.1
Summary:        Static variables without name space pollution
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Lexical-Var/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Lexical-Var-%{version}.tar.gz
# Update code to work with Perl 5.21.x (CPAN RT#101058)
Patch0:         Lexical-Var-0.009-Fix-RT-101058.patch
BuildRequires:  perl-devel >= 0:5.006
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-Time
BuildRequires:  perl(Lexical/SealRequireHints.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests
#BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Conflicts:      perl(B/Hooks/OP/Check.pm) < 0.190


Source44: import.info

%description
This module implements lexical scoping of static variables and subroutines.
Although it can be used directly, it is mainly intended to be
infrastructure for modules that manage name spaces.

%prep
%setup -q -n Lexical-Var-%{version}
%patch0 -p1

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Lexical*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_13.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_10
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_9.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_9
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_8
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_7.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_7
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_4.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_2
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt2_1
- Sisyphus build

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.008-alt2_1
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_5
- update to new release by fcimport

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_4
- update from fc import

