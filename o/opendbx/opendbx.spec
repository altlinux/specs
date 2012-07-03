%def_with mysql
%def_with pgsql
%def_with sqlite3
%def_without firebird

Name: opendbx
Version: 1.4.3
Release: alt1.2

Summary: Unified database layer with a clean and lightweight interface
Summary(de):	Bibliothek zum Zugriff auf Datenbanken über eine einheitliche Schnittstelle
License: LGPL
Group: Development/Databases
Url: http://www.linuxnetworks.de/doc/index.php/OpenDBX

Source: http://www.linuxnetworks.de/opendbx/download/%name-%version.tar.gz
Patch: %name-1.4.0-alt-sqlite3-no-threadsafe.patch

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: gcc-c++ libncurses-devel libreadline-devel

%description
OpenDBX provides a clean and lightweight API for interfacing native relational
database APIs in a consistent way. By using the OpenDBX API you don't have to
adapt your program to the different database APIs by yourself.

%description -l de
OpenDBX ist eine schlanke und einfach zu verwendende Bibliothek, die es
ermöglicht verschiedene Datenbankserver über eine konsistente Schnittstelle
anzusprechen.

%package devel
Summary: OpenDBX development headers
Summary(de):	Entwicklungsschnittstellen für OpenDBX
Group: Development/Databases
Requires: %name = %version-%release
Requires: pkgconfig %{?_with_mysql:%name-mysql} %{?_with_pgsql:%name-pgsql} %{?_with_sqlite3:%name-sqlite3} %{?_with_firebird:%name-firebird}

%description devel
Header files for the OpenDBX database abstraction library

%description -l de devel
Schnittstellen der OpenDBX Datenbankbibliothek zur Softwareentwicklung

%if_with mysql
%package mysql
Summary: MySQL backend for OpenDBX
Summary(de):	MySQL Unterstützung für OpenDBX
Group: Development/Databases
Requires: %name = %version-%release
BuildRequires: mysql-devel

%description mysql
MySQL backend for the OpenDBX database abstraction library

%description -l de mysql
MySQL Unterstützung für die OpenDBX Datenbankbibliothek
%endif

%if_with pgsql
%package pgsql
Summary: PostgreSQL backend for OpenDBX
Summary(de):	PostgreSQL Unterstützung für OpenDBX
Group: Development/Databases
Requires: %name = %version-%release
BuildRequires: postgresql-devel

%description pgsql
PostgreSQL backend for the OpenDBX database abstraction library

%description -l de pgsql
PostgreSQL Unterstützung für die OpenDBX Datenbankbibliothek
%endif

%if_with sqlite3
%package sqlite3
Summary: SQLite3 backend for OpenDBX
Summary(de):	SQLite3 Unterstützung für OpenDBX
Group: Development/Databases
Requires: %name = %version-%release
BuildRequires: libsqlite3-devel

%description sqlite3
SQLite3 backend for the OpenDBX database abstraction library

%description -l de sqlite3
Sqlite3 Unterstützung für die OpenDBX Datenbankbibliothek
%endif

%if_with firebird
%package firebird
Summary: Firebird/Interbase backend for OpenDBX
Summary(de):    Firebird/Interbase Unterstützung für OpenDBX
Group: Development/Databases
Requires: %name = %version-%release
BuildRequires: firebird-devel

%description firebird
Firebird/Interbase backend for the OpenDBX database abstraction library

%description -l de firebird
Firebird/Interbase Unterstützung für die OpenDBX Datenbankbibliothek
%endif

%prep
%setup -q
%patch -p0

%build
%if_with mysql
%add_optflags "-I%_includedir/mysql"
%endif
%if_with pgsql
%add_optflags "-I%_includedir/pgsql"
%endif

%undefine __libtoolize
%configure --with-pic --disable-static --with-backends="\
%{?_with_mysql:mysql }\
%{?_with_pgsql:pgsql }\
%{?_with_sqlite3:sqlite3 }\
%{?_with_firebird:firebird }\
"

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build -j1

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name
%_libdir/*.so.*
%_datadir/%name
%doc AUTHORS ChangeLog NEWS README TODO

%files devel
%_includedir/odbx.h
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/opendbxplus.pc

%if_with mysql
%files mysql
%_libdir/%name/libmysqlbackend.so*
%endif

%if_with pgsql
%files pgsql
%_libdir/%name/libpgsqlbackend.so*
%endif

%if_with sqlite3
%files sqlite3
%_libdir/%name/libsqlite3backend.so*
%endif

%if_with firebird
%files firebird
%_libdir/%name/libfirebirdbackend.so*
%endif

%changelog
* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.2
- Removed bad RPATH

* Wed Nov 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.3-alt1.1
- build into Sisyphus

* Mon Sep 28 2009 Grigory Batalov <bga@altlinux.ru> 1.4.3-alt1
- New upstream release.

* Wed Apr 08 2009 Grigory Batalov <bga@altlinux.ru> 1.4.0-alt0.M40.1
- New upstream release.
- Built for ALT Linux branch 4.0.

* Wed Feb 27 2008 - mge@arcor.de 1.3.8-26
- build in OBS with FreeTDS
* Wed Jan 31 2007 Norbert Sendetzky <norbert@linuxnetworks.de> 1.2.1-1
- Added German summary and descriptions
- Disabled static library builds and removed libtool files
- Added ldconfig call in post and postun sections
- Added gettext and pkgconfig as requirements
- Replaced language file handling with find_lang macro
- Used optflags macro instead of hard coded compiler flags
- Used macro style consistently
- Corrected mail addresses
- Removed oracle sections
- Fixed _without_pgqql
- Minor changes
* Sat Dec 09 2006 Norbert Sendetzky <norbert@linuxnetworks.de> 1.1.8-1
- Added mssql, sybase and oracle backend
* Tue Jun 13 2006 Kees Monshouwer <mind@monshouwer.com> 1.1.0-2
- Fixed a few minor problems
- Added conditional build support
- Added firefird and freetds backend
* Mon Jun 12 2006 Kees Monshouwer <mind@monshouwer.com> 1.1.0-1
- Initial build for CentOS 4.3
