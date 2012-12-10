# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/DBM.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Database
Version:        1.11
Release:        alt3_5
Summary:        Database handles ready for testing
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Database/
Source0:        http://www.cpan.org/authors/id/B/BO/BOOK/Test-Database-%{version}.tar.gz
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
rm -f t/pod.t

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
./Build test

%files
%doc Changes eg README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt3_5
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_3
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_3
- fc import

