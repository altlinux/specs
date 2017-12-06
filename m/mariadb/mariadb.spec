%add_findreq_skiplist %_datadir/mysql/mysql-test/mysql-test-run.pl
%add_findreq_skiplist %_bindir/wsrep_sst_xtrabackup
%add_findreq_skiplist %_bindir/wsrep_sst_xtrabackup-v2

%def_with libs
%def_with devel
%def_with common
%def_with client
%def_with bench
%def_with mariabackup
%def_enable build_test
%def_disable static
%define mysqld_user mysql
%define _libexecdir %_sbindir
%define ROOT %_localstatedir/mysql

%def_with pcre
%def_with systemd
%def_with krb5
%def_without libarchive

%ifarch x86_64
%def_with tokudb
%def_without mroonga
#def_with mroonga
%else
%def_without tokudb
%def_without mroonga
%endif

%def_with galera
%def_with cassandra
%def_with oqgraph

%def_with jemalloc

Name: mariadb
Version: 10.1.29
Release: alt1%ubt

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
Source16: mysql.control
Source17: mysqld-chroot.control

Source19: galera_new_cluster.sh

Source20: mysql.tmpfiles.d
Source21: mysqld.service
Source22: mysqld.service.d-user
Source23: mysqld.service.d-notify
Source24: mysqld.service.d-notify-chroot

Source25: client.cnf
Source26: server.cnf
Source27: mysql-clients.cnf
Source28: server-chroot.cnf
Source29: server-no-chroot.cnf

Source70: clustercheck.sh
Source71: clustercheck.sysconfig
Source72: mariadbcheck.socket
Source73: mariadbcheck@.service
Source74: mariadbcheck.xinetd


Patch0: %name-%version.patch

# ALTLinux
Patch1: mariadb-10.0.21-alt-chroot.patch
Patch2: mysql-5.0.20-alt-libdir.patch
Patch4: mariadb-10.1.8-alt-client.patch
#Patch5: mariadb-10.0.21-alt-load_defaults.patch
Patch7: mariadb-10.1.8-alt-config-libs.patch

# Patches specific for this mysql package
Patch30: mariadb-errno.patch
#Patch31: mariadb-string-overflow.patch
Patch32: mariadb-basedir.patch
Patch33: mariadb-covscan-signexpr.patch
#Patch34: mariadb-covscan-stroverflow.patch

Requires: %name-server = %EVR
Requires: %name-client = %EVR

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libncursesw-devel libreadline-devel libssl-devel perl-DBI libpam-devel libevent-devel cmake ctest bison doxygen groff-base groff-ps dos2unix xsltproc
BuildRequires: libaio-devel libwrap-devel libedit-devel perl-GD perl-threads perl-Memoize perl-devel
BuildRequires: liblz4-devel zlib-devel bzlib-devel liblzma-devel liblzo2-devel libsnappy-devel
BuildRequires: chrooted control
BuildRequires: libxml2-devel
%{?_with_cassandra:BuildRequires: boost-devel}
%{?_with_oqgraph:BuildRequires: boost-devel}
%{?_with_jemalloc:BuildRequires: libjemalloc-devel}
%{?_with_pcre:BuildRequires: libpcre-devel >= 8.35}
%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_with_krb5:BuildRequires: libkrb5-devel}
%{?_with_libarchive: BuildRequires: libarchive-devel}

%if_with galera
Provides: %name-galera = %EVR
Obsoletes: %name-galera < %EVR
%endif

%define soname 18

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

%if_with oqgraph
 - OQGraph Storage Engine
%endif
 - Sphinx Storage Engine

The following storage engines are provided in the
mariadb-obsolete package:

 - InnoDB Storage Engine

%package server
Summary: A very fast and reliable MariaDB database server
Group: Databases
Requires: libmysqlclient%soname = %EVR %name-client = %EVR
Requires: %name-common = %EVR
Provides: mysql-server = %EVR
Provides: mysql = %version
Provides: %name-engine-extra = %EVR
Obsoletes: %name-engine-extra < %EVR
Provides: %name-engine-obsolete = %EVR
Obsoletes: %name-engine-obsolete < %EVR
%if_with tokudb
Provides: %name-engine-tokudb = %EVR
Obsoletes: %name-engine-tokudb < %EVR
%endif
Conflicts: MySQL-server
%if_with galera
Provides: %name-galera-server = %EVR
Obsoletes: %name-galera-server < %EVR
Requires: libgalera_smm rsync lsof
%endif
PreReq: chrooted %name-server-control

%description server
Core mysqld server. For a full MariaDB database server, install
package 'mariadb'.

%package server-control
Summary: MariaDB database server facility control
Group: System/Servers
BuildArch: noarch
Conflicts: %name-server < %EVR

%description server-control
This package contains control rules for the MariaDB database server facility.
See control(8) for details.

%package server-perl
Summary: Perl utils for MySQL-server
Group: Databases
Requires: %name-server = %EVR
Conflicts: %name-server < %EVR
Conflicts: MySQL-server-perl
Conflicts: mytop
%if_with galera
Provides: %name-galera-server-perl = %EVR
Obsoletes: %name-galera-server-perl < %EVR
%endif
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
Requires: libmysqlclient%soname = %EVR %name-common = %EVR
Provides: mysql-client = %EVR
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

%package bench
Summary: Benchmarks and test system
Group: System/Servers
Requires: %name-client = %EVR
Provides: mysql-bench = %EVR
Conflicts: MySQL-bench

%description bench
This package contains MariaDB benchmark scripts and data.

%package backup
Summary: Backup tool for InnoDB and XtraDB
Group: Databases

%description backup
MariaDB Backup is an open source tool provided by MariaDB for performing
physical online backups of InnoDB, Aria and MyISAM tables.
For InnoDB, hot online backups are possible.

%package -n libmysqlclient%soname
Summary: Shared libraries
Group: System/Libraries

%description -n	libmysqlclient%soname
This package contains the shared libraries (*.so*) which certain languages
and applications need to dynamically load and use MariaDB/MySQL.

%package -n libmysqlclient-devel
Summary: Development header files and libraries
Group: Development/Other
# see also #28676
Requires: libssl-devel zlib-devel
Requires: libmysqlclient%soname = %EVR
Provides: mysql-devel = %version
Provides: MySQL-devel = %version
Provides: libMySQL-devel = %version

%description -n	libmysqlclient-devel
This package contains the development header files and libraries necessary
to develop MariaDB/MySQL client applications.

%package -n libmysqld%soname
Summary: MariaDB as an embeddable library
Group: System/Libraries
Requires: %name-common = %EVR
Obsoletes: libmariadbembedded < %EVR

%description -n libmysqld%soname
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains a version of the MariaDB server that can be embedded
into a client application instead of running as a separate process.

The API is identical for the embedded MariaDB version
and the client/server version.

%package -n libmysqld-devel
Summary: Development files for MySQL as an embeddable library
Group: Development/Other
Requires: libmysqld%soname = %EVR
Requires: libmysqlclient%soname = %EVR
Obsoletes: libmariadbembedded-devel < %EVR

%description -n libmysqld-devel
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains files needed for developing and testing with
the embedded version of the MariaDB server.

The API is identical for the embedded MariaDB version and the client/server
version.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
#%patch5 -p1
%patch7 -p1
%patch30 -p1
#%patch31 -p1
%patch32 -p1
#%patch33 -p1
#%patch34 -p1

# Replace that horror.
sed 's,@datadir@,%_datadir,g' <%SOURCE15 >scripts/mysql_install_db.sh

# Prepare commands list for completion in mysql client.
sed -ne 's/^\(  { "[A-Z][^"]*"\).*/\1, 0, 0, 0, "" },/pg' <sql/lex.h >client/mysql_symbols.inc

# Not needed with 5.5 but doesn't hurt anyways
chmod -R a-s,go-w sql-bench

#fix shebang.req: ERROR: /usr/src/tmp/mariadb-buildroot/usr/share/mysql/sql-bench/innotest1: trailing <CR> in interpreter: #!/usr/bin/perl<CR>
find sql-bench -type f -name 'innotest*' | xargs dos2unix

%ifarch e2k
# just like libzio
sed -i 's,makecontext,makecontext_e2k,' mysys/my_context.c
# FIXME: fails
:> cmake/do_abi_check.cmake
%endif

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
	%{?_with_jemalloc:-DWITH_JEMALLOC=system} \
	%{?_without_jemalloc:-DWITH_JEMALLOC=no} \
	-DWITH_SSL=system \
	-DWITH_ZLIB=system \
	%{?_with_pcre:-DWITH_PCRE=system -DPCRE_INCLUDES=/usr/include/pcre} \
	%{?_without_tokudb:-DWITHOUT_TOKUDB=ON} \
	%{?_without_mroonga:-DWITHOUT_MROONGA=ON} \
	-DWITH_PIC=ON \
	-DWITH_EXTRA_CHARSETS=all \
	-DWITH_INNOBASE_STORAGE_ENGINE=ON \
	-DWITH_PARTITION_STORAGE_ENGINE=ON \
	-DWITH_FEDERATED_STORAGE_ENGINE=ON \
	-DWITH_WSREP=ON \
	-DWITH_INNODB_DISALLOW_WRITES=1 \
	-DENABLED_LOCAL_INFILE=ON \
	-DWITH_EMBEDDED_SERVER=ON \
	-DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
	-DWITH_FAST_MUTEXES=ON \
	-DWITHOUT_DAEMON_EXAMPLE=ON \
	%{?_without_mariabackup:-DWITH_MARIABACKUP=OFF} \
	%{?_without_libarchive:-DWITH_LIBARCHIVE=OFF} \
	-DCOMPILATION_COMMENT="(%distribution)" \
	-DMYSQL_SERVER_SUFFIX="-%release"

#	-DWITH_EMBEDDED_SERVER=ON \
#	-DWITH_PLUGIN_FEEDBACK=ON \

%cmake_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_includedir,%_mandir,%_infodir,%_datadir/sql-bench,%_logdir/mysql}
mkdir -p %buildroot%ROOT/{etc,/%_lib,%_libdir,%_libdir/mysql/plugin/,%_libdir/galera,dev,log,tmp,run/systemd,/var/{nis,yp/binding},db/mysql,usr/share/mysql/charsets}
touch %buildroot%ROOT{%_sysconfdir/{hosts,services,{host,nsswitch,resolv}.conf},/dev/urandom,/var/nis/NIS_COLD_START,/run/systemd/notify}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%cmakeinstall_std

# RPM install style leftovers
rm -f %buildroot%_sysconfdir/init.d/mysql
rm -f %buildroot%_sbindir/rcmysql
rm -rf %buildroot{%_libdir/libmysqld.a,%_defaultdocdir/*}

mkdir -p %buildroot%_var/run/mysqld
mkdir -p %buildroot/var/lib/mysql/db/{mysql,test}

# Install various helper scripts.
install -pD -m755 %SOURCE1 %buildroot%_initdir/mysqld
install -pD -m644 %SOURCE2 %buildroot%_logrotatedir/mysql
install -pD -m755 %SOURCE3 %buildroot%_sbindir/safe_mysqld
install -pD -m755 %SOURCE4 %buildroot%_sbindir/mysqld_wrapper
install -pD -m750 %SOURCE6 %buildroot%_sysconfdir/chroot.d/mysql.lib
%if "%_libdir" == "/usr/lib64"
sed -i s,usr/lib,usr/lib64,g %buildroot%_sysconfdir/chroot.d/mysql.lib
%endif
install -pD -m750 %SOURCE7 %buildroot%_sysconfdir/chroot.d/mysql.conf
install -pD -m750 %SOURCE8 %buildroot%_sysconfdir/chroot.d/mysql.all
install -pD -m750 %SOURCE9 %buildroot%_sbindir/mysql_migrate
install -pD -m644 %SOURCE10 %buildroot%_sysconfdir/sysconfig/mysqld
install -pD -m755 %SOURCE16 %buildroot%_controldir/mysqld
install -pD -m755 %SOURCE17 %buildroot%_controldir/mysqld-chroot

# install configuration files
install -pD -m644 support-files/rpm/my.cnf %buildroot%_sysconfdir/my.cnf
install -pD -m644 %SOURCE25 %buildroot%_sysconfdir/my.cnf.d/client.cnf
install -pD -m644 %SOURCE26 %buildroot%_sysconfdir/my.cnf.d/server.cnf
install -pD -m644 %SOURCE27 %buildroot%_sysconfdir/my.cnf.d/mysql-clients.cnf
install -pD -m644 %SOURCE28 %buildroot%_sysconfdir/my.cnf.server/server-chroot.cnf
install -pD -m644 %SOURCE29 %buildroot%_sysconfdir/my.cnf.server/server-no-chroot.cnf
%if_with galera
# install galera config file
install -p -m 0644 BUILD/support-files/wsrep.cnf %buildroot%_sysconfdir/my.cnf.d/galera.cnf
%endif

%if_with tokudb
install -pD -m644 storage/tokudb/tokudb.cnf %buildroot%_sysconfdir/my.cnf.d/tokudb.cnf
%endif

install -pD -m644 %SOURCE20 %buildroot%_tmpfilesdir/mysql.conf
install -pD -m644 %SOURCE21 %buildroot%_unitdir/mysqld.service
install -pD -m644 %SOURCE22 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/user.conf
install -pD -m644 %SOURCE23 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/notify.conf
install -pD -m644 %SOURCE24 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/notify-chroot.conf

ln -s mysqld.service %buildroot%_unitdir/mariadb.service
%if_with galera
# rm upstream script
rm -f %buildroot%_bindir/galera_new_cluster
install -pD -m755 %SOURCE19 %buildroot%_bindir/galera_new_cluster
%endif

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

# Install configuration files.
#install -pD -m644 /dev/null %buildroot%_sysconfdir/my.cnf
#install -pD -m600 %SOURCE5 %buildroot%ROOT/my.cnf

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

# Populate chroot with data to some extent.
install -pD -m644 %buildroot%_datadir/mysql/charsets/* \
	     %buildroot%ROOT%_datadir/mysql/charsets

(
    cd %buildroot%_datadir/mysql
    for i in */errmsg.sys; do
	install -pD -m644 $i  %buildroot%ROOT%_datadir/mysql/$i
    done
)

# Fix perl autodetection.
grep -EZl '^[[:space:]]*use the ' %buildroot%_bindir/* |
         xargs -r0 subst -p 's/\([[:space:]]*\)\(use the \)/\1then \2/g'


subst -p 's/\(BUGmysql="\)\([^"]*\)"/\1\2,mysql@packages.altlinux.org"/g' %buildroot%_bindir/mysqlbug

mkdir -p %buildroot%_docdir/%name-%version
install -p -m644 README %SOURCE14 BUILD/support-files/*.cnf %buildroot%_docdir/%name-%version

rm -f %buildroot%_bindir/safe_mysqld
rm -f %buildroot%_datadir/mysql/mysql{-*.spec,-log-rotate,.server}


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
%pre_control mysqld-chroot

%post server
rm -rf %ROOT/dev
%_sysconfdir/chroot.d/mysql.all force
%post_control -s local mysqld
%post_control -s enabled mysqld-chroot

%post_service mysqld

%preun server
%preun_service mysqld

%postun server
if [ $1 = 0 ]; then
    rm -f %ROOT/lib/* %ROOT/var/yp/binding/*
fi

%files

%files server
%doc README COPYING
%_initdir/mysqld
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_logrotatedir/*
%config %_sysconfdir/chroot.d/*
%config(noreplace) %_sysconfdir/my.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/server.cnf
%if_with galera
%config(noreplace) %_sysconfdir/my.cnf.d/galera.cnf
%endif
%config(noreplace) %_sysconfdir/my.cnf.server/*.cnf
%if_with tokudb
%config(noreplace) %_sysconfdir/my.cnf.d/tokudb.cnf
%endif
%_tmpfilesdir/mysql.conf
%_unitdir/mysqld.service
%_unitdir/mariadb.service
%config(noreplace) %_sysconfdir/systemd/system/mysqld.service.d/*.conf

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
%endif

%if_with mroonga
%_datadir/mysql/mroonga
%endif

%if_with galera
%_bindir/wsrep_*
%_bindir/galera_new_cluster
%endif

%_bindir/clustercheck
%_unitdir/mariadbcheck.socket
%_unitdir/mariadbcheck@.service
%config(noreplace) %_sysconfdir/xinetd.d/mariadbcheck

%_sbindir/*
%_libdir/mysql/plugin
%attr(3770,root,mysql) %dir %_logdir/mysql
%dir %_docdir/%name-%version
%_docdir/%name-%version/README
%_docdir/%name-%version/README.*
%_docdir/%name-%version/*.cnf
%attr(3771,root,mysql) %dir %ROOT
%attr(710,root,mysql) %dir %ROOT/%_lib
%attr(710,root,mysql) %dir %ROOT/%_libdir
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql/plugin
%if_with galera
%attr(710,root,mysql) %dir %ROOT/%_libdir/galera
%endif
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
%attr(3770,root,mysql) %dir %ROOT/db
%attr(750,mysql,mysql) %dir %ROOT/db/*
%attr(3770,root,mysql) %dir %ROOT/log
%attr(3770,root,mysql) %dir %ROOT/tmp
%dir %ROOT/run
%dir %ROOT/run/systemd
%ghost %ROOT/run/systemd/notify

%if_with common
%files common
%_datadir/mysql
%if_with mroonga
%exclude %_datadir/mysql/mroonga
%endif
%endif

%files server-control
%config %_controldir/*

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

%if_with mariabackup
%files backup
%_bindir/mariabackup
%_bindir/mbstream
%endif

%if_with libs
%files -n libmysqlclient%soname
%_libdir/*.so.*
%exclude %_libdir/libmysqld.so.*

%files -n libmysqld%soname
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
%_datadir/pkgconfig/mariadb.pc
# mysqlservices library is static, because it doesn't contain any code
# itself, and is meant to be statically linked to all plugins.
%_libdir/libmysqlservices.a


%files -n libmysqld-devel
%_libdir/libmysqld.so
%_bindir/mysql_client_test_embedded
%_bindir/mysqltest_embedded
%_man1dir/mysql_client_test_embedded.1*
%_man1dir/mysqltest_embedded.1*

%endif
%endif

%changelog
* Wed Dec 06 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.29-alt1%ubt
- 10.1.29
- Fixes for the following security vulnerabilities:
  + CVE-2017-10378
  + CVE-2017-10268
  + MDEV-13819

* Thu Nov 02 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.28-alt1%ubt
- 10.1.28

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.27-alt1%ubt
- 10.1.27

* Thu Sep 14 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.26-alt1%ubt
- 10.1.26
- Fixes for the following security vulnerabilities:
  + CVE-2017-3636
  + CVE-2017-3641
  + CVE-2017-3653

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 10.1.25-alt2%ubt
- BOOTSTRAP: introduced systemd, krb5, galera, cassandra, oqgraph knobs
  (on by default)
- E2K: avoid ABI check for now (fails)

* Mon Jul 17 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.25-alt1%ubt
- 10.1.25

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.23-alt1%ubt
- 10.1.23
- add maria-backup package
- Fixes for the following security vulnerabilities:
  + CVE-2017-3302
  + CVE-2017-3313
  + CVE-2017-3308
  + CVE-2017-3309
  + CVE-2017-3453
  + CVE-2017-3456
  + CVE-2017-3464

* Wed Mar 15 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.22-alt1
- 10.1.22

* Thu Jan 19 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.21-alt1
- 10.1.21

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.20-alt1
- 10.1.20

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.19-alt1
- 10.1.19
- rename package libmariadbembedded -> libmysqld%soname (ALT #29389)
- drop provides and requires lib%name, change to libmysqlclient%soname

* Thu Nov 03 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.18-alt2
- do not install and delete log files with rpm package
- update logrotate config (ALT #32376)
- add Conflicts: mytop
- add mariadb-server-control package for fix upgrade (ALT #31936)

* Tue Oct 25 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.18-alt1
- 10.1.18
- Fixes for the following security vulnerabilities:
  + CVE-2016-6663
  + CVE-2016-5616
  + CVE-2016-5624
  + CVE-2016-5626
  + CVE-2016-3492
  + CVE-2016-5629
  + CVE-2016-8283

* Mon Sep 05 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.17-alt1
- 10.1.17

* Tue Aug 02 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.16-alt1
- 10.1.16

* Wed Jul 06 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.15-alt1
- 10.1.15

* Tue May 10 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.14-alt1
- 10.1.14

* Thu Apr 21 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.13-alt1
- 10.1 branch snapshot

* Fri Mar 18 2016 Alexey Shabalin <shaba@altlinux.ru> 10.1.12-alt1
- 10.1.12
- fix log permitions (ALT #31899)
- build with kerberos auth_gssapi plugin
- add innodb_file_per_table to server.cnf (ALT #31885)

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.10-alt1
- 10.1.10
- fix typo and cleanup sysv init script
- removed a deprecated options from server.cnf

* Tue Dec 22 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.9-alt5
- snapshot of 10.1 branch (d58a77020)
- drop mount --bind /run/systemd/notify to chroot
- set Type=simple to systemd unit
- add drop-in examples to /etc/systemd/system/mysqld.service.d :
  + for run as mysql user
  + set Type=notify
  + run PreStart mount --bind /run/systemd/notify to chroot

* Tue Dec 15 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.9-alt4
- add mount --bind /run/systemd/notify to chroot for run as Type=notify unit

* Fri Dec 11 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.9-alt3
- add target new-cluster to init script
- fix galera_new_cluster for systemd and sysv

* Wed Dec 09 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.9-alt2
- fixed run with systemd type=notify (fixed link mysqld with libsystemd)

* Mon Nov 30 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.9-alt1
- 10.1.9
- fix typo in logrotate script (ALT #31532)

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 10.1.8-alt1
- 10.1.8
- update BR: for use compress
- build with systemd notify support
- provides/obsoletes mariadb-galera

* Thu Oct 01 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.21-alt4
- snapshot branch upstream/10.0
- comment empty options in /etc/sysconfig/mysqld (ALT #31293)
- change description MySQL -> MySQL/MariaDB (ALT #31307)
- update README.ALT
- add bug report url in mysql_install_db

* Tue Sep 15 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.21-alt2
- don't read config in /var/lib/mysql/my.cnf
- use /etc/my.cnf.d/server.cnf as default server config
- drop hardcode chroot and datadir in safe_mysql, mysqld_wrapper, mysql_install_db;
  read chroot and datadir from config
- split chroot and non-chroot options 
  to /etc/my.cnf.server/server-chroot.cnf and /etc/my.cnf.server/server-no-chroot.cnf
- add control mysqld-chroot for enable and disable chroot
- add native systemd unit
- add optional config /etc/systemd/system/mysqld.service.d/user.conf
  for run as mysql user

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.21-alt1
- 10.0.21
- sync with MySQL-5.5.43-alt1 (patches, build options, files, chroot)

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5.34-alt1
- New version

* Tue Nov 19 2013 Sergey V Turchin <zerg@altlinux.org> 5.5.33a-alt4
- provide mysql virtual package (ALT#29595)

* Wed Oct 16 2013 Sergey V Turchin <zerg at altlinux dot org> 5.5.33a-alt2.M70P.1
- built for p7

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
