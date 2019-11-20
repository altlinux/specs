Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DBIx-Class-TimeStamp
Version:        0.14
Release:        alt2_26
Summary:        DBIx::Class extension to update and create date and time based fields
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DBIx-Class-TimeStamp
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-TimeStamp-%{version}.tar.gz
Patch0:         DBIx-Class-TimeStamp-0.14-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
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
Requires:       perl(DateTime.pm) >= 0.550
Requires:       perl(DBIx/Class.pm) >= 0.080.090
Requires:       perl(DBIx/Class/DynamicDefault.pm) >= 0.030
Requires:       perl(DBIx/Class/InflateColumn/DateTime.pm)



Source44: import.info
%filter_from_requires /^perl(DateTime.pm)/d
%filter_from_requires /^perl(DBIx.Class.pm)/d

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
%setup -q -n DBIx-Class-TimeStamp-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_26
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_22
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_17
- update to new release by fcimport

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

