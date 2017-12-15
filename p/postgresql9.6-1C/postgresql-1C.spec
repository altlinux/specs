# -*- mode: rpm-spec; coding: utf-8 -*-
%def_without devel

# "without" for 1c >=8.3.3
# "with" 1c <8.3.3
%def_without ver_old

%define prog_name            postgresql
%define postgresql_major     9
%define postgresql_minor     6
%define postgresql_subminor  6
%define postgresql_altrel    1

# Look at: src/interfaces/libpq/Makefile
%define libpq_major          5
%define libpq_minor          9

# Look at: src/interfaces/ecpg/ecpglib/Makefile
%define libecpg_major        6
%define libecpg_minor        8

Name: %prog_name%postgresql_major.%postgresql_minor-1C
Version: %postgresql_major.%postgresql_minor.%postgresql_subminor
Release: alt%postgresql_altrel.1

%define PGSQL pgsql
%define ROOT %_localstatedir/%PGSQL-root
%define docdir %_docdir/%prog_name-%version

%define libpq_name    libpq%libpq_major.%libpq_minor-1C
%define libecpg_name  libecpg%libecpg_major.%libecpg_minor-1C

Summary: PostgreSQL client programs and libraries (edition for 1C 8.3.3 and later)
License: PostgreSQL
Group: Databases
URL: http://www.postgresql.org/

Packager: Alexei Takaseev <taf@altlinux.org>

Source0: %name-%version.tar
Source1: README.ALT-ru_RU.UTF-8
Source2: README.rpm-dist
Source3: postgresql-check-db-dir
Source4: postgresql.init.in
Source5: postgresql.service

Patch2: 0002-Fix-search-for-setproctitle.patch
Patch3: 0003-Use-terminfo-not-termcap.patch
Patch4: 0004-Fix-includedirs.patch
Patch6: 0006-Workaround-for-will-always-overflow-destination-buff.patch
Patch8: 0001-Add-postgresql-startup-method-through-service-1-to-i.patch
Patch9: 0008-ALT-SeLinux-user-name.patch

# 1C
Patch100: 00001-1c_FULL_96-0.23.patch
Patch101: 00003-applock.patch
Patch102: 00004-online_analize.patch
Patch103: 00005-plantuner.patch
Patch104: 00006-postgresql-1c-9.6.patch

Requires: libpq%libpq_major >= %version-%release

Provides: %prog_name = %version-%release
Conflicts: %prog_name < %version-%release
Conflicts: %prog_name > %version-%release
Conflicts: %{prog_name}9.3
Conflicts: %{prog_name}9.4
Conflicts: %{prog_name}9.5
Conflicts: %{prog_name}9.6
Conflicts: %{prog_name}10

# Automatically added by buildreq on Thu Jul 31 2014
# optimized out: docbook-dtds gnu-config libcom_err-devel libgpg-error libkrb5-devel libossp-uuid libxml2-devel openjade python-base python-modules setproctitle sgml-common tcl xml-common
BuildRequires: OpenSP docbook-style-dsssl docbook-style-dsssl-utils docbook-style-xsl flex libicu-devel libldap-devel libossp-uuid-devel libpam-devel libreadline-devel libselinux-devel libssl-devel libxslt-devel perl-devel python-devel setproctitle-devel tcl-devel xsltproc zlib-devel

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

%package -n %libpq_name
Summary: The shared libraries required for any PostgreSQL clients (edition for 1C 8.3.3 and later)
Group: Databases
Provides: libpq = %version-%release
Provides: libpq%libpq_major = %version-%release
Conflicts: libpq%libpq_major < %version-%release
Conflicts: libpq%libpq_major > %version-%release
Obsoletes: libpq5.3 < 8.3.4-alt2

%description -n %libpq_name
C and C++ libraries to enable user programs to communicate with the
PostgreSQL database backend. The backend can be on another machine and
accessed through TCP/IP.

%if_with devel
%package -n %libpq_name-devel
Summary: Development shared library for %libpq_name (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: %libpq_name = %version-%release
Provides: libpq-devel = %version-%release
Conflicts: libpq-devel < %version-%release
Conflicts: libpq-devel > %version-%release
Provides: libpq%libpq_major-devel = %version-%release
Conflicts: libpq%libpq_major-devel < %version-%release
Conflicts: libpq%libpq_major-devel > %version-%release

%description -n %libpq_name-devel
Development shared library for %libpq_name

%package -n %libpq_name-devel-static
Summary: Development static library for %libpq_name (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: %libpq_name-devel = %version-%release
Provides: libpq-devel-static = %version-%release
Conflicts: libpq-devel-static < %version-%release
Conflicts: libpq-devel-static > %version-%release
Provides: libpq%libpq_major-devel-static = %version-%release
Conflicts: libpq%libpq_major-devel-static < %version-%release
Conflicts: libpq%libpq_major-devel-static > %version-%release

%description -n %libpq_name-devel-static
Development static library for %libpq_name
%endif

%package -n %libecpg_name
Summary: Shared library %libecpg_name for PostgreSQL (edition for 1C 8.3.3 and later)
Group: Databases
Requires: %libpq_name = %version-%release
Provides: libecpg = %version-%release
Provides: libecpg%libecpg_major = %version-%release
Conflicts: libecpg%libecpg_major < %version-%release
Conflicts: libecpg%libecpg_major > %version-%release

%description -n %libecpg_name
%libecpg_name is used by programs built with ecpg (Embedded PostgreSQL for C)
Use postgresql-dev to develop such programs.

%if_with devel
%package -n %libecpg_name-devel
Summary: Development shared library to %libecpg_name (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: %libecpg_name = %version-%release
Provides: libecpg-devel = %version-%release
Conflicts: libecpg-devel < %version-%release
Conflicts: libecpg-devel > %version-%release
Provides: libecpg%libecpg_major-devel = %version-%release
Conflicts: libecpg%libecpg_major-devel < %version-%release
Conflicts: libecpg%libecpg_major-devel > %version-%release

%description -n %libecpg_name-devel
Development shared library for %libecpg_name and the ecpg Embedded C
Postgres preprocessor.

%package -n %libecpg_name-devel-static
Summary: Development static library to %libecpg_name (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: %libecpg_name-devel = %version-%release
Provides: libecpg-devel-static = %version-%release
Conflicts: libecpg-devel-static < %version-%release
Conflicts: libecpg-devel-static > %version-%release
Provides: libecpg%libecpg_major-devel-static = %version-%release
Conflicts: libecpg%libecpg_major-devel-static < %version-%release
Conflicts: libecpg%libecpg_major-devel-static > %version-%release

%description -n %libecpg_name-devel-static
Development static library to %libecpg_name
%endif

%package docs
Summary: Extra documentation for PostgreSQL (edition for 1C 8.3.3 and later)
Group: Databases
BuildArch: noarch

%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in other formats, and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL (edition for 1C 8.3.3 and later)
Group: Databases
Requires: %name = %version-%release

%description contrib
The postgresql-contrib package includes the contrib tree distributed with
the PostgreSQL tarball.  Selected contrib modules are prebuilt.

%package server
Summary: The programs needed to create and run a PostgreSQL server (edition for 1C 8.3.3 and later)
Group: Databases
PreReq: shadow-utils, syslogd-daemon, grep, sed, chrooted
PreReq: postgresql-common > 1.0-alt3
Requires: %name = %version-%release
Requires: glibc-locales
Provides: %prog_name-server = %version-%release
Conflicts: %prog_name-server < %version-%release
Conflicts: %prog_name-server > %version-%release

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

%if_with devel
%package devel
Summary: PostgreSQL development header files (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: %libpq_name-devel = %version-%release, %libecpg_name-devel = %version-%release
Provides: postgresql-devel = %version-%release

%description devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.

%package devel-static
Summary:  Development static library for postgresql-devel (edition for 1C 8.3.3 and later)
Group: Development/Databases
Requires: postgresql-devel = %version-%release
Provides: postgresql-devel-static = %version-%release

%description devel-static
Development static library for postgresql-devel
%endif

%package tcl
Summary: The PL/Tcl procedural language for PostgreSQL (edition for 1C 8.3.3 and later)
Group: Databases
Requires: %name = %version-%release tcl >= 8.4.0-alt1
Provides: postgresql-tcl

%description tcl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-tcl package contains the PL/Tcl procedural language
for the backend.

%package perl
Summary: The PL/Perl procedural language for PostgreSQL (edition for 1C 8.3.3 and later)
Group: Databases
Requires: %name = %version-%release

%description perl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-perl package contains the PL/Perl procedural
language for the backend.

%package python
Summary: Development module for Python code to access a PostgreSQL DB (edition for 1C 8.3.3 and later)
Group: Databases
Requires: %name = %version-%release

%description python
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-python package includes a module for
developers to use when writing Python code for accessing a PostgreSQL
database.

%prep
%setup -q

%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch6 -p2
%patch8 -p1

# 1C
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1


%build
%autoreconf

%configure --includedir=%_includedir/%PGSQL \
    --sysconfdir=%_sysconfdir/%PGSQL \
    --datadir=%_datadir/%PGSQL \
    --disable-rpath \
    --enable-nls \
    --enable-thread-safety \
%if_with ver_old
    --disable-integer-datetimes \
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
    --with-ossp-uuid

%make_build pkglibdir=%_libdir/%PGSQL

pushd contrib
%make_build all libdir=%_libdir/%PGSQL/contrib
popd

# adjust dockbook styles
find doc/src/sgml/ -type f -name "stylesheet.*" -print0 | xargs -0 sed -i \
	-e "s,http://docbook.sourceforge.net/release/xsl/current,/usr/share/xml/docbook/xsl-stylesheets,g" --
%make_build -C doc all

%install
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL
ln -s /usr/include/pgsql %buildroot%_libdir/%PGSQL/pgxs/src/include

%make_build -C doc install DESTDIR=%buildroot docdir=%docdir

##### ALT-stuff

# The initscripts....
install -p -m755 -D %SOURCE4 %buildroot%_initdir/%prog_name

# README.ALT
install -p -m 644 -D %SOURCE1 %buildroot%docdir/README.ALT-ru_RU.UTF-8
install -p -m 644 -D %SOURCE2 %buildroot%docdir/README.rpm-dist

install -p -m 644 -D %SOURCE5 %buildroot%_unitdir/postgresql.service

##### end ALT-stuff

sed -e 's|^PGVERSION=.*$|PGVERSION=%version|' \
        -e 's|^PGDOCDIR=.*$|PGDOCDIR=%docdir|' \
        < %SOURCE3 >postgresql-check-db-dir
touch -r postgresql-check-db-dir postgresql-check-db-dir
install -m 755 postgresql-check-db-dir %buildroot%_bindir/postgresql-check-db-dir

# Fix initscript versions

sed -i 's,@VERSION@,%postgresql_major.%postgresql_minor,' %buildroot%_initdir/%prog_name
sed -i 's,@FULLVERSION@,%version,' %buildroot%_initdir/%prog_name

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m700 %buildroot%_localstatedir/%PGSQL/data

# backups of data go here...
install -d -m700 %buildroot%_localstatedir/%PGSQL/backups

# Fix a dangling symlink
mkdir -p %buildroot%_includedir/%PGSQL/port
cp src/include/port/linux.h %buildroot%_includedir/%PGSQL/port/
ln -s port/linux.h %buildroot%_includedir/%PGSQL/os.h

# Chrooted environment
mkdir -p %buildroot%ROOT/{bin,dev,%_lib,tmp,%_sysconfdir/%PGSQL,%_localstatedir,%_libdir/%PGSQL,%_libdir/locale}

mv %buildroot%_localstatedir/%PGSQL %buildroot%ROOT/%_localstatedir/%PGSQL
install -dm700 %buildroot%_localstatedir/%PGSQL

pushd contrib
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL docdir=%docdir
popd

cp -a COPYRIGHT README \
    doc/{KNOWN_BUGS,MISSING_FEATURES,TODO,bug.template} \
    src/tutorial %buildroot%docdir/

%find_lang libpq%libpq_major-%postgresql_major.%postgresql_minor
%find_lang pg_dump-%postgresql_major.%postgresql_minor
%find_lang postgres-%postgresql_major.%postgresql_minor
%find_lang psql-%postgresql_major.%postgresql_minor
%find_lang pg_resetxlog-%postgresql_major.%postgresql_minor
%find_lang pg_controldata-%postgresql_major.%postgresql_minor
%find_lang pgscripts-%postgresql_major.%postgresql_minor
%find_lang initdb-%postgresql_major.%postgresql_minor
%find_lang pg_config-%postgresql_major.%postgresql_minor
%find_lang pg_ctl-%postgresql_major.%postgresql_minor
%find_lang ecpg-%postgresql_major.%postgresql_minor
%find_lang ecpglib%libecpg_major-%postgresql_major.%postgresql_minor
%find_lang plperl-%postgresql_major.%postgresql_minor
%find_lang plpgsql-%postgresql_major.%postgresql_minor
%find_lang plpython-%postgresql_major.%postgresql_minor
%find_lang pltcl-%postgresql_major.%postgresql_minor
%find_lang pg_basebackup-%postgresql_major.%postgresql_minor

cat psql-%postgresql_major.%postgresql_minor.lang pg_dump-%postgresql_major.%postgresql_minor.lang pgscripts-%postgresql_major.%postgresql_minor.lang pg_basebackup-%postgresql_major.%postgresql_minor.lang > main.lang
cat postgres-%postgresql_major.%postgresql_minor.lang pg_resetxlog-%postgresql_major.%postgresql_minor.lang pg_controldata-%postgresql_major.%postgresql_minor.lang initdb-%postgresql_major.%postgresql_minor.lang pg_ctl-%postgresql_major.%postgresql_minor.lang plpgsql-%postgresql_major.%postgresql_minor.lang > server.lang
cat pg_config-%postgresql_major.%postgresql_minor.lang> devel.lang
cat ecpg-%postgresql_major.%postgresql_minor.lang ecpglib%libecpg_major-%postgresql_major.%postgresql_minor.lang > ecpg.lang

# buildreq substitution rules.
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo "%prog_name-devel" > "%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name-devel"
echo "libpq-devel" > "%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libpq_name-devel"
echo "libpq-devel-static" > "%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libpq_name-devel-static"
echo "libecpg-devel" > "%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libecpg_name-devel"
echo "libecpg-devel-static" > "%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libecpg_name-devel-static"
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*

%pre
# Need to make backups of some executables if an upgrade
# They will be needed to do a dump of the old version's database.
# All output redirected to /dev/null.
exec &>/dev/null
if [ $1 -gt 1 -a -d %_libdir/%PGSQL ]
then
    if [ ! -d %_libdir/%PGSQL/backup ]; then
        mkdir -p %_libdir/%PGSQL/backup
    fi
    cd %_bindir
    cp -fp pg_dump pg_dumpall psql %_libdir/%PGSQL/backup || :
fi

%pre server
exec &>/dev/null

if [ $1 -gt 1 ]
then
   if [ ! -d %_libdir/%PGSQL/backup ]; then
       mkdir -p %_libdir/%PGSQL/backup
   fi
   cd %_bindir
   cp -fp postmaster postgres %_libdir/%PGSQL/backup
fi

%pre -n %libpq_name
exec &>/dev/null
if [ $1 -gt 1 -a -d %_libdir/%PGSQL ]
then
    if [ ! -d %_libdir/%PGSQL/backup ]; then
        mkdir -p %_libdir/%PGSQL/backup
    fi
    cd %_libdir > /dev/null
    cp -fp libpq.* %_libdir/%PGSQL/backup
fi

%post server
echo PGLIB=%_datadir/%PGSQL >> ~postgres/.bash_profile
echo PGDATA=%_localstatedir/%PGSQL/data >> ~postgres/.bash_profile
echo export PGLIB PGDATA >> ~postgres/.bash_profile
chown postgres:postgres ~postgres/.bash_profile

SYSLOGD_SCRIPT=/etc/init.d/syslogd
SYSLOGD_CONFIG=/etc/sysconfig/syslogd

%post_service %prog_name

%preun server
%preun_service %prog_name

%triggerpostun -- %{prog_name}8.4-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.0-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.1-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.2-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

# $2, holds the number of instances of the target package that will remain
# after the operation if $2 is 0, the target package will be removed
%triggerpostun -- %{prog_name}9.3-server
if [ "$2" -eq 0 ]; then
       %post_service %prog_name
fi

%files -f main.lang
%_bindir/clusterdb
%_bindir/createdb
%_bindir/createlang
%_bindir/createuser
%_bindir/dropdb
%_bindir/droplang
%_bindir/dropuser
%_bindir/pg_dump
%_bindir/pg_dumpall
%_bindir/pg_restore
%_bindir/psql
%_bindir/reindexdb
%_bindir/vacuumdb
%_bindir/pg_basebackup
%_bindir/pg_test_fsync
%_bindir/pg_test_timing
%_bindir/pg_isready
%_bindir/pg_xlogdump
%_man1dir/clusterdb.1*
%_man1dir/createdb.1*
%_man1dir/createlang.1*
%_man1dir/createuser.1*
%_man1dir/dropdb.1*
%_man1dir/droplang.1*
%_man1dir/dropuser.1*
%_man1dir/pg_dump.1*
%_man1dir/pg_restore.1*
%_man1dir/pg_dumpall.1*
%_man1dir/pg_test_fsync.1*
%_man1dir/pg_test_timing.1*
%_man1dir/psql.1*
%_man1dir/reindexdb.1*
%_man1dir/vacuumdb.1*
%_man1dir/pg_basebackup.1*
%_man7dir/*
%dir %docdir
%docdir/KNOWN_BUGS
%docdir/MISSING_FEATURES
%docdir/TODO
%docdir/COPYRIGHT
%docdir/README
%docdir/bug.template

%files docs
%dir %docdir
%dir %docdir/html
%docdir/html/*.html
%docdir/html/*.css
%dir %docdir/tutorial
%docdir/tutorial/*
%docdir/extension

%files contrib
%docdir/contrib/
%_bindir/oid2name
%_bindir/pg_standby
%_bindir/pgbench
%_bindir/vacuumlo
%_bindir/pg_archivecleanup

%_man1dir/oid2name.1*
%_man1dir/pg_archivecleanup.1*
%_man1dir/pg_standby.1*
%_man1dir/pgbench.1*
%_man1dir/vacuumlo.1*

%dir %_libdir/pgsql
%_libdir/pgsql/_int.so
%_libdir/pgsql/adminpack.so
%_libdir/pgsql/auto_explain.so
%_libdir/pgsql/autoinc.so
%_libdir/pgsql/btree_gin.so
%_libdir/pgsql/btree_gist.so
%_libdir/pgsql/chkpass.so
%_libdir/pgsql/citext.so
%_libdir/pgsql/cube.so
%_libdir/pgsql/dblink.so
%_libdir/pgsql/dict_int.so
%_libdir/pgsql/dict_xsyn.so
%_libdir/pgsql/earthdistance.so
%_libdir/pgsql/fuzzystrmatch.so
%_libdir/pgsql/hstore.so
%_libdir/pgsql/insert_username.so
%_libdir/pgsql/isn.so
%_libdir/pgsql/lo.so
%_libdir/pgsql/ltree.so
%_libdir/pgsql/moddatetime.so
%_libdir/pgsql/uuid-ossp.so
%_libdir/pgsql/pageinspect.so
%_libdir/pgsql/pg_buffercache.so
%_libdir/pgsql/pg_freespacemap.so
%_libdir/pgsql/pg_stat_statements.so
%_libdir/pgsql/pg_trgm.so
%_libdir/pgsql/pgcrypto.so
%_libdir/pgsql/pgrowlocks.so
%_libdir/pgsql/pgstattuple.so
%_libdir/pgsql/pgxml.so
%_libdir/pgsql/refint.so
%_libdir/pgsql/seg.so
%_libdir/pgsql/sslinfo.so
%_libdir/pgsql/tablefunc.so
%_libdir/pgsql/tcn.so
%_libdir/pgsql/timetravel.so
%_libdir/pgsql/tsearch2.so
%_libdir/pgsql/passwordcheck.so
%_libdir/pgsql/unaccent.so
%_libdir/pgsql/auth_delay.so
%_libdir/pgsql/file_fdw.so
%_libdir/pgsql/sepgsql.so
%_libdir/pgsql/fasttrun.so
%_libdir/pgsql/fulleq.so
%_libdir/pgsql/mchar.so
%_libdir/pgsql/online_analyze.so
%_libdir/pgsql/plantuner.so

%files -f libpq%libpq_major-%postgresql_major.%postgresql_minor.lang -n %libpq_name
%_libdir/libpq.so.%libpq_major
%_libdir/libpq.so.%libpq_major.*

%files -f ecpg.lang -n %libecpg_name
%_libdir/libecpg.so.%libecpg_major
%_libdir/libecpg.so.%libecpg_major.*
%_libdir/libecpg_compat.so.*
%_libdir/libpgtypes.so.*

%files -f server.lang server
%config %_initdir/%prog_name
#%config %_sysconfdir/chroot.d/%prog_name.*
%_bindir/initdb
%_bindir/postgresql-check-db-dir
%_bindir/pg_controldata
%_bindir/pg_ctl
%_bindir/pg_receivexlog
%_bindir/pg_resetxlog
%_bindir/postgres
%_bindir/postmaster
%_bindir/pg_upgrade

%_man1dir/initdb.1*
%_man1dir/pg_controldata.1*
%_man1dir/pg_receivexlog.1*
%_man1dir/pg_resetxlog.1*
%_man1dir/pg_ctl.1*
%_man1dir/pg_upgrade.1*
%_man1dir/postgres.1*
%_man1dir/postmaster.1*
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plpgsql.so
%_libdir/%PGSQL/dict_snowball.so
%_libdir/%PGSQL/*_and_*.so
%_libdir/%PGSQL/euc2004_sjis2004.so
%_libdir/%PGSQL/libpqwalreceiver.so
%dir %_datadir/%PGSQL
%dir %_datadir/%PGSQL/timezone
%_datadir/%PGSQL/timezone/*
%dir %_datadir/%PGSQL/timezonesets
%_datadir/%PGSQL/timezonesets/*
%dir %_datadir/%PGSQL/tsearch_data
%_datadir/%PGSQL/tsearch_data/*
%_datadir/%PGSQL/postgres.bki
%_datadir/%PGSQL/postgres.description
%_datadir/%PGSQL/postgres.shdescription
%_datadir/%PGSQL/*.sample
%_datadir/%PGSQL/conversion_create.sql
%_datadir/%PGSQL/information_schema.sql
%_datadir/%PGSQL/sql_features.txt
%_datadir/%PGSQL/system_views.sql
%_datadir/%PGSQL/snowball_create.sql
%_datadir/%PGSQL/unknown.pltcl
%_datadir/%PGSQL/extension
%_localstatedir/%PGSQL
#_sysconfdir/syslog.d/%prog_name
%docdir/README.ALT-ru_RU.UTF-8
%docdir/README.rpm-dist
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL
%_datadir/%PGSQL/contrib
%_datadir/%PGSQL/contrib/sepgsql.sql
%_unitdir/*

%attr(751,root,root)  %dir %ROOT
%attr(751,root,root)  %dir %ROOT/bin
%attr(751,root,root)  %dir %ROOT/etc
%attr(751,root,root)  %dir %ROOT/etc/%PGSQL
%attr(751,root,root)  %dir %ROOT/dev
%attr(751,root,root)  %dir %ROOT/%_lib
%attr(1777,root,root) %dir %ROOT/tmp
%attr(751,root,root)  %dir %ROOT/usr
%attr(751,root,root)  %dir %ROOT/var
%attr(751,root,root)  %dir %ROOT%_libdir
%attr(751,root,root)  %dir %ROOT%_libdir/%PGSQL
%attr(751,root,root)  %dir %ROOT%_libdir/locale
%attr(751,root,root)  %dir %ROOT%_localstatedir
%attr(700,postgres,postgres)  %dir %ROOT%_localstatedir/%PGSQL
%attr(700,postgres,postgres)  %dir %ROOT%_localstatedir/%PGSQL/backups
%attr(700,postgres,postgres)  %dir %ROOT%_localstatedir/%PGSQL/data
#attr(666,root,root) %ghost %ROOT/dev/log

%if_with devel
%files -f devel.lang devel
%_includedir/%PGSQL
%_bindir/pg_config
%_man1dir/pg_config.*
%dir %_libdir/%PGSQL
%dir %_libdir/%PGSQL/pgxs/
%_libdir/%PGSQL/pgxs/*
%_sysconfdir/buildreqs/packages/substitute.d/%name-devel
%_man3dir/*

%files devel-static
%_libdir/libpgcommon.a

%files -n %libpq_name-devel
%_libdir/libpq*.so
%_libdir/pkgconfig/libpq.pc
%_sysconfdir/buildreqs/packages/substitute.d/%libpq_name-devel

%files -n %libecpg_name-devel
%_bindir/ecpg
%_libdir/libecpg*.so
%_libdir/libpgtypes.so
%_libdir/pkgconfig/libecpg.pc
%_libdir/pkgconfig/libecpg_compat.pc
%_libdir/pkgconfig/libpgtypes.pc
%_man1dir/ecpg.*
%_sysconfdir/buildreqs/packages/substitute.d/%libecpg_name-devel

%files -n %libpq_name-devel-static
%_libdir/libpq*.a
%_sysconfdir/buildreqs/packages/substitute.d/%libpq_name-devel-static

%files -n %libecpg_name-devel-static
%_libdir/libecpg*.a
%_libdir/libpgtypes.a
%_libdir/libpgport.a
%_sysconfdir/buildreqs/packages/substitute.d/%libecpg_name-devel-static
%endif

%files -f pltcl-%postgresql_major.%postgresql_minor.lang tcl
%dir %_libdir/%PGSQL
%_bindir/pltcl_delmod
%_bindir/pltcl_listmod
%_bindir/pltcl_loadmod
%_libdir/%PGSQL/pltcl.so

%files -f plperl-%postgresql_major.%postgresql_minor.lang perl
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plperl.so

%files -f plpython-%postgresql_major.%postgresql_minor.lang python
%dir %docdir
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plpython2.so

%changelog
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
- fix CVE-2017-7547

* Thu May 11 2017 Alexei Takaseev <taf@altlinux.org> 9.6.3-alt1
- Initial build for ALT Linux Sisyphus
