# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Attribute/Handlers.pm) perl(B/Utils.pm) perl(Devel/FindRef.pm) perl(Glib.pm) perl(Package/Constants.pm) perl(Pod/Simple/HTML.pm) perl(Smart/Comments.pm) perl(Sub/Identify.pm) perl(constant/lexical.pm) perl(lib/abs.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-constant-defer
Version:        6
Release:        alt2_5
Summary:        Constant subs with deferred value calculation
License:        GPLv3+
Group:          Development/Other
URL:            http://search.cpan.org/dist/constant-defer/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
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
# Optionals tests:
BuildRequires:  perl(Data/Dumper.pm)
# Devel::StackTrace not used
# Test::More not used
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
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc COPYING
%doc Changes examples README
%{perl_vendor_privlib}/*

%changelog
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

