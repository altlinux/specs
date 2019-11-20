Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DBIx-Class-Cursor-Cached
Version:        1.001004
Release:        alt1_10
Summary:        Cursor class with built-in caching support
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-Class-Cursor-Cached
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARCANEZ/DBIx-Class-Cursor-Cached-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/AutoInstall.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(Carp/Clan.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(vars.pm)
# Tests
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Cache/FileCache.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/Core.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Carp/Clan.pm) >= 6.0
Requires:       perl(DBIx/Class.pm) >= 0.081.240



Source44: import.info
%filter_from_requires /perl(Carp.Clan.pm)/d

%description
This module provides a DBIx cursor class with built-in caching support.

%prep
%setup -q -n DBIx-Class-Cursor-Cached-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.001004-alt1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.001004-alt1_6
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.001004-alt1_5
- update to new release by fcimport

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.001004-alt1
- automated CPAN update

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

