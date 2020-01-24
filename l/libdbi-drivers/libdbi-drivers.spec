%define _unpackaged_files_terminate_build 1

%def_with firebird
%def_without sqlite2
%def_disable doc

Name: libdbi-drivers
Version: 0.9.0
Release: alt6
Epoch: 1

Summary: Database drivers for libdbi
License: LGPL
Group: System/Libraries

Url: http://libdbi-drivers.sourceforge.net/
Source: %name-%version.tar
Patch: 0001-freetds-resolve-compile-error-with-1.0.patch

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: gcc-c++ libdbi-devel zlib-devel
BuildRequires: libMySQL-devel postgresql-devel
BuildRequires: libfreetds-devel
BuildRequires: libsqlite3-devel
%{?_with_sqlite2:BuildRequires: libsqlite-devel}
%{?_with_firebird:BuildRequires: firebird-devel docbook-style-dsssl jadetex}
%{?_enable_doc:BuildRequires: docbook-style-dsssl jadetex openjade}

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

%if_with sqlite2
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

%endif

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

%prep
%setup
%patch -p1

# lib64 fix
sed -i "s|/lib\b|/%_lib|g" acinclude.m4

%build
%autoreconf
%configure \
    --with-mysql \
    --with-pgsql \
%if_with sqlite2
    --with-sqlite \
%endif
    --with-sqlite3 \
    --with-freetds \
    --with-freetds-incdir=%_includedir \
    --with-freetds-libdir=%_libdir \
    --with-dbi-incdir=%_includedir/dbi \
    --with-dbi-libdir=%_libdir \
    --localstatedir=%_var \
    --sharedstatedir=%_var \
    %{subst_with firebird} \
    %{subst_enable docs}

%make_build

%install
%makeinstall_std

# install development headers
install -d %buildroot%_includedir/dbi
install -pm0644 drivers/mysql/dbd_mysql.h %buildroot%_includedir/dbi/
install -pm0644 drivers/pgsql/dbd_pgsql.h %buildroot%_includedir/dbi/
%if_with sqlite2
install -pm0644 drivers/sqlite/dbd_sqlite.h %buildroot%_includedir/dbi/
%endif
install -pm0644 drivers/sqlite3/dbd_sqlite3.h %buildroot%_includedir/dbi/
install -pm0644 drivers/freetds/dbd_freetds.h %buildroot%_includedir/dbi/
%if_with firebird
install -pm0644 drivers/firebird/dbd_firebird.h %buildroot%_includedir/dbi/
%endif

%if_enabled docs
# fix some docs
cp -a drivers/mysql/TODO TODO.mysql
cp -a drivers/pgsql/TODO TODO.pgsql
%if_with sqlite2
cp -a drivers/sqlite/TODO TODO.sqlite
%endif
cp -a drivers/sqlite3/TODO TODO.sqlite3
%if_with firebird
cp -a drivers/firebird/TODO TODO.firebird
%endif
%else
# firebird tries to build those unconditionally
rm -rf %buildroot%_docdir/*
%endif

# remove unpackaged files
rm -f %buildroot%_libdir/dbd/*.la

%files dbd-mysql
%doc drivers/mysql/README
%_libdir/dbd/libdbdmysql.so

%files dbd-pgsql
%doc drivers/pgsql/README
%_libdir/dbd/libdbdpgsql.so

%if_with sqlite2
%files dbd-sqlite
%doc drivers/sqlite/README
%_libdir/dbd/libdbdsqlite.so
%endif

%files dbd-sqlite3
%doc drivers/sqlite3/README
%_libdir/dbd/libdbdsqlite3.so

%files dbd-freetds
%doc drivers/freetds/README
%_libdir/dbd/libdbdfreetds.so

%if_with firebird
%files dbd-firebird
%doc drivers/firebird/README
%_libdir/dbd/libdbdfirebird.so
%endif

%files devel
%doc AUTHORS ChangeLog INSTALL README TODO*
%_includedir/dbi/*.h

%files devel-static
%_libdir/dbd/*.a

%if_enabled docs
%files doc
%_docdir/*
%exclude %_docdir/*devel*
%endif

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.9.0-alt6
- build without sqlite2 support

* Tue Jul 02 2019 Michael Shigorin <mike@altlinux.org> 1:0.9.0-alt5
- introduced firebird knob (on by default)
- replaced builddoc variable with docs knob (off by default),
  put extra BRs under it either

* Fri Mar 22 2019 Anton Farygin <rider@altlinux.ru> 1:0.9.0-alt4
- removed w3c-markup-validator-libs build dependency

* Fri Sep 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.9.0-alt3
- Fixed build with new freetds.

* Tue Oct 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.9.0-alt2
- Fixed localstatedir/sharedstatedir location.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.9.0-alt1
- Updated to upstream release version 0.9.0.

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt3.cvs20092729.qa1
- NMU: rebuilt with libmysqlclient.so.18.

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

