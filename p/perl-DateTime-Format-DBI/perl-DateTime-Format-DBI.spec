# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Date/Manip.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(Module/Build.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-DBI
Version:        0.040
Release:        alt2_5
Summary:        Find a parser class for a database connection
License:        GPL+ or Artistic 
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DateTime-Format-DBI/
Source0:        http://www.cpan.org/authors/id/C/CF/CFAERBER/DateTime-Format-DBI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/SQLite.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/Database.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
# require the dbd-specific datetime formats, so this "just works" the way we
# expect it to.
Requires:       perl(DateTime/Format/MySQL.pm)
Requires:       perl(DateTime/Format/Pg.pm)
Requires:       perl(DateTime/Format/DB2.pm)
Source44: import.info

%description
This module finds a DateTime::Format::* class that is suitable for the use
with a given DBI connection (and DBD::* driver).

Note that this is most useful if you actually have the DateTime::Format::*
class for your particular database(s) installed!  See, e.g.,
perl-DateTime-MySQL, perl-DateTime-Oracle, perl-DateTime-DB2, etc.

%prep
%setup -q -n DateTime-Format-DBI-%{version}
for i in LICENSE README lib/DateTime/Format/DBI.pm ; do
    # correct UTF-8 wonkiness
    cat $i | iconv -f ISO-8859-1 -t UTF-8 > foo
    mv foo $i
done

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test

%files
%doc Changes LICENSE README t/
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.040-alt2_5
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1_3
- fc import

