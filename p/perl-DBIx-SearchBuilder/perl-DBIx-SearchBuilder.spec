%define dist DBIx-SearchBuilder
Name: perl-%dist
Version: 1.61
Release: alt1

Summary: Encapsulate SQL queries and rows in simple perl objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# requires DBD::Oracle
%add_findreq_skiplist */DBIx/SearchBuilder/Handle/Oracle.pm

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Cache-Simple-TimedExpiry perl-Class-Accessor perl-Class-ReturnValue perl-Clone perl-DBD-ODBC perl-DBD-SQLite perl-DBD-Sybase perl-DBD-mysql perl-DBIx-DBSchema perl-Test-Pod perl-Want perl-capitalization

%description
This module provides an object-oriented mechanism for retrieving and
updating data in a DBI-accesible database.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DBIx

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.61-alt1
- 1.54 -> 1.61

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.54-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.54-alt2
- fix directory ownership violation

* Wed Sep 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.54-alt1
- new version 1.54 (with rpmrb script) - fix bug #16772

* Fri Jun 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.53-alt1
- new version 1.53 (with rpmrb script)

* Wed Feb 27 2008 Vitaly Lipatov <lav@altlinux.ru> 1.51-alt1
- new version 1.51 (with rpmrb script)

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 1.49-alt1
- new version 1.49 (with rpmrb script)
- update buildreq

* Tue Mar 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48-alt1
- new version 1.48 (with rpmrb script)

* Thu Jun 22 2006 Vitaly Lipatov <lav@altlinux.ru> 1.43-alt0.1
- new version 1.43 (with rpmrb script)

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.38-alt0.1
- new version

* Sat Sep 24 2005 Vitaly Lipatov <lav@altlinux.ru> 1.33-alt1
- new version

* Thu Sep 01 2005 Vitaly Lipatov <lav@altlinux.ru> 1.30_02-alt1
- first build for ALT Linux Sisyphus
- Oracle support disabled
