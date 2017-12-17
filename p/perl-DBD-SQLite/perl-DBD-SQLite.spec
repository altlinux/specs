%define _unpackaged_files_terminate_build 1
%define dist DBD-SQLite
Name: perl-%dist
Version: 1.54
Release: alt1.1.1

Summary: SQLite driver for DBI interface in Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011 (-bi)
BuildRequires: libsqlite3-devel perl-DBI-devel perl-Encode perl-Test-NoWarnings perl-autodie

%description
DBD::SQLite is a DBI driver for SQLite database.
SQLite is a small C library that implements a self-contained,
embeddable, zero-configuration SQL database engine.

%prep
%setup -q -n %dist-%version
#rm -rv inc/

# remove sqlite sources
rm sqlite3*.[ch] fts3_tokenizer.h

# disable upgrade check
sed -i- 's/require DBD::SQLite/die/' Makefile.PL

# broken test?
[ %version = 1.48 ] && rm -f t/virtual_table/11_filecontent_fulltext.t

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
	%perl_vendor_archlib/DBD/SQLite/Constants.pm
	%perl_vendor_archlib/DBD/SQLite/VirtualTable.pm
%dir	%perl_vendor_archlib/DBD/SQLite/VirtualTable
	%perl_vendor_archlib/DBD/SQLite/VirtualTable/*.pm
	%perl_vendor_autolib/DBD

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1.1
- rebuild with new perl 5.24.1

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1.1
- rebuild with new perl 5.20.1

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.40-alt2
- built for perl 5.18

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.37-alt1
- 1.33 -> 1.37
- built for perl-5.16

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
