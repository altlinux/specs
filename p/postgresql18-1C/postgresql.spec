# -*- mode: rpm-spec; coding: utf-8 -*-
%def_without devel

# Use ICU
%def_with icu

%ifarch x86_64
# Use coverage
%def_without coverage
%endif

# Use JIT
%ifarch %e2k
# LLVM no official support on E2K
%def_without jit
%else
# Use JIT elsewhere
%def_with jit
%endif

%set_autoconf_version 2.60

%define prog_name            postgresql
%define postgresql_major     18
%define postgresql_minor     4
%define postgresql_altrel    4

# Look at: src/interfaces/libpq/Makefile
%define libpq_major          5

# Look at: src/interfaces/ecpg/ecpglib/Makefile
%define libecpg_major        6

%define libpq_name    libpq%libpq_major
%define libecpg_name  libecpg%libecpg_major

Name: %prog_name%postgresql_major-1C
Version: %postgresql_major.%postgresql_minor
Release: alt%postgresql_altrel

Summary: PostgreSQL client programs and libraries (edition for 1C 8.3.13 and later)
License: PostgreSQL
Group: Databases
URL: http://www.postgresql.org/

Packager: PostgreSQL Maintainers Team <pgsql@packages.altlinux.org>

%define PGSQL pgsql
%define docdir %_docdir/%prog_name-%version

Source0: %name-%version.tar

Patch3: 0003-Use-terminfo-not-termcap.patch
Patch5: 0005-Setup-logging.patch
Patch6: 0006-Workaround-for-will-always-overflow-destination-buff.patch
Patch8: 0001-Add-postgresql-startup-method-through-service-1-to-i.patch
Patch9: 0008-Add_event-id_to_jsonlog.patch

# 1C
Patch101: 00001-1C-FULL.patch
Patch103: 00003-1C-Fix-test-aggregates.patch

Conflicts: %{prog_name}13
Conflicts: %{prog_name}14
Conflicts: %{prog_name}15
Conflicts: %{prog_name}16
Conflicts: %{prog_name}17
Conflicts: %{prog_name}17-1C
Conflicts: %{prog_name}18

BuildRequires: OpenSP docbook-style-dsssl docbook-style-dsssl-utils docbook-style-xsl flex libldap-devel libossp-uuid-devel libpam-devel libreadline-devel libssl-devel libxslt-devel openjade perl-DBI perl-devel postgresql-common python3-dev setproctitle-devel tcl-devel xsltproc zlib-devel
BuildRequires: libselinux-devel libkrb5-devel liblz4-devel libzstd-devel libuuid-devel libnuma-devel liburing-devel
%if_with icu
BuildRequires: libicu-devel
%endif
%if_with jit
BuildRequires: llvm20.1-devel clang20.1-devel gcc-c++
%endif
%if_without devel
BuildRequires: libpq5
%endif
# Need for make check
BuildRequires: rpm-build-vm rpm-build-vm-createimage
%if_with coverage
BuildRequires: lcov
%endif

%description
PostgreSQL is an advanced Object-Relational database management system
(DBMS) that supports almost all SQL constructs (including
transactions, subselects and user-defined types and functions). The
postgresql package includes the client programs and libraries that
you'll need to access a PostgreSQL DBMS server.  These PostgreSQL
client programs are programs that directly manipulate the internal
structure of PostgreSQL databases on a PostgreSQL server. These client
programs can be located on the same machine with the PostgreSQL
server, or may be on a remote machine which accesses a PostgreSQL
server over a network connection. This package contains the docs
in HTML for the whole package, as well as command-line utilities for
managing PostgreSQL databases on a PostgreSQL server.

If you want to manipulate a PostgreSQL database on a remote PostgreSQL
server, you need this package. You also need to install this package
if you're installing the postgresql-server package.

%if_with devel
%package -n %libpq_name
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases
Requires: %libpq_name-%postgresql_major-1C = %EVR

%description -n %libpq_name
C and C++ libraries to enable user programs to communicate with the
PostgreSQL database backend. The backend can be on another machine and
accessed through TCP/IP.

%package -n libpq-devel
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases
Requires: %libpq_name-%postgresql_major-1C-devel = %EVR

%description -n libpq-devel
The libpq package provides the essential shared library for any PostgreSQL
client program or interface.  You will need to install this package to build any
package or any clients that need to connect to a PostgreSQL server.

%package -n libpq-devel-static
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases
Requires: %libpq_name-%postgresql_major-1C-devel-static = %EVR

%description -n libpq-devel-static
Development static library for %libpq_name-1C-devel

%package -n %libpq_name-%postgresql_major-1C
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases

Conflicts: %libpq_name-13
Conflicts: %libpq_name-14
Conflicts: %libpq_name-15
Conflicts: %libpq_name-16
Conflicts: %libpq_name-17
Conflicts: %libpq_name-17-1C
Conflicts: %libpq_name-18

%description -n %libpq_name-%postgresql_major-1C
C and C++ libraries to enable user programs to communicate with the
PostgreSQL database backend. The backend can be on another machine and
accessed through TCP/IP.

%package -n libecpg-devel
Summary: Development files for ECPG - Embedded SQL in C
Group: Development/Databases
Requires: %libecpg_name-%postgresql_major-1C-devel = %EVR

%description -n libecpg-devel
ECPG development files.  You will need to install this package to build any
package or any clients that use the ECPG to connect to a PostgreSQL server.

%package -n libecpg-devel-static
Summary: Development static library for libecpg-devel
Group: Development/Databases
Requires: %libecpg_name-%postgresql_major-1C-devel-static = %EVR

%description -n libecpg-devel-static
Development static library for libecpg-devel

%package -n %prog_name-devel
Summary: PostgreSQL development header files
Group: Development/Databases
Requires: %name-devel = %EVR

%description -n %prog_name-devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.

%package -n %prog_name-devel-static
Summary: Development static library for %libpq_name-1C-devel and %libecpg_name-1C-devel
Group: Development/Databases
Requires: %libpq_name-%postgresql_major-1C-devel-static = %EVR
Requires: %libecpg_name-%postgresql_major-1C-devel-static = %EVR
Requires: %name-devel-static = %EVR

%description -n %prog_name-devel-static
Development static library for %libpq_name-1C-devel
and %libecpg_name-%postgresql_major-1C-devel
%endif

%package -n %libpq_name-%postgresql_major-1C-devel
Summary: The shared libraries required for any PostgreSQL clients
Group: Development/Databases
%if_with devel
Requires: %libpq_name-%postgresql_major-1C = %EVR
%else
Requires: libpq5
%add_findprov_skiplist %_libdir/pkgconfig/*.pc
%add_findprov_skiplist %_libdir/libpq*.so.*
%endif

Conflicts: %libpq_name-13-devel
Conflicts: %libpq_name-14-devel
Conflicts: %libpq_name-15-devel
Conflicts: %libpq_name-16-devel
Conflicts: %libpq_name-17-devel
Conflicts: %libpq_name-17-1C-devel
Conflicts: %libpq_name-18-devel

%description -n %libpq_name-%postgresql_major-1C-devel
The libpq package provides the essential shared library for any PostgreSQL
client program or interface.  You will need to install this package to build any
package or any clients that need to connect to a PostgreSQL server.

%package -n %libpq_name-%postgresql_major-1C-devel-static
Summary: Development static library for %libpq_name-devel
Group: Development/Databases
Requires: %libpq_name-%postgresql_major-1C-devel = %EVR

%description -n %libpq_name-%postgresql_major-1C-devel-static
Development static library for %libpq_name-devel

%package devel
Summary: PostgreSQL development header files
Group: Development/Databases
Requires: %libpq_name-%postgresql_major-1C-devel = %EVR
Requires: %libecpg_name-%postgresql_major-1C-devel = %EVR
Requires: %name-server-devel = %EVR

Conflicts: %{prog_name}13-devel
Conflicts: %{prog_name}14-devel
Conflicts: %{prog_name}15-devel
Conflicts: %{prog_name}16-devel
Conflicts: %{prog_name}17-devel
Conflicts: %{prog_name}17-1C-devel
Conflicts: %{prog_name}18-devel

%description devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.

%package devel-static
Summary: Development static library for %libpq_name-devel and %libecpg_name-devel
Group: Development/Databases
Requires: %libpq_name-%postgresql_major-1C-devel-static = %EVR
Requires: %libecpg_name-%postgresql_major-1C-devel-static = %EVR
Requires: %name-devel = %EVR

%description devel-static
Development static library for %libpq_name-devel
and %libecpg_name-%postgresql_major-1C-devel

%package -n rpm-macros-%prog_name-%postgresql_major-1C
Summary: RPM macros to PostgreSQL
Group: Development/Other
BuildArch: noarch
%if_with devel
Provides: rpm-macros-%prog_name
%endif
Conflicts: rpm-macros-%prog_name-13
Conflicts: rpm-macros-%prog_name-14
Conflicts: rpm-macros-%prog_name-15
Conflicts: rpm-macros-%prog_name-16
Conflicts: rpm-macros-%prog_name-17
Conflicts: rpm-macros-%prog_name-17-1C
Conflicts: rpm-macros-%prog_name-18

%description -n rpm-macros-%prog_name-%postgresql_major-1C
RPM macros to PostgreSQL for build server extentions

%package -n %libecpg_name-%postgresql_major-1C
Summary: ECPG - Embedded SQL in C
Group: Databases
Requires: %libpq_name-%postgresql_major-1C-devel = %EVR
%if_without devel
%add_findprov_skiplist %_libdir/libecpg*.so*
%add_findprov_skiplist %_libdir/libpgtypes*.so*
%add_findreq_skiplist %_libdir/libecpg*.so*
%add_findreq_skiplist %_libdir/libpgtypes*.so*
%endif
Conflicts: %libecpg_name-13
Conflicts: %libecpg_name-14
Conflicts: %libecpg_name-15
Conflicts: %libecpg_name-16
Conflicts: %libecpg_name-17
Conflicts: %libecpg_name-17-1C
Conflicts: %libecpg_name-18

%description -n %libecpg_name-%postgresql_major-1C
An embedded SQL program consists of code written in an ordinary programming
language, in this case C, mixed with SQL commands in specially marked sections.
To build the program, the source code (*.pgc) is first passed through the
embedded SQL preprocessor, which converts it to an ordinary C program (*.c), and
afterwards it can be processed by a C compiler.

%package -n %libecpg_name-%postgresql_major-1C-devel
Summary: Development files for ECPG - Embedded SQL in C
Group: Development/Databases
Requires: %libecpg_name-%postgresql_major-1C = %EVR
%if_without devel
%add_findprov_skiplist %_libdir/pkgconfig/*.pc
%endif
Conflicts: %libecpg_name-13-devel
Conflicts: %libecpg_name-14-devel
Conflicts: %libecpg_name-15-devel
Conflicts: %libecpg_name-16-devel
Conflicts: %libecpg_name-17-devel
Conflicts: %libecpg_name-17-1C-devel
Conflicts: %libecpg_name-18-devel

%description -n %libecpg_name-%postgresql_major-1C-devel
ECPG development files.  You will need to install this package to build any
package or any clients that use the ECPG to connect to a PostgreSQL server.

%package -n %libecpg_name-%postgresql_major-1C-devel-static
Summary: Development static library for %libecpg_name-devel
Group: Development/Databases
Requires: %libecpg_name-%postgresql_major-1C-devel = %EVR

Conflicts: %libecpg_name-13-devel-static
Conflicts: %libecpg_name-14-devel-static
Conflicts: %libecpg_name-15-devel-static
Conflicts: %libecpg_name-16-devel-static
Conflicts: %libecpg_name-17-devel-static
Conflicts: %libecpg_name-17-1C-devel-static
Conflicts: %libecpg_name-18-devel-static

%description -n %libecpg_name-%postgresql_major-1C-devel-static
Development static library for %libecpg_name-%postgresql_major-1C-devel

%package server-devel
Summary: PostgreSQL development header files
Group: Development/Databases
Requires: %libpq_name-%postgresql_major-1C-devel
Requires: %libecpg_name-%postgresql_major-1C-devel
%if_with jit
Requires: llvm20.1-devel clang20.1-devel gcc-c++
%endif
%if_with devel
Provides: %prog_name-server-devel = %EVR
Obsoletes: %prog_name-server-devel < %EVR
%endif
%filter_from_requires /^\/usr\/include\/pgsql\/libpq-fe\.h/d

Conflicts: %{prog_name}13-server-devel
Conflicts: %{prog_name}14-server-devel
Conflicts: %{prog_name}15-server-devel
Conflicts: %{prog_name}16-server-devel
Conflicts: %{prog_name}17-server-devel
Conflicts: %{prog_name}17-1C-server-devel
Conflicts: %{prog_name}18-server-devel

%description server-devel
The %name-server-devel package contains the header files and configuration
needed to compile PostgreSQL server extension.

%package docs
Summary: Extra documentation for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
BuildArch: noarch
# 1C
Conflicts: %{prog_name}17-1C-docs

%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in other formats, and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
# 1C
Conflicts: %{prog_name}17-1C-contrib

%description contrib
The postgresql-contrib package includes the contrib tree distributed with (edition for 1C 8.3.13 and later)
the PostgreSQL tarball.  Selected contrib modules are prebuilt.

%package server
Summary: The programs needed to create and run a PostgreSQL server (edition for 1C 8.3.13 and later)
Group: Databases
Requires(pre): shadow-utils, syslogd-daemon, grep, sed
Requires(pre): postgresql-common > 1.0-alt8
Requires: %name = %EVR
Requires: glibc-locales

Conflicts: %{prog_name}13-server
Conflicts: %{prog_name}14-server
Conflicts: %{prog_name}15-server
Conflicts: %{prog_name}16-server
Conflicts: %{prog_name}17-server
Conflicts: %{prog_name}17-1C-server
Conflicts: %{prog_name}18-server

%description server
The postgresql-server package includes the programs needed to create
and run a PostgreSQL server, which will in turn allow you to create
and maintain PostgreSQL databases.  PostgreSQL is an advanced
Object-Relational database management system (DBMS) that supports
almost all SQL constructs (including transactions, subselects and
user-defined types and functions). You should install
postgresql-server if you want to create and maintain your own
PostgreSQL databases and/or your own PostgreSQL server. You also need
to install the postgresql package.


%package tcl
Summary: The PL/Tcl procedural language for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
# 1C
Conflicts: %{prog_name}17-1C-tcl

%description tcl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-tcl package contains the PL/Tcl procedural language
for the backend.

%package perl
Summary: The PL/Perl procedural language for PostgreSQL (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
# 1C
Conflicts: %{prog_name}17-1C-perl

%description perl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-perl package contains the PL/Perl procedural
language for the backend.

%package python
Summary: Development module for Python code to access a PostgreSQL DB (edition for 1C 8.3.13 and later)
Group: Databases
Requires: %name-server = %EVR
# 1C
Conflicts: %{prog_name}17-1C-python

%description python
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-python package includes a module for
developers to use when writing Python code for accessing a PostgreSQL
database.

%if_with jit
%package llvmjit
Summary: Just-in-time compilation support for PostgreSQL
Group: Databases
Requires: %name-server = %EVR
Requires: llvm20.1

%description llvmjit
The postgresql-llvmjit package contains support for
just-in-time compiling parts of PostgreSQL queries. Using LLVM it
compiles e.g. expressions and tuple deforming into native code, with the
goal of accelerating analytics queries.
%endif

%prep
%setup -q

%patch3 -p2
%patch5 -p1
%patch6 -p2
%patch8 -p1
%patch9 -p1

# 1C
%patch101 -p1
%patch103 -p1

%ifarch %e2k
# disable SSE4.2 emulation
sed -i 's/_mm_crc32_/_no_crc32_/g' configure* meson.build config/c-compiler.m4
%endif

%build
export CC=%__cc
export CXX=%__cxx

%if_with jit
export LLVM_CONFIG=/usr/bin/llvm-config-20
export CLANG=/usr/bin/clang-20
%endif

 %{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf

%configure --includedir=%_includedir/%PGSQL \
    --sysconfdir=%_sysconfdir/%PGSQL \
    --datadir=%_datadir/%PGSQL \
    --disable-rpath \
    --enable-nls \
    --enable-thread-safety \
%if_with icu
    --with-icu \
%endif
%if_with jit
    --with-llvm \
%endif
%if_with coverage
    --enable-coverage \
%endif
    --with-docdir=%docdir \
    --with-includes=%_includedir/krb5 \
    --with-pam \
    --with-openssl \
    --with-perl \
    --with-gssapi \
    --with-krb5 \
    --with-ldap \
    --with-tcl --with-tclconfig=%_libdir \
    --with-readline \
    --with-python \
    --with-libxml \
    --with-selinux \
    --with-libxslt \
    --with-gnu-ld \
    --with-ossp-uuid \
    --with-lz4 \
    --with-zstd \
    --with-libnuma \
    --with-liburing

%make_build pkglibdir=%_libdir/%PGSQL

pushd contrib
%make_build all libdir=%_libdir/%PGSQL/contrib
popd

# adjust dockbook styles
find doc/src/sgml/ -type f -name "stylesheet.*" -print0 | xargs -0 sed -i \
	-e "s,http://docbook.sourceforge.net/release/xsl/current,/usr/share/xml/docbook/xsl-stylesheets,g" --
%make_build -C doc all

%ifnarch %ix86
%check
vm-run --rootfs --user --sudo --cpu=1 "sudo mount -o remount,size=256M /dev/shm; make check pkglibdir=%_libdir/%PGSQL"
%endif

%install
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL
%make_build -C doc install DESTDIR=%buildroot docdir=%docdir

##### ALT-stuff
pushd altlinux

# The initscripts....
install -p -m644 -D postgresql.sysconfig %buildroot%_sysconfdir/sysconfig/%prog_name
install -p -m755 -D postgresql.init.in %buildroot%_initdir/%prog_name


# README.ALT
install -p -m 644 -D README.ALT-ru_RU.UTF-8 %buildroot%docdir/README.ALT-ru_RU.UTF-8
install -p -m 644 -D README.rpm-dist %buildroot%docdir/README.rpm-dist

install -p -m 644 -D postgresql.service %buildroot%_unitdir/postgresql.service
install -p -m 755 -D pg_initdb.in %buildroot%_bindir/pg_initdb

popd
##### end ALT-stuff

# Create file for rpm-build-postgresql
install -d %buildroot%_rpmmacrosdir
echo "%%pg_ver %postgresql_major" > %buildroot%_rpmmacrosdir/postgresql

sed -e 's|^PGVERSION=.*$|PGVERSION=%version|' \
        -e 's|^PGDOCDIR=.*$|PGDOCDIR=%docdir|' \
        < altlinux/postgresql-check-db-dir >postgresql-check-db-dir
touch -r postgresql-check-db-dir postgresql-check-db-dir
install -m 755 postgresql-check-db-dir %buildroot%_bindir/postgresql-check-db-dir

# Fix initscript versions

sed -i 's,@VERSION@,%postgresql_major,' %buildroot%_initdir/%prog_name
sed -i 's,@FULLVERSION@,%version,' %buildroot%_initdir/%prog_name

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m700 %buildroot%_localstatedir/%PGSQL/data

# backups of data go here...
install -d -m700 %buildroot%_localstatedir/%PGSQL/backups

# Fix a dangling symlink
ln -s %_includedir/%PGSQL %buildroot%_includedir/postgresql

install -dm700 %buildroot%_localstatedir/%PGSQL

pushd contrib
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL docdir=%docdir
popd

# Copy pg_config for server-devel
cp -a %buildroot%_bindir/pg_config %buildroot%_bindir/pg_server_config

cp -a COPYRIGHT README.md \
    doc/{KNOWN_BUGS,MISSING_FEATURES,TODO} \
    src/tutorial %buildroot%docdir/

# Install log directory
install -d %buildroot%_logdir/postgres

%find_lang ecpglib%libecpg_major-%postgresql_major
%find_lang ecpg-%postgresql_major
%find_lang initdb-%postgresql_major
%find_lang libpq%libpq_major-%postgresql_major
%find_lang pg_amcheck-%postgresql_major
%find_lang pg_archivecleanup-%postgresql_major
%find_lang pg_basebackup-%postgresql_major
%find_lang pg_config-%postgresql_major
%find_lang pg_controldata-%postgresql_major
%find_lang pg_ctl-%postgresql_major
%find_lang pg_createsubscriber-%postgresql_major
%find_lang pg_dump-%postgresql_major
%find_lang pg_resetwal-%postgresql_major
%find_lang pg_rewind-%postgresql_major
%find_lang pg_test_fsync-%postgresql_major
%find_lang pg_test_timing-%postgresql_major
%find_lang pg_upgrade-%postgresql_major
%find_lang pg_waldump-%postgresql_major
%find_lang pg_walsummary-%postgresql_major
%find_lang pgscripts-%postgresql_major
%find_lang plperl-%postgresql_major
%find_lang plpgsql-%postgresql_major
%find_lang plpython-%postgresql_major
%find_lang pltcl-%postgresql_major
%find_lang postgres-%postgresql_major
%find_lang psql-%postgresql_major
%find_lang pg_checksums-%postgresql_major
%find_lang pg_combinebackup-%postgresql_major
%find_lang pg_verifybackup-%postgresql_major

cat psql-%postgresql_major.lang \
    pg_dump-%postgresql_major.lang \
    pgscripts-%postgresql_major.lang \
    pg_basebackup-%postgresql_major.lang \
    pg_combinebackup-%postgresql_major.lang \
    pg_test_fsync-%postgresql_major.lang \
    pg_test_timing-%postgresql_major.lang \
    pg_verifybackup-%postgresql_major.lang \
    pg_amcheck-%postgresql_major.lang > main.lang

cat postgres-%postgresql_major.lang \
    pg_controldata-%postgresql_major.lang \
    initdb-%postgresql_major.lang \
    pg_ctl-%postgresql_major.lang \
    plpgsql-%postgresql_major.lang \
    pg_rewind-%postgresql_major.lang \
    pg_upgrade-%postgresql_major.lang \
    pg_resetwal-%postgresql_major.lang \
    pg_waldump-%postgresql_major.lang \
    pg_walsummary-%postgresql_major.lang \
    pg_checksums-%postgresql_major.lang \
    pg_createsubscriber-%postgresql_major.lang > server.lang

cat pg_config-%postgresql_major.lang > devel.lang

cat ecpg-%postgresql_major.lang > ecpg.lang

cat ecpglib%libecpg_major-%postgresql_major.lang > ecpglib.lang

cat pg_archivecleanup-%postgresql_major.lang > contrib.lang

%pre
# Need to make backups of some executables if an upgrade
# They will be needed to do a dump of the old version's database.
# All output redirected to /dev/null.
exec &>/dev/null
if [ -d %_libdir/%PGSQL ]
then
    if [ ! -d %_libdir/%PGSQL/backup ]; then
        mkdir -p %_libdir/%PGSQL/backup
    fi
    cd %_bindir
    cp -fp pg_dump pg_dumpall psql %_libdir/%PGSQL/backup || :
fi

%pre server
exec &>/dev/null

if [ -d %_libdir/%PGSQL ]
then
   if [ ! -d %_libdir/%PGSQL/backup ]; then
       mkdir -p %_libdir/%PGSQL/backup
   fi
   cd %_bindir
   cp -fp pg_controldata pg_ctl pg_resetwal postgres %_libdir/%PGSQL/backup

   # Need for PG 15 and older
   if [ -f %_bindir/postmaster ]; then
       cp -fp postmaster %_libdir/%PGSQL/backup
   fi
fi

%post server
echo PGLIB=%_datadir/%PGSQL >> ~postgres/.bash_profile
echo PGDATA=%_localstatedir/%PGSQL/data >> ~postgres/.bash_profile
echo export PGLIB PGDATA >> ~postgres/.bash_profile
chown postgres:postgres ~postgres/.bash_profile

%post_service %prog_name

%preun server
%preun_service %prog_name

# $2, holds the number of instances of the target package that will remain
# after the operation if $2 is 0, the target package will be removed
%triggerpostun -- %{prog_name}13-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}14-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}14-1C-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}15-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}16-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}17-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}17-1C-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}18-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%triggerpostun -- %{prog_name}18-1C-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%files -f main.lang
%_bindir/clusterdb
%_bindir/createdb
%_bindir/createuser
%_bindir/dropdb
%_bindir/dropuser
%_bindir/pg_amcheck
%_bindir/pg_dump
%_bindir/pg_dumpall
%_bindir/pg_restore
%_bindir/psql
%_bindir/reindexdb
%_bindir/vacuumdb
%_bindir/pg_basebackup
%_bindir/pg_combinebackup
%_bindir/pg_test_fsync
%_bindir/pg_test_timing
%_bindir/pg_isready
%_bindir/pg_recvlogical
%_bindir/pg_verifybackup
%_man1dir/clusterdb.1*
%_man1dir/createdb.1*
%_man1dir/createuser.1*
%_man1dir/dropdb.1*
%_man1dir/dropuser.1*
%_man1dir/pg_amcheck.1*
%_man1dir/pg_dump.1*
%_man1dir/pg_restore.1*
%_man1dir/pg_dumpall.1*
%_man1dir/pg_test_fsync.1*
%_man1dir/pg_test_timing.1*
%_man1dir/psql.1*
%_man1dir/reindexdb.1*
%_man1dir/vacuumdb.1*
%_man1dir/pg_basebackup.1*
%_man1dir/pg_combinebackup.1*
%_man1dir/pg_isready.1*
%_man1dir/pg_recvlogical.1*
%_man1dir/pg_verifybackup.1*
%_man7dir/*
%dir %docdir
%docdir/KNOWN_BUGS
%docdir/MISSING_FEATURES
%docdir/TODO
%docdir/COPYRIGHT
%docdir/README.md

%files docs
%dir %docdir
%dir %docdir/html
%docdir/html/*.html
%docdir/html/*.css
%docdir/html/*.svg
%dir %docdir/tutorial
%docdir/tutorial/*
%docdir/contrib
%docdir/extension

%files -f contrib.lang contrib
%_bindir/oid2name
%_bindir/pgbench
%_bindir/vacuumlo
%_bindir/pg_archivecleanup

%_man1dir/oid2name.1*
%_man1dir/pg_archivecleanup.1*
%_man1dir/pgbench.1*
%_man1dir/vacuumlo.1*

%dir %_datadir/%PGSQL/contrib
%dir %_libdir/%PGSQL

%_libdir/%PGSQL/_int.so
%_datadir/%PGSQL/extension/intarray-*.sql
%_datadir/%PGSQL/extension/intarray.control
%_libdir/%PGSQL/amcheck.so
%_datadir/%PGSQL/extension/amcheck-*.sql
%_datadir/%PGSQL/extension/amcheck.control
%_libdir/%PGSQL/auth_delay.so
%_libdir/%PGSQL/autoinc.so
%_datadir/%PGSQL/extension/autoinc-*.sql
%_datadir/%PGSQL/extension/autoinc.control
%_libdir/%PGSQL/bloom.so
%_datadir/%PGSQL/extension/bloom-*.sql
%_datadir/%PGSQL/extension/bloom.control
%_libdir/%PGSQL/btree_gin.so
%_datadir/%PGSQL/extension/btree_gin-*.sql
%_datadir/%PGSQL/extension/btree_gin.control
%_libdir/%PGSQL/btree_gist.so
%_datadir/%PGSQL/extension/btree_gist-*.sql
%_datadir/%PGSQL/extension/btree_gist.control
%_libdir/%PGSQL/citext.so
%_datadir/%PGSQL/extension/citext-*.sql
%_datadir/%PGSQL/extension/citext.control
%_libdir/%PGSQL/cube.so
%_datadir/%PGSQL/extension/cube-*.sql
%_datadir/%PGSQL/extension/cube.control
%_libdir/%PGSQL/dblink.so
%_datadir/%PGSQL/extension/dblink-*.sql
%_datadir/%PGSQL/extension/dblink.control
%_libdir/%PGSQL/dict_int.so
%_datadir/%PGSQL/extension/dict_int-*.sql
%_datadir/%PGSQL/extension/dict_int.control
%_libdir/%PGSQL/dict_xsyn.so
%_datadir/%PGSQL/extension/dict_xsyn-*.sql
%_datadir/%PGSQL/extension/dict_xsyn.control
%_libdir/%PGSQL/earthdistance.so
%_datadir/%PGSQL/extension/earthdistance-*.sql
%_datadir/%PGSQL/extension/earthdistance.control
%_libdir/%PGSQL/file_fdw.so
%_datadir/%PGSQL/extension/file_fdw-*.sql
%_datadir/%PGSQL/extension/file_fdw.control
%_libdir/%PGSQL/fuzzystrmatch.so
%_datadir/%PGSQL/extension/fuzzystrmatch-*.sql
%_datadir/%PGSQL/extension/fuzzystrmatch.control
%_libdir/%PGSQL/hstore.so
%_datadir/%PGSQL/extension/hstore-*.sql
%_datadir/%PGSQL/extension/hstore.control
%_libdir/%PGSQL/hstore_plperl.so
%_datadir/%PGSQL/extension/hstore_plperl*.sql
%_datadir/%PGSQL/extension/hstore_plperl*.control
%_libdir/%PGSQL/hstore_plpython3.so
%_datadir/%PGSQL/extension/hstore_plpython3u-*.sql
%_datadir/%PGSQL/extension/hstore_plpython3u.control
%_libdir/%PGSQL/insert_username.so
%_datadir/%PGSQL/extension/insert_username-*.sql
%_datadir/%PGSQL/extension/insert_username.control
%_datadir/%PGSQL/extension/intagg-*.sql
%_datadir/%PGSQL/extension/intagg.control
%_libdir/%PGSQL/isn.so
%_datadir/%PGSQL/extension/isn-*.sql
%_datadir/%PGSQL/extension/isn.control
%_libdir/%PGSQL/jsonb_plperl.so
%_datadir/%PGSQL/extension/jsonb_plperl-*.sql
%_datadir/%PGSQL/extension/jsonb_plperl.control
%_datadir/%PGSQL/extension/jsonb_plperlu-*.sql
%_datadir/%PGSQL/extension/jsonb_plperlu.control
%_libdir/%PGSQL/jsonb_plpython3.so
%_datadir/%PGSQL/extension/jsonb_plpython3u-*.sql
%_datadir/%PGSQL/extension/jsonb_plpython3u.control
%_libdir/%PGSQL/lo.so
%_datadir/%PGSQL/extension/lo-*.sql
%_datadir/%PGSQL/extension/lo.control
%_libdir/%PGSQL/ltree.so
%_datadir/%PGSQL/extension/ltree-*.sql
%_datadir/%PGSQL/extension/ltree.control
%_libdir/%PGSQL/ltree_plpython3.so
%_datadir/%PGSQL/extension/ltree_plpython3u-*.sql
%_datadir/%PGSQL/extension/ltree_plpython3u.control
%_libdir/%PGSQL/moddatetime.so
%_datadir/%PGSQL/extension/moddatetime-*.sql
%_datadir/%PGSQL/extension/moddatetime.control
%_libdir/%PGSQL/pageinspect.so
%_datadir/%PGSQL/extension/pageinspect-*.sql
%_datadir/%PGSQL/extension/pageinspect.control
%_libdir/%PGSQL/passwordcheck.so
%_libdir/%PGSQL/pg_buffercache.so
%_datadir/%PGSQL/extension/pg_buffercache-*.sql
%_datadir/%PGSQL/extension/pg_buffercache.control
%_libdir/%PGSQL/pg_freespacemap.so
%_datadir/%PGSQL/extension/pg_freespacemap-*.sql
%_datadir/%PGSQL/extension/pg_freespacemap.control
%_libdir/%PGSQL/pg_logicalinspect.so
%_datadir/%PGSQL/extension/pg_logicalinspect-*.sql
%_datadir/%PGSQL/extension/pg_logicalinspect.control
%_libdir/%PGSQL/pg_prewarm.so
%_datadir/%PGSQL/extension/pg_prewarm-*.sql
%_datadir/%PGSQL/extension/pg_prewarm.control
%_libdir/%PGSQL/pg_surgery.so
%_datadir/%PGSQL/extension/pg_surgery-*.sql
%_datadir/%PGSQL/extension/pg_surgery.control
%_libdir/%PGSQL/pg_trgm.so
%_datadir/%PGSQL/extension/pg_trgm-*.sql
%_datadir/%PGSQL/extension/pg_trgm.control
%_libdir/%PGSQL/pg_visibility.so
%_datadir/%PGSQL/extension/pg_visibility-*.sql
%_datadir/%PGSQL/extension/pg_visibility.control
%_libdir/%PGSQL/pg_walinspect.so
%_datadir/%PGSQL/extension/pg_walinspect-*.sql
%_datadir/%PGSQL/extension/pg_walinspect.control
%_libdir/%PGSQL/pgcrypto.so
%_datadir/%PGSQL/extension/pgcrypto-*.sql
%_datadir/%PGSQL/extension/pgcrypto.control
%_libdir/%PGSQL/pgoutput.so
%_libdir/%PGSQL/pgrowlocks.so
%_datadir/%PGSQL/extension/pgrowlocks-*.sql
%_datadir/%PGSQL/extension/pgrowlocks.control
%_libdir/%PGSQL/pgstattuple.so
%_datadir/%PGSQL/extension/pgstattuple-*.sql
%_datadir/%PGSQL/extension/pgstattuple.control
%_libdir/%PGSQL/pgxml.so
%_datadir/%PGSQL/extension/xml2-*.sql
%_datadir/%PGSQL/extension/xml2.control
%_libdir/%PGSQL/postgres_fdw.so
%_datadir/%PGSQL/extension/postgres_fdw-*.sql
%_datadir/%PGSQL/extension/postgres_fdw.control
%_libdir/%PGSQL/refint.so
%_datadir/%PGSQL/extension/refint-*.sql
%_datadir/%PGSQL/extension/refint.control
%_libdir/%PGSQL/seg.so
%_datadir/%PGSQL/extension/seg-*.sql
%_datadir/%PGSQL/extension/seg.control
%_libdir/%PGSQL/sepgsql.so
%_datadir/%PGSQL/contrib/sepgsql.sql
%_libdir/%PGSQL/sslinfo.so
%_datadir/%PGSQL/extension/sslinfo-*.sql
%_datadir/%PGSQL/extension/sslinfo.control
%_libdir/%PGSQL/tablefunc.so
%_datadir/%PGSQL/extension/tablefunc-*.sql
%_datadir/%PGSQL/extension/tablefunc.control
%_libdir/%PGSQL/tcn.so
%_datadir/%PGSQL/extension/tcn-*.sql
%_datadir/%PGSQL/extension/tcn.control
%_libdir/%PGSQL/test_decoding.so
%_libdir/%PGSQL/tsm_system_rows.so
%_datadir/%PGSQL/extension/tsm_system_rows-*.sql
%_datadir/%PGSQL/extension/tsm_system_rows.control
%_libdir/%PGSQL/tsm_system_time.so
%_datadir/%PGSQL/extension/tsm_system_time-*.sql
%_datadir/%PGSQL/extension/tsm_system_time.control
%_libdir/%PGSQL/unaccent.so
%_datadir/%PGSQL/extension/unaccent-*.sql
%_datadir/%PGSQL/extension/unaccent.control
%_libdir/%PGSQL/uuid-ossp.so
%_datadir/%PGSQL/extension/uuid-ossp-*.sql
%_datadir/%PGSQL/extension/uuid-ossp.control

%files -f server.lang server
%config %_initdir/%prog_name
%config %_sysconfdir/sysconfig/*
%_bindir/initdb
%_bindir/pg_initdb
%_bindir/postgresql-check-db-dir
%_bindir/pg_controldata
%_bindir/pg_createsubscriber
%_bindir/pg_ctl
%_bindir/postgres
%_bindir/pg_upgrade
%_bindir/pg_rewind
%_bindir/pg_receivewal
%_bindir/pg_resetwal
%_bindir/pg_waldump
%_bindir/pg_checksums
%_bindir/pg_walsummary

%_man1dir/initdb.1*
%_man1dir/pg_controldata.1*
%_man1dir/pg_ctl.1*
%_man1dir/pg_createsubscriber.1*
%_man1dir/pg_upgrade.1*
%_man1dir/postgres.1*
%_man1dir/pg_rewind.1*
%_man1dir/pg_receivewal.1*
%_man1dir/pg_resetwal.1*
%_man1dir/pg_waldump.1*
%_man1dir/pg_checksums.1*
%_man1dir/pg_walsummary.1*

%dir %_libdir/%PGSQL
%dir %_datadir/%PGSQL/extension
%_libdir/%PGSQL/plpgsql.so
%_datadir/%PGSQL/extension/plpgsql-*.sql
%_datadir/%PGSQL/extension/plpgsql.control
%_libdir/%PGSQL/basebackup_to_shell.so
%_libdir/%PGSQL/basic_archive.so
%_libdir/%PGSQL/dbcopies_decoding.so
%_libdir/%PGSQL/dict_snowball.so
%_libdir/%PGSQL/*_and_*.so
%_libdir/%PGSQL/euc2004_sjis2004.so
%_libdir/%PGSQL/libpqwalreceiver.so
%_libdir/%PGSQL/pg_overexplain.so
%_libdir/%PGSQL/online_analyze.so
%_libdir/%PGSQL/plantuner.so
%dir %_datadir/%PGSQL
%_datadir/%PGSQL/errcodes.txt
%dir %_datadir/%PGSQL/timezone
%_datadir/%PGSQL/timezone/*
%dir %_datadir/%PGSQL/timezonesets
%_datadir/%PGSQL/timezonesets/*
%dir %_datadir/%PGSQL/tsearch_data
%_datadir/%PGSQL/tsearch_data/*
%_datadir/%PGSQL/postgres.bki
%_datadir/%PGSQL/*.sample
%_datadir/%PGSQL/information_schema.sql
%_datadir/%PGSQL/sql_features.txt
%_datadir/%PGSQL/system_constraints.sql
%_datadir/%PGSQL/system_functions.sql
%_datadir/%PGSQL/system_views.sql
%_datadir/%PGSQL/snowball_create.sql
%_libdir/%PGSQL/auto_explain.so
%_libdir/%PGSQL/auto_dump.so
%_datadir/%PGSQL/extension/auto_dump-*.sql
%_datadir/%PGSQL/extension/auto_dump.control
%_libdir/%PGSQL/fasttrun.so
%_datadir/%PGSQL/extension/fasttrun-*.sql
%_datadir/%PGSQL/extension/fasttrun.control
%_libdir/%PGSQL/fulleq.so
%_datadir/%PGSQL/extension/fulleq-*.sql
%_datadir/%PGSQL/extension/fulleq.control
%_libdir/%PGSQL/mchar.so
%_datadir/%PGSQL/extension/mchar-*.sql
%_datadir/%PGSQL/extension/mchar.control
%_libdir/%PGSQL/pg_stat_statements.so
%_datadir/%PGSQL/extension/pg_stat_statements-*.sql
%_datadir/%PGSQL/extension/pg_stat_statements.control
%_libdir/%PGSQL/pg_wait_sampling.so
%_datadir/%PGSQL/extension/pg_wait_sampling-*.sql
%_datadir/%PGSQL/extension/pg_wait_sampling.control
%_localstatedir/%PGSQL
%docdir/README.ALT-ru_RU.UTF-8
%docdir/README.rpm-dist
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL/backups
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL/data
%attr(750,postgres,postgres)  %dir %_logdir/postgres
%_unitdir/*

%files server-devel
%_bindir/pg_server_config
%_includedir/%PGSQL/server
%_libdir/%PGSQL/pgxs

%files -f pltcl-%postgresql_major.lang tcl
%_libdir/%PGSQL/pltcl.so
%_datadir/%PGSQL/extension/pltcl-*.sql
%_datadir/%PGSQL/extension/pltcl.control
%_datadir/%PGSQL/extension/pltclu-*.sql
%_datadir/%PGSQL/extension/pltclu.control

%files -f plperl-%postgresql_major.lang perl
%_libdir/%PGSQL/plperl.so
%_datadir/%PGSQL/extension/plperl-*.sql
%_datadir/%PGSQL/extension/plperl.control
%_datadir/%PGSQL/extension/plperlu-*.sql
%_datadir/%PGSQL/extension/plperlu.control
%_libdir/%PGSQL/bool_plperl.so
%_datadir/%PGSQL/extension/bool_plperl--1.0.sql
%_datadir/%PGSQL/extension/bool_plperl.control
%_datadir/%PGSQL/extension/bool_plperlu--1.0.sql
%_datadir/%PGSQL/extension/bool_plperlu.control

%files -f plpython-%postgresql_major.lang python
%_libdir/%PGSQL/plpython3.so
%_datadir/%PGSQL/extension/plpython3u-*.sql
%_datadir/%PGSQL/extension/plpython3u.control

%files -f ecpglib.lang -n %libecpg_name-%postgresql_major-1C
%_libdir/libecpg.so.%libecpg_major
%_libdir/libecpg.so.%libecpg_major.*
%_libdir/libecpg_compat.so.*
%_libdir/libpgtypes.so.*

%files -f ecpg.lang -n %libecpg_name-%postgresql_major-1C-devel
%_bindir/ecpg
%_includedir/%PGSQL/informix/esql
%_includedir/%PGSQL/ecpg*.h
%_includedir/%PGSQL/pgtypes*.h
%_includedir/%PGSQL/sql*.h
%_libdir/libecpg*.so
%_libdir/libpgtypes.so
%_libdir/pkgconfig/libecpg.pc
%_libdir/pkgconfig/libecpg_compat.pc
%_libdir/pkgconfig/libpgtypes.pc
%_man1dir/ecpg.*

%files -n %libecpg_name-%postgresql_major-1C-devel-static
%_libdir/libecpg*.a
%_libdir/libpgcommon.a
%_libdir/libpgcommon_shlib.a
%_libdir/libpgfeutils.a
%_libdir/libpgtypes.a
%_libdir/libpgport.a
%_libdir/libpgport_shlib.a

%files devel
%files devel-static

%if_with devel
%files -f libpq%libpq_major-%postgresql_major.lang -n %libpq_name-%postgresql_major-1C
%_libdir/libpq.so.%libpq_major
%_libdir/libpq.so.%libpq_major.*

%files -n %libpq_name
%files -n libpq-devel
%files -n libpq-devel-static
%files -n libecpg-devel
%files -n libecpg-devel-static
%files -n %prog_name-devel
%files -n %prog_name-devel-static
%endif

%files -f devel.lang -n %libpq_name-%postgresql_major-1C-devel
%_bindir/pg_config
%_includedir/%PGSQL
%_includedir/postgresql
%exclude %_includedir/%PGSQL/server
%exclude %_includedir/%PGSQL/informix/esql
%exclude %_includedir/%PGSQL/ecpg*.h
%exclude %_includedir/%PGSQL/pgtypes*.h
%exclude %_includedir/%PGSQL/sql*.h
%_libdir/libpq*.so
%if_without devel
# No pack libpq.so.%%libpq_major.* if major version 1C and vanilla same
#%_libdir/libpq.so.%libpq_major.*
%endif
%_libdir/pkgconfig/libpq.pc
%_man1dir/pg_config.*
%_man3dir/*

%files -n %libpq_name-%postgresql_major-1C-devel-static
%_libdir/libpq*.a

%files -n rpm-macros-%prog_name-%postgresql_major-1C
%_rpmmacrosdir/postgresql

%if_with jit
%files llvmjit
%_libdir/pgsql/bitcode
%_libdir/pgsql/llvmjit.so
%_libdir/pgsql/llvmjit_types.bc
%endif

%changelog
* Mon Jun 15 2026 Alexei Takaseev <taf@altlinux.org> 18.4-alt4
- Move extention auto_dump, auto_explain, fasttrun, fulleq, mchar,
  pg_stat_statements, pg_wait_sampling from -contrib to -server (ALT #59522)
- Fix run tests. Use 1 cpu

* Mon Jun 01 2026 Alexei Takaseev <taf@altlinux.org> 18.4-alt3
- Update 1C patch
- Drop 00002-1C-Fix-test-join.patch fix upstream

* Sat May 16 2026 Alexei Takaseev <taf@altlinux.org> 18.4-alt2
- Fix NUMA tests
- Add conflicts for postgresqlXY and -server subpackages

* Wed May 13 2026 Alexei Takaseev <taf@altlinux.org> 18.4-alt1
- 18.4 (Fixes CVE-2026-6472, CVE-2026-6473, CVE-2026-6474, CVE-2026-6475,
              CVE-2026-6476, CVE-2026-6477, CVE-2026-6478, CVE-2026-6479,
              CVE-2026-6575, CVE-2026-6637, CVE-2026-6638)
- Change requires version postgresql-common to  >1.0-alt8 (ALT #46555)
- Add patch 00003-1C-Fix-test-aggregates.patch

* Fri Mar 20 2026 Alexei Takaseev <taf@altlinux.org> 18.3-alt3
- Disable SSE4.2 emulation on e2k (ilyakurdyukov@)

* Tue Mar 10 2026 Alexei Takaseev <taf@altlinux.org> 18.3-alt2
- Delete Provides: %%prog_name = %%EVR, %%prog_name-contrib = %%EVR,
  %%prog_name-server = %%EVR, %%prog_name-tcl = %%EVR, %%prog_name-perl = %%EVR,
  %%prog_name-python = %%EVR, %%prog_name-llvmjit = %%EVR - this version only for 1C
  (ALT #58181, #58182, #58183, #58184, #58185, #58186, #58187)

* Wed Feb 25 2026 Alexei Takaseev <taf@altlinux.org> 18.3-alt1
- 18.2
- Add 00002-1C-Fix-test-join.patch

* Fri Feb 13 2026 Alexei Takaseev <taf@altlinux.org> 18.2-alt1
- 18.2 (Fixes CVE-2026-2003, CVE-2026-2004, CVE-2026-2005,
              CVE-2026-2006, CVE-2026-2007)

* Wed Jan 14 2026 Alexei Takaseev <taf@altlinux.org> 18.1-alt1
- 18.1
- Update 1C patch
- Enable NUMA support
- Enable io_uring support
- Add Conflicts: 17-1C

* Wed Nov 12 2025 Alexei Takaseev <taf@altlinux.org> 17.7-alt1
- 17.7 (Fixes CVE-2025-12817, CVE-2025-12818)
- Use LLVM 20.1
- Fix 1C patch for PG 17.7

* Wed Sep 24 2025 Alexei Takaseev <taf@altlinux.org> 17.6-alt2
- Add triggerpostun and conflict for PG 18
- Remove triggerpostun and conflict for PG 12 and 16-1C
- Add libpq-devel, libpq-devel-static, libecpg-devel, libecpg-devel-static,
  postgresql-devel, postgresql-devel-static subpackage
- Update 1C patch
- Add 00002-1C-Fix-test-join.patch and 00003-1C-Fix-test-sysviews.patch
- Drop unneeded 00002-Disable-join-test.patch

* Wed Aug 13 2025 Alexei Takaseev <taf@altlinux.org> 17.6-alt1
- 17.6 (Fixes CVE-2025-8713, CVE-2025-8714, CVE-2025-8715)

* Fri Jun 27 2025 Alexei Takaseev <taf@altlinux.org> 17.5-alt2
- Update 1C patch

* Sat May 31 2025 Alexei Takaseev <taf@altlinux.org> 17.5-alt1
- 17.5
- Update 1C patch
- Drop 00001-Estimate-the-selectivity-as-quadratic-mean-of-non.patch, exist in 1C patch
- Add 00002-Disable-join-test.patch

* Wed May 07 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt9
- Fixes CVE-2025-4207

* Sat Apr 12 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt8
- Add libpq5 subpackage (ALT #53800)

* Tue Apr 08 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt7
- Rollback change log_directory from 17.2-alt5
- Set path to logfile via /etc/sysconfig/postgresql
- Enable checksums by default

* Wed Apr 02 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt6
- Add 00001-Estimate-the-selectivity-as-quadratic-mean-of-non.patch for speedup 1C operations

* Tue Apr 01 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt5
- Add catalog /var/log/postgres for logs
- Use LLVM 19.1
- Enable JIT on loongarch64 and Disable on E2K

* Tue Feb 18 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt4
- Fixes CVE-2025-1094

* Fri Feb 14 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt3
- Create libpq5-XY only with devel option
- Filtered libpq.so.5 provides and exclude pack libpq.so.5 file for all non-devel version.

* Sat Feb 08 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt2
- Build libpq5, libpq5-devel, libpq5-devel-static, %%prog_name-devel,
  %%prog_name-devel-static and rpm-macros-%%prog_name as libpq5-XY,
  libpq5-XY-devel, libpq5-XY-devel-static, %%prog_nameXY-devel,
  %%prog_nameXY-devel-static and rpm-macros-%%prog_name-XY and
  package every major version
- Move ALT specific files to catalog altlinux/ for more simplification support

* Mon Jan 27 2025 Alexei Takaseev <taf@altlinux.org> 17.2-alt1
- 17.2
- Update 1C patch
- Add coverage support
- Add run test regressions (64-bit arch only)

* Wed Nov 20 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt7
- Fix ABI break in struct ResultRelInfo.
- Fix per-session activation of ALTER {ROLE|DATABASE} SET role.

* Wed Nov 13 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt6
- Fixes CVE-2024-10976, CVE-2024-10977, CVE-2024-10978, CVE-2024-10979
- Fix build by GCC > 13 and LLVM > 15 (drop patch 0002-Fix-search-for-setproctitle.patch)

* Thu Oct 31 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt5
- Use GCC 13

* Mon Oct 28 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt4
- Update 1C patch

* Fri Sep 27 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt3
- Build libecpg6, libecpg6-devel and libecpg6-devel-static as
  libecpg6-XY, libecpg6-XY-devel and libecpg6-XY-devel-static
  and package every major version
- Remove provides libpq and libecpg - no needed very long time

* Wed Sep 25 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt2
- Add triggerpostun and conflict for PG 17
- Remove triggerpostun and conflict for PG 10 and 11

* Fri Aug 09 2024 Alexei Takaseev <taf@altlinux.org> 16.4-alt1
- 16.4 (Fixes CVE-2024-7348)

* Fri May 24 2024 Alexei Takaseev <taf@altlinux.org> 16.3-alt2
- Fix copy to %%_libdir/%%PGSQL/backup

* Thu May 23 2024 Alexei Takaseev <taf@altlinux.org> 16.3-alt1
- 16.3

* Wed May 15 2024 Alexei Takaseev <taf@altlinux.org> 15.7-alt1
- 15.7 (Fixes CVE-2024-4317)
- Update 1C patch

* Mon Feb 12 2024 Alexei Takaseev <taf@altlinux.org> 15.5-alt4
- Update 1C patch
- Fixes CVE-2024-0985

* Tue Nov 14 2023 Alexei Takaseev <taf@altlinux.org> 15.5-alt3
- Update 1C patch

* Fri Nov 10 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 15.5-alt2
- NMU: fixed FTBFS on LoongArch (build without JIT)

* Wed Nov 08 2023 Alexei Takaseev <taf@altlinux.org> 15.5-alt1
- 15.5 (Fixes CVE-2023-5868, CVE-2023-5869, CVE-2023-5870)
- Change 0004-Setup-logging.patch to JSON log format
- Add patch 0008-Add_event-id_to_jsonlog.patch

* Mon Oct 09 2023 Alexei Takaseev <taf@altlinux.org> 15.4-alt3
- Fix typo (Fixes ALT 47838)

* Fri Sep 15 2023 Alexei Takaseev <taf@altlinux.org> 15.4-alt2
- Add triggerpostun and conflict for PG 16

* Thu Aug 24 2023 Alexei Takaseev <taf@altlinux.org> 15.4-alt1
- 15.4
- Update 1C patch

* Sun Aug 13 2023 Alexei Takaseev <taf@altlinux.org> 15.3-alt4
- Change BR llvm 13.0 -> llvm15.0

* Wed Aug 09 2023 Alexei Takaseev <taf@altlinux.org> 15.3-alt3
- Fixes CVE-2023-39417, CVE-2023-39418

* Mon Jul 24 2023 Alexei Takaseev <taf@altlinux.org> 15.3-alt2
- Use autoconf_2.60

* Wed May 10 2023 Alexei Takaseev <taf@altlinux.org> 15.3-alt1
- 15.3 (Fixes CVE-2023-2454, CVE-2023-2455)

* Wed Apr 19 2023 Alexei Takaseev <taf@altlinux.org> 15.2-alt5
- Add lost dbcopies_decoding.so

* Tue Apr 18 2023 Alexei Takaseev <taf@altlinux.org> 15.2-alt4
- Update 1C patch

* Mon Mar 20 2023 Alexei Takaseev <taf@altlinux.org> 15.2-alt3
- Delete noreplace for /etc/sysconfig/postgresql

* Fri Mar 03 2023 Alexei Takaseev <taf@altlinux.org> 15.2-alt2
- Cleanup postgresql.service (ALT #44917)
- Set database locale different from system (ALT #43207)
- Add /etc/sysconfig/postgresql with staring and initializating environment
- Initialization databases with secure connection methods
- Mandatory set password for superuser postgres

* Wed Feb 08 2023 Alexei Takaseev <taf@altlinux.org> 15.2-alt1
- 15.2 (Fixes CVE-2022-41862)

* Thu Jan 19 2023 Alexei Takaseev <taf@altlinux.org> 15.1-alt1
- 15.1
- Update 1C patch

* Thu Dec 22 2022 Alexei Takaseev <taf@altlinux.org> 14.6-alt2
- Add conflicts for server-devel subpackages
- Add triggerpostun for PG 15
- Change BR llvn 12.0 -> llvm13.0

* Wed Nov 09 2022 Alexei Takaseev <taf@altlinux.org> 14.6-alt1
- 14.6
- Add patch for E2K

* Wed Oct 19 2022 Alexei Takaseev <taf@altlinux.org> 14.5-alt2
- Update 1C patch

* Wed Aug 10 2022 Alexei Takaseev <taf@altlinux.org> 14.5-alt1
- 14.5 (Fixes CVE-2022-2625)

* Tue Jul 26 2022 Alexei Takaseev <taf@altlinux.org> 14.4-alt1
- 14.4
- Update 1C patch

* Mon Jun 20 2022 Alexei Takaseev <taf@altlinux.org> 14.3-alt2
- Update 1C patch

* Wed May 11 2022 Alexei Takaseev <taf@altlinux.org> 14.3-alt1
- 14.3 (Fixes CVE-2022-1552)

* Thu Apr 28 2022 Alexei Takaseev <taf@altlinux.org> 14.2-alt1
- 14.2
- Update 1C patch

* Wed Apr 13 2022 Alexei Takaseev <taf@altlinux.org> 14.1-alt4
- Build with llvm 12

* Sat Feb 26 2022 Alexei Takaseev <taf@altlinux.org> 14.1-alt3
- Build with JIT feature

* Mon Feb 21 2022 Alexei Takaseev <taf@altlinux.org> 14.1-alt2
- Update 1C patch
- Move %_includedir/%PGSQL/server and %_libdir/%PGSQL/pgxs to
  separe server-devel subpackage.
- Remove 0004-Fix-includedirs.patch patch
- Add %_rpmmacrosdir/postgresql
- Add Provides: postgresql-server-devel for build _with devel
- Split postgresql-devel to libpq-devel and libecpg-devel
- Split postgresql-devel-static to libpq-devel-static and
  libecpg-devel-static
- Add Requires: postgresql-server-devel to postgresql-devel

* Mon Jan 10 2022 Alexei Takaseev <taf@altlinux.org> 14.1-alt1
- 14.1
- Update 1C patch

* Fri Dec 24 2021 Alexei Takaseev <taf@altlinux.org> 13.4-alt1
- 13.4
- Update 1C patch

* Wed Nov 10 2021 Alexei Takaseev <taf@altlinux.org> 13.3-alt5
- Fixes CVE-2021-23214, CVE-2021-23222

* Wed Sep 29 2021 Alexei Takaseev <taf@altlinux.org> 13.3-alt4
- Add %%triggerpostun for PG 14

* Tue Sep 28 2021 Alexei Takaseev <taf@altlinux.org> 13.3-alt3
- Update 1C patch

* Wed Aug 25 2021 Alexei Takaseev <taf@altlinux.org> 13.3-alt2
- Added -ffat-lto-objects to %optflags_lto

* Fri Aug 20 2021 Alexei Takaseev <taf@altlinux.org> 13.3-alt1
- 13.3
- Update 1C patch

* Wed Aug 11 2021 Alexei Takaseev <taf@altlinux.org> 12.7-alt2
- Fixes CVE-2021-3677

* Fri Jul 23 2021 Alexei Takaseev <taf@altlinux.org> 12.7-alt1
- 12.7
- Update 1C patch

* Wed May 19 2021 Alexei Takaseev <taf@altlinux.org> 12.6-alt3
- Update 1C patch

* Mon May 17 2021 Alexei Takaseev <taf@altlinux.org> 12.6-alt2
- Fixes CVE-2021-32027, CVE-2021-32028, CVE-2021-32029

* Wed Apr 07 2021 Alexei Takaseev <taf@altlinux.org> 12.6-alt1
- 12.6
- Update 1C patch

* Tue Feb 16 2021 Alexei Takaseev <taf@altlinux.org> 12.5-alt5
- Decrased shared_buffers from 4G to 512M (lost when reapplay
  new 1C patch)

* Thu Feb 11 2021 Alexei Takaseev <taf@altlinux.org> 12.5-alt4
- Fix permission checks on constraint violation errors on partitions.
  (Fixes CVE-2021-3393)
- Re-applay patch from 1C

* Thu Dec 03 2020 Alexei Takaseev <taf@altlinux.org> 12.5-alt3
- Decrased shared_buffers from 4G to 512M

* Wed Nov 18 2020 Alexei Takaseev <taf@altlinux.org> 12.5-alt2
- Add %%triggerpostun for PG 13

* Mon Nov 16 2020 Alexei Takaseev <taf@altlinux.org> 12.5-alt1
- 12.5 (Fixes CVE-2020-25694, CVE-2020-25695, CVE-2020-25696)
- Re-applay patch from 1C

* Wed Aug 12 2020 Alexei Takaseev <taf@altlinux.org> 11.9-alt1
- 11.9 (Fixes CVE-2020-14349, CVE-2020-14350)

* Fri Jul 17 2020 Alexei Takaseev <taf@altlinux.org> 11.8-alt2
- Move online_analyze.so and plantuner.so from -contrib
  to -server subpackage

* Tue Jul 14 2020 Alexei Takaseev <taf@altlinux.org> 11.8-alt1
- 11.8

* Tue Jul 14 2020 Alexei Takaseev <taf@altlinux.org> 11.7-alt1
- 11.7
- Re-applay patch from 1C

* Fri May 22 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt5
- Replace all 1C patches by 00001-1C-FULL.patch

* Wed Feb 12 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt4
- Fix priv checks for ALTER <object> DEPENDS ON EXTENSION (Fixes CVE-2020-1720)

* Tue Feb 04 2020 Alexei Takaseev <taf@altlinux.org> 11.5-alt3
- Add patch from 1C:
    * 00016-empty_materialize.patch
    * 00017-eqjoinsel_hist.patch
    * 00018-explain_tuple_count.patch
    * 00019-aggfix.patch

* Tue Dec 10 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00010-joinsel.patch
    * 00015-lessmem.patch

* Tue Oct 29 2019 Alexei Takaseev <taf@altlinux.org> 11.5-alt1
- 11.5
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
    * 00006-pg_receivewal.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch
    * 00012-index_getattr_optimization.patch
    * 00013-notransvalue.patch
    * 00014-optimizer_utils.patch
    * 00015-lessmem.patch

* Fri Oct 25 2019 Alexei Takaseev <taf@altlinux.org> 10.10-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00010-joinsel.patch
    * 00015-lessmem.patch

* Wed Aug 07 2019 Alexei Takaseev <taf@altlinux.org> 10.10-alt1
- 10.10 (Fixes CVE-2019-10208)

* Fri Aug 02 2019 Alexei Takaseev <taf@altlinux.org> 10.9-alt2
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00002-online_analyze.patch
    * 00003-plantuner.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
    * 00007-remove_selfjoin.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch
    * 00012-index_getattr_optimization.patch
- Add patch from 1C:
    * 00013-notransvalue.patch
    * 00014-optimizer_utils.patch
    * 00015-lessmem.patch

* Thu Jun 20 2019 Alexei Takaseev <taf@altlinux.org> 10.9-alt1
- 10.9 (Fixes CVE-2019-10164)

* Mon May 13 2019 Alexei Takaseev <taf@altlinux.org> 10.8-alt1
- 10.8
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch

* Fri Apr 05 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt3
- Re-applay patches from 1C:
    * 00003-plantuner.patch
    * 00004-postgresql-1c-10.patch
    * 00006-pg_receivewal.patch
    * 00007-remove_selfjoin.patch
    * 00009-opt_group_by_and_cost_sort.patch
    * 00010-joinsel.patch
- Add patch from 1C:
    * 00012-index_getattr_optimization.patch

* Thu Apr 04 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt2
- Move *.control and *.sql files from -server to -contrib subpackage
  (Fixes ALT#36271)
- Removed unnecessary minor version in package name libpq and libecpg
- Join subpackages libpq-devel, libecpg-devel and postgresql-devel to
  one postgresql-devel subpackage
- Remove unneeded Conflicts like postgresqlX.Y
- Remove unneeded Conflicts < and > for all subpackages
- Rename postgresqlX-devel to postgresql-devel
- Add Requires to -server for -contrib, -perl, -python and -tcl and subpackages
- Remove unneeded Requires tcl >= 8.4.0-alt1 for -tcl subpackages

* Thu Feb 14 2019 Alexei Takaseev <taf@altlinux.org> 10.7-alt1
- 10.7

* Mon Feb 04 2019 Alexei Takaseev <taf@altlinux.org> 10.6-alt3
- Re-applay patches from 1C:
    * 00007-remove_selfjoin.patch
    * 00010-joinsel.patch
- Cleanup spec: remove "%%def_without ver_old"

* Wed Jan 30 2019 Alexei Takaseev <taf@altlinux.org> 10.6-alt2
- Build with ICU
- Re-applay patches from 1C:
    * 00002-online_analyze.patch
    * 00004-postgresql-1c-10.patch
- Add patches from 1C:
    * 0009-postgresql-10-logging.patch
    * 00007-remove_selfjoin.patch
    * 00008-planner_timing.patch
    * 00009-opt_group_by~nd_cost_sort.patch
    * 00010-joinsel.patch
    * 00011-max_files_per_process.patch

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 10.6-alt1.1
- rebuild with new perl 5.28.1

* Thu Nov 08 2018 Alexei Takaseev <taf@altlinux.org> 10.6-alt1
- 10.6
- (Fixes CVE-2018-16850)

* Fri Oct 19 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt3
- Disable package libs for --without devel. This will provide
  one set of libraries for all versions of the PG.

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt2
- Add BR: libkrb5-devel
- Rebuild with OpenSSL 1.1.x

* Sat Aug 11 2018 Alexei Takaseev <taf@altlinux.org> 10.5-alt1
- 10.5
- (Fixes CVE-2018-10915, CVE-2018-10925)

* Mon Jul 16 2018 Alexei Takaseev <taf@altlinux.org> 10.4-alt1
- 10.4
- Re-applay patches from 1C:
    * 00001-1c_FULL_100_EXT.patch
    * 00004-postgresql-1c-10.patch
    * 00005-coalesce_cost.patch
- Remove patches:
    * 00005-exists_opt-2.patch
    * 00006-coalesce_cost-1.patch
    * 00007-drop-orphan-tt.patch
    * 00008-receivexlog-umask.patch
- Add patch:
    * 00006-pg_receivewal.patch

* Wed May 09 2018 Alexei Takaseev <taf@altlinux.org> 9.6.9-alt1
- 9.6.9
- (Fixes CVE-2018-1115)

* Wed Feb 28 2018 Alexei Takaseev <taf@altlinux.org> 9.6.8-alt1
- 9.6.8
- Re-applay patches from 1C:
    * 00001-1c_FULL_96.patch
    * 00004-postgresql-1c-9.6.patch
    * 00005-exists_opt-2.patch
- Remove path 00001-1c_create_append_path.patch (fixed in 00001-1c_FULL_96.patch)
- (Fixes CVE-2018-1058)

* Wed Feb 07 2018 Alexei Takaseev <taf@altlinux.org> 9.6.7-alt1
- 9.6.7
- Add patches:
    * 00001-1c_create_append_path.patch
    * 00005-exists_opt-2.patch
    * 00006-coalesce_cost-1.patch
    * 00007-drop-orphan-tt.patch
    * 00008-receivexlog-umask.patch
- Re-applay patch 00002-online_analyze.patch from 1C
- Remove patch 00003-applock.patch

* Fri Feb 02 2018 Alexei Takaseev <taf@altlinux.org> 9.6.6-alt2
- Rename pg_rewind's copy_file_range() to avoid conflict with new linux syscall

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 9.6.6-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 09 2017 Alexei Takaseev <taf@altlinux.org> 9.6.6-alt1
- 9.6.6
- Remove conflicts to PG 9.1, 9.2

* Thu Oct 05 2017 Alexei Takaseev <taf@altlinux.org> 9.6.5-alt2
- Add conflicts to PG 10

* Wed Aug 30 2017 Alexei Takaseev <taf@altlinux.org> 9.6.5-alt1
- 9.6.5

* Wed Aug 09 2017 Alexei Takaseev <taf@altlinux.org> 9.6.4-alt1
- 9.6.4
- (Fixes CVE-2017-7547)

* Thu May 11 2017 Alexei Takaseev <taf@altlinux.org> 9.6.3-alt1
- Initial build for ALT Linux Sisyphus
