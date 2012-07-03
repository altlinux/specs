Name: MySQL
Version: 5.1.63
Release: alt1

%def_without debug
%def_disable static
%define mysql_version %version
%define mysqld_user mysql
%define _libexecdir %_sbindir
%define ROOT %_localstatedir/mysql

Summary: MySQL: A very fast and reliable SQL database engine
Summary(ru_RU.UTF-8): MySQL: Очень быстрый и надежный SQL-сервер
Group: Databases
License: GPL / LGPL
Url: http://www.mysql.com/
Packager: MySQL Development Team <mysql@packages.altlinux.org>

Source: mysql-%mysql_version.tar
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

# ALTLinux
Patch0: mysql-3.23.55-alt-configure.patch
Patch1: mysql-5.1.50-alt-chroot.patch
Patch2: mysql-5.0.20-alt-libdir.patch
Patch4: mysql-5.0.67-alt-client.patch
Patch5: mysql-5.0.89-alt-load_defaults.patch
Patch6: mysql-5.1.50-alt-fPIC-innodb.patch
Patch7: mysql-5.1.56-alt-mysql_config-libs.patch
Patch8: mysql-5.1.56-alt-libmysql-cxa.patch
Patch9: mysql-5.1.56-alt-plugins-link.patch

# Automatically added by buildreq on Wed Mar 16 2011 (-bi)
BuildRequires: chrooted gcc-c++ libncursesw-devel libreadline-devel libssl-devel perl-DBI zlib-devel

%define soversion 16
%package -n libmysqlclient%soversion
Summary: MySQL: Shared libraries
Summary(ru_RU.UTF-8): MySQL: Динамические библиотеки
License: LGPL
Group: System/Libraries
Provides: libMySQL = %version libMySQL5.1 = %version
Obsoletes: libMySQL < %version libMySQL5.1 < %version

%package -n libmysqlclient-devel
Summary: MySQL: Development header files and libraries
Summary(ru_RU.UTF-8): MySQL: Интерфейс прикладного уровня для разработки программ
License: LGPL
Group: Development/C
Requires: libmysqlclient%soversion = %version-%release
Provides: MySQL-devel = %version mysql-devel = %version
Obsoletes: MySQL-devel < %version mysql-devel < %version
Provides: libMySQL-devel = %version libMySQL5.1-devel = %version
Obsoletes: libMySQL-devel < %version libMySQL5.1-devel < %version

%package -n libmysqlclient-devel-static
Summary: MySQL: Development static libraries
Summary(ru_RU.UTF-8): MySQL: Интерфейс прикладного уровня для разработки программ
License: LGPL
Group: Development/C
Requires: libmysqlclient-devel = %version-%release
Provides: libMySQL-devel-static = %version libMySQL5.1-devel-static = %version
Obsoletes: libMySQL-devel-static < %version libMySQL5.1-devel-static < %version

%package client
Summary: MySQL: Client
Summary(ru_RU.UTF-8): MySQL: Клиент
License: GPL
Group: Databases
Requires: libmysqlclient%soversion = %version-%release
Provides: mysql-client = %version
Obsoletes: mysql-client < %version

%package server
Summary: MySQL: A very fast and reliable SQL database engine
Summary(ru_RU.UTF-8): MySQL: Очень быстрый и надежный SQL-сервер
License: GPL
Group: Databases
PreReq: libmysqlclient%soversion = %version-%release, MySQL-client = %version-%release
PreReq: shadow-utils, coreutils, glibc-locales
Requires(post,preun): chkconfig, chrooted, coreutils, findutils, grep, sed, %__subst
Provides: mysql-server = %version MySQL = %version mysql = %version
Obsoletes: mysql-server < %version MySQL < %version mysql < %version

%package server-perl
Summary: MySQL: Perl utils for MySQL-server
License: GPL
Group: Databases
Requires: MySQL-server = %version-%release, perl-DBD-mysql
BuildArch: noarch

%package bench
Summary: MySQL: Benchmarks
Summary(ru_RU.UTF-8): MySQL: Тесты производительности
License: GPL
Group: Databases
Requires: MySQL-client = %version-%release, perl-DBD-mysql
Provides: mysql-bench = %version
Obsoletes: mysql-bench < %version
BuildArch: noarch

%define see_base For a description of MySQL see the base MySQL RPM or %url
%define see_base_ru Подробное описание смотрите в пакете MySQL или на %url

%description
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.

The main goals of MySQL are speed, robustness and ease of use.  MySQL
was originally developed because we needed a SQL server that could
handle very big databases with magnitude higher speed than what any
database vendor could offer to us. And since we did not need all the
features that made their server slow we made our own. We have now been
using MySQL since 1996 in a environment with more than 40 databases,
10,000 tables, of which more than 500 have more than 7 million
rows. This is about 200G of data.

The base upon which MySQL is built is a set of routines that have been
used in a highly demanding production environment for many
years. While MySQL is still in development, it already offers a rich
and highly useful function set.

This version allows to use transactions with BDB tables and extended
character set support. See the documentation for more information

%description -l ru_RU.UTF-8
MySQL - это многопользовательский, многопоточный SQL-сервер (SQL -
структурированный язык запросов) баз данных. MySQL построен по технологии
клиент/сервер и включает в себя сервер mysqld и набор различных клиентских
программ и библиотек разработчиков.

Козыри MySQL - скорость, надежность и простота использования. Разработка
MySQL ведется на основе программного кода, который используется в
критических промышленных приложениях уже в течение многих лет. Несмотря на
то, что MySQL только разрабатывается, он уже предоставляет богатый и очень
полезный набор функций.

Данная версия MySQL собрана с поддержкой транзакций и расширенной поддержкой
различных текстовых кодировок. См. документацию для более подробной информации.

%description server
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.

The main goals of MySQL are speed, robustness and ease of use.  MySQL
was originally developed because we needed a SQL server that could
handle very big databases with magnitude higher speed than what any
database vendor could offer to us. And since we did not need all the
features that made their server slow we made our own. We have now been
using MySQL since 1996 in a environment with more than 40 databases,
10,000 tables, of which more than 500 have more than 7 million
rows. This is about 200G of data.

The base upon which MySQL is built is a set of routines that have been
used in a highly demanding production environment for many
years. While MySQL is still in development, it already offers a rich
and highly useful function set.

This version allows to use transactions with BDB tables and extended
character set support. See the documentation for more information.

By default, MySQL server runs in safe chrooted environment with own uid and gid.

%description server-perl
MySQL is a true multi-user, multi-threaded SQL (Structured Query
Language) database server. MySQL is a client/server implementation
that consists of a server daemon (mysqld) and many different client
programs/libraries.
This package contents perl utils for MySQL-server.

%description server -l ru_RU.UTF-8
MySQL - это многопользовательский, многопоточный SQL-сервер (SQL -
структурированный язык запросов) баз данных. MySQL построен по технологии
клиент/сервер и включает в себя сервер mysqld и набор различных клиентских
программ и библиотек разработчиков.

Козыри MySQL - скорость, надежность и простота использования. Разработка
MySQL ведется на основе программного кода, который используется в
критических промышленных приложениях уже в течение многих лет. Несмотря на
то, что MySQL только разрабатывается, он уже предоставляет богатый и очень
полезный набор функций.

Данная версия MySQL собрана с поддержкой транзакций и расширенной поддержкой
различных текстовых кодировок. См. документацию для более подробной информации.

%description -n libmysqlclient16
This package contains the shared libraries (*.so*) which certain
languages and applications need to dynamically load and use MySQL.

%description -n libmysqlclient16 -l ru_RU.UTF-8
Этот пакет содержит динамически загружаемые библиотеки (файлы *.so*),
требуемые для работы большинства клиентских приложений, взаимодействующих
с SQL-сервером MySQL.

%description -n libmysqlclient-devel
This package contains the development header files and libraries
necessary to develop MySQL client applications.

%see_base

%description -n libmysqlclient-devel -l ru_RU.UTF-8
Этот пакет содержит файлы заголовков и библиотеки интерфейса
прикладного уровня, необходимые для разработки клиентских
приложений, взаимодействующих с SQL-сервером MySQL.

%see_base_ru

%description -n libmysqlclient-devel-static
This package contains the development libraries for static linking
necessary to develop MySQL client applications.

%see_base

%description -n libmysqlclient-devel-static -l ru_RU.UTF-8
Этот пакет содержит статические библиотеки интерфейса прикладного уровня,
необходимые для разработки клиентских приложений,
взаимодействующих с SQL-сервером MySQL.

%see_base_ru

%description client
This package contains the standard MySQL clients.

%see_base

%description client -l ru_RU.UTF-8
Этот пакет содержит стандартные клиентские программы для SQL-сервера MySQL

%see_base_ru

%description bench
This package contains MySQL benchmark scripts and data.

%see_base

%description bench -l ru_RU.UTF-8
Этот пакет содержит данные и утилиты для тестирования
производительности SQL-сервера MySQL.

%see_base_ru

%prep
%setup -n mysql-%mysql_version
# ALTLinux
%patch0 -p1
%patch1 -p1
%patch2 -p1

%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2

# BK patches

cp -af %SOURCE15 scripts/mysql_install_db.sh

# Use local regex.h header.
find -type f -print0 |
	xargs -r0 grep -FZl '<regex.h>' -- |
	xargs -r0 sed -i 's,<regex\.h>,"../regex/regex.h",g' --

# Prepare commands list for completion in mysql client.
sed -ne 's/^\(  { "[A-Z][^"]*"\).*/\1, 0, 0, 0, "" },/pg' <sql/lex.h >client/mysql_symbols.inc

find -type d -name CVS -print0 |
	xargs -r0 rm -rf --
find -type f -name .cvsignore -print0 |
	xargs -r0 rm -f --

chmod -R a-s,go-w sql-bench

%build

# Force HAVE_ERRNO_AS_DEFINE defined to wrong expansion
# of bits/errno.h's definition of errno in my_sys.h
%{!?_with_debug:%add_optflags %optflags_notraceback}
%add_optflags -D_FILE_OFFSET_BITS=64 -DHAVE_ERRNO_AS_DEFINE -DONE_THREAD
export CXXFLAGS="%optflags -felide-constructors -fno-exceptions -fno-rtti"

%autoreconf

# Precache these values to enable /proc-less build.
export \
	FIND_PROC='/bin/ps p $$PID | grep mysqld >/dev/null' \
	CHECK_PID='/bin/kill -0 $$PID >/dev/null 2>/dev/null' \
	#

%configure \
	--localstatedir=%ROOT \
	--enable-assembler \
	--enable-shared \
	--enable-thread-safe-client \
	--without-readline \
	--without-mysqlfs \
	--enable-largefile=yes \
	--enable-large-files=yes \
	--with-archive-storage-engine \
	--with-blackhole-storage-engine \
	--without-example-storage-engine \
	%{subst_with debug} \
	%{subst_enable static} \
	--with-raid \
	--with-berkeley-db \
	--with-big-tables \
	--with-isam \
	--with-extra-charsets=all \
	--with-mysqld-user=%mysqld_user \
	--with-unix-socket-path=%ROOT/mysql.sock \
	--with-comment="%distribution MySQL RPM" \
	--with-plugin-innobase \
	--with-plugin-innodb_plugin \
	--with-plugin-partition \
	--with-ssl=%_prefix

# Benchdir does not fit in above model. Maybe a separate bench distribution
%make_build benchdir=%buildroot%_datadir/sql-bench

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_includedir,%_mandir,%_infodir,%_datadir/sql-bench,/var/log/mysql}
mkdir -p %buildroot%ROOT/{etc,/%_lib,%_libdir,%_libdir/mysql/plugin/,dev,log,tmp,/var/{nis,yp/binding},db/mysql,usr/share/mysql/charsets}
touch %buildroot%ROOT{%_sysconfdir/{hosts,services,{host,nsswitch,resolv}.conf},/dev/urandom,/var/nis/NIS_COLD_START}

%makeinstall_std DESTDIR=%buildroot \
	localstatedir=%buildroot%ROOT/db \
	benchdir=%_datadir/sql-bench

# Relocate mysql_install_db
mv %buildroot%_bindir/mysql_install_db %buildroot%_sbindir/

# Relocate libmysqlclient* libraries.
mv %buildroot%_libdir/mysql/libmysqlclient* %buildroot%_libdir/

# Install various helper scripts.
install -pD -m755 %SOURCE1 %buildroot%_initdir/mysqld
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/mysql
install -pD -m755 %SOURCE3 %buildroot%_sbindir/safe_mysqld
install -pD -m755 %SOURCE4 %buildroot%_sbindir/mysqld_wrapper
install -pD -m750 %SOURCE6 %buildroot%_sysconfdir/chroot.d/mysql.lib
%ifarch x86_64
sed -i s,usr/lib,usr/lib64,g %buildroot%_sysconfdir/chroot.d/mysql.lib
%endif
install -pD -m750 %SOURCE7 %buildroot%_sysconfdir/chroot.d/mysql.conf
install -pD -m750 %SOURCE8 %buildroot%_sysconfdir/chroot.d/mysql.all
install -pD -m750 %SOURCE9 %buildroot%_sbindir/mysql_migrate
install -pD -m644 %SOURCE10 %buildroot%_sysconfdir/sysconfig/mysqld

# Make backwards compatibility links (ALT #14863)
mkdir -p %buildroot%_bindir
ln -snf ../sbin/safe_mysqld %buildroot%_bindir/mysqld_safe

# Install configuration files.
install -pD -m644 /dev/null %buildroot%_sysconfdir/my.cnf
install -pD -m600 %SOURCE5 %buildroot%ROOT/my.cnf

# FIXME! bdb maybe work on x86/Linux and amd64/Linux
%ifarch %ix86
sed -i 's,^skip\-bdb,#skip-bdb,' %buildroot%ROOT/my.cnf
%endif

install -pD -m644 %buildroot%_datadir/mysql/charsets/* \
		     %buildroot%ROOT%_datadir/mysql/charsets

# Fix \r.
r="$(echo -ne \\r)"
grep -lZ "$r\$" %buildroot%_datadir/sql-bench/innotest* |
	xargs -r0 sed -i "s/$r//g" --

# Fixed perl autodetection.
grep -EZl '^[[:space:]]*use the ' %buildroot%_bindir/* |
	xargs -r0 subst -p 's/\([[:space:]]*\)\(use the \)/\1then \2/g'
	
# Install texinfo documentation.
install -m644 Docs/*.info* %buildroot%_infodir/

subst -p 's/\(BUGmysql="\)\([^"]*\)"/\1\2,mysql@packages.altlinux.org"/g' %buildroot%_bindir/mysqlbug

mkdir -p %buildroot%_docdir/MySQL-%version
install -p -m644 README %SOURCE14 support-files/*.cnf %buildroot%_docdir/MySQL-%version

rm -f %buildroot%_bindir/safe_mysqld
rm -f %buildroot%_datadir/mysql/mysql{-*.spec,-log-rotate,.server}

install -p -m644 ChangeLog %buildroot%_docdir/MySQL-%version/
bzip2 -f9 %buildroot%_docdir/MySQL-%version/ChangeLog

touch %buildroot%ROOT/log/queries
touch %buildroot/var/log/mysql/info

rm -rf %buildroot/usr/mysql-test
rm -f %buildroot/%_libdir/mysql/plugin/*.la

%define get_datadir \
DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\\(.*\\)/\\1/pg' |tail -1` \
[ -n "$DATADIR" ] || { echo "Failed to read configuration"; exit 1; }

%pre server
/usr/sbin/groupadd -r -f %mysqld_user
/usr/sbin/useradd -r -g %mysqld_user -d %ROOT -s /dev/null -c "MySQL server" -n %mysqld_user >/dev/null 2>&1 ||:

if [ ! -e %ROOT/my.cnf -a -f /etc/my.cnf -a ! -L /etc/my.cnf -a ! -e /etc/my.cnf.rename ]; then
	mv -v /etc/my.cnf /etc/my.cnf.rename &&
	chown 0:0 /etc/my.cnf.rename &&
	chmod 600 /etc/my.cnf.rename ||
	{ echo "Error moving my.cnf" >&2; exit 1; }
fi

%post server
if [ -f /etc/my.cnf.rename -a ! -L /etc/my.cnf.rename -a ! -e /etc/my.cnf ]; then
	mv -fv %ROOT/my.cnf %ROOT/my.cnf.rpmnew &&
	mv -v /etc/my.cnf.rename %ROOT/my.cnf &&
	chown 0:0 %ROOT/my.cnf &&
	chmod 600 %ROOT/my.cnf ||
	{ echo "Error moving my.cnf" >&2; mv -v /etc/my.cnf.rename /etc/my.cnf; }
fi

if grep "^[[:space:]]*skip-bdb[[:space:]]*$" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*skip-bdb[[:space:]]*$/#skip-bdb/" /var/lib/mysql/my.cnf;
fi

if grep "^[[:space:]]*bdb-logdir=" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*bdb-logdir=/#bdb-logdir=/" /var/lib/mysql/my.cnf;
fi


if grep "^[[:space:]]*skip-locking[[:space:]]*$" /var/lib/mysql/my.cnf > /dev/null 2>&1; then
	sed -i "s/^[[:space:]]*skip-locking[[:space:]]*$/skip-external-locking/" /var/lib/mysql/my.cnf;
fi

rm -rf %ROOT/dev
%_sysconfdir/chroot.d/mysql.all force

%post_service mysqld

%get_datadir
if [ "$DATADIR" = / ]; then
	# Have to update configuration manually.
	sed -i 's,^datadir=/$,datadir=/db,g' /etc/my.cnf &&
		DATADIR=`/usr/bin/my_print_defaults mysqld |sed -ne 's/^--datadir=\(.*\)/\1/pg' |tail -1` ||
		{ echo "Failed to update configuration"; exit 1; }
fi

NEED_RESTART=
if [ -f "%ROOT/mysql/db.frm" -a ! -f "%ROOT$DATADIR/mysql/db.frm" ]; then
	%_initdir/mysqld status &>/dev/null && %_initdir/mysqld stop && NEED_RESTART=1 ||:
	(cd %ROOT
	install -d -m750 -o %mysqld_user -g adm ".$DATADIR"
	for d in `find -mindepth 1 -maxdepth 1 -type d |grep -Ev '\./(dev|etc|lib|log|tmp|db)$'`; do
		mv -i "$d" ".$DATADIR/$d"
	done)
	echo "Database root have been moved to $DATADIR"
fi

if [ -n "$NEED_RESTART" ]; then
	%_initdir/mysqld start ||:
else
	%_initdir/mysqld condrestart ||:
fi

%triggerpostun server -- MySQL-server <= 5.1.60-alt1
%get_datadir
if [ -f /var/lib/mysql/my.cnf -a -f "%ROOT$DATADIR/ibdata1" ]; then
	if ! grep "^plugin-load=innodb=ha_innodb_plugin\.so" /var/lib/mysql/my.cnf; then
		echo "  WARNING: if InnoDB is used, please examine /var/lib/mysql/my.cnf*"
		echo "  and ensure that the innodb plugin is loaded"
	fi
fi

%triggerpostun server -- MySQL-server < 5.0
%get_datadir
[ -x /usr/bin/mysql_upgrade ] || exit 0
if [ -f "%ROOT/mysql/db.frm" -a ! -f "%ROOT$DATADIR/mysql/db.frm" ]; then
	%_initdir/mysqld status >/dev/null 2>&1 && NEED_RESTART=1 || NEED_RESTART=
	/usr/bin/mysql_upgrade --datadir=%ROOT$DATADIR >/dev/null 2>&1
fi

if [ -n "$NEED_RESTART" ]; then 
	%_initdir/mysqld condrestart ||:
else
	echo "mysqld service is not running so you should run " 
	echo "/usr/bin/mysql_upgrade --datadir=%ROOT$DATADIR manually "
	echo "after service mysql start!"
	%_initdir/mysqld condrestart ||:
fi

%preun server
%preun_service mysqld

%postun server
if [ $1 = 0 ]; then
	rm -f %ROOT/lib/* %ROOT/var/yp/binding/*
fi

%files -n libmysqlclient16
%_libdir/*.so.*

%files -n libmysqlclient-devel
%_bindir/mysql_config
%_libdir/*.so
%_includedir/*
%_aclocaldir/mysql.m4

%if_enabled static
%files -n libmysqlclient-devel-static
%_libdir/*.a
%_libdir/mysql
%endif #static 

%files client
%_bindir/innochecksum
%_bindir/msql2mysql
%_bindir/my_print_defaults
%_bindir/mysql
%_bindir/mysql_client_test
%_bindir/mysqladmin
%_bindir/mysqlbinlog
%_bindir/mysqlbug
%_bindir/mysqlcheck
%_bindir/mysqldump
%_bindir/mysqlimport
%_bindir/mysqlshow
%_bindir/mysqltest
%_bindir/mysqlslap
%_bindir/mysql_waitpid
%_bindir/perror
%_bindir/replace
%_bindir/resolve*
%_mandir/man?/*
%_infodir/*.info*

%files server-perl
%_bindir/mysql_convert_table_format
%_bindir/mysql_find_rows
%_bindir/mysql_setpermission
%_bindir/mysql_zap
%_bindir/mysqlhotcopy
%_bindir/mysqlaccess
%_bindir/mysqldumpslow

%files server
%_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/logrotate.d/*
%config %_sysconfdir/chroot.d/*
%ghost %config(noreplace,missingok) %_sysconfdir/my.cnf
%_bindir/*isam*
%_bindir/mysql_fix_extensions
%_bindir/mysql_fix_privilege_tables
%_bindir/mysql_secure_installation
%_bindir/mysql_tzinfo_to_sql
%_bindir/mysql_upgrade
%_bindir/mysqld_multi
%_bindir/mysqld_safe
%_sbindir/*
%_libdir/mysql/plugin
%_datadir/mysql
%attr(750,root,adm) %dir /var/log/mysql
%ghost %verify(not md5 mtime size) /var/log/mysql/*
%dir %_docdir/MySQL-%version
%_docdir/MySQL-%version/ChangeLog*
%_docdir/MySQL-%version/README
%_docdir/MySQL-%version/README.*
%_docdir/MySQL-%version/*.cnf
%attr(600,root,root) %config(noreplace,missingok) %ROOT/my.cnf
%attr(3771,root,mysql) %dir %ROOT
%attr(710,root,mysql) %dir %ROOT/%_lib
%attr(710,root,mysql) %dir %ROOT/%_libdir
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql
%attr(710,root,mysql) %dir %ROOT/%_libdir/mysql/plugin
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
%attr(660,mysql,mysql) %ghost %verify(not md5 mtime size) %ROOT/log/*
%attr(3770,root,mysql) %dir %ROOT/tmp

%files bench
%_datadir/sql-bench

%changelog
* Mon May 07 2012 Michael Shigorin <mike@altlinux.org> 5.1.63-alt1
- 5.1.63

* Fri Mar 23 2012 Michael Shigorin <mike@altlinux.org> 5.1.62-alt1
- 5.1.62
- /dev/urandom tweaks
- spec cleanup

* Wed Mar 21 2012 Michael Shigorin <mike@altlinux.org> 5.1.61-alt2
- create /dev/urandom in chroot so SSL support actually works;
  thanks naf@ (closes: #27100)

* Thu Jan 12 2012 Michael Shigorin <mike@altlinux.org> 5.1.61-alt1
- 5.1.61

* Fri Dec 30 2011 Michael Shigorin <mike@altlinux.org> 5.1.60-alt2
- please note that 5.1.50-alt1 introduced modular InnoDB support
  thus the plugin must be loaded if it's supposed to be used

* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.60-alt1
- 5.1.60

* Tue Sep 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.59-alt1
- 5.1.59

* Wed Jul 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.58-alt1
- 5.1.58

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.57-alt1
- 5.1.57

* Fri Mar 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.56-alt4
- make mysqld plugins usable (ALT #25248)

* Thu Mar 17 2011 Alexey Tourbin <at@altlinux.ru> 5.1.56-alt3
- hack around __cxa_pure_virtual issue

* Thu Mar 17 2011 Alexey Tourbin <at@altlinux.ru> 5.1.56-alt2
- built with OpenSSL instead of bunled yaSSL
- mysql_config: disabled dependency on libssl-devel

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.56-alt1
- 5.1.56

* Wed Feb 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.55-alt1
- 5.1.55

* Tue Nov 02 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.52-alt1
- 5.1.52

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.51-alt1
- 5.1.51

* Mon Sep 27 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt6
- upgrade old my.cnf more gracefully (closes #24165)

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.1.50-alt5
- added my_compiler.h for build with my_global.h

* Thu Sep 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt4
- remove unsupported --skip-bdb from /usr/sbin/mysql_migrate

* Wed Sep 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt3
- remove unsupported options from /usr/sbin/mysql_install_db

* Wed Sep 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt2
- Provide/Oblosete libMySQL5.1{-devel,-devel-static} (closes #24134)

* Fri Sep 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.50-alt1
- 5.1.50

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 5.0.89-alt1
- new version (closes #18943)
- fixed CVE-2009-2446 from upstream (closes #20724)
- setup utf8 encoding instead of latin1 by default (closes #12390)
- include C99 aliasing violation patch from mythtv (closes #22452)
- removed username-length patch
- wait for mysqld shutdown (closes #22234)
- don't run initial setup mysql database if mysql.user table already exists

* Mon Jun 29 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.83-alt2
- Security fixes:
  + CVE-2008-4456: potential XSS in HTML output (closes #19843).
- Remove obsoleted macros.

* Thu Jun 25 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.83-alt1
- 5.0.83.
- Remove obsoleted macros.
- Disabled patch20,patch22, updated htmlhelp to revision 15415.

* Wed May 13 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.81-alt1
- 5.0.81.
- Update htmlhelp to revision 14892.

* Sun May 03 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.77-alt1
- 5.0.77.
- Update htmlhelp to revision 14789.
- Remove obsoleted patches.

* Sun Jan 18 2009 L.A. Kostis <lakostis@altlinux.ru> 5.0.75-alt1
- 5.0.75.
- Package some packages as noarch.
- Change htmlhelp package group to Documentation.
- Update htmlhelp to revision 13252.

* Fri Nov 21 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.67-alt2
- Bugfix build.
- Remove deprecated %%post_ldconfig/%%postun_ldconfig.
- Added patches:
  + mysql-5.0.68-BUG#37027: expire_logs_days and missing 
    binlogs cause a crash !

* Tue Nov 11 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.67-alt1
- 5.0.67.
- rediffed patches.
- Applied patches from Debian unstable/Ubuntu intrepid:
  + mysqlhotcopy-invalid-dbtable.patch: fix broken security fix.
  + upstream_bug_23921: Fixes random build failures.
  + scripts__mysql_config__libs: Removes unnecessary library dependencies. 
- Applied patch from Gentoo:
  + ltmain.patch: fix build with recent automake.

* Sun Sep 14 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt3.a
- Build for Sisyphus.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt2.a.M40.2
- mysql_install_db: Fixed typo (closes: #15924).
- Reduced rpm macros abuse in specfile.
- Updated reference manual.

* Sat May 31 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0.51-alt2.a.M40.1
- Fixed build for 4.0 branch.

* Sun Mar 16 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.51-alt2.a
- 5.0.51a.
- Security fixes:
  + CVE-2008-0226, CVE-2008-0227 (Three vulnerabilities in yaSSL versions 1.7.5
    that could lead to a server crash or execution of unauthorized code.)
  + ALTER VIEW retained the original DEFINER value, even when altered by
    another user, which could allow that user to gain the access rights of the
    view (MySQL #29908).
- Add glibc-locales to -server deps (ALT #13909 #14731).
- Make links to mysqld_safe for backwards compatibility (ALT #14863).
- Update html documentation to 10265 revsion.

* Tue Jan 01 2008 L.A. Kostis <lakostis@altlinux.ru> 5.0.51-alt1
- 5.0.51.
- Security fixes:
  + CVE-2007-5969 (RENAME TABLE System Table Overwrite Vulnerability)
  + CVE-2007-6303 CVE-2007-6304 
    (Server Privilege Escalation And Denial Of Service Vulnerabilities) 
- Update html documentation to 9232 revision.

* Thu Aug 09 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.46-alt2
- fix a typo in alt-mysql_install_db.patch.

* Mon Aug 06 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.46-alt1
- 5.0.46.
- Update -alt-install-db.patch.
- Update -alt-username-length patch.
- Update documentation to 7319 revision.

* Wed Jun 20 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.42-alt1
- 5.0.42.

* Mon May 28 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.41-alt1
- 5.0.41 release.
- Fix CVE-2007-2583 DoS (Failure to Handle Exceptional Conditions).
- Added patches from BK:
  + BUG#28337 (NOT EXISTS with GROUP BY behaves different in 5.0.40).
- Update ALTLinux patches:
  + install-db patch.
  + username-length patch.
- Updated html help (to 6552 revision).
- Allow custom nice setting for mysqld (fix ALT #10941).
- Added mysqld-multi (fix ALT #5715).
- Added several files for -server and client.

* Sun Feb 11 2007 L.A. Kostis <lakostis@altlinux.ru> 5.0.34-alt1
- 5.0.34 release.
- update html help (to 4891 revision).
- Fix db_install in hasher (closes #10788).
- Fix charset detection routes in init.d script.
- Update install-db patch.
- Remove obsoleted patches.

* Sat Dec 30 2006 L.A. Kostis <lakostis@altlinux.ru> 5.0.30-alt0.1
- Unofficial 5.0.30 release (use Debian sources).
- Use Docs from previous 5.0.27-GA release.
- Fix SSL docs install.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.27-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Nov 02 2006 L.A. Kostis <lakostis@altlinux.ru> 5.0.27-alt1
- 5.0.27 release;
- Added patches:
  + db-4.1.24-disable-pthreadsmutexes.patch: fix NPTL issues 
    (found in Mandriva package); 
  + mysql-5.0.15-disable-pthreadsmutexes.patch: fix NPTL issues 
    (found in Mandriva package);
  + mysql-5.0.27-alt-username-length.patch: add custom username-length 
    (5.0 backport of BUG#16553) and README.ALT-ru_RU.UTF-8 about incompatible
    changes introduced by this patch;
- Add html documentation from http://dev.mysql.com/docs.

* Sat Aug 26 2006 LAKostis <lakostis at altlinux.org> 5.0.24-alt2
- fix libmysqlclient ABI breakage introduced in 5.0.24 (see
  http://bugs.mysql.com/bug.php?id=21543 for details).

* Wed Aug 09 2006 LAKostis <lakostis at altlinux.org> 5.0.24-alt1
- 5.0.24 release. 

* Thu Jun 01 2006 LAKostis <lakostis at altlinux.ru> 5.0.22-alt1
- 5.0.22.
- Security fix of SQL-injection multibyte encoding processing.

* Wed May 10 2006 LAKostis <lakostis at altlinux.ru> 5.0.21-alt1
- 5.0.21.
- Remove bk patches (merged to upstream).
- Update install_db patch.
- Update -no-atomic patch.
- Remove tinfo patch (http://bugs.mysql.com/bug.php?id=18912).
- Security fixes:
  + CVE-2006-1516;
  + CVE-2006-1517;
  + CVE-2006-1518.

* Fri Apr 14 2006 LAKostis <lakostis at altlinux.ru> 5.0.20-alt1
- 5.0.20.
- Add mysql_upgrade trigger/script for proper 4.x -> 5.0 upgrade.
- Added some fixing patches from upcoming 5.0.21:
  + BUG#16281 (Multi-table update failing to change matched rows).
  + BUG#18830 (incompatibility new libraries with old server).
- Removed obsoleted patches.

* Sun Apr 09 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt2
- Added patches:
  + BUG#15719 fix (see #9348 for details);
  + BUG#17667 (aka CVE-2006-0903) fix;
  
* Thu Feb 23 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.4
- fix #9135;
- fix debug switch.
- fix non-static build switch.

* Sun Feb 12 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.3
- fix bogus vars in init.d script.
- add skip-bdb only for x86_64.

* Tue Feb 07 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.2
- fix alt-chroot patch.
- fix init.d script and add /etc/sysconfig/mysqld entry.

* Sun Feb 05 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1.1
- remove chroot patch. Need to rework!
- disable ssl support.
- fix ssl switch.

* Wed Feb 01 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt1
- release for Sisyphus;
- cleanup patches.

* Thu Jan 26 2006 LAKostis <lakostis at altlinux.ru> 5.0.18-alt0.1
- jump to 5.0.18.
- update patches from Fedora.
- update create_db patch.
- update defaults patch, add DATADIR to config_search path.
- add old_passwords=1 for compatibility with old clients.
- disable log queries by default.
- disable bdb support (for AMD64/x86 see comment in my.cnf).
- disable -static builds by default.

* Tue Jan 17 2006 LAKostis <lakostis at altlinux.ru> 4.1.16-alt0.1
- 4.1.16.

* Sun Dec 25 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.5
- remove chroot build switch.

* Sun Nov 20 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.4
- fix chroot config handling.

* Sat Sep 17 2005 LAKostis <lakostis at altlinux.ru> 4.1.14-alt0.3
- 4.1.14;
- FIXME - need rework chroot patch for proper charset handling; 
- add isam support for old db installs.
- add x86_64 patches from RH and Annvix;
- add non-chroot build switch;
- remove doc package.

* Thu Mar 24 2005 Kachalov Anton <mouse@altlinux.ru> 4.0.24-alt1
- 4.0.24

* Wed Oct 20 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.21-alt1
- 4.0.21
- don't kill other mysqld processes on service stop (#5371)

* Mon Jun 07 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.20-alt1
- new version 4.0.20
- Added script mysqlhotcopy (#3365)
- Merge -utils package with -server-perl
- fixed mysqld.init script (3rd time :)

* Wed Apr 28 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt4
- Move mysqlaccess and mysqldumpslow scripts to new MySQL-utils package (#3964)

* Wed Mar 17 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt3
- Added requires for MySQL-client for perl-CGI (#2359)

* Fri Feb 27 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt2
- MySQL server crashes while running on systems with LDAP (#3729)

* Wed Feb 18 2004 Kachalov Anton <mouse@altlinux.ru> 4.0.18-alt1
- new version 4.0.18
- fixed mysqld.init script (Dmitry Vukolov <dav@altlinux.org>)

* Thu Dec 18 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.17-alt1
- new version 4.0.17

* Fri Nov 28 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.16-alt2
- fixed setting of default charset
- removed depreciated buildreqs

* Tue Nov 25 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.16-alt1
- new version 4.0.16
- fixed Requires(post,preun) (#3155)
- Do not package .la files.

* Tue Sep 30 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.15-alt2
- added mysql_migrate script for migration from 3.x to 4.0 version of MySQL
- mysql_install_db script fix (based on old ldv's script)

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.15-alt1
- new version 4.0.15
- enabled charset conversion for more charsets

* Thu Jul 10 2003 Kachalov Anton <mouse@altlinux.ru> 4.0.13-alt1
- new version 4.0.13

* Fri Mar 21 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt3
- Fixed my.cnf migration support.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt2
- Fixed build in environment without /proc.
- Fixed build without libncurses-devel.
- Updated buildrequires.
- server: handle default my.cnf migration.

* Tue Mar 18 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.56-alt1
- Updated to 3.23.56, redone few patches.

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt3
- load_defaults: do not process untrusted files if executed by root.

* Mon Mar 10 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt2
- Packaged %ROOT/my.cnf, owned by root and available to root only,
  to avoid mysql->root possible privilege escalation described by
  Gufino in his Bugtraq posting:
  http://www.securityfocus.com/archive/1/314391
- Changed /etc/my.cnf permissions from 0600 to 0644.
  Check your /etc/my.cnf file and move all sensitive data out there.
- Updated comment in logrotate script, thanks to discussion in
  Sisyphus mailing list:
  http://www.altlinux.ru/pipermail/sisyphus/2003-February/039434.html

* Tue Jan 28 2003 Dmitry V. Levin <ldv@altlinux.org> 3.23.55-alt1
- Updated to 3.23.55.
- Applied docs build fixes from Lenz Grimmer.

* Fri Dec 13 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.54-alt2
- mysqlbug: fixed contact email address.

* Thu Dec 12 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.54-alt1
- Updated to 3.23.54.
- Updated chroot patch to new version.
- Added reservedwords.texi (lost in new version).
- Updated interpackage dependencies.
- Adjusted perl dependencies.

* Tue Dec 03 2002 Stanislav Ievlev <inger@altlinux.ru> 3.23.53-alt2
- added server-perl subpackage, to reduce deps on perl of server

* Tue Oct 15 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.53-alt1
- 3.23.53
- Better debugging support.

* Mon Sep 16 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.52-alt1
- 3.23.52
- Ensure tzset(3) is called before chroot(2).
- Removed %_sysconfdir/localtime from %ROOT chroot.
- Use subst instead of perl for text substitution.
- Linked with readline-4.3.
- Built with gcc-3.2.

* Wed Jul 03 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.51-alt2
- Patched to link with libtinfo.

* Fri Jun 14 2002 Dmitry V. Levin <ldv@altlinux.org> 3.23.51-alt1
- 3.23.51
- Fixed typo in safe_mysqld.
- Removed aggressive optimization.

* Sat Apr 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.50-alt1
- 3.23.50

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt5
- Fixed recent fix.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt4
- Updated chroot (fixed permissions, added NIS/NIS+ support).

* Mon Apr 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt3
- Added my_dir.h to libMySQL-devel (#0000701).

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt2
- Added %ROOT/dev removal from existing configurations.
- Dropped mysql.chroot.log script (unneeded anymore).

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.49-alt1
- 3.23.49.
- Removed /dev from %ROOT.
- Fixed server %%post/%%preun scripts (#0000324).

* Fri Jan 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.23.47-alt1
- 3.23.47.

* Thu Dec 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.46-alt2
- Made gif2png conversion configurable.
- Automatically regenerated buildrequires.

* Mon Dec 03 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.46-alt1
- 3.23.46

* Mon Nov 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.45-alt1
- 3.23.45
- Fixed relocation of libmysqlclient* libraries (#0000145).
- Split html documentation (#0000179).
- Added png pictures to html documentation subpackage.

* Sun Nov 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.23.44-alt1
- 3.23.44

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.43-alt1
- 3.23.43
- Patched scripts in MySQL-bench to make them functional (mdk).

* Fri Sep 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.42-alt1
- 3.23.42
- Updated interpackage dependencies.
- Built with internal db-3.2.9a.

* Fri Apr 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl8mdk
- Fixed mysqld_wrapper to handle server shutdown correctly.
- Relocated mysql_install_db from %_bindir to %_sbindir/
- Updated mysql_install_db to work with chrooted environments.

* Thu Apr 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl7mdk
- Fixed (finally?) server %%postin script to handle recent database move.

* Wed Apr 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl6mdk
- Fixed (again) server %%postin script to handle recent database move.
- Updated PreReqs for server subpackage.

* Tue Apr 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.23.33-ipl5mdk
- Updated %%postin script to handle recent database move.

* Sat Apr 21 2001 Alexander Bokovoy <ab@avilink.net> 3.23.33-ipl4mdk
- Fixed bug in datadir handling for chrooted environments.
- MySQL databases moved to $chrootdir/db/
- libMySQL-devel has been transformed to libMySQL-devel and libMySQL-devel-static
- mysql_config has been changed to reflect libMySQL-devel splitting:
    + it returns $libs set to shared ones only when libMySQL-devel-static not installed

* Tue Feb 27 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.33-ipl3mdk
- Fixed dependencies for server subpackage (added PreReqs).
- Moved %_bindir/my_print_defaults utility back to client subpackage.
- Moved texinfo documentation back to client subpackage.
- Fixed %%post/%%preun scripts for proper texinfo documentation (un)installation.

* Sat Feb 24 2001 Alexander Bokovoy <ab@avilink.net> 3.23.33-ipl2mdk
- Proper distribution of utilites along packages
- Fixed texinfo documentation
- Fixed dependencies

* Thu Feb 15 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.33-ipl1mdk
- 3.23.33
- Rewritten startup scripts.
- Ported to new chrooted scheme.
- Changed address for bug reports to devel@alt-linux.org.

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.23.32-ipl6mdk
- Libification.
- Fixed texinfo documentation.
- Client: added readline expansion for all symbols.

* Thu Feb 01 2001 Alexander Bokovoy <ab@avilink.net> 3.23.32-ipl5mdk
- New version with correct db3

* Sat Dec 30 2000 Alexander Bokovoy <ab@avilink.net> 3.23.29-ipl4mdk
- MySQL-devel depends on MySQL-shared, not MySQL-client
- Syntax error in mysql_install_db fixed

* Sun Dec 24 2000 Alexander Bokovoy <ab@avilink.net> 3.23.29-ipl3mdk
- Update to 3.23.29
- Rebuild with db3-3.2.3e

* Sun Dec 17 2000 Alexander Bokovoy <ab@avilink.net> 3.23.28-ipl2mdk
- Duplication of files in MySQL/MySQL-Client fixed
- mysql_config moved to MySQL-shared
- Various programs from MySQL package require DBI and DBD::mysql perl modules,
  dependencies fixed
- mysqlbug redirects bug reports to devel@linux.iplabs.ru mailing list
- MyISAM RAID type enabled by default

* Sat Dec 16 2000 Alexander Bokovoy <ab@avilink.net> 3.23.28-ipl1mdk
- Updated to 3.23.28
- SPEC file cleaned and uses now IPL rules
- Russian translations added
- Transactions support with BDB tables
- Bench package now requires perl-DBD-mysql instead of perl-Mysql
- Init script has new status command which displays pids of mysqld processes
- Various C++ fixes against g++ 2.96

* Tue Nov 16 2000 Mikhail Zabaluev <mookid@sigent.ru> 3.23.27-1mdk_mhz
- Updated to 3.23.27
- --with-extra-charsets=all, because we need Cyrillic
- made sure that readline is external
- macroized install-info
- mandrakized init script
- custom logrotate config to rotate *.err logs

* Sat Sep 02 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.23-1mdk
- Updated to 3.23.23 to correct php segfaults
- Added separate libmysql_r directory; now both a threaded
  and non-threaded library is shipped.

* Tue Aug 09 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.22-2mdk
- Put libmysqlclient.so in devel package

* Mon Aug 07 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.23.22-1mdk
- Updated to 3.23.22
  (this is a beta version, but starting from 3.23.19, the license is
   GPL, so we prefer the beta to the non-GPL stable tree)
- Macroize
- Merged with the spec from David Axmark <davida@mysql.com>
  :Added the support-files/my-example.cnf to the docs directory.
  :Removed devel dependency on base since it is about client
   development.
  :The --enable-assembler switch is now automatically disables on
   platforms there assembler code is unavailable. This should allow
   building this RPM on non i386 systems.

* Tue May 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.22.32-6mdk
- Recompile with egcs on alpha.

* Tue Apr 18 2000 Pixel <pixel@mandrakesoft.com> 3.22.32-5mdk
- disable starting of mysql while in install

* Thu Apr 06 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-4mdk
- fix bench perms

* Thu Apr 06 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-3mdk
- cleaned spec file

* Mon Apr 03 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.22.32-2mdk
- new group

* Mon Feb 27 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.22.32-1mdk
- updated to 3.22.32 - security updates

* Wed Jan 19 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.30

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Mon Jan 3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.29

* Wed Dec 31 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Mandrake 7.0

* Sat Dec 12 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 3.22.27

* Wed Sep 1 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- put the shared libs in separate package
- fixed dependancies

* Thu Aug 19 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- added fr locale
- Mandrake adaptations
- Solaris adaptations

* Mon Feb 22 1999 David Axmark <david@detron.se>
- Removed unportable cc switches from the spec file. The defaults can
  now be overridden with environment variables. This feature is used
  to compile the official RPM with optimal (but compiler version
  specific) switches.
- Removed the repetitive description parts for the sub rpms. Maybe add
  again if RPM gets a multiline macro capability.
- Added support for a pt_BR translation. Translation contributed by
  Jorge Godoy <jorge@bestway.com.br>.

* Wed Nov 4 1998 David Axmark <david@detron.se>
- A lot of changes in all the rpm and install scripts. This may even
  be a working RPM :-)

* Sun Aug 16 1998 David Axmark <david@detron.se>
- A developers changelog for MySQL is available in the source RPM. And
  there is a history of major user visible changed in the Reference
  Manual.  Only RPM specific changes will be documented here.
