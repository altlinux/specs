# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/SQLite.pm) perl(DBIx/XHTML_Table.pm) perl(Object/Accessor.pm) perl(SQL/Abstract.pm) perl(SQL/Interp.pm) perl(Text/Table.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Simple
Summary:        Easy-to-use OO interface to DBI
Version:        1.35
Release:        alt2_10
License:        Public Domain
Group:          Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/J/JU/JUERD/DBIx-Simple-%{version}.tar.gz
URL:            http://search.cpan.org/dist/DBIx-Simple/
BuildArch:      noarch

BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(DBI.pm) >= 1.21



Source44: import.info

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

%prep
%setup -q -n DBIx-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_10
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt2_9
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1_9
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- initial import by package builder

