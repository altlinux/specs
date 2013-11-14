# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Attribute/Handlers.pm) perl(B.pm) perl(B/Utils.pm) perl(Devel/Peek.pm) perl(FindBin.pm) perl(Glib.pm) perl(POSIX.pm) perl(Package/Constants.pm) perl(Pod/Simple/HTML.pm) perl(Smart/Comments.pm) perl(Sub/Identify.pm) perl(base.pm) perl(constant.pm) perl(constant/lexical.pm) perl(lib/abs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-constant-defer
Version:        5
Release:        alt2_6
Summary:        Constant subs with deferred value calculation
License:        GPLv3+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/constant-defer/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
# The inc/my_pod2html is not called
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(lib.pm)
# Run-Time:
BuildRequires:  perl(Carp.pm)
# Tests:
BuildRequires:  perl(Devel/FindRef.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/More.pm)
# Optionals tests:
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Devel/StackTrace.pm)
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
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING examples README
%{perl_vendor_privlib}/*

%changelog
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

