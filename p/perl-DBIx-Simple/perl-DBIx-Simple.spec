Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBIx/XHTML_Table.pm) perl(SQL/Abstract.pm) perl(Text/Table.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.35
Release:        alt2_16
License:        Public Domain
Source0:        http://search.cpan.org/CPAN/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz
URL:            http://search.cpan.org/dist/DBIx-Simple/
BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DBI.pm)
# DBIx::XHTML_Table - not used for test
BuildRequires:  perl(Object/Accessor.pm)
BuildRequires:  perl(overload.pm)
# SQL::Abstract - not used for test
BuildRequires:  perl(SQL/Interp.pm)
BuildRequires:  perl(strict.pm)
# Text::Table - not used for test
# Tests
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DBI.pm) >= 1.21
Requires:       perl(DBIx/XHTML_Table.pm)
Requires:       perl(SQL/Abstract.pm)
Requires:       perl(SQL/Interp.pm)
Requires:       perl(Text/Table.pm)



Source44: import.info

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

%prep
%setup -q -n DBIx-Simple-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_10
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_9
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1_9
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- initial import by package builder

