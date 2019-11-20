Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Attribute/Handlers.pm) perl(B/Utils.pm) perl(Devel/FindRef.pm) perl(Glib.pm) perl(Package/Constants.pm) perl(Pod/Simple/HTML.pm) perl(Smart/Comments.pm) perl(Sub/Identify.pm) perl(constant/lexical.pm) perl(lib/abs.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform optional tests
%bcond_without perl_constant_defer_enables_optional_test

Name:           perl-constant-defer
Version:        6
Release:        alt2_15
Summary:        Constant subs with deferred value calculation
License:        GPLv3+
URL:            https://metacpan.org/release/constant-defer
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
# The inc/my_pod2html is not called
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
# Run-Time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(vars.pm)
# Tests:
# Devel::FindRef not used
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test.pm)
%if %{with perl_constant_defer_enables_optional_test}
# Optionals tests:
BuildRequires:  perl(Data/Dumper.pm)
# Devel::StackTrace not used
# Test::More not used
%endif
Requires:       perl(Carp.pm)
Source44: import.info

%description
constant::defer creates a subroutine which on the first call runs given
code to calculate its value, and on the second and subsequent calls just
returns that value, like a constant. The value code is discarded once run,
allowing it to be garbage collected.

%prep
%setup -q -n constant-defer-%{version}
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc --no-dereference COPYING
%doc Changes examples README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 6-alt2_15
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 6-alt2_10
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 6-alt2_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 6-alt2_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 6-alt2_6
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 6-alt2_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 6-alt2_4
- update to new release by fcimport

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 6-alt2_3
- dropped BR: perl(Devel/FindRef.pm)

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 6-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 6-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 6-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_7
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt2_6
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_1
- fc import

