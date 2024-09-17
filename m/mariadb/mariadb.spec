%add_findreq_skiplist %_datadir/mysql/mysql-test/mysql-test-run.pl
%add_findreq_skiplist %_bindir/wsrep_sst_xtrabackup
%add_findreq_skiplist %_bindir/wsrep_sst_xtrabackup-v2

%define embedded_soname 19
%define soname 3
# default plugin dir is %%_libdir/mysql/plugin
%define plugindir %_lib/%name/plugin

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_with server
%def_with libs
%def_with devel
%def_with client
%def_with bench
%def_with mariabackup
%def_disable build_test
%def_disable static
%define mysqld_user mysql
%define _libexecdir %_sbindir
%define ROOT %_localstatedir/mysql

%def_without libwrap
%def_with pcre
%def_with systemd
%def_without libarchive

%ifarch x86_64 aarch64 ppc64le
%def_without mroonga
%def_with rocksdb
%else
%def_without mroonga
%def_without rocksdb
%endif

%def_without cassandra
%ifnarch armh
%def_with galera
%def_with oqgraph
%else
%def_without galera
%def_without oqgraph
%endif
%def_with s3
%def_with sphinx
%def_with connect
%def_with gssapi
%def_with cracklib
%def_with jemalloc

Name: mariadb
Version: 11.4.3
Release: alt2

Summary: A very fast and reliable SQL database engine
License: GPLv2 and LGPLv2
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

# git submodules
Source101: libmariadb.tar
Source102: rocksdb.tar
Source103: wsrep-lib.tar
Source104: wsrep-API.tar
Source105: columnstore.tar
Source106: libmarias3.tar
Source107: fmt.tar

Patch0: %name-%version.patch

# ALTLinux
Patch1: mariadb-10.6.8-alt-chroot.patch
Patch2: mysql-5.0.20-alt-libdir.patch
Patch4: mariadb-10.1.8-alt-client.patch
#Patch5: mariadb-10.0.21-alt-load_defaults.patch
Patch7: mariadb-10.3.8-alt-config-libs.patch

# Patches specific for this mysql package
Patch30: mariadb-errno.patch
#Patch31: mariadb-string-overflow.patch
Patch32: mariadb-basedir.patch
Patch33: mariadb-covscan-signexpr.patch
#Patch34: mariadb-covscan-stroverflow.patch

Patch101: rocksdb-6.8.0-alt-add-libatomic-if-needed.patch
Patch102: mariadb-10.5.11-alt-link-with-latomic-if-needed.patch
Patch103: rocksdb-alt-upstream-gcc13.patch
Patch104: mariadb-10.11.9-disable-download-fmt.patch
Patch105: mariadb-10.11.9-alt-wsrep-API_fix_api-ver.patch

Patch2000: mariadb-e2k.patch

Requires: %name-server = %EVR
Requires: %name-client = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libncursesw-devel libreadline-devel libssl-devel perl-DBI perl-DBD-MariaDB libpam-devel libevent-devel cmake ctest bison doxygen groff-base groff-ps dos2unix xsltproc
BuildRequires: libaio-devel libedit-devel perl-GD perl-threads perl-Memoize perl-devel
BuildRequires: liblz4-devel zlib-devel bzlib-devel liblzma-devel liblzo2-devel libsnappy-devel libzstd-devel
BuildRequires: chrooted control
BuildRequires: libxml2-devel xml-utils
BuildRequires: libcurl-devel
BuildRequires: python3
BuildRequires: checkpolicy policycoreutils
%{?_with_libwrap:BuildRequires: libwrap-devel}
%{?_with_cassandra:BuildRequires: boost-devel}
%{?_with_oqgraph:BuildRequires: boost-devel libjudy-devel}
%{?_with_jemalloc:BuildRequires: libjemalloc-devel}
%{?_with_pcre:BuildRequires: libpcre2-devel}
%{?_with_systemd:BuildRequires: libsystemd-devel}
%{?_with_gssapi:BuildRequires: libkrb5-devel}
%{?_with_libarchive:BuildRequires: libarchive-devel}
%{?_with_cracklib:BuildRequires: cracklib-devel cracklib-words}
%{?_with_sphinx:BuildRequires: sphinx libsphinxclient-devel}
%{?_with_cassandra:BuildRequires: cassandra thrift-devel}

%ifnarch %arm
BuildRequires: libnuma-devel
%endif

%description
MariaDB is a community developed branch of MySQL - a multi-user, multi-threaded
SQL database server. It is a client/server implementation consisting of
a server daemon (mysqld) and many different client programs and libraries.
The base package contains the standard MariaDB/MySQL client programs and
generic MySQL files.

%package server
Summary: A very fast and reliable MariaDB database server
Group: Databases
Requires: lib%name%soname = %EVR %name-client = %EVR
Requires: %name-common = %EVR
Provides: mysql-server = %EVR
Provides: mysql = %version
Provides: %name-engine-extra = %EVR
Obsoletes: %name-engine-extra < %EVR
Provides: %name-engine-obsolete = %EVR
Obsoletes: %name-engine-obsolete < %EVR
Provides: %name-pam = %EVR
Obsoletes: %name-pam < %EVR
Conflicts: MySQL-server
Requires: chrooted %name-server-control

%description server
MariaDB is a multi-user, multi-threaded SQL database server. It is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. This package contains
the MariaDB server and some accompanying files and directories.
MariaDB is a community developed branch of MySQL.

%package server-galera
Summary: The configuration files and scripts for galera replication
Group: Databases
Requires: %name-common = %EVR
Requires: %name-server = %EVR
# wsrep requirements
Requires: libgalera_smm >= 26.4.4
Requires: rsync lsof
# obsoletion of mariadb-galera-server
Provides: %name-galera-server = %EVR
Obsoletes: %name-galera-server < %EVR
Provides: %name-galera = %EVR
Obsoletes: %name-galera < %EVR
Conflicts: %name-server < 10.3.8-alt3

%description server-galera
MariaDB is a multi-user, multi-threaded SQL database server. It is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. This package contains
the MariaDB server and some accompanying files and directories.
MariaDB is a community developed branch of MySQL.

This package contains configuration files and scripts for galera replication.

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
Requires: perl-DBD-MariaDB
Conflicts: %name-server < %EVR
Conflicts: MySQL-server-perl
Conflicts: mytop
Provides: %name-galera-server-perl = %EVR
Obsoletes: %name-galera-server-perl < %EVR
BuildArch: noarch

%description server-perl
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.
This package contents perl utils for MySQL-server.

%package oqgraph-engine
Summary: The Open Query GRAPH engine for MariaDB
Group: Databases
Requires: %name-server = %EVR

%description oqgraph-engine
The package provides Open Query GRAPH engine (OQGRAPH) as plugin for MariaDB
database server. OQGRAPH is a computation engine allowing hierarchies and more
complex graph structures to be handled in a relational fashion. In a nutshell,
tree structures and friend-of-a-friend style searches can now be done using
standard SQL syntax, and results joined onto other tables.

%package connect-engine
Summary: The CONNECT storage engine for MariaDB
Group: Databases
Requires: %name-server = %EVR

%description connect-engine
The CONNECT storage engine enables MariaDB to access external local or
remote data (MED). This is done by defining tables based on different data
types, in particular files in various formats, data extracted from other DBMS
or products (such as Excel), or data retrieved from the environment
(for example DIR, WMI, and MAC tables).

%package rocksdb-engine
Summary: The RocksDB storage engine for MariaDB
Group: Databases
Requires: %name-server = %EVR
Conflicts: rocksdb-tools

%description rocksdb-engine
The RocksDB storage engine is used for high performance servers on SSD drives.

%package cracklib-password-check
Summary: The password strength checking plugin
Group: Databases
Requires: %name-server = %EVR
Requires: cracklib-words

%description cracklib-password-check
CrackLib is a password strength checking library. It is installed by default
in many Linux distributions and is invoked automatically (by pam_cracklib.so)
whenever the user login password is modified.
Now, with the cracklib_password_check password validation plugin, one can
also use it to check MariaDB account passwords.

%package gssapi-server
Summary: GSSAPI authentication plugin for server
Group: Databases
Requires: %name-server = %EVR

%description gssapi-server
GSSAPI authentication server-side plugin for MariaDB for passwordless login.
This plugin includes support for Kerberos on Unix.

%package sphinx-engine
Summary: The Sphinx storage engine for MariaDB
Group: Databases
Requires: %name-server = %EVR
Requires: sphinx libsphinxclient

%description sphinx-engine
The Sphinx storage engine for MariaDB.

%package cassandra-engine
Summary: The Cassandra storage engine for MariaDB - EXPERIMENTAL VERSION
Group: Databases
Requires: %name-server = %EVR

%description cassandra-engine
The Cassandra storage engine for MariaDB. EXPERIMENTAL VERSION!

%package s3-engine
Summary: The S3 storage engine for MariaDB
Group: Databases
Requires: %name-server = %EVR

%description s3-engine
The S3 read only storage engine allows archiving MariaDB tables in Amazon S3,
or any third-party public or private cloud that implements S3 API,
but still have them accessible for reading in MariaDB.

%package client
Summary: Client
Group: Databases
Requires: lib%name%soname = %EVR %name-common = %EVR
Provides: mysql-client = %EVR
Conflicts: MySQL-client

%description client
This package contains the standard MariaDB clients.

%package common
Summary: Common files used in client and servers
Group: Databases
BuildArch: noarch
Conflicts: MySQL-server

%description common
This package contains the common files for MariaDB client and servers.

%package bench
Summary: Benchmarks and test system
Group: System/Servers
BuildArch: noarch
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

%package -n lib%name%soname
Summary: Shared libraries
Group: System/Libraries
License: LGPLv2.1
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%name%soname
This package contains the shared libraries (*.so*) which certain languages
and applications need to dynamically load and use MariaDB.

%package -n lib%name-devel
Summary: Development header files and libraries
Group: Development/Other
# see also #28676
Requires: libssl-devel zlib-devel
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
This package contains the development header files and libraries necessary
to develop MariaDB client applications.

%package -n lib%{name}d%embedded_soname
Summary: MariaDB as an embeddable library
Group: System/Libraries
Requires: %name-common = %EVR
Obsoletes: libmariadbembedded < %EVR
Provides: libmysqld%embedded_soname = %EVR
Obsoletes: libmysqld%embedded_soname < %EVR

%description -n lib%{name}d%embedded_soname
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains a version of the MariaDB server that can be embedded
into a client application instead of running as a separate process.

The API is identical for the embedded MariaDB version
and the client/server version.

%package -n lib%{name}d-devel
Summary: Development files for MariaDB as an embeddable library
Group: Development/Other
Requires: libmariadbd%embedded_soname = %EVR
Obsoletes: libmariadbembedded-devel < %EVR
Provides: libmysqld%embedded_soname-devel = %EVR
Obsoletes: libmysqld%embedded_soname-devel < %EVR

%description -n lib%{name}d-devel
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains files needed for developing and testing with
the embedded version of the MariaDB server.

The API is identical for the embedded MariaDB version and the client/server
version.

%prep
%setup
tar -xf %SOURCE101 -C libmariadb
tar -xf %SOURCE102 -C storage/rocksdb/rocksdb
tar -xf %SOURCE103 -C wsrep-lib
tar -xf %SOURCE104 -C wsrep-lib/wsrep-API/v26
tar -xf %SOURCE105 -C storage/columnstore/columnstore
tar -xf %SOURCE106 -C storage/maria/libmarias3
mkdir -p extra/libfmt/src/libfmt
tar -xf %SOURCE107 -C extra/libfmt/src/libfmt

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
#%%patch5 -p1
%patch7 -p1

%patch30 -p1
#%%patch31 -p1
%patch32 -p1
#%%patch33 -p1
#%%patch34 -p1

%patch101 -p1 -d ./storage/rocksdb/rocksdb
#%%patch102 -p1
%patch103 -p1 -d ./storage/rocksdb/rocksdb
%patch104 -p1
%patch105 -p1 -d ./wsrep-lib/wsrep-API/v26

%ifarch %e2k
%patch2000 -p1
sed -i 's|-fno-sanitize=shift|""|' \
  plugin/auth_ed25519/CMakeLists.txt \
  libmariadb/plugins/auth/CMakeLists.txt
sed -i 's|WSREP_NORETURN|__attribute__((noreturn))|' \
  wsrep-lib/include/wsrep/thread_service.hpp
sed -i 's|xmlGetLastError|(xmlErrorPtr)&|' \
	storage/connect/libdoc.cpp
%endif

# Replace that horror.
sed 's,@datadir@,%_datadir,g' <%SOURCE15 >scripts/mysql_install_db.sh

# Prepare commands list for completion in mysql client.
sed -ne 's/^\(  { "[A-Z][^"]*"\).*/\1, 0, 0, 0, "" },/pg' <sql/lex.h >client/mysql_symbols.inc

# Not needed with 5.5 but doesn't hurt anyways
chmod -R a-s,go-w sql-bench

#fix shebang.req: ERROR: /usr/src/tmp/mariadb-buildroot/usr/share/mysql/sql-bench/innotest1: trailing <CR> in interpreter: #!/usr/bin/perl<CR>
find sql-bench -type f -name 'innotest*' | xargs dos2unix

%build
%ifarch %ix86
# Disable LTO for fix crash compile on i586, until fix gcc-13 bug
%define optflags_lto %nil
%endif
CFLAGS="%optflags -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
# force PIC mode so that we can build libmysqld.so
CFLAGS="$CFLAGS -fPIC"
# GCC 4.9 causes segfaults: https://mariadb.atlassian.net/browse/MDEV-6360
CFLAGS="$CFLAGS -fno-delete-null-pointer-checks"
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS
LDFLAGS="$LDFLAGS -pie -Wl,-z,relro,-z,now"
export LDFLAGS

%cmake_insource \
    -DBUILD_CONFIG=mysql_release \
    -DFEATURE_SET="community" \
    -DINSTALL_LAYOUT=RPM \
    -DRPM="fedora29" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS" \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
    -DCMAKE_INSTALL_PREFIX="%prefix" \
    -DINSTALL_SYSCONFDIR="%_sysconfdir" \
    -DINSTALL_SYSCONF2DIR="%_sysconfdir/my.cnf.d" \
    -DINSTALL_SYSTEMD_SYSUSERSDIR:STRING="/lib/sysusers.d" \
    -DINSTALL_SYSTEMD_TMPFILESDIR:STRING="%_tmpfilesdir" \
    -DINSTALL_SYSTEMD_UNITDIR:STRING="%_unitdir" \
    -DMYSQL_UNIX_ADDR="%ROOT/mysql.sock" \
    -DMYSQL_DATADIR="%ROOT" \
    -DMYSQL_USER=mysql \
    -DWITH_READLINE=ON \
    -DPYTHON_SHEBANG=%__python3 \
    -DWITH_JEMALLOC=%{?_with_jemalloc:system}%{?_without_jemalloc:NO} \
    -DWITH_SSL=system \
    -DWITH_ZLIB=system \
    %{?_with_pcre:-DWITH_PCRE=system -DPCRE_INCLUDES=/usr/include/pcre} \
    -DPLUGIN_MROONGA=%{?_with_mroonga:DYNAMIC}%{?_without_mroonga:NO} \
    -DPLUGIN_OQGRAPH=%{?_with_oqgraph:DYNAMIC}%{?_without_oqgraph:NO} \
    -DPLUGIN_ROCKSDB=%{?_with_rocksdb:DYNAMIC}%{?_without_rocksdb:NO} \
    -DPLUGIN_SPHINX=%{?_with_sphinx:DYNAMIC}%{?_without_sphinx:NO} \
    -DPLUGIN_CONNECT=%{?_with_connect:DYNAMIC}%{?_without_connect:NO} \
    -DWITH_CASSANDRA=%{?_with_cassandra:TRUE}%{?_without_cassandra:FALSE} \
    -DDPLUGIN_S3=%{?_with_s3:DYNAMIC}%{?_without_s3:NO} \
    -DPLUGIN_COLUMNSTORE=NO \
    -DWITH_PIC=ON \
    -DWITH_EXTRA_CHARSETS=all \
    -DWITH_INNOBASE_STORAGE_ENGINE=ON \
    -DWITH_PARTITION_STORAGE_ENGINE=ON \
    -DWITH_FEDERATED_STORAGE_ENGINE=ON \
    -DWITH_WSREP=ON \
    -DWITH_INNODB_DISALLOW_WRITES=1 \
    -DENABLED_LOCAL_INFILE=ON \
    -DPLUGIN_AWS_KEY_MANAGEMENT=NO \
    -DCONNECT_WITH_MONGO=OFF \
    -DCONNECT_WITH_JDBC=OFF \
    -DWITH_EMBEDDED_SERVER=ON \
    -DWITH_LIBWRAP=%{?_with_libwrap:ON}%{?_without_libwrap:FALSE} \
    %{?_without_mariabackup:-DWITH_MARIABACKUP=OFF} \
    %{?_without_libarchive:-DWITH_LIBARCHIVE=OFF} \
    %{?_without_server:-DWITHOUT_SERVER=ON} \
%if "%_lib" == "lib64"
    -DCMAKE_SIZEOF_VOID_P=8 \
%endif
    -DINSTALL_PLUGINDIR=%plugindir \
    -DCOMPILATION_COMMENT="(%distribution)" \
    -DMYSQL_SERVER_SUFFIX="-%release"

#    -DWITH_EMBEDDED_SERVER=ON \
#    -DWITH_PLUGIN_FEEDBACK=ON \

%make_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_includedir,%_mandir,%_infodir,%_datadir/sql-bench,%_logdir/mysql}
mkdir -p %buildroot%ROOT/{etc,/%_lib,%_libdir,%prefix/%plugindir/auth_pam_tool_dir,%_libdir/galera,dev,log,tmp,run/systemd,/var/{nis,yp/binding},db/mysql,usr/share/mariadb/charsets}
touch %buildroot%ROOT{%_sysconfdir/{hosts,services,{host,nsswitch,resolv}.conf},/dev/urandom,/var/nis/NIS_COLD_START,/run/systemd/notify,%prefix/%plugindir/auth_pam_tool_dir/auth_pam_tool}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%makeinstall_std

# RPM install style leftovers
rm -f %buildroot%_sysconfdir/init.d/mysql
rm -f %buildroot%_sbindir/rcmysql
rm -rf %buildroot{%_libdir/libmysqld.a,%_defaultdocdir/*}
rm -rf %buildroot{%_unitdir,%_tmpfilesdir,/lib/sysusers.d}

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

install -pD -m644 %SOURCE20 %buildroot%_tmpfilesdir/%name.conf
install -pD -m644 %SOURCE21 %buildroot%_unitdir/mysqld.service
install -pD -m644 %SOURCE22 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/user.conf
install -pD -m644 %SOURCE23 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/notify.conf
install -pD -m644 %SOURCE24 %buildroot%_sysconfdir/systemd/system/mysqld.service.d/notify-chroot.conf

%if_with galera
# install galera config file
sed -i -r 's|^wsrep_provider=none|wsrep_provider=%_libdir/galera/libgalera_smm.so|' support-files/wsrep.cnf
install -p -m 0644 support-files/wsrep.cnf %buildroot%_sysconfdir/my.cnf.d/galera.cnf
# rm upstream script
rm -f %buildroot%_bindir/galera_new_cluster
install -pD -m755 %SOURCE19 %buildroot%_bindir/galera_new_cluster

# install the clustercheck script
install -pD -m755 %SOURCE70 %buildroot%_bindir/clustercheck
install -pD -m644 %SOURCE71 %buildroot%_sysconfdir/sysconfig/clustercheck
install -pD -m644 %SOURCE72 %buildroot%_unitdir/mariadbcheck.socket
install -pD -m644 %SOURCE73 %buildroot%_unitdir/mariadbcheck@.service
install -pD -m644 %SOURCE74 %buildroot%_sysconfdir/xinetd.d/mariadbcheck
%endif

ln -s mysqld.service %buildroot%_unitdir/mariadb.service

# Backwards compatibility symlinks (ALT #14863)
mkdir -p %buildroot%_bindir
ln -snf ../sbin/safe_mysqld %buildroot%_bindir/mysqld_safe

pushd %buildroot%_bindir
    ln -sf mysqlcheck mysqlrepair
    ln -sf mysqlcheck mysqlanalyze
    ln -sf mysqlcheck mysqloptimize
popd

# Install configuration files.
#install -pD -m644 /dev/null %%buildroot%%_sysconfdir/my.cnf
#install -pD -m600 %%SOURCE5 %%buildroot%%ROOT/my.cnf

# most current distro packages have it in %%_bindir (hello kde4?)
# but the server subpackage obtains /usr/sbin/mysql_install_db autoreq
ln -sf {../bin,%buildroot%_sbindir}/mysql_install_db

# move pkgconfig file to arch dep path
#mv %%buildroot%%_datadir/pkgconfig/mariadb.pc %%buildroot%%_pkgconfigdir/
# NB: still a problem for cmake on %%e2k as of 10.4.14, do not remove
# (gave up on figuring out what was the particular crap that
# generated broken libmariadb/cmake/install.cmake) // mike@
mkdir -p %buildroot%_pkgconfigdir
%if "%_lib" == "lib64"
    if [ -f %buildroot%_prefix/lib/pkgconfig/libmariadb.pc ]; then
        mv %buildroot%_prefix/lib/pkgconfig/libmariadb.pc %buildroot%_pkgconfigdir/
    fi
%endif

# Populate chroot with data to some extent.
install -pD -m644 %buildroot%_datadir/mariadb/charsets/* \
         %buildroot%ROOT%_datadir/mariadb/charsets

(
    cd %buildroot%_datadir/mariadb
    for i in */errmsg.sys; do
    install -pD -m644 $i  %buildroot%ROOT%_datadir/mariadb/$i
    done
)

# Fix perl autodetection.
grep -EZl '^[[:space:]]*use the ' %buildroot%_bindir/* |
         xargs -r0 subst -p 's/\([[:space:]]*\)\(use the \)/\1then \2/g'


mkdir -p %buildroot%_docdir/%name-%version
install -p -m644 README.md %SOURCE14 support-files/*.cnf %buildroot%_docdir/%name-%version

rm -f %buildroot%_bindir/safe_mysqld
rm -f %buildroot%_datadir/mysql/mysql{-*.spec,-log-rotate,.server}
# remove unneeded expamles
rm -f %buildroot%_datadir/mysql/{mariadb.logrotate,mini-benchmark}


rm -rf %buildroot%_datadir/mariadb-test
rm -f %buildroot%prefix/%plugindir/*.la
#rmdir %%buildroot%%prefix/%%plugindir/debug

# broken manpages referencing missing paths
#rm -f %%buildroot%%_man1dir/mysql{_client_,}test_embedded.1

%define get_datadir \
DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\\(.*\\)/\\1/pg' |tail -1` \
[ -n "$DATADIR" ] || { echo "Failed to read configuration"; exit 1; }


# this command enables plugins, but needs ini file + configuration in my.cnf before executing
# and oh yeah, mysql must be stopped... => useless
rm -f %buildroot%_bindir/mysql_plugin
rm -f %buildroot%_bindir/mariadb-plugin
rm -f %buildroot%_mandir/man1/mysql_plugin.1*
rm -f %buildroot%_mandir/man1/mariadb-plugin.1*
rm -f %buildroot%prefix/%plugindir/daemon_example.ini

# remove more useless plugins
#rm -f %%buildroot%%prefix/%%plugindir/auth_test_plugin.so
#rm -f %%buildroot%%prefix/%%plugindir/dialog_examples.so


# house cleaning
rm -f %buildroot%_bindir/mysql_embedded
rm -f %buildroot%_bindir/mariadb-embedded
rm -rf %buildroot%_datadir/info
rm -f %buildroot%_datadir/mariadb/binary-configure
rm -f %buildroot%_datadir/mariadb/my-huge.cnf
rm -f %buildroot%_datadir/mariadb/my-innodb-heavy-4G.cnf
rm -f %buildroot%_datadir/mariadb/my-large.cnf
rm -f %buildroot%_datadir/mariadb/my-medium.cnf
rm -f %buildroot%_datadir/mariadb/my-small.cnf
rm -f %buildroot%_datadir/mariadb/wsrep.cnf
rm -f %buildroot%_datadir/mariadb/mysqld_multi.server
rm -f %buildroot%_datadir/mariadb/mysql-log-rotate
rm -f %buildroot%_datadir/mariadb/mysql.server
rm -f %buildroot%_datadir/mariadb/magic

# cleanup
rm -f %buildroot/etc/my.cnf.d/enable_encryption.preset
rm -f %buildroot%_bindir/galera_recovery
rm -f %buildroot%_bindir/mariadb-service-convert
rm -f %buildroot%_bindir/mysqld_safe_helper
rm -f %buildroot%_bindir/mariadbd-safe-helper
rm -f %buildroot%_bindir/test-connect-t
rm -f %buildroot%_libdir/libmariadbd.a
rm -f %buildroot%_libdir/libmysqlclient.a
rm -f %buildroot%_libdir/libmysqlclient_r.a
rm -f %buildroot%_libdir/libmariadbclient.a
rm -f %buildroot%_libdir/libmariadb.a

################################################################################
# run the tests
%if_enabled build_test
%check
make test-force
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

%if_with server
%files

%files server
%doc README.md COPYING
%_initdir/mysqld
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_logrotatedir/*
%config %_sysconfdir/chroot.d/*
%config(noreplace) %_sysconfdir/my.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/server.cnf
%config(noreplace) %_sysconfdir/my.cnf.server/*.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/spider.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/hashicorp_key_management.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/provider_bzip2.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/provider_lz4.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/provider_lzma.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/provider_lzo.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/provider_snappy.cnf
%_tmpfilesdir/%name.conf
%_unitdir/mysqld.service
%_unitdir/mariadb.service
%config(noreplace) %_sysconfdir/systemd/system/mysqld.service.d/*.conf

%_bindir/aria*
%{?_with_s3:%exclude %_bindir/aria_s3_copy}
%_bindir/*isam*
%_bindir/mysql_fix_extensions
%_bindir/mariadb-fix-extensions
%_bindir/mysql_secure_installation
%_bindir/mariadb-secure-installation
%_bindir/mysql_tzinfo_to_sql
%_bindir/mariadb-tzinfo-to-sql
%_bindir/mysql_upgrade
%_bindir/mariadb-upgrade
%_bindir/mysqld_multi
%_bindir/mariadbd-multi
%_bindir/mysqld_safe
%_bindir/mariadbd-safe
%_bindir/mysql_install_db
%_bindir/mariadb-install-db
%_bindir/mariadb-conv
%if_with mroonga
%_datadir/mariadb/mroonga
%endif

%_sbindir/*
%prefix/%plugindir/*
%{?_with_oqgraph:%exclude %prefix/%plugindir/ha_oqgraph.so}
%{?_with_connect:%exclude %prefix/%plugindir/ha_connect.so}
%{?_with_cracklib:%exclude %prefix/%plugindir/cracklib_password_check.so}
%{?_with_rocksdb:%exclude %prefix/%plugindir/ha_rocksdb.so}
%{?_with_gssapi:%exclude %prefix/%plugindir/auth_gssapi.so}
%{?_with_sphinx:%exclude %prefix/%plugindir/ha_sphinx.so}
%{?_with_cassandra:%exclude %prefix/%plugindir/ha_cassandra.so}
%{?_with_s3:%exclude %prefix/%plugindir/ha_s3.so}
%{?_with_gssapi:%exclude %prefix/%plugindir/auth_gssapi_client.so}
%exclude %prefix/%plugindir/client_ed25519.so
%exclude %prefix/%plugindir/dialog.so
%exclude %prefix/%plugindir/mysql_clear_password.so
%exclude %prefix/%plugindir/caching_sha2_password.so
%exclude %prefix/%plugindir/sha256_password.so

# pam
%config(noreplace) %_sysconfdir/security/user_map.conf
%_pam_modules_dir/pam_user_map.so
%attr(755,root,root) %dir %prefix/%plugindir/auth_pam_tool_dir
%attr(4710,root,mysql) %prefix/%plugindir/auth_pam_tool_dir/auth_pam_tool
%attr(755,root,root) %dir %ROOT/%prefix/%plugindir/auth_pam_tool_dir
%attr(4710,root,mysql) %ROOT/%prefix/%plugindir/auth_pam_tool_dir/auth_pam_tool

%attr(3770,root,mysql) %dir %_logdir/mysql
%dir %_docdir/%name-%version
%_docdir/%name-%version/README.*
%_docdir/%name-%version/*.cnf
%attr(3771,root,mysql) %dir %ROOT
%attr(710,root,mysql) %dir %ROOT/%_lib
%attr(710,root,mysql) %dir %ROOT/%_libdir
%attr(710,root,mysql) %dir %ROOT/%_libdir/%name
%attr(750,root,mysql) %dir %ROOT/%prefix/%plugindir
%if_with galera
%attr(750,root,mysql) %dir %ROOT/%_libdir/galera
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
%ROOT%_datadir/mariadb
%attr(3770,root,mysql) %dir %ROOT/db
%attr(750,mysql,mysql) %dir %ROOT/db/*
%attr(3770,root,mysql) %dir %ROOT/log
%attr(3770,root,mysql) %dir %ROOT/tmp
%dir %ROOT/run
%dir %ROOT/run/systemd
%ghost %ROOT/run/systemd/notify

%if_with galera
%files server-galera
%doc Docs/README-wsrep
%_bindir/wsrep_*
%_bindir/galera_new_cluster
%_bindir/clustercheck
%_unitdir/mariadbcheck.socket
%_unitdir/mariadbcheck@.service
%config(noreplace) %_sysconfdir/xinetd.d/mariadbcheck
%config(noreplace) %_sysconfdir/my.cnf.d/galera.cnf
%_datadir/mariadb/wsrep_notify
%endif

%if_with cracklib
%files cracklib-password-check
%config(noreplace) %_sysconfdir/my.cnf.d/cracklib_password_check.cnf
%prefix/%plugindir/cracklib_password_check.so
%endif

%if_with rocksdb
%files rocksdb-engine
%config(noreplace) %_sysconfdir/my.cnf.d/rocksdb.cnf
%_bindir/myrocks_hotbackup
%_bindir/mysql_ldb
%_bindir/mariadb-ldb
%_bindir/sst_dump
%prefix/%plugindir/ha_rocksdb.so
%_man1dir/mysql_ldb.1*
%_man1dir/mariadb-ldb.1*
%endif

%if_with gssapi
%files gssapi-server
%prefix/%plugindir/auth_gssapi.so
%config(noreplace) %_sysconfdir/my.cnf.d/auth_gssapi.cnf
%endif

%if_with sphinx
%files sphinx-engine
%prefix/%plugindir/ha_sphinx.so
%endif

%if_with oqgraph
%files oqgraph-engine
%config(noreplace) %_sysconfdir/my.cnf.d/oqgraph.cnf
%prefix/%plugindir/ha_oqgraph.so
%endif

%if_with connect
%files connect-engine
%config(noreplace) %_sysconfdir/my.cnf.d/connect.cnf
%prefix/%plugindir/ha_connect.so
%endif

%if_with cassandra
%files cassandra-engine
%config(noreplace) %_sysconfdir/my.cnf.d/cassandra.cnf
%prefix/%plugindir/ha_cassandra.so
%endif

%if_with s3
%files s3-engine
%_bindir/aria_s3_copy
%_man1dir/aria_s3_copy.1*
%config(noreplace) %_sysconfdir/my.cnf.d/s3.cnf
%prefix/%plugindir/ha_s3.so
%endif

%files common
%_datadir/mariadb
%if_with mroonga
%exclude %_datadir/mariadb/mroonga
%endif
%exclude %_datadir/mariadb/wsrep_notify

%files server-control
%config %_controldir/*

%files server-perl
%_bindir/mysql_convert_table_format
%_bindir/mariadb-convert-table-format
%_bindir/mysql_find_rows
%_bindir/mariadb-find-rows
%_bindir/mysql_setpermission
%_bindir/mariadb-setpermission
%_bindir/mysqlhotcopy
%_bindir/mariadb-hotcopy
%_bindir/mysqlaccess
%_bindir/mariadb-access
%_bindir/mysqldumpslow
%_bindir/mariadb-dumpslow
%_bindir/mytop
%endif

%if_with client
%files client
%dir %_sysconfdir/my.cnf.d
%config(noreplace) %_sysconfdir/my.cnf.d/client.cnf
%config(noreplace) %_sysconfdir/my.cnf.d/mysql-clients.cnf
%_bindir/innochecksum
%_bindir/msql2mysql
%_bindir/my_print_defaults
%_bindir/mysql
%_bindir/mariadb
%_bindir/mysql_client_test
%_bindir/mariadb-client-test
%_bindir/mysqladmin
%_bindir/mariadb-admin
%_bindir/mysqlanalyze
%_bindir/mysqlbinlog
%_bindir/mariadb-binlog
%_bindir/mysqlcheck
%_bindir/mariadb-check
%_bindir/mysqldump
%_bindir/mariadb-dump
%_bindir/mysqlimport
%_bindir/mariadb-import
%_bindir/mysqloptimize
%_bindir/mysqlrepair
%_bindir/mysqlshow
%_bindir/mariadb-show
%_bindir/mysqlslap
%_bindir/mariadb-slap
%_bindir/mysqltest
%_bindir/mariadb-test
%_bindir/mysql_waitpid
%_bindir/mariadb-waitpid
%_bindir/perror
%_bindir/replace
%_bindir/resolve*

%_mandir/man?/*
%exclude %_man1dir/mysql_config.1*
%exclude %_man1dir/mariadb_config.1*
%exclude %_man1dir/mysql_client_test_embedded.1*
%exclude %_man1dir/mariadb-client-test-embedded.1*
%exclude %_man1dir/mariadb-client-test.1*
%exclude %_man1dir/mariadb-client-test-embedded.1*
%exclude %_man1dir/mysqltest_embedded.1*
%exclude %_man1dir/mariadb-test-embedded.1*
%exclude %_man1dir/mariadb-test.1*
%if_with rocksdb
%exclude %_man1dir/mysql_ldb.1*
%exclude %_man1dir/mariadb-ldb.1*
%endif
%{?_with_rocksdb:%exclude %_man1dir/mysql_ldb.1*}
%{?_with_rocksdb:%exclude %_man1dir/mariadb-ldb.1*}
%{?_with_s3:%exclude %_man1dir/aria_s3_copy.1*}
%endif

%if_with bench
%files bench
%_datadir/sql-bench
%endif

%if_with mariabackup
%files backup
%_bindir/mariabackup
%_bindir/mariadb-backup
%_bindir/mbstream
%endif

%if_with libs
%files -n lib%name%soname
%_libdir/lib%name.so.%soname
# Clients plugin
%dir %prefix/%plugindir
%{?with_gssapi:%prefix/%plugindir/auth_gssapi_client.so}
%prefix/%plugindir/client_ed25519.so
%prefix/%plugindir/dialog.so
%prefix/%plugindir/mysql_clear_password.so
%prefix/%plugindir/caching_sha2_password.so
%prefix/%plugindir/sha256_password.so

%if_with server
%files -n lib%{name}d%embedded_soname
%_libdir/lib%{name}d.so.%embedded_soname
%endif

%if_with devel
%files -n lib%name-devel
%doc INSTALL-SOURCE
%_bindir/mysql_config
%_bindir/mariadb_config
%_bindir/mariadb-config
%_libdir/lib%name.so
%_libdir/libmysqlclient.so
%_libdir/libmysqlclient_r.so
%_includedir/*
#_mandir/man1/comp_err.1*
%_man1dir/mysql_config.1*
%_man1dir/mariadb_config.1*
%_aclocaldir/mysql.m4
%_pkgconfigdir/mariadb.pc
%_pkgconfigdir/libmariadb.pc
# mysqlservices library is static, because it doesn't contain any code
# itself, and is meant to be statically linked to all plugins.
%_libdir/libmysqlservices.a

%if_with server
%files -n lib%{name}d-devel
%_libdir/lib%{name}d.so
%_libdir/libmysqld.so
%_bindir/mysql_client_test_embedded
%_bindir/mariadb-client-test-embedded
%_bindir/mysqltest_embedded
%_bindir/mariadb-test-embedded
%_man1dir/mysql_client_test_embedded.1*
%_man1dir/mariadb-client-test-embedded.1*
%_man1dir/mariadb-client-test.1*
%_man1dir/mysqltest_embedded.1*
%_man1dir/mariadb-test-embedded.1*
%_man1dir/mariadb-test.1*
%endif
%endif
%endif

%changelog
* Tue Sep 17 2024 Alexei Takaseev <taf@altlinux.org> 11.4.3-alt2
- Fix wsrep-API version (ALT #43918)

* Wed Aug 14 2024 Alexei Takaseev <taf@altlinux.org> 11.4.3-alt1
- 11.4.3
- Add conflick to rocksdb-tools

* Mon Aug 12 2024 Alexei Takaseev <taf@altlinux.org> 10.11.9-alt1
- 10.11.9
- Update disable download libfmt

* Thu May 16 2024 Alexei Takaseev <taf@altlinux.org> 10.11.8-alt1
- 10.11.8 (Fixes: CVE-2024-21096)
- Drop no needed patch 1063738-revert-c432c9ef.patch

* Sun Feb 25 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.11.7-alt2.1
- Fix build on e2k

* Thu Feb 22 2024 Alexei Takaseev <taf@altlinux.org> 10.11.7-alt2
- Fix build on armh

* Sat Feb 17 2024 Alexei Takaseev <taf@altlinux.org> 10.11.7-alt1
- 10.11.7

* Tue Nov 14 2023 Alexei Takaseev <taf@altlinux.org> 10.11.6-alt1
- 10.11.6

* Tue Oct 24 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.11.5-alt1.1
- e2k patch update

* Mon Oct 16 2023 Alexei Takaseev <taf@altlinux.org> 10.11.5-alt1
- 10.11.5 (ALT #46388)
- Add patch mariadb-10.11.5-disable-download-fmt.patch
- Drop mariadb-10.6.11-alt-upstream-gcc13.patch
- Fixes: CVE-2022-47015
- Disable LTO for fix crash compile on i586, until fix gcc-13 bug

* Fri Jul 14 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 10.6.11-alt1.qa1
- NMU: backported upstream commits to fix FTBFS with gcc13 (thx Khem Raj and
  Heiko Becker).

* Fri Dec 02 2022 Alexey Shabalin <shaba@altlinux.org> 10.6.11-alt1
- 10.6.11

* Mon Oct 31 2022 Alexey Shabalin <shaba@altlinux.org> 10.6.10-alt1
- 10.6.10

* Wed Aug 31 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.6.9-alt1.1
- e2k patch update

* Mon Aug 15 2022 Alexey Shabalin <shaba@altlinux.org> 10.6.9-alt1
- 10.6.9
- Fixes: CVE-2022-32082, CVE-2022-32089, CVE-2022-32081, CVE-2018-25032,
  CVE-2022-32091, CVE-2022-32084

* Thu Aug 11 2022 Alexey Shabalin <shaba@altlinux.org> 10.6.8-alt2
- Fix requires on perl-DBD-MariaDB for server-perl package

* Fri Aug 05 2022 Alexey Shabalin <shaba@altlinux.org> 10.6.8-alt1
- 10.6.8
- mariadb-client not requires libmariadb-devel (ALT #42774)
- Merge pam subpackage to server (ALT #41295, #35242)
- Fixes: CVE-2022-32088, CVE-2022-32087, CVE-2022-32086, CVE-2022-32085, CVE-2022-32083,
  CVE-2022-31624, CVE-2022-27458, CVE-2022-27457, CVE-2022-27456, CVE-2022-27455,
  CVE-2022-27452, CVE-2022-27451, CVE-2022-27449, CVE-2022-27448, CVE-2022-27447,
  CVE-2022-27446, CVE-2022-27445, CVE-2022-27444, CVE-2022-27387, CVE-2022-27386,
  CVE-2022-27385, CVE-2022-27384, CVE-2022-27383, CVE-2022-27382, CVE-2022-27381,
  CVE-2022-27380, CVE-2022-27379, CVE-2022-27378, CVE-2022-27377, CVE-2022-27376,
  CVE-2022-24052, CVE-2022-24051, CVE-2022-24050, CVE-2022-24048, CVE-2022-0778,
  CVE-2021-46669, CVE-2021-46668, CVE-2021-46667, CVE-2021-46665, CVE-2021-46664,
  CVE-2021-46663, CVE-2021-46662, CVE-2021-46661, CVE-2021-46659, CVE-2021-46658,
  CVE-2021-35604, CVE-2021-2389, CVE-2021-2372

* Tue Sep 14 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.5.11-alt2
- Proper patch for Elbrus
- Fixed -flto

* Mon Jul 12 2021 Alexey Shabalin <shaba@altlinux.org> 10.5.11-alt1
- 10.5.11
- Drop tokudb build support
- Add package with S3 storage engine
- Move pam plugin to separate package

* Sun Jul 11 2021 Alexey Shabalin <shaba@altlinux.org> 10.4.20-alt1
- 10.4.20 (ALT #40403)
- Fixes for the following security vulnerabilities:
  + CVE-2021-27928
  + CVE-2021-2166
  + CVE-2021-2154

* Thu May 20 2021 Slava Aseev <ptrnine@altlinux.org> 10.4.17-alt2
- fix FTBFS due to missing rpm-build-python

* Thu Nov 12 2020 Alexey Shabalin <shaba@altlinux.org> 10.4.17-alt1
- 10.4.17
- backport fix for MDEV-24096, MDEV-24121, MDEV-24134
- Fixes for the following security vulnerabilities:
  + CVE-2020-14812
  + CVE-2020-14765
  + CVE-2020-14776
  + CVE-2020-14789
  + CVE-2020-15180

* Sat Sep 12 2020 Michael Shigorin <mike@altlinux.org> 10.4.14-alt1.1
- E2K: install pkgconfig file properly (lib64)

* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 10.4.14-alt1
- 10.4.14

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 10.4.13-alt1
- 10.4.13
- Fixes for the following security vulnerabilities:
  + CVE-2020-2752
  + CVE-2020-2812
  + CVE-2020-2814
  + CVE-2020-2760
  + CVE-2020-13249

* Sun Feb 09 2020 Alexey Shabalin <shaba@altlinux.org> 10.4.12-alt1
- 10.4.12
- Fixes for the following security vulnerabilities:
  + CVE-2020-2574
  + CVE-2020-2574

* Thu Dec 19 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.11-alt1
- 10.4.11
- move client plugins to libmariadb package (ALT #37639):
  + caching_sha2_password
  + sha256_password

* Fri Dec 06 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.10-alt1
- 10.4.10

* Fri Dec 06 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.9-alt1
- 10.4.9
- Fixes for the following security vulnerabilities:
  + CVE-2019-2974
  + CVE-2019-2938

* Thu Sep 12 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.8-alt1
- 10.4.8

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.7-alt1
- 10.4.7
- Fixes for the following security vulnerabilities:
  + CVE-2019-2805
  + CVE-2019-2740
  + CVE-2019-2739
  + CVE-2019-2737
  + CVE-2019-2758

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.6-alt4
- fix execute prestart chroot build

* Tue Jul 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.4.6-alt3
- built without galera/oqgraph on armh

* Tue Jul 16 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.6-alt2
- add dir /usr/lib/mariadb/plugin/auth_pam_tool_dir to chroot

* Fri Jul 12 2019 Alexey Shabalin <shaba@altlinux.org> 10.4.6-alt1
- 10.4.6

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.15-alt1
- 10.3.15
- Fixes for the following security vulnerabilities:
  + CVE-2019-2614
  + CVE-2019-2627
  + CVE-2019-2628

* Sun Apr 07 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.14-alt1
- 10.3.14
- Fix build on e2kv4 through %%e2k macro use (mike@)
- split packages:
  + oqgraph-engine
  + connect-engine
  + rocksdb-engine
  + tokudb-engine (disabled)
  + cracklib-password-check
  + gssapi-server
  + sphinx-engine
  + cassandra-engine (disabled)

* Sat Mar 02 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.13-alt1
- 10.3.13
- Fixes for the following security vulnerabilities:
  + CVE-2019-2510
  + CVE-2019-2537

* Wed Feb 27 2019 Ivan A. Melnikov <iv@altlinux.org> 10.3.12-alt2.0.mips1
- Link with -latomic if needed.
- Build on mipsel.

* Tue Feb 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 10.3.12-alt2
- Fixed build on ppc64le architecture.

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.12-alt1
- 10.3.12

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.11-alt1
- 10.3.11
- Fixes for the following security vulnerabilities:
  + CVE-2018-3282
  + CVE-2016-9843
  + CVE-2018-3174
  + CVE-2018-3143
  + CVE-2018-3156
  + CVE-2018-3251
  + CVE-2018-3185
  + CVE-2018-3277
  + CVE-2018-3162
  + CVE-2018-3173
  + CVE-2018-3200
  + CVE-2018-3284

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.10-alt1
- 10.3.10

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.9-alt2
- rebuild with openssl-1.1

* Sun Aug 19 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.9-alt1
- 10.3.9
- Fixes for the following security vulnerabilities:
  + CVE-2018-3060
  + CVE-2018-3064
  + CVE-2018-3063
  + CVE-2018-3058
  + CVE-2018-3066
- fix path to plugin dir in chroot (ALT #35242)
- change mode of plugin dir in chroot (ALT #33259)

* Fri Jul 13 2018 Alexey Shabalin <shaba@altlinux.ru> 10.3.8-alt2
- split galera to mariadb-server-galera package

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 10.3.8-alt1
- 10.3.8

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 10.2.15-alt3
- NMU: reverted provides update.

* Wed Jun 06 2018 Alexey Shabalin <shaba@altlinux.ru> 10.2.15-alt2
- add libmysqld-devel provides (ALT #34997)

* Fri May 18 2018 Alexey Shabalin <shaba@altlinux.ru> 10.2.15-alt1
- 10.2.15
- rename libmysqlclient18 to libmariadb
- relocate plugindir to %%_libdir/%%name/plugin
- build without libwrap support
- Fixes for the following security vulnerabilities:
  + CVE-2018-2562
  + CVE-2018-2622
  + CVE-2018-2640
  + CVE-2018-2665
  + CVE-2018-2668
  + CVE-2018-2612
  + CVE-2018-2786
  + CVE-2018-2759
  + CVE-2018-2777
  + CVE-2018-2810
  + CVE-2018-2782
  + CVE-2018-2784
  + CVE-2018-2787
  + CVE-2018-2766
  + CVE-2018-2755
  + CVE-2018-2819
  + CVE-2018-2817
  + CVE-2018-2761
  + CVE-2018-2781
  + CVE-2018-2771
  + CVE-2018-2813

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 10.1.30-alt1
- 10.1.30
- Fixes for the following security vulnerabilities:
  + CVE-2017-15365

* Wed Dec 06 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.29-alt1
- 10.1.29
- Fixes for the following security vulnerabilities:
  + CVE-2017-10378
  + CVE-2017-10268
  + MDEV-13819

* Thu Nov 02 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.28-alt1
- 10.1.28

* Tue Sep 26 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.27-alt1
- 10.1.27

* Thu Sep 14 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.26-alt1
- 10.1.26
- Fixes for the following security vulnerabilities:
  + CVE-2017-3636
  + CVE-2017-3641
  + CVE-2017-3653

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 10.1.25-alt2
- BOOTSTRAP: introduced systemd, krb5, galera, cassandra, oqgraph knobs
  (on by default)
- E2K: avoid ABI check for now (fails)

* Mon Jul 17 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.25-alt1
- 10.1.25

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.23-alt1
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
- rename package libmariadbembedded -> libmysqld%%soname (ALT #29389)
- drop provides and requires lib%%name, change to libmysqlclient%%soname

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
- Add new subpackage %%name-engine-tokudb
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
