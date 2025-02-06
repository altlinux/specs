%def_disable static

%define aprver 1
%define apudir %name-%version

Name: aprutil%aprver
Version: 1.6.3
Release: alt2

Summary: Apache Portable Runtime Utility shared library
Group: System/Libraries
License: Apache-2.0
Url: https://apr.apache.org/

# Source-url: http://archive.apache.org/dist/apr/apr-util-%version.tar.gz
Source: apr-util-%version.tar

Patch1: aprutil1-1.6.1-alt-mysql8-transition.patch
Patch2: apr-util-1.6.3-lmdb-support.patch

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: libapr1-devel libexpat-devel zlib-devel libuuid-devel
BuildRequires: libssl-devel
BuildRequires: liblmdb-devel

%package -n lib%name
Summary: Apache Portable Runtime Utility shared library
Group: System/Libraries
Requires: libapr1 > 1.3.0
Conflicts: libaprutil

%package -n lib%name-devel
Summary: Apache Portable Runtime Utility development files
Group: Development/C
Requires: lib%name = %EVR, libapr%aprver-devel > 1.3.0
Requires: libldap-devel

%if_enabled static
%package -n lib%name-devel-static
Summary: Apache Portable Runtime Utility static library
Group: Development/C
Requires: lib%name-devel = %EVR , libapr%aprver-devel-static > 1.3.0
%endif

%description
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.

%description -n lib%name
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APU shared library.

%description -n lib%name-devel
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APU development files.

%if_enabled static
%description -n lib%name-devel-static
The mission of the Apache Portable Runtime (APR) is to provide a free
library of C data structures and routines, forming a system portability
layer to as many operating systems as possible, including Unices,
MS Win32, BeOS and OS/2.
This package contains APU static library.
%endif

%package -n lib%name-pgsql
Group: System/Libraries
Summary: APR utility library PostgreSQL DBD driver
BuildRequires: libpq5-devel
Requires: lib%name = %EVR

%description -n lib%name-pgsql
This package provides the PostgreSQL driver for the apr-util
DBD (database abstraction) interface.

%package -n lib%name-mysql
Group: System/Libraries
Summary: APR utility library MySQL DBD driver
BuildRequires: libMySQL-devel
Requires: lib%name = %EVR

%description -n lib%name-mysql
This package provides the MySQL driver for the apr-util DBD
(database abstraction) interface.

%package -n lib%name-sqlite3
Group: System/Libraries
Summary: APR utility library SQLite DBD driver
BuildRequires: libsqlite3-devel >= 3.0.0
Requires: lib%name = %EVR

%description -n lib%name-sqlite3
This package provides the SQLite driver for the apr-util DBD
(database abstraction) interface.

%package -n lib%name-ldap
Group: System/Libraries
Summary: APR utility library LDAP DBD driver
BuildRequires: libldap-devel
Requires: lib%name = %EVR

%description -n lib%name-ldap
This package provides the LDAP driver for the apr-util DBD
(database abstraction) interface.

%package -n lib%name-odbc
Group: System/Libraries
Summary: APR utility library ODBC DBD driver
BuildRequires: libunixODBC-devel
Requires: lib%name = %EVR

%description -n lib%name-odbc
This package provides the ODBC driver for the apr-util DBD
(database abstraction) interface.

%package -n lib%name-openssl
Group: System/Libraries
Summary: APR utility library OpenSSL crypto support
Requires: lib%name = %EVR

%description -n lib%name-openssl
This package provides the OpenSSL crypto support for the apr-util.

%prep
%setup -n apr-util-%version
%patch1 -p2
%patch2 -p1

%build
autoheader && autoconf
%configure \
	--with-apr=%prefix \
	--with-installbuilddir=%_datadir/apr-%aprver/build \
	--includedir=%_includedir/apu-%aprver \
	--with-dbm=lmdb --with-lmdb \
	--with-sqlite3 \
	--with-crypto \
	--with-openssl \
	--with-mysql --with-pgsql \
	--with-ldap \
	%{subst_enable static}

%make_build

%install
%makeinstall_std
find %buildroot%_bindir -type f -print0 |
	xargs -r0 grep -FZl "%_builddir/%apudir" -- |
	xargs -r0 sed -i "s,%_builddir/%apudir,%_datadir/apr-%aprver," --
find %buildroot%_datadir -type f -print0 |
	xargs -r0 grep -FZl "%_builddir/%apudir" -- |
	xargs -r0 sed -i "s,%_builddir/%apudir\(/build\)\?,%_datadir/apr-%aprver/build," --

rm -rf %buildroot%_libdir/apr-util-%aprver/*.la

%check
%make check

%files -n lib%name
%_libdir/lib*.so.*
%dir %_libdir/apr-util-%aprver

%files -n lib%name-devel
%_bindir/*-config
%_libdir/lib*.so
%_libdir/*.exp
%_pkgconfigdir/apr-util-%aprver.pc
%_includedir/*
%_libdir/apr-util-%aprver/apr_dbm_lmdb*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

%files -n lib%name-pgsql
%_libdir/apr-util-%aprver/apr_dbd_pgsql*.so

%files -n lib%name-mysql
%_libdir/apr-util-%aprver/apr_dbd_mysql*.so

%if_with sqlite2
%files -n lib%name-sqlite2
%_libdir/apr-util-%aprver/apr_dbd_sqlite2*.so
%endif

%files -n lib%name-sqlite3
%_libdir/apr-util-%aprver/apr_dbd_sqlite3*.so

%files -n lib%name-ldap
%_libdir/apr-util-%aprver/apr_ldap*.so

%files -n lib%name-odbc
%_libdir/apr-util-%aprver/apr_dbd_odbc*.so

%files -n lib%name-openssl
%_libdir/apr-util-%aprver/apr_crypto_openssl*.so

%changelog
* Thu Feb 06 2025 Anton Farygin <rider@altlinux.ru> 1.6.3-alt2
- built with lmdb instead of BerkleyDB (thnx, Fedora)
- added openssl subpackage with crypto support
- cleanup specfile

* Mon Sep 30 2024 Alexei Takaseev <taf@altlinux.org> 1.6.3-alt1
- 1.6.3 (Fixes CVE-2022-25147)

* Fri Sep 10 2021 Ivan A. Melnikov <iv@altlinux.org> 1.6.1-alt4
- Update mysql patch to avoid calling absent my_init function

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt3
- rebuild with sqlite2 disabled

* Mon Mar 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.6.1-alt2
- Fix FTBFS against libmysqlclient21

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.1-alt1
- New version.
- Drop upsupported lib%name-freetds.

* Wed Apr 27 2016 Sergey Alembekov <rt@altlinux.ru> 1.5.4-alt1
- New version 1.5.4

* Wed Nov 28 2012 Aleksey Avdeev <solo@altlinux.ru> 1.5.1-alt1
- New version (1.5.1)
- Use libdb4-devel by default

* Thu Nov 15 2012 Aleksey Avdeev <solo@altlinux.ru> 1.3.12-alt1
- New version (1.3.12) (ALT#27746)

* Sat Oct 20 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.10-alt6
- Fix build with GCC 4.6

* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.10-alt5
- Rebuilt for debuginfo.

* Wed Dec 01 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.10-alt4
- apr_queue_pop_timeout() implementation added

* Thu Nov 25 2010 Aleksey Avdeev <solo@altlinux.ru> 1.3.10-alt3
- Rebuilt for soname set-versions.

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 1.3.10-alt2
- Rebuilt with apr 1.4.2

* Sat Oct 16 2010 Aleksey Avdeev <solo@altlinux.ru> 1.3.10-alt1
- New version (1.3.10)
- Security fixes (CVE-2009-3560, CVE-2009-3720, CVE-2010-1623)
  (Closes: #24224)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.9-alt3
- Rebuilt with python 2.6

* Tue Sep 01 2009 Aleksey Avdeev <solo@altlinux.ru> 1.3.9-alt2
- Rebuild with libldap2.4

* Sun Aug 16 2009 Aleksey Avdeev <solo@altlinux.ru> 1.3.9-alt1
- New version (1.3.9)
- Security fixes (CVE-2009-2412)

* Wed Jul 22 2009 Boris Savelev <boris@altlinux.org> 1.3.8-alt1
- new version

* Fri Jun 05 2009 Boris Savelev <boris@altlinux.org> 1.3.7-alt1
- CVE-2009-0023 (ALT#20329)
- update version

* Wed Jun 03 2009 Boris Savelev <boris@altlinux.org> 1.3.4-alt3.4
- add patch to fix "billion laughs" attack (ALT#20279)

* Mon Apr 13 2009 Boris Savelev <boris@altlinux.org> 1.3.4-alt3.3
- fix build
- remove ldconfig

* Fri Oct 31 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.4-alt3.2
- NMU
- add lib%%name-libdb = %%libdb_v1.%%libdb_v2_req provides
- add conflicts for libsubversion < 1.4.4-alt2.3.1

* Fri Oct 31 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.4-alt3.1
- NMU
- use libdb4.7-devel by default

* Tue Sep 16 2008 Boris Savelev <boris@altlinux.org> 1.3.4-alt3
- libaprutil1-devel requires libldap-devel (fix #17149)

* Wed Sep 10 2008 Boris Savelev <boris@altlinux.org> 1.3.4-alt2
- fix unmet on libaprutil1-devel

* Wed Sep 03 2008 Boris Savelev <boris@altlinux.org> 1.3.4-alt1
- new version
- add dso support

* Tue Sep 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt1.1
- NMU: rebuild with libdb4.7

* Thu Mar 06 2008 Grigory Batalov <bga@altlinux.ru> 1.2.12-alt1
- New upstream release.
- Linkage patch updated.

* Sun Feb 25 2007 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.8-alt2
- Added dependency: libaprutil1-devel requires libdb4.4-devel

* Thu Feb 01 2007 Aleksey Avdeev <solo@altlinux.ru> 1.2.8-alt1.1
- NMU:
  + delete apr_common.m4 and find_apr.m4, for use system file
  + merge from apr1.spec
  + save build/*.m4 in %%_datadir/apr-%%aprver/build/

* Sun Dec 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.8-alt1
- Updated to 1.2.8
- Rebuilt with libdb4.4

* Mon Jun 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.2-alt1.1
- Rebuilt with libldap-2.3.so.0.

* Sun Jan 22 2006 Sviatoslav Sviridov <svd@altlinux.ru> 1.2.2-alt1
- Switched to aprutil1 branch
- Updated alt-linkage patch
- Updated BuildRequires (added python-base python-modules-encodings due
  to usage of buildconf.py script)
- added export LDFLAGS='-Wl,--as-needed' to build and install sections
- added dependency to libdb4.3-devel (was libdb4-devel)
- added patch for apr-util-1.pc

* Thu Nov 03 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.7-alt2
- Updated alt-linkage patch (#8394, x86_64 build)

* Mon Oct 17 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.7-alt1
- Updated to 0.9.7

* Mon May 30 2005 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.6-alt1
- Updated to 0.9.6

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.9.5-alt0.4.1
- Rebuilt with libdb4.3.

* Mon Aug 16 2004 Dmitry V. Levin <ldv@altlinux.org> 1:0.9.5-alt0.4
- Updated to version from apache 2.0.50 tarball.
- Fixed library linkage.
- Renamed source package.
- Package libaprutil separately.
- Do not build static library by default.

* Thu Feb 12 2004 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.3
- used workaround for build with libexpat without .la files
- updated BuildRequires
- rebuild with libdb4.2

* Sun Nov 30 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.2
- removed *.la files

* Wed Nov 19 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.5-alt0.1
- new version: 0.9.5 (from apache 2.0.48 tarball)

* Fri Aug 22 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.4-alt1
- new version: 0.9.4 (from apache 2.0.47 tarball)

* Tue Apr 15 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.3-alt1
- new version: 0.9.3

* Tue Mar 25 2003 Sviatoslav Sviridov <svd@altlinux.ru> 1:0.9.2-alt0.1
- first build for ALT Linux
