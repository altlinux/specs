# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/mysql.pm) perl(Pod/Coverage/TrustPod.pm) perl(SQL/Statement.pm) perl(Test/CPAN/Meta.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Database
Version:        1.113
Release:        alt1_5
Summary:        Database handles ready for testing
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-Database/
Source0:        http://www.cpan.org/authors/id/B/BO/BOOK/Test-Database-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(DBD/DBM.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(YAML/Tiny.pm)
# Recommended run-time:
# DBD::CSV 0.30 not used at tests
BuildRequires:  perl(DBD/SQLite.pm)
# Tests:
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(List/Util.pm)
# Pod::Coverage::TrustPod not used
# SQL::Statement not needed
# Test::CPAN::Meta not used
BuildRequires:  perl(Test/More.pm)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(YAML/Tiny.pm) >= 1.62


# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(YAML.Tiny.pm\\)$/d

%description
Test::Database Perl module provides a simple way for test authors to request
a test database, without worrying about environment variables or the test host
configuration.

%prep
%setup -q -n Test-Database-%{version}
rm -f t/pod.t

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes eg LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.113-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.113-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.113-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.113-alt1_1
- update to new release by fcimport

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.113-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.112-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt3_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt3_6
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt3_5
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_3
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_3
- fc import

