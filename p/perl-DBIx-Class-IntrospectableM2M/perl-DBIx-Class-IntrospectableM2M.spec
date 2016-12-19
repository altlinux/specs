# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Class-IntrospectableM2M
Version:        0.001002
Release:        alt1_4
Summary:        Introspect many-to-many shortcuts
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/DBIx-Class-IntrospectableM2M/
Source0:        http://www.cpan.org/authors/id/I/IL/ILMARI/DBIx-Class-IntrospectableM2M-%{version}.tar.gz
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
BuildRequires:  perl(base.pm)
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(DBIx/Class/Core.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Because the many-to-many relationships are not real relationships, they can
not be introspected with DBIx::Class. Many-to-many relationships are
actually just a collection of convenience methods installed to bridge two
relationships. This DBIx::Class component can be used to store all relevant
information about these non-relationships so they can later be introspected
and examined.

%prep
%setup -q -n DBIx-Class-IntrospectableM2M-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.001002-alt1_4
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.001002-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.001002-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_1
- fc import

