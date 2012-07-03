%define builddoc 0
Summary: Database drivers for libdbi
Name: libdbi-drivers
Version: 1.0
Release: alt3.cvs20092729
License: LGPL
Group: System/Libraries
Url: http://libdbi-drivers.sourceforge.net/
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: docbook-style-dsssl gcc-c++ libMySQL-devel libdbi-devel zlib-devel
BuildRequires: libfreetds-devel libsqlite-devel libsqlite3-devel openjade
BuildRequires: postgresql-devel w3c-markup-validator-libs jadetex firebird-devel

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package dbd-mysql
Summary: MySQL driver for libdbi
Group: System/Libraries

%description dbd-mysql
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to MySQL database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package dbd-pgsql
Summary: PostgreSQL driver for libdbi
Group: System/Libraries

%description dbd-pgsql
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to PostgreSQL database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package dbd-sqlite
Summary: SQLite driver for libdbi
Group: System/Libraries

%description dbd-sqlite
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to SQLite database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package dbd-sqlite3
Summary: SQLite3 driver for libdbi
Group: System/Libraries

%description dbd-sqlite3
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to SQLite3 database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package dbd-freetds
Summary: MSSQL (FreeTDS) driver for libdbi
Group: System/Libraries

%description dbd-freetds
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to MSSQL database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package dbd-firebird
Summary: Firebird driver for libdbi
Group: System/Libraries

%description dbd-firebird
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to Firebird database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package devel
Summary: Header files for the %name library drivers
Group: Development/C
Provides: %name-drivers-devel
Requires: libdbi-devel >= 0.8.2

%description devel
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains header files.

%package devel-static
Summary: Static library for the %name library drivers
Group: Development/C
Provides: %name-drivers-devel
Requires: libdbi-devel >= 0.8.2

%description devel-static
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the static libraries.

%if %builddoc
%package doc
Summary: Docs for the %name library drivers
Group: Development/C
Provides: %name-drivers-devel
Requires: libdbi-devel >= 0.8.2

%description doc
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the doc.
%endif

%prep
%setup

# lib64 fix
%__subst "s|/lib\b|/%_lib|g" acinclude.m4

%build
%autoreconf
%configure \
    --with-mysql \
    --with-pgsql \
    --with-sqlite \
    --with-sqlite3 \
    --with-firebird \
    --with-freetds \
    --with-freetds-incdir=%_includedir \
    --with-freetds-libdir=%_libdir \
    --with-dbi-incdir=%_includedir/dbi \
    --with-dbi-libdir=%_libdir \
    --disable-docs

%make_build

%install
%makeinstall_std

# install development headers
install -d %buildroot%_includedir/dbi
install -m0644 drivers/mysql/dbd_mysql.h %buildroot%_includedir/dbi/
install -m0644 drivers/pgsql/dbd_pgsql.h %buildroot%_includedir/dbi/
install -m0644 drivers/sqlite/dbd_sqlite.h %buildroot%_includedir/dbi/
install -m0644 drivers/sqlite3/dbd_sqlite3.h %buildroot%_includedir/dbi/
install -m0644 drivers/freetds/dbd_freetds.h %buildroot%_includedir/dbi/
install -m0644 drivers/firebird/dbd_firebird.h %buildroot%_includedir/dbi/

# fix some docs
cp drivers/mysql/TODO TODO.mysql
cp drivers/pgsql/TODO TODO.pgsql
cp drivers/sqlite/TODO TODO.sqlite
cp drivers/sqlite3/TODO TODO.sqlite3
cp drivers/firebird/TODO TODO.firebird

%files dbd-mysql
%doc drivers/mysql/README
%_libdir/dbd/libdbdmysql.so

%files dbd-pgsql
%doc drivers/pgsql/README
%_libdir/dbd/libdbdpgsql.so

%files dbd-sqlite
%doc drivers/sqlite/README
%_libdir/dbd/libdbdsqlite.so

%files dbd-sqlite3
%doc drivers/sqlite3/README
%_libdir/dbd/libdbdsqlite3.so

%files dbd-freetds
%doc drivers/freetds/README
%_libdir/dbd/libdbdfreetds.so

%files dbd-firebird
%doc drivers/firebird/README
%_libdir/dbd/libdbdfirebird.so

%files devel
%doc AUTHORS ChangeLog INSTALL README TODO*
%_includedir/dbi/*.h

%files devel-static
%_libdir/dbd/*.a

%if %builddoc
%files doc
%_docdir/%name
%endif

%changelog
* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.cvs20092729
- rebuild with libmysqlclient.so.16

* Sat Sep 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.cvs20092729
- rebuild with libmysqlclient.so.16

* Wed Apr 29 2009 Boris Savelev <boris@altlinux.org> 1.0-alt1.cvs20092729
- disable docs
- rebuild with new libdbi
- add firebird subpackage

* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 0.8.3-alt1
- initial build for Sisyphus from Mandriva

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-4mdv2009.0
+ Revision: 233768
- rebuild

* Mon Jun 16 2008 Anssi Hannula <anssi@mandriva.org> 0.8.3-3mdv2009.0
+ Revision: 219475
- build with main freetds, it has equal functionality now

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-2mdv2008.1
+ Revision: 178294
- bump release
- 0.8.3-1

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 169620
- 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2008.0
+ Revision: 81075
- 0.8.2-1

* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2007.0
+ Revision: 110697
- rebuilt against new postgresql libs

* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2007.1
+ Revision: 94098
- fix doc inclusion
- added the sqlite3 driver
- Import libdbi-drivers

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1
- added the freetds backend

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2mdk
- rebuilt against MySQL-5.0.15

* Fri Sep 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdk
- lib64 fixes (P0)

* Fri Jun 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

