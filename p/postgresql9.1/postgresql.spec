# -*- mode: rpm-spec; coding: utf-8 -*-
%def_with devel

%define prog_name            postgresql
%define postgresql_major     9
%define postgresql_minor     1
%define postgresql_subminor  3
%define postgresql_altrel    1
%define libpq_major          5
%define libpq_minor          4
%define libecpg_major        6
%define libecpg_minor        3

Name: %prog_name%postgresql_major.%postgresql_minor
Version: %postgresql_major.%postgresql_minor.%postgresql_subminor
Release: alt%postgresql_altrel

%define PGSQL pgsql
%define ROOT %_localstatedir/%PGSQL-root
%define docdir %_docdir/%prog_name-%version

%define libpq_name    libpq%libpq_major.%libpq_minor
%define libecpg_name  libecpg%libecpg_major.%libecpg_minor

Summary: PostgreSQL client programs and libraries
License: PostgreSQL
Group: Databases
URL: http://www.postgresql.org/

Packager: PostgreSQL Maintainers Team <pgsql@packages.altlinux.org>

Source0: %name-%version.tar

Patch1: 0001-9.0-Fix-searching-for-autoconf.patch
Patch2: 0002-Fix-search-for-setproctitle.patch
Patch3: 0003-Use-terminfo-not-termcap.patch
Patch4: 0004-Fix-includedirs.patch
Patch6: 0006-Workaround-for-will-always-overflow-destination-buff.patch
Patch7: 0001-Apply-chroot-patch.patch
Patch8: 0001-Add-postgresql-startup-method-through-service-1-to-i.patch

Requires: %libpq_name = %version-%release

Provides: %prog_name = %version-%release
Conflicts: %prog_name < %version-%release
Conflicts: %prog_name > %version-%release
Conflicts: %{prog_name}8.0
Conflicts: %{prog_name}8.1
Conflicts: %{prog_name}8.2
Conflicts: %{prog_name}8.3
Conflicts: %{prog_name}9.0

BuildRequires: OpenSP chrooted docbook-style-dsssl docbook-style-dsssl-utils docbook-style-xsl flex libldap-devel libossp-uuid-devel libpam-devel libreadline-devel libssl-devel libxslt-devel openjade perl-DBI perl-devel postgresql-common python-devel setproctitle-devel tcl-devel xsltproc zlib-devel

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
Summary: The shared libraries required for any PostgreSQL clients
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
Summary: Development shared library for %libpq_name
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
Summary: Development static library for %libpq_name
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
Summary: Shared library %libecpg_name for PostgreSQL
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
Summary: Development shared library to %libecpg_name
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
Summary: Development static library to %libecpg_name
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
Summary: Extra documentation for PostgreSQL
Group: Databases
BuildArch: noarch

%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in other formats, and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL
Group: Databases
Requires: %name = %version-%release

%description contrib
The postgresql-contrib package includes the contrib tree distributed with
the PostgreSQL tarball.  Selected contrib modules are prebuilt.

%package server
Summary: The programs needed to create and run a PostgreSQL server
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
Summary: PostgreSQL development header files
Group: Development/Databases
Requires: %libpq_name-devel = %version-%release, %libecpg_name-devel = %version-%release
Provides: postgresql-devel = %version-%release

%description devel
The postgresql-devel package contains the header files needed to compile applications
which will directly interact with a PostgreSQL database management server.
You need to install this package if you want to develop applications which will interact
with a PostgreSQL server.
%endif

%package tcl
Summary: The PL/Tcl procedural language for PostgreSQL
Group: Databases
Requires: %name = %version-%release tcl >= 8.4.0-alt1
Provides: postgresql-tcl

%description tcl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-tcl package contains the PL/Tcl procedural language
for the backend.

%package perl
Summary: The PL/Perl procedural language for PostgreSQL
Group: Databases
Requires: %name = %version-%release

%description perl
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-perl package contains the PL/Perl procedural
language for the backend.

%package python
Summary: Development module for Python code to access a PostgreSQL DB
Group: Databases
Requires: %name = %version-%release

%description python
PostgreSQL is an advanced Object-Relational database management
system.  The postgresql-python package includes a module for
developers to use when writing Python code for accessing a PostgreSQL
database.

%prep
%setup

%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch6 -p2
%patch7 -p1
%patch8 -p1

%build
%autoreconf

%configure --includedir=%_includedir/%PGSQL \
--sysconfdir=%_sysconfdir/%PGSQL \
    --datadir=%_datadir/%PGSQL \
    --disable-rpath \
    --enable-nls \
    --enable-thread-safety \
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
pushd altlinux

# The initscripts....
install -p -m755 -D %prog_name.init.in %buildroot%_initdir/%prog_name
install -p -m750 -D %prog_name.chroot.lib.in %buildroot%_sysconfdir/chroot.d/%prog_name.lib
install -p -m750 -D %prog_name.chroot.conf.in %buildroot%_sysconfdir/chroot.d/%prog_name.conf
install -p -m750 -D %prog_name.chroot.all %buildroot%_sysconfdir/chroot.d/%prog_name.all
install -p -m750 -D %prog_name.chroot.bin.in %buildroot%_sysconfdir/chroot.d/%prog_name.bin

# README.ALT
install -p -m 644 -D README.ALT-ru_RU.UTF-8 %buildroot%docdir/README.ALT-ru_RU.UTF-8

popd
##### end ALT-stuff

# Fix initscript versions

sed -i 's,@VERSION@,%postgresql_major.%postgresql_minor,' %buildroot%_initdir/%prog_name
sed -i 's,@FULLVERSION@,%version,' %buildroot%_initdir/%prog_name

pushd %buildroot%_sysconfdir/chroot.d
for f in %prog_name.*; do
 if [ -f "$f" ]; then
   subst -p 's|@LIB@|%_lib|g' $f
 fi
done
popd

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

mksock %buildroot%ROOT/dev/log
mkdir -p -m700 %buildroot%_sysconfdir/syslog.d
ln -s %ROOT/dev/log %buildroot%_sysconfdir/syslog.d/%prog_name

mv %buildroot%_localstatedir/%PGSQL %buildroot%ROOT/%_localstatedir/%PGSQL
install -dm700 %buildroot%_localstatedir/%PGSQL

pushd contrib
%make_build install DESTDIR=%buildroot pkglibdir=%_libdir/%PGSQL docdir=%docdir
popd

cp -a COPYRIGHT README README.git \
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
if grep -qs '^SYSLOGD_OPTIONS=.*-a %ROOT/dev/log' "$SYSLOGD_CONFIG"; then
    subst 's|^\(SYSLOGD_OPTIONS=.*\) \?-a %ROOT/dev/log|\1|' "$SYSLOGD_CONFIG"
    if [ -x "$SYSLOGD_SCRIPT" ]; then
        "$SYSLOGD_SCRIPT" condreload ||:
    fi
fi

if [ $1 -eq 2 ]; then
	%_sysconfdir/chroot.d/%prog_name.all force
fi

%post_service %prog_name

%preun server
%preun_service %prog_name

%triggerpostun -- %{prog_name}8.2-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}8.3-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}8.4-server
if [ "$2" -eq 0 ]; then
	%post_service %prog_name
fi

%triggerpostun -- %{prog_name}9.0-server
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
%docdir/README.git
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
%_bindir/oid2name
%_bindir/pg_standby
%_bindir/pgbench
%_bindir/vacuumlo
%_bindir/pg_archivecleanup

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
%_libdir/pgsql/test_parser.so
%_libdir/pgsql/timetravel.so
%_libdir/pgsql/tsearch2.so
%_libdir/pgsql/passwordcheck.so
%_libdir/pgsql/unaccent.so
%_libdir/pgsql/auth_delay.so
%_libdir/pgsql/dummy_seclabel.so
%_libdir/pgsql/file_fdw.so

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
%config %_sysconfdir/chroot.d/%prog_name.*
%_bindir/initdb
%_bindir/pg_controldata
%_bindir/pg_ctl
%_bindir/pg_resetxlog
%_bindir/postgres
%_bindir/postmaster
%_bindir/pg_upgrade

%_man1dir/initdb.1*
%_man1dir/pg_controldata.1*
%_man1dir/pg_resetxlog.1*
%_man1dir/pg_ctl.1*
%_man1dir/postgres.1*
%_man1dir/postmaster.1*
%dir %_libdir/%PGSQL
%_libdir/%PGSQL/plpgsql.so
%_libdir/%PGSQL/dict_snowball.so
%_libdir/%PGSQL/*_and_*.so
%_libdir/%PGSQL/euc2004_sjis2004.so
%_libdir/%PGSQL/libpqwalreceiver.so
%_libdir/pgsql/pg_upgrade_support.so
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
%_sysconfdir/syslog.d/%prog_name
%docdir/README.ALT-ru_RU.UTF-8
%attr(700,postgres,postgres)  %dir %_localstatedir/%PGSQL

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
%attr(666,root,root) %ghost %ROOT/dev/log

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

%files -n %libpq_name-devel
%_libdir/libpq*.so
%_sysconfdir/buildreqs/packages/substitute.d/%libpq_name-devel

%files -n %libecpg_name-devel
%_bindir/ecpg
%_libdir/libecpg*.so
%_libdir/libpgtypes.so
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
* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.3-alt1
- 9.1.3.
- Package /var/lib/pgsql as a directory.

* Wed Dec 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.2-alt1
- 9.1.2.

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 9.1.1-alt1.1
- Rebuild with Python-2.7.

* Tue Nov 01 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.1.1-alt1
- 9.1.1.
- Enable devel.
- Rediff chroot patch.
- Fix symlink adjustment when chroot mode enabled.

* Tue Oct 11 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.5-alt1
- 9.0.5 fixes CVE-2011-2483.
- Disable devel subpackage.

* Wed Apr 27 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.4-alt1
- 9.0.4.
- Write initdb progress messages to stdout instead of syslog.

* Mon Mar 28 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.3-alt2
- Add build dependency on zlib-devel for fix building.

* Wed Feb 09 2011 Alexey Tourbin <at@altlinux.ru> 9.0.3-alt1.1
- rebuilt for debuginfo provides

* Wed Feb 02 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.3-alt1
- 9.0.3. Fixes CVE-2010-4015.
- Chroot scripts: exit silently when PG_CHROOT_DIR is not set.
- Initscript: remove LOCKFILE when stopping the service.

* Mon Dec 20 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.2-alt1
- 9.0.2.

* Fri Nov 12 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt4
- Initscript:
  + Introduce "service postgresql initdb" and don't run initdb
    automatically.
  + Use SourceIfNotEmpty for sysconf-file sourcing.
  + Start postgres directly (without wrapping around "start_daemon
    --make-pidfile") and with output redirection to separate
    pgstartup.log (Closes: #19337).
  + When chroot mode enabled, adjust symlink /var/lib/pgsql at every
    startup.
- Unhardcode PG_CHROOT_DIR, let users redefine it (Closes: #22287).
- Return back pg_upgrade.

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 9.0.1-alt3.1
- Rebuilt with perl 5.12.

* Wed Nov 03 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt3
- Enable -devel subpackage.
- postgresql.init: fix checking of executable path in
  delete_wrong_pidfile(). Before this condstop() has no chance to stop
  running daemon when doing package upgrade.
- Fix locales copying to chroot dir according to change of localedir
  introduced in glibc-locales-2.11.2-alt3.
- postgresql.init: disable autostart on system startup by default.
- Add rpm trigger for properly restoring chkconfig state after upgrading
  postgresql version.
- Don't package pg_upgrade and postgresql-dump.

* Wed Oct 27 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 9.0.1-alt2
- Rebuild for Sisyphus (without devel part).
- Run chroot script only when upgrading package (tnx ldv@ for hit).
- Avoid leaving unowned directories after package uninstall.
- Use only local dockbook xsl-stylesheets when building.

* Thu Oct 07 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.1-alt1
- 9.0.1 release.

* Mon Sep 06 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.0-alt1.rc1
- 9.0 release candidate 1.

* Wed Aug 11 2010 Konstantin Pavlov <thresh@altlinux.org> 9.0.0-alt1.beta4
- 9.0 beta 4.

* Mon Aug 09 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.4-alt2
- Copy all locale files in chroot (fixes #23821).

* Wed May 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.4-alt1
- 8.4.4 release.

* Fri Mar 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.3-alt1
- 8.4.3 release.

* Fri Mar 19 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.2-alt2
- Build contrib with libossp-uuid.

* Thu Mar 04 2010 Konstantin Pavlov <thresh@altlinux.org> 8.4.2-alt1
- 8.4.2 release.
- Use patches by Alexey Novikov (http://gitorious.org/shader-alt/postgresql/).

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.8-alt1.1
- Rebuilt with python 2.6

* Sat Nov 07 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.8-alt1
- 8.3.8

* Sat Sep 05 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.7-alt4
- Apply buffer overflow patch by Ivan Fedorov

* Sat Aug 01 2009 Michael Bochkaryov <misha@altlinux.ru> 8.3.7-alt3
- fix buffer overflow (import from postgresql-8.3eter)

* Thu Mar 19 2009 Ivan Fedorov <ns@altlinux.org> 8.3.7-alt2
- fix building

* Thu Mar 19 2009 Ivan Fedorov <ns@altlinux.org> 8.3.7-alt1
- 8.3.7

* Thu Nov 06 2008 Ivan Fedorov <ns@altlinux.org> 8.3.5-alt1
- 8.3.5
  + Fix GiST index corruption

* Fri Oct 17 2008 Ivan Fedorov <ns@altlinux.org> 8.3.4-alt2
- fixed #10861, #14576.
- spec cleanup.
- rework contrib subsytem.
- rename libpq subpackages to real names.

* Mon Oct 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 8.3.4-alt1
- updated to 8.3.4 version (fixes #17534).
- added support to use non-chrooted postgresql server, see control postgresql.
- fixed #16683.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 8.3.3-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jun 15 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.3-alt1
- updated to 8.3.3 version

* Tue Jun 03 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt5
- Built with GSSAPI, thanks to Dmitry M. Maslennikov (fix #15877)
- Built with LDAP support

* Tue May 13 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt4
- fixed tsearch_data directory packaging bug

* Thu Apr 10 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt3
- LSB compatible init header added
- init script fix (#15269)
- full text search data added
- explicit build with libxml2 and libxslt support

* Sat Mar 29 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt2
- fix libpq name to avoid unmets

* Fri Mar 28 2008 Michael Bochkaryov <misha@altlinux.ru> 8.3.1-alt1
- rebuild for ALT Linux Sisyphus

* Thu Mar 27 2008 Serge A. Ribalchenko <fisher@netstyle.com.ua> 8.3.1-nets1
- chroot patch from postgresql-8.2.4 merged;
- libpgport.a exclude discarded
1
