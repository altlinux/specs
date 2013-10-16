%define build_debug 0
%define build_test 1
%define build_bench 1

Name: mariadb
Version: 5.5.33a
Release: alt3

Summary: A very fast and reliable SQL database engine
License: GPLv2 with exceptions
Group: Databases

Url: http://mariadb.org/
Source0: %name-%version.tar
Source2: mysqld.sysconfig
Source4: libmysql.version
Source5: mysqld.init
Source6: mysqld_wrapper
Source7: safe_mysqld
Source10: mysql.tmpfiles.d
Source11: mysqld.service

Source12: mysqld-prepare-db-dir
Source13: mysqld-wait-ready

Source15: client.cnf
Source16: server.cnf
Source17: mysql-clients.cnf


# the following patches are rediffed from the mysql-5.5 src.rpm to mariadb-5.5
# fedora patches
Patch1: mariadb-5.5-errno.patch
Patch2: mariadb-5.5-strmov.patch
Patch3: mariadb-5.5-install-test.patch
Patch4: mysql-expired-certs.patch
Patch7: mariadb-5.5-versioning.patch
Patch8: mariadb-5.5-dubious-exports.patch
#Patch12: mysql-openssl-test.patch

# mandriva patches
Patch101: mariadb-5.5-logrotate.patch
Patch102: mariadb-5.5-initscript.patch
Patch103: mariadb-5.5-mysql_upgrade-exit-status.patch
Patch106: mariadb-5.5-hotcopy.patch
Patch107: mariadb-5.5-mysql_install_db-quiet.alt.patch

Requires: %name-server = %EVR %name-client = %EVR

BuildRequires: gcc-c++ libncursesw-devel libreadline-devel libssl-devel perl-DBI zlib-devel libpam0-devel libevent-devel cmake ctest bison doxygen groff-base groff-ps dos2unix xsltproc
BuildRequires: libaio-devel libjemalloc-devel libwrap-devel boost-devel libedit-devel perl-GD perl-threads perl-Memoize perl-devel

%define soname 18

%add_findreq_skiplist %_datadir/mysql/mysql-test/mysql-test-run.pl

%description
The MariaDB software delivers a very fast, multi-threaded, multi-user,
and robust SQL (Structured Query Language) database server.

MariaDB Server is intended for mission-critical, heavy-load production
systems as well as for embedding into mass-deployed software.

The mariadb server is compiled with the following storage engines:

 - Aria Storage Engine
 - Archive Storage Engine
 - Blackhole Storage Engine
 - CSV Storage Engine
 - FederatedX Storage Engine (Federated replacement)
 - Heap Storage Engine
 - MyISAM Storage Engine
 - MyISAMMRG Storage Engine
 - Partition Storage Engine
 - Perfschema Storage Engine
 - XtraDB Storage Engine (InnoDB replacement)

The following extra storage engines are provided by the
mariadb-extra package:

 - OQGraph Storage Engine
 - Sphinx Storage Engine

The following storage engines are provided in the
mariadb-obsolete package:

 - InnoDB Storage Engine

%package server
Summary: A very fast and reliable MariaDB database server
Group: System/Servers
Requires: lib%name = %EVR %name-client = %EVR
Requires: %name-common = %EVR
Provides: mysql-server = %version-%release
Conflicts: MySQL-server

%description server
Core mysqld server. For a full MariaDB database server, install
package 'mariadb'.

%ifarch x86_64
%package engine-tokudb
Summary: MariaDB tokudb storage engines
Group: System/Servers
Requires: %name-server = %EVR

%description engine-tokudb
MariaDB tokudb storage engine.
%endif

%package engine-extra
Summary: MariaDB extra storage engines
Group: System/Servers
Requires: %name-server = %EVR

%description engine-extra
MariaDB oqgraph and sphinx storage engines.

%package engine-obsolete
Summary: MariaDB obsolete storage engines
Group: System/Servers
Requires: %name-server = %EVR

%description engine-obsolete
MariaDB obsolete storage engines. InnoDB and Federated are being replaced
by XtraDB and FederatedX storage engines. These obsolete storage engines
are provided in case you need the vanilla mysql storage engines.

%package client
Summary: Client
Group: Databases
Requires: lib%name = %EVR %name-common = %EVR
Provides: mysql-client = %version-%release
Conflicts: MySQL-client

%description client
This package contains the standard MariaDB clients.

%package common
Summary: Common files used in client and servers
Group: Databases
BuildArch: noarch
Conflicts: MySQL-server
#Conflicts: %name-server < 5.5.33a

%description common
This package contains the common files for MariaDB client and servers.

%if %build_bench
%package bench
Summary: Benchmarks and test system
Group: System/Servers
Requires: %name-client = %EVR
Provides: mysql-bench = %version-%release
Conflicts: MySQL-bench

%description bench
This package contains MariaDB benchmark scripts and data.
%endif

%package -n libmysqlclient%soname
Summary: Shared libraries
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n	libmysqlclient%soname
This package contains the shared libraries (*.so*) which certain languages
and applications need to dynamically load and use MariaDB/MySQL.

%package -n libmysqlclient-devel
Summary: Development header files and libraries
Group: Development/Other
# see also #28676
Requires: libssl-devel zlib-devel
Requires: lib%name = %EVR
Provides: mysql-devel = %version
Provides: MySQL-devel = %version
Provides: libMySQL-devel = %version
Provides: lib%name-devel = %version-%release
Obsoletes: lib%name-devel < %EVR

%description -n	libmysqlclient-devel
This package contains the development header files and libraries necessary
to develop MariaDB/MySQL client applications.

%package -n libmariadbembedded
Summary: MariaDB as an embeddable library
Group: System/Libraries
Requires: %name-common = %EVR

%description -n libmariadbembedded
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains a version of the MariaDB server that can be embedded
into a client application instead of running as a separate process.

The API is identical for the embedded MariaDB version
and the client/server version.

%package -n libmariadbembedded-devel
Summary: Development files for MySQL as an embeddable library
Group: Development/Other
Requires: libmariadbembedded = %EVR lib%name-devel = %EVR

%description -n libmariadbembedded-devel
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains files needed for developing and testing with
the embedded version of the MariaDB server.

The API is identical for the embedded MariaDB version and the client/server
version.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p1
%patch8 -p1
#patch12 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch106 -p1
%patch107 -p0

# antiborker
perl -pi -e "s|\@bindir\@|%_bindir|g" support-files/* scripts/*
perl -pi -e "s|\@sbindir\@|%_sbindir|g" support-files/* scripts/*
perl -pi -e "s|\@libexecdir\@|%_sbindir|g" support-files/* scripts/*
perl -pi -e "s|\@localstatedir\@|/var/lib/mysql|g" support-files/* scripts/*
perl -pi -e "s|^basedir=.*|basedir=%prefix|g" support-files/* scripts/mysql_install_db*

# this may be part of the problems with mysql-test
# http://bugs.mysql.com/bug.php?id=52223
perl -pi -e "s|basedir/lib\b|basedir/%_lib\b|g" mysql-test/mysql-test-run.pl
perl -pi -e "s|basedir/lib/|basedir/%_lib/|g" mysql-test/mysql-test-run.pl

# workaround for upstream bug #56342
rm -f mysql-test/t/ssl_8k_key-master.opt

#fix shebang.req: ERROR: /usr/src/tmp/mariadb-buildroot/usr/share/mysql/sql-bench/innotest1: trailing <CR> in interpreter: #!/usr/bin/perl<CR>
find sql-bench -type f -name 'innotest*' | xargs dos2unix

%build
mkdir build
pushd build
    cmake .. \
	-DBUILD_CONFIG=mysql_release \
	-DFEATURE_SET="community" \
	-DINSTALL_LAYOUT=RPM \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DMYSQL_DATADIR=/var/lib/mysql \
	-DINSTALL_SBINDIR=sbin \
	-DINSTALL_SYSCONFDIR=%_sysconfdir \
	-DINSTALL_PLUGINDIR=%_lib/mysql/plugin \
	-DINSTALL_MANDIR=share/man \
	-DINSTALL_SHAREDIR=share/mysql \
	-DINSTALL_LIBDIR=%_lib \
	-DINSTALL_INCLUDEDIR=include/mysql \
	-DINSTALL_INFODIR=share/info \
	-DINSTALL_MYSQLDATADIR=/var/lib/mysql \
	-DINSTALL_MYSQLTESTDIR=share/mysql/mysql-test \
	-DINSTALL_SQLBENCHDIR=share/mysql \
	-DINSTALL_SUPPORTFILESDIR=share/mysql \
	-DINSTALL_MYSQLSHAREDIR=share/mysql \
	-DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock \
	-DWITH_READLINE=ON \
	-DWITH_LIBWRAP=ON \
	-DWITH_JEMALLOC=system \
	-DWITH_SSL=system \
	-DWITH_ZLIB=system \
	-DWITH_PIC=ON \
	-DEXTRA_CHARSETS=all \
	-DENABLED_LOCAL_INFILE=ON \
	-DWITH_EMBEDDED_SERVER=ON \
	-DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
	-DWITH_FAST_MUTEXES=ON \
	-DWITHOUT_DAEMON_EXAMPLE=ON \
	-DCOMPILATION_COMMENT="(%distribution)" \
	-DMYSQL_SERVER_SUFFIX="-%release"

#	-DWITH_PLUGIN_FEEDBACK=ON \

# override upstream version script by now (adds 747 symbols as of 5.5.30)
# NB: might be dropped some day in favour of upstream one
# (which is also based on fedora's and mageia's in its turn);
# so far there's a problem with version script not being used
# thus had to kludge it in indefinitely again :-/
install -pD %SOURCE4 libmysql/libmysql.version

popd

%make_build -C build

%install
# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%makeinstall_std -C build

# RPM install style leftovers
rm -rf %buildroot%_sysconfdir/init.d/mysql
rm -rf %buildroot{%_libdir/libmysqld.a,%_defaultdocdir/*}

mkdir -p %buildroot%_var/run/mysqld
mkdir -p %buildroot%_var/log/mysqld
mkdir -p %buildroot/var/lib/mysql/db/{mysql,test}

# install init scripts
install -Dm0755 %SOURCE5 %buildroot%_initdir/mysqld
install -Dm 755 %SOURCE6 %buildroot%_sbindir/mysqld_wrapper
install -Dm 755 %SOURCE7 %buildroot%_sbindir/safe_mysqld

# install configuration files
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/mysqld
install -m0644 support-files/rpm/my.cnf %buildroot%_sysconfdir/my.cnf
install -m0644 %SOURCE15 %buildroot%_sysconfdir/my.cnf.d/client.cnf
install -m0644 %SOURCE16 %buildroot%_sysconfdir/my.cnf.d/server.cnf
install -m0644 %SOURCE17 %buildroot%_sysconfdir/my.cnf.d/mysql-clients.cnf
%ifarch x86_64
install -m0644 storage/tokudb/tokudb.cnf %buildroot%_sysconfdir/my.cnf.d/tokudb.cnf
%endif

install -Dm 0644 %SOURCE10 %buildroot%_tmpfilesdir/mysql.conf
install -Dm 644 %SOURCE11 %buildroot%_unitdir/mysqld.service
sed -i 's|@dir@|%_libexecdir/%name|g' %buildroot%_unitdir/mysqld.service
mkdir -p %buildroot%_libexecdir/%name
install -Dm 755 %SOURCE12 %buildroot%_libexecdir/%name
install -Dm 755 %SOURCE13 %buildroot%_libexecdir/%name


install -Dm 644 support-files/mysql-log-rotate.sh %buildroot%_sysconfdir/logrotate.d/mysql

# bork
#mv %buildroot%_bindir/mysqlaccess.conf %buildroot%_sysconfdir/
#chmod 644 %buildroot%_sysconfdir/mysqlaccess.conf
mv %buildroot%_datadir/mysql/aclocal %buildroot%_datadir/aclocal

pushd %buildroot%_bindir
    ln -sf mysqlcheck mysqlrepair
    ln -sf mysqlcheck mysqlanalyze
    ln -sf mysqlcheck mysqloptimize
popd

# most current distro packages have it in %_bindir (hello kde4?)
# but the server subpackage obtains /usr/sbin/mysql_install_db autoreq
ln -sf {../bin,%buildroot%_sbindir}/mysql_install_db

# nuke -Wl,--as-needed from the mysql_config file
#perl -pi -e "s|^ldflags=.*|ldflags=\'-rdynamic\'|g" %buildroot%_bindir/mysql_config

# cmake generates some completely wacko references to -lprobes_mysql when
# building with dtrace support.  Haven't found where to shut that off,
# so resort to this blunt instrument.  While at it, let's not reference
# libmysqlclient_r anymore either.
#sed -e 's/-lprobes_mysql//' -e 's/-lmysqlclient_r/-lmysqlclient/' \
#	%%buildroot%%_bindir/mysql_config >mysql_config.tmp
#cp -f mysql_config.tmp %%buildroot%%_bindir/mysql_config
#chmod 755 %%buildroot%%_bindir/mysql_config
#install -m 0755 -d %%buildroot/var/lib/mysql

# Remove libmysqld.a, + hardlink libmysqld.so.%%libmysqlembedded_major so that it's provided
#rm -f %%buildroot%%_libdir/libmysqld.a
#ln %%buildroot%%_libdir/libmysqld.so.%%major %%buildroot%%_libdir/libmysqld.so.%%libmysqlembedded_major.%%libmysqlembedded_minor
#ln -s libmysqld.so.%%libmysqlembedded_major.%%libmysqlembedded_minor %%buildroot%%_libdir/libmysqld.so.%%libmysqlembedded_major

# libmysqlclient_r is no more.  Upstream tries to replace it with symlinks
# but that really doesn't work (wrong soname in particular).  We'll keep
# just the devel libmysqlclient_r.so link, so that rebuilding without any
# source change is enough to get rid of dependency on libmysqlclient_r.
rm -f %buildroot%_libdir/libmysqlclient_r.so*
ln -s libmysqlclient.so %buildroot%_libdir/libmysqlclient_r.so

# remove static libs
rm -f %buildroot%_libdir/libmysqlclient.a
rm -f %buildroot%_libdir/libmysqlclient_r.a

# mysql-test includes one executable that doesn't belong under /usr/share,
# so move it and provide a symlink
mv %buildroot%_datadir/mysql/mysql-test/lib/My/SafeProcess/my_safe_process %buildroot%_bindir
ln -s %_bindir/my_safe_process %buildroot%_datadir/mysql/mysql-test/lib/My/SafeProcess/my_safe_process

# fix location perl modules
mkdir -p %buildroot%perl_vendor_privlib
mv %buildroot%_datadir/mysql/mysql-test/lib/* %buildroot%perl_vendor_privlib/
rm -rf %buildroot%_datadir/mysql/mysql-test/lib
ln -s ../../../../%perl_vendor_privlib %buildroot%_datadir/mysql/mysql-test/lib
# rm v1 test framework
rm -rf %buildroot%_datadir/mysql/mysql-test/lib/v1

# mysql client statically built against a local embedded library, pretty useless
rm -f %buildroot%_bindir/mysql_embedded

# this command enables plugins, but needs ini file + configuration in my.cnf before executing
# and oh yeah, mysql must be stopped... => useless
rm -f %buildroot%_bindir/mysql_plugin
rm -f %buildroot%_mandir/man1/mysql_plugin.1*
rm -f %buildroot%_libdir/mysql/plugin/daemon_example.ini

# remove more useless plugins
#rm -f %buildroot%_libdir/mysql/plugin/auth_test_plugin.so
#rm -f %buildroot%_libdir/mysql/plugin/dialog_examples.so

# house cleaning
rm -rf %buildroot%_datadir/info
rm -rf %buildroot%_datadir/mysql/solaris
rm -f %buildroot%_bindir/client_test
rm -f %buildroot%_bindir/make_win_binary_distribution
rm -f %buildroot%_bindir/make_win_src_distribution
rm -f %buildroot%_datadir/mysql/binary-configure
rm -f %buildroot%_datadir/mysql/config.huge.ini
rm -f %buildroot%_datadir/mysql/config.medium.ini
rm -f %buildroot%_datadir/mysql/config.small.ini
rm -f %buildroot%_datadir/mysql/mysqld_multi.server
rm -f %buildroot%_datadir/mysql/mysql-log-rotate
rm -f %buildroot%_datadir/mysql/mysql.server
rm -f %buildroot%_datadir/mysql/ndb-config-2-node.ini
rm -f %buildroot%_datadir/mysql/binary-configure
rm -f %buildroot%_mandir/man1/make_win_bin_dist.1*
rm -f %buildroot%_mandir/man1/make_win_src_distribution.1*
rm -f %buildroot%_datadir/mysql/magic

# no idea how to fix this
rm -rf %buildroot%prefix/data
rm -rf %buildroot%prefix/docs
rm -rf %buildroot%prefix/scripts
rm -f %buildroot%prefix/COPYING
rm -f %buildroot%prefix/COPYING.LESSER
rm -f %buildroot%prefix/INSTALL-BINARY
rm -f %buildroot%prefix/README

################################################################################
# run the tests
%if %build_test
%check
pushd build
    ctest -VV
popd
%endif

%pre server
# delete the mysql group if no mysql user is found, before adding the user
if [ -z "`getent passwd mysql`" ] && ! [ -z "`getent group mysql`" ]; then
    %_sbindir/groupdel mysql 2> /dev/null || :
fi

/usr/sbin/groupadd -r -f mysql
/usr/sbin/useradd -r -g mysql -d /var/lib/mysql -s /dev/null -c "MariaDB server" -n mysql >/dev/null 2>&1 ||:

# enable plugins
#if [ -f %_sysconfdir/my.cnf ]; then
#    perl -pi -e "s|^#plugin-load|plugin-load|g" %_sysconfdir/my.cnf
#    perl -pi -e "s|^#federated|federated|g" %_sysconfdir/my.cnf
#    # switch to federatedx provider
#    perl -pi -e "s|;ha_federated\.so$|;ha_federatedx\.so|g" %_sysconfdir/my.cnf
#fi

%post server
%post_service mysqld

%preun server
%preun_service mysqld

%postun server
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/mysqld ]; then
        %_initdir/mysqld restart > /dev/null 2>/dev/null || :
    fi
fi

%files

%files server
%doc README COPYING
%_initdir/mysqld
%_tmpfilesdir/mysql.conf
%_sysconfdir/logrotate.d/mysql
%config(noreplace) %_sysconfdir/sysconfig/mysqld
%config(noreplace) %_sysconfdir/my.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/server.cnf
%_unitdir/mysqld.service
%dir %_libexecdir/%name
%_libexecdir/%name/*

%_libdir/mysql/plugin

%_sbindir/*

%_bindir/aria_chk
%_bindir/aria_dump_log
%_bindir/aria_ftdump
%_bindir/aria_pack
%_bindir/aria_read_log
%_bindir/innochecksum
%_bindir/myisamchk
%_bindir/myisam_ftdump
%_bindir/myisamlog
%_bindir/myisampack
%_bindir/my_print_defaults
%_bindir/mysqlbug
%_bindir/mysql_convert_table_format
%_bindir/mysqld_multi
%_bindir/mysqld_safe
%_bindir/mysql_install_db
%_bindir/mysql_fix_extensions
%_bindir/mysqlhotcopy
%_bindir/mysql_secure_installation
%_bindir/mysql_setpermission
%_bindir/mysqltest
%_bindir/mysql_tzinfo_to_sql
%_bindir/mysql_upgrade
%_bindir/mysql_zap
%_bindir/perror
%_bindir/resolveip
%_bindir/resolve_stack_dump

%attr(0755,mysql,mysql) %dir /var/lib/mysql
%attr(0755,mysql,mysql) %dir %_var/run/mysqld
%attr(0755,mysql,mysql) %dir %_var/log/mysqld

%_mandir/man1/innochecksum.1*
%_mandir/man1/myisamchk.1*
%_mandir/man1/myisamlog.1*
%_mandir/man1/myisampack.1*
%_mandir/man1/my_print_defaults.1*
#_mandir/man1/mysqlbug.1*
%_mandir/man1/mysql_convert_table_format.1*
%_mandir/man1/mysqld_multi.1*
%_mandir/man1/mysqld_safe.1*
%_mandir/man1/mysql_fix_extensions.1*
%_mandir/man1/mysql_fix_privilege_tables.1*
%_mandir/man1/mysqlhotcopy.1*
%_mandir/man1/mysql_install_db.1*
%_mandir/man1/mysqlman.1*
%_mandir/man1/mysql_secure_installation.1*
%_mandir/man1/mysql.server.1*
%_mandir/man1/mysql_setpermission.1*
%_mandir/man1/mysqlslap.1*
%_mandir/man1/mysql_tzinfo_to_sql.1*
%_mandir/man1/mysql_upgrade.1*
%_mandir/man1/mysql_zap.1*
%_mandir/man1/perror.1*
%_mandir/man1/resolveip.1*
%_mandir/man1/resolve_stack_dump.1*
%_mandir/man1/mysqlbug.1.*
%_mandir/man8/mysqld.8*
%_mandir/man8/mysqlmanager.8*

%exclude %_libdir/mysql/plugin/ha_innodb.so
%exclude %_libdir/mysql/plugin/ha_oqgraph.so
%exclude %_libdir/mysql/plugin/ha_sphinx.so
%ifarch x86_64
%exclude %_libdir/mysql/plugin/ha_tokudb.so
%endif

%files common
%_datadir/mysql
%exclude %_datadir/mysql/sql-bench
%exclude %_datadir/mysql/mysql-test

%ifarch x86_64
%files engine-tokudb
%config(noreplace) %_sysconfdir/my.cnf.d/tokudb.cnf
%doc storage/tokudb/README*
%_bindir/tokuftdump
%_libdir/mysql/plugin/ha_tokudb.so
%endif

%files engine-obsolete
%_libdir/mysql/plugin/ha_innodb.so

%files engine-extra
%_libdir/mysql/plugin/ha_oqgraph.so
%_libdir/mysql/plugin/ha_sphinx.so

%files client
%dir %_sysconfdir/my.cnf.d
%config(noreplace) %_sysconfdir/my.cnf.d/client.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/mysql-clients.cnf
%_bindir/msql2mysql
%_bindir/mysql
%_bindir/mysqlaccess
%_bindir/mysqladmin
%_bindir/mysqlanalyze
%_bindir/mysqlbinlog
%_bindir/mysqlcheck
%_bindir/mysqldump
%_bindir/mysqldumpslow
%_bindir/mysql_find_rows
%_bindir/mysqlimport
%_bindir/mysqloptimize
%_bindir/mysqlrepair
%_bindir/mysqlshow
%_bindir/mysqlslap
%_bindir/mysql_waitpid
%_bindir/replace
%_bindir/mytop

%_mandir/man1/msql2mysql.1*
%_mandir/man1/myisam_ftdump.1*
%_mandir/man1/mysql.1*
%_mandir/man1/mysqlaccess.1*
%_mandir/man1/mysqladmin.1*
%_mandir/man1/mysqlbinlog.1*
%_mandir/man1/mysqlcheck.1*
%_mandir/man1/mysqldump.1*
%_mandir/man1/mysqldumpslow.1*
%_mandir/man1/mysql_find_rows.1*
%_mandir/man1/mysqlimport.1*
%_mandir/man1/mysqlshow.1*
%_mandir/man1/mysql_waitpid.1*
%_mandir/man1/replace.1*

%if %build_bench
%files bench
%doc build/sql-bench/README
%_bindir/my_safe_process
%_bindir/mysql_client_test
%_bindir/mysql_client_test_embedded
%_bindir/mysqltest_embedded
%_datadir/mysql/sql-bench
#attr(-,mysql,mysql) %_datadir/mysql/mysql-test
%perl_vendor_privlib/*
%_mandir/man1/mysql-stress-test.pl.1*
%_mandir/man1/mysql-test-run.pl.1*
%_mandir/man1/mysql_client_test.1*
%_mandir/man1/mysql_client_test_embedded.1*
%_mandir/man1/mysqltest.1*
%_mandir/man1/mysqltest_embedded.1*
%endif

%files -n libmysqlclient%soname
%_libdir/libmysqlclient.so.*

%files -n libmysqlclient-devel
%doc INSTALL-SOURCE
%_bindir/mysql_config
%_libdir/libmysqlclient_r.so
%_libdir/libmysqlclient.so
%_includedir/mysql
#_mandir/man1/comp_err.1*
%_mandir/man1/mysql_config.1*
%_datadir/aclocal/mysql.m4
# mysqlservices library is static, because it doesn't contain any code
# itself, and is meant to be statically linked to all plugins.
%_libdir/libmysqlservices.a

%files -n libmariadbembedded
%doc README COPYING
%_libdir/libmysqld.so.*
#%_libdir/libmysqld.so.%%libmysqlembedded_major*

%files -n libmariadbembedded-devel
%_libdir/libmysqld.so

%changelog
* Wed Oct 16 2013 Sergey V Turchin <zerg at altlinux dot org> 5.5.33a-alt3
- fix depends (ALT#29415)

* Tue Oct 01 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.33a-alt2
- Fix (ALT#29415)

* Mon Sep 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.33a-alt1
- New version
- Fix (ALT#29388) - allocated errmsg files to common subpackage
- Add /etc/my.cnf.d
- Add new subpackage %name-engine-tokudb
- Enable tests

* Mon Sep 16 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.32-alt2
- Fix (ALT#29209)

* Tue Jul 30 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.32-alt1
- New version

* Tue Jun 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.31-alt2
- Fixed check for the first start

* Tue Jun 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.31-alt1
- New version

* Sun Apr 14 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 5.5.30-alt12
- Fix systemd service

* Tue Apr 02 2013 Michael Shigorin <mike@altlinux.org> 5.5.30-alt11
- devel subpackage:
  + added extra Provides: which have been missed out optimistically
  + added extra Requires: to avoid unneccessary build breakage

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 5.5.30-alt10
- New version
- NB: 5.5.29 had important security fixes, including:
  + A buffer overflow that can cause a server crash or
    arbitrary code execution (a variant of CVE-2012-5611)
  + CVE-2012-5627 fast password brute-forcing using the "change user"
  + CVE-2012-5615 information leakage about existing user accounts
    via the protocol handshake
  + fixes for DoS attacks - crashes and server lockups
  + all security fixes from MySQL 5.5.29, such as fix for CVE-2012-5612
- please note that client libraries are now built from MariaDB code;
  these should be backwards compatible (but still add 84 symbols),
  see also #28289
  + merged fedora's version script changes (but left ours in too)
- selectively synced build options with fedora
  + enabled readline support
  + do not force PBXT storage plugin build (deprecated in 5.5)
    - see also https://kb.askmonty.org/en/about-pbxt/
    - causes ICE
- removed MySQL-MariaDB subpackage being rather superfluous
- updated BR: (see #16878)
- bumped Release: to be higher than MySQL's, just in case

* Sun Dec 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.28a-alt1
- New version (fix CVE-2012-5579)

* Tue Oct 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.27-alt1
- New version

* Sun Jul 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.25-alt1
- New version

* Fri Jun 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.24-alt1
- New version

* Fri Apr 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.23-alt1
- New version

* Sat Mar 31 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.21-alt1.beta
- Build for ALT
