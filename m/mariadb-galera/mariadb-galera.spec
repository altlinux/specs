
%def_disable alt_chroot
%def_enable build_test
%def_without libs
%def_without devel
%def_without common
%def_without client
%def_without bench
%def_disable static
%define mysqld_user mysql
%define _libexecdir %_sbindir
%define ROOT %_localstatedir/mysql

%def_with pcre

%ifarch x86_64
%def_with tokudb
%def_with mroonga
%else
%def_without tokudb
%def_without mroonga
%endif

Name: mariadb-galera
Version: 10.0.21
Release: alt1

Summary: A very fast and reliable SQL database engine
License: GPLv2 with exceptions
Group: Databases

Url: http://mariadb.org/
Source: %name-%version.tar

Source1: mysqld.init
Source2: mysql.logrotate
Source3: safe_mysqld
Source4: mysqld_wrapper
Source5: my.cnf
Source6: mysql.chroot.lib
Source7: mysql.chroot.conf
Source8: mysql.chroot.all
Source9: mysql_migrate
Source10: mysqld.sysconfig
Source14: README.ALT-ru_RU.UTF-8
Source15: alt-mysql_install_db.sh
Source115: alt-mysql_install_db_without_chroot.sh
Source16: mysql.control


Source20: mysql.tmpfiles.d
Source21: mysqld.service
Source22: mysqld-prepare-db-dir
Source23: mysqld-wait-ready

Source25: client.cnf
Source26: server.cnf
Source27: mysql-clients.cnf

Source70: clustercheck.sh
Source71: clustercheck.sysconfig
Source72: mariadbcheck.socket
Source73: mariadbcheck@.service
Source74: mariadbcheck.xinetd

# ALTLinux
Patch1: mariadb-10.0.21-alt-chroot.patch
Patch2: mysql-5.0.20-alt-libdir.patch
Patch4: mariadb-10.0.21-alt-client.patch
Patch5: mariadb-10.0.21-alt-load_defaults.patch
Patch7: mysql-5.5.25-alt-mysql_config-libs.patch

# Patches specific for this mysql package
Patch30: mariadb-errno.patch
Patch31: mariadb-string-overflow.patch
Patch32: mariadb-basedir.patch
Patch33: mariadb-covscan-signexpr.patch
Patch34: mariadb-covscan-stroverflow.patch
Patch36: mariadb-ssltest.patch

Requires: %name-server = %EVR
%if_with client
Requires: %name-client = %EVR
%else
Requires: mariadb-client
%endif

BuildRequires: gcc-c++ libncursesw-devel libreadline-devel libssl-devel perl-DBI zlib-devel libpam0-devel libevent-devel cmake ctest bison doxygen groff-base groff-ps dos2unix xsltproc
BuildRequires: libaio-devel libjemalloc-devel libwrap-devel boost-devel libedit-devel perl-GD perl-threads perl-Memoize perl-devel liblz4-devel
BuildRequires: chrooted control
%{?_with_pcre:BuildRequires: libpcre-devel >= 8.35}

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
Group: Databases
Provides: mysql-server = %version-%release
Provides: mysql = %version
Conflicts: MySQL-server
Conflicts: mariadb-server
Requires: libgalera_smm rsync lsof

%if_with common
Requires: %name-common = %EVR
%else
Requires: mariadb-common
%endif

%if_with libs
Requires: lib%name = %EVR
%else
Requires: libmariadb
%endif

%if_with client
Requires: %name-client = %EVR
%else
Requires: mariadb-client
%endif

%description server
Core mysqld server. For a full MariaDB database server, install
package 'mariadb'.

%package server-perl
Summary: Perl utils for MySQL-server
Group: Databases
Requires: %name-server = %EVR
Conflicts: %name-server < %EVR
Conflicts: MySQL-server-perl
Conflicts: mariadb-server-perl
BuildArch: noarch

%description server-perl
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.
This package contents perl utils for MySQL-server.

%package client
Summary: Client
Group: Databases
Requires: lib%name = %EVR %name-common = %EVR
Provides: mysql-client = %version-%release
Conflicts: MySQL-client
Conflicts: mariadb-client

%description client
This package contains the standard MariaDB clients.

%package common
Summary: Common files used in client and servers
Group: Databases
BuildArch: noarch
Conflicts: MySQL-server
Conflicts: mariadb-common
#Conflicts: %name-server < 5.5.33a

%description common
This package contains the common files for MariaDB client and servers.

%package bench
Summary: Benchmarks and test system
Group: System/Servers
Requires: %name-client = %EVR
Provides: mysql-bench = %version-%release
Conflicts: MySQL-bench
Conflicts: mariadb-bench

%description bench
This package contains MariaDB benchmark scripts and data.

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
Provides: libmariadb-devel = %version-%release
Obsoletes: libmariadb-devel < %EVR

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

%if_enabled alt_chroot
%patch1 -p1
%patch5 -p1
%endif

%patch2 -p1
%patch4 -p1
%patch7 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch36 -p1

# Replace that horror.
%if_enabled alt_chroot
sed 's,@datadir@,%_datadir,g' <%SOURCE15 >scripts/mysql_install_db.sh
%else
sed 's,@datadir@,%_datadir,g' <%SOURCE115 >scripts/mysql_install_db.sh
%endif

# Prepare commands list for completion in mysql client.
sed -ne 's/^\(  { "[A-Z][^"]*"\).*/\1, 0, 0, 0, "" },/pg' <sql/lex.h >client/mysql_symbols.inc

# Not needed with 5.5 but doesn't hurt anyways
chmod -R a-s,go-w sql-bench

#fix shebang.req: ERROR: /usr/src/tmp/mariadb-buildroot/usr/share/mysql/sql-bench/innotest1: trailing <CR> in interpreter: #!/usr/bin/perl<CR>
find sql-bench -type f -name 'innotest*' | xargs dos2unix

%build
CFLAGS="%optflags -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
# force PIC mode so that we can build libmysqld.so
CFLAGS="$CFLAGS -fPIC"
# GCC 4.9 causes segfaults: https://mariadb.atlassian.net/browse/MDEV-6360
CFLAGS="$CFLAGS -fno-delete-null-pointer-checks"
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS
LDFLAGS="$LDFLAGS -pie -Wl,-z,relro,-z,now"
export LDFLAGS

%cmake \
	-DBUILD_CONFIG=mysql_release \
	-DFEATURE_SET="community" \
	-DINSTALL_LAYOUT=RPM \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="$CFLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DMYSQL_UNIX_ADDR="%ROOT/mysql.sock" \
	-DMYSQL_DATADIR="%ROOT" \
	-DMYSQL_USER=mysql \
	-DWITH_READLINE=ON \
	-DWITH_LIBWRAP=ON \
	-DWITH_JEMALLOC=system \
	-DWITH_SSL=system \
	-DWITH_ZLIB=system \
	%{?_with_pcre: -DWITH_PCRE=system -DPCRE_INCLUDES=/usr/include/pcre} \
	%{?_without_tokudb: -DWITHOUT_TOKUDB=ON} \
	%{?_without_mroonga: -DWITHOUT_MROONGA=ON} \
	-DWITH_PIC=ON \
	-DWITH_EXTRA_CHARSETS=all \
	-DWITH_INNOBASE_STORAGE_ENGINE=ON \
	-DWITH_PARTITION_STORAGE_ENGINE=ON \
	-DWITH_FEDERATED_STORAGE_ENGINE=ON \
	-DWITH_WSREP=ON \
	-DWITH_INNODB_DISALLOW_WRITES=1 \
	-DENABLED_LOCAL_INFILE=ON \
	%{?_with_libs: -DWITH_EMBEDDED_SERVER=ON} \
	-DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
	-DWITH_FAST_MUTEXES=ON \
	-DWITHOUT_DAEMON_EXAMPLE=ON \
	-DCOMPILATION_COMMENT="(%distribution)" \
	-DMYSQL_SERVER_SUFFIX="-%release"

%cmake_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_includedir,%_mandir,%_infodir,%_datadir/sql-bench,/var/log/mysql}
mkdir -p %buildroot%ROOT
%if_enabled alt_chroot
mkdir -p %buildroot%ROOT/{etc,/%_lib,%_libdir,%_libdir/mysql/plugin/,%_libdir/galera,dev,log,tmp,/var/{nis,yp/binding},db/mysql,usr/share/mysql/charsets}
touch %buildroot%ROOT{%_sysconfdir/{hosts,services,{host,nsswitch,resolv}.conf},/dev/urandom,/var/nis/NIS_COLD_START}
%endif

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%cmakeinstall_std

# RPM install style leftovers
rm -f %buildroot%_sysconfdir/init.d/mysql
rm -f %buildroot%_sbindir/rcmysql
rm -rf %buildroot{%_libdir/libmysqld.a,%_defaultdocdir/*}

mkdir -p %buildroot%_var/run/mysqld
mkdir -p %buildroot%_var/log/mysqld
mkdir -p %buildroot/var/lib/mysql/db/{mysql,test}

%if_enabled alt_chroot
# Install various helper scripts.
install -pD -m750 %SOURCE6 %buildroot%_sysconfdir/chroot.d/mysql.lib
%ifarch x86_64
sed -i s,usr/lib,usr/lib64,g %buildroot%_sysconfdir/chroot.d/mysql.lib
%endif
install -pD -m750 %SOURCE7 %buildroot%_sysconfdir/chroot.d/mysql.conf
install -pD -m750 %SOURCE8 %buildroot%_sysconfdir/chroot.d/mysql.all
%else
# install configuration files
install -m0644 support-files/rpm/my.cnf %buildroot%_sysconfdir/my.cnf
install -m0644 %SOURCE26 %buildroot%_sysconfdir/my.cnf.d/server.cnf
%endif

install -pD -m755 %SOURCE3 %buildroot%_sbindir/safe_mysqld
install -pD -m755 %SOURCE4 %buildroot%_sbindir/mysqld_wrapper
install -pD -m755 %SOURCE1 %buildroot%_initdir/mysqld
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/mysql
install -m0644 %SOURCE27 %buildroot%_sysconfdir/my.cnf.d/mysql-clients.cnf
install -m0644 %SOURCE25 %buildroot%_sysconfdir/my.cnf.d/client.cnf
install -pD -m644 %SOURCE10 %buildroot%_sysconfdir/sysconfig/mysqld
install -pD -m755 %SOURCE16 %buildroot%_sysconfdir/control.d/facilities/mysqld
install -pD -m750 %SOURCE9 %buildroot%_sbindir/mysql_migrate

# install galera config file
install -p -m 0644 BUILD/support-files/wsrep.cnf %buildroot%_sysconfdir/my.cnf.d/galera.cnf

%if_with tokudb
install -m0644 storage/tokudb/tokudb.cnf %buildroot%_sysconfdir/my.cnf.d/tokudb.cnf
%endif

install -Dm 0644 %SOURCE20 %buildroot%_tmpfilesdir/mysql.conf
install -Dm 644 %SOURCE21 %buildroot%_unitdir/mysqld.service
#sed -i 's|@dir@|%_libexecdir/%name|g' %buildroot%_unitdir/mysqld.service
#mkdir -p %buildroot%_libexecdir/%name
#install -Dm 755 %SOURCE22 %buildroot%_libexecdir/%name
#install -Dm 755 %SOURCE23 %buildroot%_libexecdir/%name

# install the clustercheck script
install -pD -m755 %SOURCE70 %buildroot%_bindir/clustercheck
install -pD -m644 %SOURCE71 %buildroot%_sysconfdir/sysconfig/clustercheck
install -pD -m644 %SOURCE72 %buildroot%_unitdir/mariadbcheck.socket
install -pD -m644 %SOURCE73 %buildroot%_unitdir/mariadbcheck@.service
install -pD -m644 %SOURCE74 %buildroot%_sysconfdir/xinetd.d/mariadbcheck

# Backwards compatibility symlinks (ALT #14863)
mkdir -p %buildroot%_bindir
ln -snf ../sbin/safe_mysqld %buildroot%_bindir/mysqld_safe

pushd %buildroot%_bindir
    ln -sf mysqlcheck mysqlrepair
    ln -sf mysqlcheck mysqlanalyze
    ln -sf mysqlcheck mysqloptimize
popd

%if_enabled alt_chroot
# Install configuration files.
install -pD -m644 /dev/null %buildroot%_sysconfdir/my.cnf
install -pD -m600 %SOURCE5 %buildroot%ROOT/my.cnf
%endif

# most current distro packages have it in %_bindir (hello kde4?)
# but the server subpackage obtains /usr/sbin/mysql_install_db autoreq
ln -sf {../bin,%buildroot%_sbindir}/mysql_install_db

# Fix libmysqlclient_r symlinks
(
        cd %buildroot%_libdir
        N="libmysqlclient_r.so"
        for l in $N.*; do
                if [ -h $l ]; then
                        t=${l#$N}
                        ln -sf libmysqlclient.so$t $N$t
                fi
        done
)

#rm -f %buildroot%_libdir/libmysqlclient_r.so*
#ln -s libmysqlclient.so %buildroot%_libdir/libmysqlclient_r.so

# remove static libs
rm -f %buildroot%_libdir/libmysqlclient.a
rm -f %buildroot%_libdir/libmysqlclient_r.a

%if_enabled alt_chroot
# Populate chroot with data to some extent.
install -pD -m644 %buildroot%_datadir/mysql/charsets/* \
	     %buildroot%ROOT%_datadir/mysql/charsets

(
    cd %buildroot%_datadir/mysql
    for i in */errmsg.sys; do
	install -pD -m644 $i  %buildroot%ROOT%_datadir/mysql/$i
    done
)
%endif

# Fix perl autodetection.
grep -EZl '^[[:space:]]*use the ' %buildroot%_bindir/* |
         xargs -r0 subst -p 's/\([[:space:]]*\)\(use the \)/\1then \2/g'


subst -p 's/\(BUGmysql="\)\([^"]*\)"/\1\2,mysql@packages.altlinux.org"/g' %buildroot%_bindir/mysqlbug

mkdir -p %buildroot%_docdir/%name-%version
install -p -m644 README %SOURCE14 BUILD/support-files/*.cnf %buildroot%_docdir/%name-%version

rm -f %buildroot%_bindir/safe_mysqld
rm -f %buildroot%_datadir/mysql/mysql{-*.spec,-log-rotate,.server}

%if_enabled alt_chroot
touch %buildroot%ROOT/log/queries
%else
touch %buildroot%_logdir/mysql/queries
%endif
touch %buildroot%_logdir/mysql/info

rm -rf %buildroot%_datadir/mysql-test
rm -f %buildroot%_libdir/mysql/plugin/*.la
#rmdir %buildroot%_libdir/mysql/plugin/debug

# broken manpages referencing missing paths
#rm -f %buildroot%_man1dir/mysql{_client_,}test_embedded.1

%define get_datadir \
DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\\(.*\\)/\\1/pg' |tail -1` \
[ -n "$DATADIR" ] || { echo "Failed to read configuration"; exit 1; }


# this command enables plugins, but needs ini file + configuration in my.cnf before executing
# and oh yeah, mysql must be stopped... => useless
rm -f %buildroot%_bindir/mysql_plugin
rm -f %buildroot%_mandir/man1/mysql_plugin.1*
rm -f %buildroot%_libdir/mysql/plugin/daemon_example.ini

# remove more useless plugins
#rm -f %buildroot%_libdir/mysql/plugin/auth_test_plugin.so
#rm -f %buildroot%_libdir/mysql/plugin/dialog_examples.so


# house cleaning
rm -f %buildroot%_bindir/mysql_embedded
rm -rf %buildroot%_datadir/info
rm -f %buildroot%_datadir/mysql/binary-configure
rm -f %buildroot%_datadir/mysql/config.huge.ini
rm -f %buildroot%_datadir/mysql/config.medium.ini
rm -f %buildroot%_datadir/mysql/config.small.ini
rm -f %buildroot%_datadir/mysql/mysqld_multi.server
rm -f %buildroot%_datadir/mysql/mysql-log-rotate
rm -f %buildroot%_datadir/mysql/mysql.server
rm -f %buildroot%_datadir/mysql/ndb-config-2-node.ini
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
%if_enabled build_test
%check
pushd BUILD
    ctest -VV
popd
%endif

%pre server
/usr/sbin/groupadd -r -f %mysqld_user
/usr/sbin/useradd -r -g %mysqld_user -d %ROOT -s /dev/null -c "MariaDB server" -n %mysqld_user >/dev/null 2>&1 ||:

%pre_control mysqld

%post server
%if_enabled alt_chroot
rm -rf %ROOT/dev
%_sysconfdir/chroot.d/mysql.all force
%endif

%post_control -s local mysqld
%post_service mysqld

%preun server
%preun_service mysqld

%postun server
%if_enabled alt_chroot
if [ $1 = 0 ]; then
    rm -f %ROOT/lib/* %ROOT/var/yp/binding/*
fi
%endif

%files

%files server
%doc README COPYING Docs/README-wsrep
%_initdir/mysqld
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/control.d/facilities/*
%if_enabled alt_chroot
%ghost %config(noreplace,missingok) %_sysconfdir/my.cnf
%else
%config(noreplace) %_sysconfdir/my.cnf
%endif
%config(noreplace) %_sysconfdir/my.cnf.d/server.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/galera.cnf
%if_with tokudb
%config(noreplace) %_sysconfdir/my.cnf.d/tokudb.cnf
%endif

%_tmpfilesdir/mysql.conf
%_unitdir/mysqld.service
#%dir %_libexecdir/%name
#%_libexecdir/%name/*

%_bindir/aria*
%_bindir/*isam*
%_bindir/mysql_fix_extensions
%_bindir/mysql_secure_installation
%_bindir/mysql_tzinfo_to_sql
%_bindir/mysql_upgrade
%_bindir/mysqld_multi
%_bindir/mysqld_safe

%_bindir/mysql_install_db

%if_with tokudb
%_bindir/tokuftdump
%_bindir/tokuft_logprint
%_datadir/mysql/mroonga
%endif

%_bindir/wsrep_sst_common
%_bindir/wsrep_sst_mysqldump
%_bindir/wsrep_sst_rsync
%_bindir/wsrep_sst_xtrabackup
%_bindir/wsrep_sst_xtrabackup-v2
%_datadir/mysql/wsrep.cnf
%_datadir/mysql/wsrep_notify

%_bindir/clustercheck
%_unitdir/mariadbcheck.socket
%_unitdir/mariadbcheck@.service
%config(noreplace) %_sysconfdir/xinetd.d/mariadbcheck


%_sbindir/*
%_libdir/mysql/plugin
%attr(750,mysql,adm) %dir %_logdir/mysql
%ghost %verify(not md5 mtime size) %_logdir/mysql/*
%dir %_docdir/%name-%version
%_docdir/%name-%version/README
%_docdir/%name-%version/README.*
%_docdir/%name-%version/*.cnf

%attr(3771,root,mysql) %dir %ROOT
%attr(3770,root,mysql) %dir %ROOT/db
%attr(750,mysql,mysql) %dir %ROOT/db/*

%if_enabled alt_chroot
%config %_sysconfdir/chroot.d/*
%attr(600,root,root) %config(noreplace,missingok) %ROOT/my.cnf
%attr(710,root,mysql) %dir %ROOT/%_lib
%attr(710,root,mysql) %dir %ROOT/%_libdir
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql/plugin
%attr(710,root,mysql) %dir %ROOT/%_libdir/galera
%attr(710,root,mysql) %dir %ROOT%_sysconfdir
%ghost %ROOT%_sysconfdir/hosts
%ghost %ROOT%_sysconfdir/services
%ghost %ROOT%_sysconfdir/*.conf
%dir %ROOT/dev
%ghost %ROOT/dev/urandom
%attr(710,root,mysql) %dir %ROOT/var
%dir %ROOT/var/nis
%ghost %ROOT/var/nis/NIS_COLD_START
%dir %ROOT/var/yp
%dir %ROOT/var/yp/binding
%dir %ROOT/usr
%dir %ROOT%_datadir
%ROOT%_datadir/mysql
%attr(3770,root,mysql) %dir %ROOT/log
%attr(660,mysql,mysql) %ghost %verify(not md5 mtime size) %ROOT/log/*
%attr(3770,root,mysql) %dir %ROOT/tmp
%endif

%if_with common
%files common
%_datadir/mysql
%exclude %_datadir/mysql/SELinux
%if_with tokudb
%exclude %_datadir/mysql/mroonga
%endif
%endif

%files server-perl
%_bindir/mysql_convert_table_format
%_bindir/mysql_find_rows
%_bindir/mysql_setpermission
%_bindir/mysql_zap
%_bindir/mysqlhotcopy
%_bindir/mysqlaccess
%_bindir/mysqldumpslow
%_bindir/mytop

%if_with client
%files client
%dir %_sysconfdir/my.cnf.d
%config(noreplace) %_sysconfdir/my.cnf.d/client.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/mysql-clients.cnf
%_bindir/innochecksum
%_bindir/msql2mysql
%_bindir/my_print_defaults
%_bindir/mysql
%_bindir/mysql_client_test
%_bindir/mysqladmin
%_bindir/mysqlanalyze
%_bindir/mysqlbinlog
%_bindir/mysqlbug
%_bindir/mysqlcheck
%_bindir/mysqldump
%_bindir/mysqlimport
%_bindir/mysqloptimize
%_bindir/mysqlrepair
%_bindir/mysqlshow
%_bindir/mysqlslap
%_bindir/mysqltest
%_bindir/mysql_waitpid
%_bindir/perror
%_bindir/replace
%_bindir/resolve*

%_mandir/man?/*
%exclude %_man1dir/mysql_config.1*
%exclude %_man1dir/mysql_client_test_embedded.1*
%exclude %_man1dir/mysqltest_embedded.1*
%endif

%if_with bench
%files bench
%_datadir/sql-bench
%endif

%if_with libs
%files -n libmysqlclient%soname
%_libdir/*.so.*
%exclude %_libdir/libmysqld.so.*

%files -n libmariadbembedded
%doc README COPYING
%_libdir/libmysqld.so.*
#%_libdir/libmysqld.so.%%libmysqlembedded_major*

%if_with devel
%files -n libmysqlclient-devel
%doc INSTALL-SOURCE
%_bindir/mysql_config
%_libdir/*.so
%exclude %_libdir/libmysqld.so
%_includedir/*
#_mandir/man1/comp_err.1*
%_man1dir/mysql_config.1*
%_aclocaldir/mysql.m4
# mysqlservices library is static, because it doesn't contain any code
# itself, and is meant to be statically linked to all plugins.
%_libdir/libmysqlservices.a

%files -n libmariadbembedded-devel
%_libdir/libmysqld.so
%_bindir/mysql_client_test_embedded
%_bindir/mysqltest_embedded
%_man1dir/mysql_client_test_embedded.1*
%_man1dir/mysqltest_embedded.1*

%endif
%endif

%changelog
* Wed Sep 02 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.21-alt1
- initial build based on mariadb spec (build only server)
