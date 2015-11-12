# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-SQL-Statement
Version:        1.407
Release:        alt1_4
Summary:        SQL parsing and processing engine
Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/SQL-Statement/
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/SQL-Statement-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Clone.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Errno.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Math/Base/Convert.pm)
BuildRequires:  perl(Math/Trig.pm)
BuildRequires:  perl(Module/Runtime.pm)
BuildRequires:  perl(Params/Util.pm)
BuildRequires:  perl(Scalar/Util.pm)
# XXX: BuildRequires:  perl(SQL::UserDefs)
BuildRequires:  perl(sort.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(Text/Soundex.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests only
# DBD::CSV buildrequires SQL::Statement
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(DBD/CSV.pm)
%endif
BuildRequires:  perl(DBD/DBM.pm)
BuildRequires:  perl(DBD/File.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(MLDBM.pm)
Requires:       perl(Clone.pm) >= 0.30
Requires:       perl(DBI.pm) >= 1.616
Requires:       perl(Math/Base/Convert.pm)
Requires:       perl(Params/Util.pm) >= 1.00
Requires:       perl(Scalar/Util.pm) >= 1.0
# This module doesn't seem to exist...
# XXX: Requires:       perl(SQL::UserDefs)
Requires:       perl(Text/Soundex.pm)


Source44: import.info
%filter_from_requires /^perl\\((Clone|Params.Util|Scalar.Util).pm\\)$/d

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine.  While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complexly nested search conditions, and
other features.

%prep
%setup -q -n SQL-Statement-%{version}
find -type f -exec chmod a-x {} +
sed -i -e 's/\r//' README

%build
export SQL_STATEMENT_WARN_UPDATE=sure
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/SQL/

%changelog
* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.407-alt1_4
- new version

* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 1.405-alt1
- 1.33 -> 1.405

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.27 -> 1.33

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Sun Jun 28 2009 Michael Bochkaryov <misha@altlinux.ru> 1.20-alt1
- 1.20 version
- broken tests removed

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1
- NMU to fix directory ownership violation

* Sat Feb 02 2008 Michael Bochkaryov <misha@altlinux.ru> 1.15-alt1
- first build for ALT Linux Sisyphus

