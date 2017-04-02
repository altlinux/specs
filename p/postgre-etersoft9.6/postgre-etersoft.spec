#redefine __patch for strict patching
#define __patch /usr/bin/patch --fuzz=0

%define major 9.6
%define pqversion 5.9

%define _disable_ld_no_undefined 1

%def_with plpython
%def_without pltcl
%def_with plperl
%def_with nls
%def_with pgfts
%def_with xml
%def_without ssl
%def_without pam
%def_without kerberos

%def_without runselftest
%def_without test

%define kerbdir "/usr"

%add_verify_elf_skiplist %_libdir/postgresql/*.so

Name: postgre-etersoft%major
Version: %major.1.2
Release: alt2

Summary: PostgreSQL client programs and libraries (Etersoft edition for SELTA and 1C)

License: BSD
Group: Databases
Url: http://www.postgresql.org/

Source: ftp://updates.etersoft.ru/pub/Etersoft/Postgre@Etersoft/%version/sources/%name-%version.tar
Source2: postgresql.outformat
Source3: postgresql.init
Source4: Makefile.regress
Source6: README.rpm-dist
Source14: postgresql.pam
Source15: postgresql-bashprofile
Source16: filter-requires-perl-Pg.sh
Source17: postgresql.sysconfig
Source18: postgresql.service
Source19: postgresql-check-db-dir


BuildRequires: rpm-build-intro
BuildRequires: perl glibc-devel bison flex autoconf perl-devel
#BuildRequires: docbook-style-dsssl-utils docbook-style-dsssl OpenSP xsltproc
BuildRequires: libreadline-devel
BuildRequires: zlib-devel >= 1.0.4
BuildRequires: openjade
BuildRequires: libicu-devel

%if_with plpython
BuildPreReq: python-devel
%endif

%if_with pltcl
BuildRequires: tcl-devel
%endif

%if_with ssl
BuildRequires: openssl-devel
%endif

%if_with kerberos
BuildRequires: krb5-devel
BuildRequires: e2fsprogs-devel
%endif

%if_with nls
BuildRequires: gettext >= 0.10.35
%endif

%if_with xml
BuildRequires: libxml2-devel libxslt-devel
%endif

%if_with pam
BuildRequires: pam-devel
%endif

Requires: libpq%pqversion-%{major}eter = %version-%release

%if %_vendor == "alt"
Conflicts: postgresql-common
%else
#Provides: postgresql
Provides: postgre-etersoft%major
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
server over a network connection. This package contains the command-line
utilities for managing PostgreSQL databases on a PostgreSQL server.

If you want to manipulate a PostgreSQL database on a local or remote PostgreSQL
server, you need this package. You also need to install this package
if you're installing the postgresql-server package.

Etersoft edition appointed for SELTA@Etersoft and 1C Enterprise Server

%package -n libpq%pqversion-%{major}eter
Summary: The shared libraries required for any PostgreSQL clients
Group: Databases
#Obsoletes: libpq5.5

%description -n libpq%pqversion-%{major}eter
The postgresql-libs package provides the essential shared libraries for any
PostgreSQL client program or interface. You will need to install this package
to use any other PostgreSQL package or any clients that need to connect to a
PostgreSQL server.

%package server
Summary: The programs needed to create and run a PostgreSQL server
Group: Databases
Requires: %name = %version-%release
Conflicts: postgresql8.4 postgresql8.3 postgresql8.2 postgresql8.1 postgresql8.0 postgresql-8.2eter postgresql-8.3eter postgre-etersoft8.4 postgre-etersoft9.1 postgre-etersoft9.2

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

%package docs
Summary: Extra documentation for PostgreSQL
Group: Databases
%description docs
The postgresql-docs package includes the SGML source for the documentation
as well as the documentation in PDF format and some extra documentation.
Install this package if you want to help with the PostgreSQL documentation
project, or if you want to generate printed documentation. This package also
includes HTML version of the documentation.

%package contrib
Summary: Contributed source and binaries distributed with PostgreSQL
Group: Databases
Requires: %name = %version-%release
Conflicts: postgresql8.4-contrib postgresql8.3-contrib postgresql8.2-contrib postgresql8.1-contrib postgresql8.0-contrib
Conflicts: postgresql-8.2eter-contrib postgresql-8.3eter-contrib
%add_findprov_lib_path %_libdir/postgresql

%description contrib
The postgresql-contrib package contains contributed packages that are
included in the PostgreSQL distribution.
This package include mchar additional module.

%package seltaaddon
Summary: Selta addon for postgresql
Group: Databases
Requires: %name = %version-%release
%add_findprov_lib_path %_libdir/postgresql

%description seltaaddon
Selta addon for postgresql

%if_with plperl
%package plperl
Summary: The Perl procedural language for PostgreSQL
Group: Databases
Requires: %name = %version-%release
Requires: %name-server = %version-%release
Obsoletes: postgresql-pl

%description plperl
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-plperl package contains the PL/Perl language
for the backend.
%endif

%if_with plpython
%package plpython
Summary: The Python procedural language for PostgreSQL
Group: Databases
Requires: %name = %version-%release
Requires: %name-server = %version-%release
Obsoletes: postgresql-pl

%description plpython
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-plpython package contains the PL/Python language
for the backend.
%endif

%if_with pltcl
%package pltcl
Summary: The Tcl procedural language for PostgreSQL
Group: Databases
Requires: %name = %version-%release
Requires: %name-server = %version-%release
Obsoletes: postgresql-pl

%description pltcl
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-pltcl package contains the PL/Tcl language
for the backend.
%endif

%if_with test
%package test
Summary: The test suite distributed with PostgreSQL
Group: Databases
Requires: %name = %version-%release
Requires: %name-server = %version-%release

%description test
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-test package includes the sources and pre-built
binaries of various tests for the PostgreSQL database management
system, including regression tests and benchmarks.
%endif

%define __perl_requires %SOURCE16

%prep
%setup

subst "s,PACKAGE_VERSION='%version',PACKAGE_VERSION='%version-%release',g" configure
subst "s,PACKAGE_STRING='PostgreSQL %version',PACKAGE_STRING='PostgreSQL %version Etersoft Edition',g" configure
subst "s,PACKAGE_BUGREPORT='pgsql-bugs\@postgresql.org',PACKAGE_BUGREPORT='support\@etersoft.ru',g" configure

find . -type f -name Makefile | xargs sed -i 's|libpq\.a|libpq-%{major}eter.a|g'
find src/bin -type f -name Makefile | xargs sed -i 's| -lpq||g'

#cd doc
#tar -zcf postgres.tar.gz *.html stylesheet.css
#rm -f *.html stylesheet.css
#cd -

%build
export LIBNAME=%_lib
%configure --disable-rpath \
%if_with plperl
	--with-perl \
%endif
%if_with plpython
	--with-python \
%endif
%if_with pltcl
	--with-tcl \
	--with-tclconfig=%_libdir \
%endif
%if_with ssl
	--with-openssl \
%endif
	%{subst_with pam} \
%if_with kerberos
	--with-krb5 \
	--with-includes=%kerbdir/include \
	--with-libraries=%kerbdir/%_lib \
%endif
	%{subst_with nls} \
%if_with pgfts
	--enable-thread-safety \
%endif
	--with-icu \
%if_with xml
	--with-libxml \
	--with-libxslt \
%endif
	--disable-integer-datetimes \
	--sysconfdir=%_sysconfdir/postgresql \
	--datadir=%_datadir/postgresql \
	--docdir=%{_docdir}

%make_build all
%make_build -C contrib all CFLAGS="%optflags -Werror=implicit-function-declaration"
%if_with xml
%make_build -C contrib/xml2 all CFLAGS="%optflags -Werror=implicit-function-declaration"
%endif

# Have to hack makefile to put correct path into tutorial scripts
#sed "s|C=\`pwd\`;|C=%_libdir/postgresql/tutorial;|" < src/tutorial/Makefile > src/tutorial/GNUmakefile
#%make_build -C src/tutorial NO_PGXS=1 all
#rm -f src/tutorial/GNUmakefile
%make_build

%if_with runselftest
cd src/test/regress
make all
make MAX_CONNECTIONS=5 check
make clean
cd -
%endif

%if_with test
cd src/test/regress
make RPMTESTING=1 all
cd -
%endif

# do not build doc
#cd doc/src
#make
#cd -

%install
# do not override INSTALL
%make install DESTDIR=%buildroot
%make install DESTDIR=%buildroot -C contrib
%if_with xml
	%make install DESTDIR=%buildroot -C contrib/xml2
%endif

install -d %buildroot%_initdir/
sed 's/^PGVERSION=.*$/PGVERSION=%version/' <%SOURCE3 > postgresql.init
install -m 755 postgresql.init %buildroot%_initdir/postgresql

%if %_vendor != "alt"
install -m 755 %SOURCE2 %buildroot%_initdir/postgresql.outformat
%endif

%if_with pam
	install -d %buildroot%_sysconfdir/pam.d
	install -m 644 %SOURCE14 %buildroot%_sysconfdir/pam.d/postgresql
%endif

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m 700 %buildroot/var/lib/postgresql/data

# backups of data go here...
install -d -m 700 %buildroot/var/lib/postgresql/backups

# postgres' .bash_profile
install -m 644 %SOURCE15 %buildroot/var/lib/postgresql/.bash_profile

# postgres' systemd file service
mkdir -p  %buildroot%_unitdir
install -m 644 %SOURCE18 %buildroot%_unitdir
# postgres' postgresql-check-db-dir file
sed 's/^PGVERSION=.*$/PGVERSION=%version/' <%SOURCE19 > postgresql-check-db-dir
install -m 755 postgresql-check-db-dir %buildroot%_bindir

# Create the multiple postmaster startup directory
install -d -m 700 %buildroot%_sysconfdir/postgresql/

%if_with test
	# tests. There are many files included here that are unnecessary, but include
	# them anyway for completeness.
	mkdir -p %buildroot%_libdir/postgresql/test
	cp -a src/test/regress %buildroot%_libdir/postgresql/test
	install -m 0755 contrib/spi/refint.so %buildroot%_libdir/postgresql/test/regress
	install -m 0755 contrib/spi/autoinc.so %buildroot%_libdir/postgresql/test/regress
	cd  %buildroot%_libdir/postgresql/test/regress/
	strip *.so
	rm -f GNUmakefile Makefile
	cd -
	cp %SOURCE4 %buildroot%_libdir/postgresql/test/regress/Makefile
	chmod 0644 %buildroot%_libdir/postgresql/test/regress/Makefile
%endif

# Fix some more documentation
# gzip doc/internals.ps
cp %{SOURCE6} README.rpm-dist

# do not pack devel
rm -f %buildroot%_libdir/*.so
rm -f %buildroot%_libdir/libpgtypes*
rm -f %buildroot%_libdir/libecpg*
rm -rf %buildroot%_includedir
rm -f %buildroot%_bindir/pg_config
rm -f %buildroot%_bindir/ecpg
rm -f %buildroot%_datadir/locale/*/*/pg_config*.mo
rm -f %buildroot%_datadir/locale/*/*/pg_basebackup*.mo
rm -f %buildroot%_datadir/locale/*/*/ecpg*.mo
rm -f %buildroot%_man1dir/ecpg*
rm -f %buildroot%_man1dir/pg_config*
rm -rf %buildroot%_libdir/postgresql/pgxs
#rm -rf %buildroot%_libdir/postgresql/*.so
rm -f %buildroot%_libdir/*.a
rm -rf %buildroot/%_pkgconfigdir/

%find_lang libpq5-%major
%find_lang initdb-%major
%find_lang pg_ctl-%major
%find_lang pg_dump-%major
%find_lang pg_rewind-%major
%find_lang postgres-%major
%find_lang psql-%major
%find_lang pg_resetxlog-%major
%find_lang pg_controldata-%major
%find_lang pgscripts-%major
%find_lang plperl-%major
%find_lang plpgsql-%major
%find_lang plpython-%major

cat initdb-%major.lang pg_ctl-%major.lang psql-%major.lang pg_dump-%major.lang pgscripts-%major.lang pg_rewind-%major.lang > main.lst
cat postgres-%major.lang pg_resetxlog-%major.lang pg_controldata-%major.lang plpgsql-%major.lang > server.lst

install -D -m644 %SOURCE17 %buildroot%_sysconfigdir/postgresql

%if %_vendor != "alt"
%post -n libpq%pqversion-%{major}eter -p %post_ldconfig
if [ -f /etc/debian_version ]; then
   grep 'en_US en_US.UTF8' /etc/locale.alias || locale-gen en_US && dpkg-reconfigure locales
fi
%postun -n libpq%pqversion-%{major}eter -p %postun_ldconfig
%endif

# FIXME: 26 uid!
%pre server
userdel postgres >/dev/null 2>&1
groupadd -g 26 -o postgres >/dev/null 2>&1 || :
useradd -g postgres -o -r -d /var/lib/postgresql -s /bin/bash \
	-c "PostgreSQL Server" -u 26 postgres >/dev/null 2>&1 || :
touch /var/log/postgresql
chown postgres:postgres /var/log/postgresql
chmod 0700 /var/log/postgresql

%post server
%if %_vendor != "alt"
%post_ldconfig
%endif
%post_service postgresql

%preun server
%preun_service postgresql

%if %_vendor != "alt"
%postun server
%post_ldconfig
%endif

%if_with test
%post test
chown -R postgres:postgres %_datadir/postgresql/test >/dev/null 2>&1 || :
%endif

# FILES section.

%files -f main.lst
%doc doc/KNOWN_BUGS doc/MISSING_FEATURES 
%doc COPYRIGHT README doc/bug.template
%doc README.rpm-dist
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
%_bindir/pg_test_fsync
%_bindir/pg_basebackup
%_datadir/postgresql/extension/
#%_man1dir/clusterdb.*
#%_man1dir/createdb.*
#%_man1dir/createlang.*
#%_man1dir/createuser.*
#%_man1dir/dropdb.*
#%_man1dir/droplang.*
#%_man1dir/dropuser.*
#%_man1dir/pg_dump.*
#%_man1dir/pg_dumpall.*
#%_man1dir/pg_restore.*
#%_man1dir/psql.*
#%_man1dir/reindexdb.*
#%_man1dir/vacuumdb.*
#%_man7dir/*

%if_with docs
%files docs
#%doc src/tutorial
%doc doc/src/sgml/html/
%_docdir/postgresql/contrib/README.fasttrun 
%_docdir/postgresql/contrib/README.fulleq 
%_docdir/postgresql/contrib/README.mchar 
%_docdir/postgresql/contrib/README.online_analyze
%_docdir/postgresql/contrib/README.plantuner
%_docdir/postgresql/extension/
%endif

%files contrib
%_libdir/postgresql/mchar.so
%_libdir/postgresql/fulleq.so
%_libdir/postgresql/fasttrun.so
%_libdir/postgresql/_int.so
%_libdir/postgresql/autoinc.so
%_libdir/postgresql/btree_gist.so
%_libdir/postgresql/chkpass.so
%_libdir/postgresql/cube.so
%_libdir/postgresql/dblink.so
%_libdir/postgresql/earthdistance.so
%_libdir/postgresql/fuzzystrmatch.so
%_libdir/postgresql/insert_username.so
%_libdir/postgresql/isn.so
%_libdir/postgresql/hstore.so
%_libdir/postgresql/pg_freespacemap.so
%_libdir/postgresql/pgrowlocks.so
%_libdir/postgresql/auth_delay.so
#%_libdir/postgresql/dummy_seclabel.so
%_libdir/postgresql/file_fdw.so
%_libdir/postgresql/online_analyze.so
%_libdir/postgresql/plantuner.so

%if_with ssl
%_libdir/postgresql/sslinfo.so
%endif
%_libdir/postgresql/lo.so
%_libdir/postgresql/ltree.so
%_libdir/postgresql/moddatetime.so
%_libdir/postgresql/pgcrypto.so
%_libdir/postgresql/pgstattuple.so
%_libdir/postgresql/pg_buffercache.so
%_libdir/postgresql/pg_trgm.so
%_libdir/postgresql/refint.so
%_libdir/postgresql/seg.so
%_libdir/postgresql/tablefunc.so
%_libdir/postgresql/timetravel.so
%_libdir/postgresql/tsearch2.so
%_libdir/postgresql/adminpack.so
%_libdir/postgresql/dict_int.so
%_libdir/postgresql/dict_xsyn.so
%_libdir/postgresql/euc2004_sjis2004.so
%_libdir/postgresql/pageinspect.so
#%_libdir/postgresql/test_parser.so
%_libdir/postgresql/auto_explain.so
%_libdir/postgresql/btree_gin.so
%_libdir/postgresql/citext.so
%_libdir/postgresql/pg_stat_statements.so
%_libdir/postgresql/tcn.so
%_libdir/postgresql/bloom.so
%_libdir/postgresql/dump_stat.so
%_libdir/postgresql/hstore_plperl.so
%_libdir/postgresql/hstore_plpython2.so
%_libdir/postgresql/jsquery.so
%_libdir/postgresql/ltree_plpython2.so
%_libdir/postgresql/pg_pathman.so
%_libdir/postgresql/pg_prewarm.so
%_libdir/postgresql/pg_query_state.so
%_libdir/postgresql/pg_variables.so
%_libdir/postgresql/pg_visibility.so
%_libdir/postgresql/postgres_fdw.so
%_libdir/postgresql/shared_ispell.so
%_libdir/postgresql/sr_plan.so
%_libdir/postgresql/test_decoding.so
%_libdir/postgresql/tsm_system_rows.so
%_libdir/postgresql/tsm_system_time.so

%if_with xml
%_libdir/postgresql/pgxml.so
%endif

#%_datadir/postgresql/contrib/
%_datadir/postgresql/tsearch_data
%_bindir/oid2name
%_bindir/pgbench
%_bindir/vacuumlo
#doc contrib/*/README.*
%dir %_docdir/postgresql/
%dir %_docdir/postgresql/extension/
%dir %_docdir/postgresql/contrib/
%_docdir/postgresql/contrib/README.*
%_docdir/postgresql/extension/README.*
%_docdir/postgresql/extension/*.example

%doc contrib/spi/*.example
%doc contrib/adminpack/*.sql
%doc contrib/btree_gin/*.sql
%doc contrib/btree_gist/*.sql
%doc contrib/chkpass/*.sql
%doc contrib/citext/*.sql
%doc contrib/cube/*.sql
%doc contrib/dblink/*.sql
%doc contrib/dict_int/*.sql
%doc contrib/dict_xsyn/*.sql
%doc contrib/earthdistance/*.sql
%doc contrib/fuzzystrmatch/*.sql
%doc contrib/hstore/*.sql
%doc contrib/intagg/*.sql
%doc contrib/intarray/*.sql
%doc contrib/isn/*.sql
%doc contrib/lo/*.sql
%doc contrib/ltree/*.sql
%doc contrib/pageinspect/*.sql
%doc contrib/pg_buffercache/*.sql
%doc contrib/pgcrypto/*.sql
%doc contrib/pg_freespacemap/*.sql
%doc contrib/pgrowlocks/*.sql
%doc contrib/pg_stat_statements/*.sql
%doc contrib/pgstattuple/*.sql
%doc contrib/pg_trgm/*.sql
%doc contrib/seg/*.sql
%doc contrib/spi/*.sql
%doc contrib/sslinfo/*.sql
%doc contrib/tablefunc/*.sql
#%doc contrib/test_parser/*.sql
%doc contrib/tsearch2/*.sql
%doc contrib/unaccent/*.sql
%doc contrib/uuid-ossp/*.sql
%doc contrib/xml2/*.sql

%files seltaaddon
%_libdir/postgresql/seltapgaddon.so
%doc contrib/seltapgaddon/*.sql


%files -n libpq%pqversion-%{major}eter -f libpq5-%{major}.lang
%_libdir/libpq-%{major}eter.so.5
%_libdir/libpq-%{major}eter.so.%pqversion

%files server -f server.lst
%config %_initdir/postgresql
%config(noreplace) %_sysconfigdir/postgresql
%if %_vendor != "alt"
%_initdir/postgresql.outformat
%endif
%if_with pam
%config(noreplace) %_sysconfdir/pam.d/postgresql
%endif
%_bindir/initdb
%_bindir/pg_controldata
%_bindir/pg_ctl
%_bindir/pg_resetxlog
%_bindir/postgres
%_bindir/postmaster
%_bindir/pg_standby
%_bindir/pg_archivecleanup
%_bindir/pg_upgrade
%_bindir/postgresql-check-db-dir
%_libdir/postgresql/libpqwalreceiver.so
%_libdir/postgresql/passwordcheck.so
#%_libdir/postgresql/pg_upgrade_support.so
%_libdir/postgresql/unaccent.so
%_unitdir/postgresql.service

%_bindir/pg_isready
%_bindir/pg_probackup
%_bindir/pg_receivexlog
%_bindir/pg_recvlogical
%_bindir/pg_rewind
%_bindir/pg_test_timing
%_bindir/pg_xlogdump
%_bindir/pgpro_upgrade

#%_man1dir/initdb.*
#%_man1dir/pg_controldata.*
#%_man1dir/pg_ctl.*
#%_man1dir/pg_resetxlog.*
#%_man1dir/postgres.*
#%_man1dir/postmaster.*
%_datadir/postgresql/pgpro-upgrade/
%_datadir/postgresql/postgres.bki
%_datadir/postgresql/postgres.description
%_datadir/postgresql/postgres.shdescription
%_datadir/postgresql/system_views.sql
%_datadir/postgresql/*.sample
%_datadir/postgresql/timezone/
%_datadir/postgresql/timezonesets/
%_libdir/postgresql/plpgsql.so
%_libdir/postgresql/dict_snowball.so
%dir %_libdir/postgresql
%dir %_datadir/postgresql
%dir /var/lib/postgresql
%attr (700,postgres,postgres) %dir /var/lib/postgresql/data
%dir /var/lib/postgresql/backups
/var/lib/postgresql/.bash_profile
%_libdir/postgresql/*_and_*.so
%_datadir/postgresql/conversion_create.sql
%_datadir/postgresql/information_schema.sql
%_datadir/postgresql/sql_features.txt
%_datadir/postgresql/snowball_create.sql

%if_with plperl
%files plperl -f plperl-%major.lang
%_libdir/postgresql/plperl.so
%endif

%if_with pltcl
%files pltcl
%_libdir/postgresql/pltcl.so
%_bindir/pltcl_delmod
%_bindir/pltcl_listmod
%_bindir/pltcl_loadmod
%_datadir/postgresql/unknown.pltcl
%endif

%if_with plpython
%files plpython -f plpython-%{major}.lang
%_libdir/postgresql/plpython2.so
%endif

%if_with test
%files test
%_libdir/postgresql/test/*
%dir %_libdir/postgresql/test
%endif

%changelog
* Sun Apr 02 2017 Vitaly Lipatov <lav@altlinux.ru> 9.6.1.2-alt2
- cleanup spec

* Wed Mar 29 2017 Vitaly Lipatov <lav@altlinux.ru> 9.6.1.2-alt1
- initial build 9.6.1.2 Postgre Pro + SELTA@Etersoft patches
