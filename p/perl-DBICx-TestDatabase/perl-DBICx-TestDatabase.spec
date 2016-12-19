# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBICx-TestDatabase 
Summary:        Create a temporary database from a DBIx::Class::Schema 
Version:        0.05
Release:        alt1_5
License:        GPL+ or Artistic 
Group:          Development/Other
Source0:        http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/DBICx-TestDatabase-%{version}.tar.gz
URL:            http://search.cpan.org/dist/DBICx-TestDatabase
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/MM_Unix.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Runtime
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(SQL/Translator.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl(base.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(ok.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
Requires:       perl(DBD/SQLite.pm) >= 1.29
Requires:       perl(SQL/Translator.pm)


Source44: import.info

%description
This module creates a temporary SQLite database, deploys your DBIC
schema, and then connects to it. This lets you easily test your DBIC
schema. Since you have a fresh database for every test, you don't have
to worry about cleaning up after your tests, ordering of tests affecting
failure, etc.


%prep
%setup -q -n DBICx-TestDatabase-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_6
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- fc import

