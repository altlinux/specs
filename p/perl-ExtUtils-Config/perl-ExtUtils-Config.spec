# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
# Test suite needs patching if we have Test::More < 0.88
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION) < 0.88 ? 1 : 0);' 2>/dev/null || echo 0)

Name:		perl-ExtUtils-Config
Version:	0.008
Release:	alt1_6
Summary:	A wrapper for perl's configuration
Group:		Development/Other
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/ExtUtils-Config
Source0:	http://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Config-%{version}.tar.gz
Patch1:		ExtUtils-Config-0.008-old-Test::More.patch
BuildArch:	noarch
# Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Data/Dumper.pm)
# Test Suite
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
Source44: import.info
# Runtime

%description
ExtUtils::Config is an abstraction around the %%Config hash.

%prep
%setup -q -n ExtUtils-Config-%{version}

# Test suite needs patching if we have Test::More < 0.88
%if %{old_test_more}
%patch1
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/ExtUtils/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_2
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_5
- update to new release by fcimport

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_3
- converted for ALT Linux by srpmconvert tools

