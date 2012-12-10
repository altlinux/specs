# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Class-TimeStamp
Version:        0.14
Release:        alt2_7
Summary:        DBIx::Class extension to update and create date and time based fields
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DBIx-Class-TimeStamp/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/DBIx-Class-TimeStamp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class/Accessor/Grouped.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/MySQL.pm)
BuildRequires:  perl(DateTime/Format/SQLite.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/DynamicDefault.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Time/Warp.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
# not picked up automatically
Requires:       perl(DBIx/Class.pm) >= 0.080.090
Requires:       perl(DBIx/Class/DynamicDefault.pm) >= 0.03


Source44: import.info

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
%setup -q -n DBIx-Class-TimeStamp-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_7
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_5
- fc import

