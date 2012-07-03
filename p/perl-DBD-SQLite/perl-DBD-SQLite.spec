%define dist DBD-SQLite
Name: perl-%dist
Version: 1.33
Release: alt1

Summary: SQLite driver for DBI interface in Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011 (-bi)
BuildRequires: libsqlite3-devel perl-DBI-devel perl-Encode perl-Test-NoWarnings perl-autodie

%description
DBD::SQLite is a DBI driver for SQLite database.
SQLite is a small C library that implements a self-contained,
embeddable, zero-configuration SQL database engine.

%prep
%setup -q -n %dist-%version
rm -rv inc/

# remove sqlite sources
rm sqlite3*.[ch] fts3_tokenizer.h

# disable upgrade check
sed -i- 's/require DBD::SQLite/die/' Makefile.PL

%build
%perl_vendor_build LIBS=-lsqlite3

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/SQLite.pm
%dir	%perl_vendor_archlib/DBD/SQLite
%doc	%perl_vendor_archlib/DBD/SQLite/*.pod
	%perl_vendor_autolib/DBD

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.31 -> 1.33
- built for perl-5.12
- rebuilt as plain src.rpm

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.29 -> 1.31
- t/43_fts3.t: disabled tests which require SQLITE_ENABLE_FTS3_PARENTHESIS

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.29-alt2
- t/lib/Test.pm: updated from 1.31, fixes test failures
- built for perl-5.12

* Mon Apr 05 2010 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- 1.14 -> 1.29

* Sat May 24 2008 Alexey Tourbin <at@altlinux.ru> 1.14-alt2
- dbdimp.c: use sqlite3_reset() where appropriate (cpan #32100)

* Tue Oct 16 2007 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.13 -> 1.14

* Mon Aug 06 2007 Alexey Tourbin <at@altlinux.ru> 1.13-alt3
- applied debian fix for "Unknown named parameter" (deb #422209)

* Sun Oct 22 2006 Alexey Tourbin <at@altlinux.ru> 1.13-alt2
- imported sources into git and built with gear
- backported fix for pragmas on empty db causing "Not an error" errors
- there's still a problem with Class::DBI, but I think I should also
  fix Class::DBI for this time

* Sat Sep 09 2006 Alexey Tourbin <at@altlinux.ru> 1.13-alt1
- 1.12 -> 1.13

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.09 -> 1.12

* Fri Jun 24 2005 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- 1.08 -> 1.09

* Fri Mar 04 2005 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- 1.07 -> 1.08

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- 1.05 -> 1.07
- manual pages not packaged (use perldoc)

* Thu Sep 16 2004 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.03 -> 1.05

* Fri Aug 13 2004 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- initial revision
- remove sqlite3 sources and use system-wide libsqlite3
