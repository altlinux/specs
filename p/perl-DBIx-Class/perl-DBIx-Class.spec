%define _unpackaged_files_terminate_build 1
Name: perl-DBIx-Class
Version: 0.082841
Release: alt1

Summary: Extensible and flexible object <-> relational mapper
License: Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/DBIx-Class/
Source0: http://www.cpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Nov 10 2011 (-bi)
BuildRequires: perl-Module-Install perl-Test-Deep perl-Class-C3 perl-Class-C3-Componentised perl-Class-Trigger perl-Class-Unload perl-Clone perl-Config-Any perl-Context-Preserve perl-DBD-Pg perl-DBD-SQLite perl-DBIx-ContextualFetch perl-Data-Compare perl-Data-Dumper-Concise perl-Data-Page perl-Date-Simple perl-DateTime-Format-Strptime perl-JSON-Any perl-JSON-DWIW perl-Math-Base36 perl-Module-Find perl-MooseX-Getopt perl-MooseX-Types-JSON perl-MooseX-Types-Path-Class perl-PPerl perl-SQL-Abstract perl-SQL-Translator perl-Scope-Guard perl-Test-Exception perl-Test-Memory-Cycle perl-Test-Warn perl-Text-CSV perl-Text-CSV_XS perl-Time-Piece perl-namespace-autoclean perl-podlators perl-threads perl-MooseX-Types-LoadableClass


# Avoid dependency on DBD::ADO
%add_findreq_skiplist */DBIx/Class/Storage/DBI/ADO*
# Avoid dependency on DBD::Oracle
%add_findreq_skiplist */DBIx/Class/Storage/DBI/Oracle*

%description
This is an SQL to OO mapper with an object API inspired by
Class::DBI (and a compatibility layer as a springboard for
porting) and a resultset API that allows abstract encapsulation
of database operations. It aims to make representing queries in
your code as perl-ish as possible while still providing access
to as many of the capabilities of the database as possible,
including retrieving related records from multiple tables in a
single query, JOIN, LEFT JOIN, COUNT, DISTINCT, GROUP BY and
HAVING support.

%prep
%setup -q -n DBIx-Class-%{version}

[ %version = 0.082840 ] && rm t/resultset/update_delete.t

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README AUTHORS examples
%_bindir/dbic*
%_man1dir/dbic*.1*
%perl_vendor_privlib/DBIx*
%perl_vendor_privlib/SQL*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.082841-alt1
- automated CPAN update

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.082840-alt2
- added Patch0: DBIx-Class-0.082840-Fix-test-RT117271.patch

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.082840-alt1
- automated CPAN update

* Mon Feb 29 2016 Vladimir Lettiev <crux@altlinux.ru> 0.082821-alt1
- 0.082821

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.082820-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.082810-alt1
- automated CPAN update

* Tue Feb 25 2014 Vladimir Lettiev <crux@altlinux.ru> 0.08270-alt1
- 0.08270

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.08250-alt1
- 0.08250

* Fri Apr 19 2013 Andrey Cherepanov <cas@altlinux.org> 0.08203-alt1.1
- Fix build by removing one test

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.08203-alt1
- automated CPAN update

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.08202-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.08200-alt1
- 0.08195 -> 0.08200

* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 0.08195-alt1
- 0.08123 -> 0.08195

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08123-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Aug 22 2010 Alexey Tourbin <at@altlinux.ru> 0.08123-alt1
- 0.08121 -> 0.08123

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.08121-alt1
- 0.08010 -> 0.08121

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08010-alt4
- add missing SQL::Translator::Producer::DBIx::Class::File

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08010-alt3
- fix directory ownership violation

* Fri Jun 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08010-alt2
- wrong bad perl version warning removed

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08010-alt1
- 0.08010 version
- dbicadmin utility added to binary package

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.07999_02-alt1
- first build for ALT Linux Sisyphus

