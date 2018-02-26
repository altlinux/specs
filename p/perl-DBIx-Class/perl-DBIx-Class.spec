Name: perl-DBIx-Class
Version: 0.08195
Release: alt1

Summary: Extensible and flexible object <-> relational mapper
License: Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/DBIx-Class/
Source: DBIx-Class-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Nov 10 2011 (-bi)
BuildRequires: perl-Class-C3 perl-Class-C3-Componentised perl-Class-Trigger perl-Class-Unload perl-Clone perl-Config-Any perl-Context-Preserve perl-DBD-Pg perl-DBD-SQLite perl-DBIx-ContextualFetch perl-Data-Compare perl-Data-Dumper-Concise perl-Data-Page perl-Date-Simple perl-DateTime-Format-Strptime perl-JSON-Any perl-JSON-DWIW perl-Math-Base36 perl-Module-Find perl-MooseX-Getopt perl-MooseX-Types-JSON perl-MooseX-Types-Path-Class perl-PPerl perl-SQL-Abstract perl-SQL-Translator perl-Scope-Guard perl-Test-Exception perl-Test-Memory-Cycle perl-Test-Warn perl-Text-CSV perl-Text-CSV_XS perl-Time-Piece perl-namespace-autoclean perl-podlators perl-threads

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
%setup -q -n DBIx-Class-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README 
%_bindir/dbic*
%_man1dir/dbic*.1*
%perl_vendor_privlib/DBIx*
%perl_vendor_privlib/SQL*

%changelog
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

