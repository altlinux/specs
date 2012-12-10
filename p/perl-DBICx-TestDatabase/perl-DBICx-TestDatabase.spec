# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(DBIx/Class/Schema.pm) perl(Fcntl.pm) perl(FindBin.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBICx-TestDatabase 
Summary:        Create a temporary database from a DBIx::Class::Schema 
Version:        0.04
Release:        alt2_5
License:        GPL+ or Artistic 
Group:          Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/DBICx-TestDatabase-%{version}.tar.gz
URL:            http://search.cpan.org/dist/DBICx-TestDatabase
BuildArch:      noarch

BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(ok.pm)
BuildRequires:  perl(SQL/Translator.pm)
BuildRequires:  perl(Test/More.pm)

Requires:       perl(DBD/SQLite.pm) >= 1.29
Requires:       perl(SQL/Translator.pm)

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.04-3
Provides:       %{name}-tests = %{version}-%{release}


Source44: import.info

%description
This module creates a temporary SQLite database, deploys your DBIC
schema, and then connects to it. This lets you easily test your DBIC
schema. Since you have a fresh database for every test, you don't have
to worry about cleaning up after your tests, ordering of tests affecting
failure, etc.


%prep
%setup -q -n DBICx-TestDatabase-%{version}

# silence rpmlint warnings
find t/ -name '*.t' -type f -print0 \
  | xargs -0 sed -i '1s,#!.*perl,#!%{__perl},'

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'


%check
make test

%files
%doc README Changes t/
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- fc import

