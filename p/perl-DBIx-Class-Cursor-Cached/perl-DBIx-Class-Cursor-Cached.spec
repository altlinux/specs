# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Class-Cursor-Cached
Version:        1.001002
Release:        alt3_11
Summary:        Cursor class with built-in caching support
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DBIx-Class-Cursor-Cached/
Source0:        http://www.cpan.org/authors/id/A/AR/ARCANEZ/DBIx-Class-Cursor-Cached-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Cache/FileCache.pm)
BuildRequires:  perl(Carp/Clan.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/Core.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Carp/Clan.pm) >= 6.0
Requires:       perl(DBIx/Class.pm) >= 0.081.240

%{echo 
%filter_from_requires /perl.Carp.Clan.pm.$/d
}


Source44: import.info

%description
This module provides a DBIx cursor class with built-in caching support.

%prep
%setup -q -n DBIx-Class-Cursor-Cached-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt3_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt3_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt3_7
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt3_6
- moved to Sisyphus as dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt2_6
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt2_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.001002-alt1_2
- fc import

