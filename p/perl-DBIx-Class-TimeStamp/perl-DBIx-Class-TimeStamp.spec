Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Class-TimeStamp
Version:        0.14
Release:        alt2_16
Summary:        DBIx::Class extension to update and create date and time based fields
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBIx-Class-TimeStamp/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/DBIx-Class-TimeStamp-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(CPAN.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(ExtUtils/MM_Unix.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/DynamicDefault.pm)
BuildRequires:  perl(DBIx/Class/InflateColumn/DateTime.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl(Class/Accessor/Grouped.pm)
BuildRequires:  perl(Data/Dump.pm)
BuildRequires:  perl(DateTime/Format/MySQL.pm)
BuildRequires:  perl(DateTime/Format/SQLite.pm)
BuildRequires:  perl(DBIx/Class/Core.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Builder/Module.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Time/Warp.pm)
# Optional tests only
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Requires:       perl(DateTime.pm) >= 0.55
Requires:       perl(DBIx/Class.pm) >= 0.080.090
Requires:       perl(DBIx/Class/DynamicDefault.pm) >= 0.03
Requires:       perl(DBIx/Class/InflateColumn/DateTime.pm)



Source44: import.info
%filter_from_requires /^perl\\(DateTime.pm\\)$/d
%filter_from_requires /^perl\\(DBIx.Class.pm\\)$/d

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
%setup -q -n DBIx-Class-TimeStamp-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_9
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_8
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_5
- fc import

