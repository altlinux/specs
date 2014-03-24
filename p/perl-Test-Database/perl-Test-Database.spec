%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/DBM.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Database
Version:        1.112
Release:        alt1
Summary:        Database handles ready for testing
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Database/
Source:        http://www.cpan.org/authors/id/B/BO/BOOK/Test-Database-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Pod/Coverage.pm)
BuildRequires:  perl(SQL/Statement.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(YAML/Tiny.pm)



Source44: import.info

%description
Test::Database provides a simple way for test authors to request a test
database, without worrying about environment variables or the test host
configuration.

%prep
%setup -q -n Test-Database-%{version}
#rm -f t/pod.t

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes eg README
%{perl_vendor_privlib}/*

%changelog
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

