Name:		pdns
Version:	2.9.22
Release:	alt1.1

%def_with	ssl
%def_with	mysql
%def_with	pgsql
%def_with	sqlite
%def_with	ldap
%def_without	tdb
%def_with	sqlite3

Summary:	PowerDNS is a Versatile Database Driven Nameserver
License:	GPL
Group:		System/Servers
URL:		http://www.powerdns.com/
Source0:	http://downloads.powerdns.com/releases/pdns-%version.tar.gz
Patch0:		pdns-2.9.7-init.patch
Patch1:		pdns-2.9.20-alt-rcstuff.patch
Patch2:		pdns-2.9.21.2-init.patch
Patch3:		pdns-2.9.21.2-gcc4.4.patch

Packager:	Pavel Shilovsky <piastry@altlinux.org>
Provides:	nameserver powerdns PowerDNS
Obsoletes:	nameserver powerdns PowerDNS

Summary(ru_RU.UTF8): DNS-сервер с хранением данных в LDAP, SQL или файлах BIND

#--------   Override standard directories   -------------#

%define            statedir  %_localstatedir/powerdns
%define            socketdir       %_var/run/powerdns
%{expand:%%global  sysconfdir0  %_sysconfdir}
%{expand:%%global _sysconfdir   %_sysconfdir/powerdns}
%{expand:%%global    libdir0        %_libdir}
%{expand:%%global  mylibdir         %_libdir/powerdns}
%{expand:%%global   _libdir         %mylibdir}

#--------   BuildPreReq and Dynamic modules   -----------#

%define		dynmodules pipe

BuildPreReq:	bison, flex, gdbm-devel, gcc-c++, libstdc++-devel, zlib-devel, boost-devel >= 1.33

%if_with ssl
BuildPreReq:	openssl-devel
%endif

%if_with mysql
BuildPreReq:	MySQL-devel
%{expand:%%global dynmodules %dynmodules gmysql}
%endif

%if_with pgsql
BuildRequires:	postgresql-devel libpq-devel-static
%{expand:%%global dynmodules %dynmodules gpgsql}
%endif

%if_with sqlite
BuildPreReq:	sqlite-devel
%{expand:%%global dynmodules %dynmodules gsqlite}
%endif

%if_with sqlite3
BuildPreReq:    libsqlite3-devel
%{expand:%%global dynmodules %dynmodules gsqlite3}
%endif

%if_with tdb
BuildPreReq:	libtdb-devel
%{expand:%%global dynmodules %dynmodules xdb}
%endif

%if_with ldap
BuildPreReq:	openldap-devel
%{expand:%%global dynmodules %dynmodules ldap}
%endif

%if_with geo
%{expand:%%global dynmodules %dynmodules geo}
%endif

%description
PowerDNS is a versatile nameserver which supports a large number
of different backends ranging from simple zonefiles to relational
databases and load balancing/failover algorithms.

This RPM is statically compiled and should work on all Linux distributions.
It comes with support for MySQL, PostgreSQL, Bind zonefiles and the 'pipe
backend' availible as external packages.

%description -l ru_RU.UTF8
PowerDNS является популярным сервером DNS, выпускаемым под лицензией GNU GPL.
По сравнению с BIND, PowerDNS быстрее, надёжнее и компактнее.
По сравнению с dnsmasq PowerDNS поддерживает больше функций,
в частности, Zone transfer.

Отличительной особенностью PowerDNS является поддержка большого количества
модулей хранения данных (т.н. backends): в файлах DNS-сервера BIND,
в базах LDAP, MySQL, PostgreSQL, TDB (Trivial Database, используемая в Samba)
и т.н. pipes - модуля, обменивающегося данными с внешним обработчиком
через стандартный ввод-вывод.

%package	backend-pipe
Summary:	Pipe/coprocess backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-pipe
This package contains the pipe backend for the PowerDNS nameserver.
This allows PowerDNS to retrieve domain info from a process
that accepts questions on stdin and returns answers on stdout. 

%if_with mysql

%package	backend-mysql
Summary:	MySQL backend for %name
Group:		System/Servers
Requires:	%name = %version
Requires:	libMySQL

%description	backend-mysql
This package contains a MySQL backend for the PowerDNS nameserver.

%endif

%if_with pgsql

%package	backend-pgsql
Summary:	Generic PostgreSQL backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-pgsql
This package contains a generic PostgreSQL backend
for the PowerDNS nameserver. It has configurable SQL statements.

%endif

%if_with tdb

%package	backend-tdb
Summary:	XDB/tdb/gdb backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-tdb
This package contains a table backend for PowerDNS. Currently includes TDB,
the Trivial Database or Tridgell Database.

%endif

%if_with ldap

%package	backend-ldap
Summary:	LDAP backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-ldap
This package contains a LDAP backend for the PowerDNS nameserver.

%endif

%if_with sqlite

%package	backend-sqlite
Summary:	SQLite backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-sqlite
This package contains a SQLite backend for the PowerDNS nameserver.

%endif

%if_with sqlite3

%package       backend-sqlite3
Summary:       SQLite3 backend for %name
Group:         System/Servers
Requires:      %name = %version

%description   backend-sqlite3
This package contains a SQLite3 backend for the PowerDNS nameserver.

%endif

%if_with geo

%package	backend-geo
Summary:	GEO backend for %name
Group:		System/Servers
Requires:	%name = %version

%description	backend-geo
This package contains a geo backend for the PowerDNS nameserver.

%endif

%package	devel
Summary:	Development headers and libraries for %name
Group:		System/Servers
Requires:	%name = %version
Requires:	%name-backend-pipe   = %version
%if_with mysql
Requires:	%name-backend-mysql  = %version
%endif
%if_with pgsql
Requires:	%name-backend-pgsql  = %version
%endif
%if_with tdb
Requires:	%name-backend-tdb    = %version
%endif
%if_with ldap
Requires:	%name-backend-ldap   = %version
%endif
%if_with sqlite
Requires:	%name-backend-sqlite = %version
%endif
%if_with sqlite3
Requires:	%name-backend-sqlite3 = %version
%endif

%description	devel
Development headers and libraries for %name

%prep
%setup -q
%patch0 -p0
%patch1
%patch2 -p1
%patch3 -p1

# lib64 fix
%if "%_lib" != "/lib"
find -type f -name "configure.in" | xargs %__subst "s|/lib/|/%_lib/|g"
find -type f -name "configure.in" | xargs %__subst "s|/lib\ |/%_lib\ |g"
find -type f -name "configure.in" | xargs %__subst "s|/lib\"|/%_lib\"|g"
%endif

%build
touch NEWS AUTHORS
libtoolize --copy --force
aclocal
autoconf
automake --copy --add-missing

export   CFLAGS="%optflags -DLDAP_DEPRECATED"
export CXXFLAGS="%optflags -DLDAP_DEPRECATED"

%configure \
    --with-socketdir=%socketdir \
    --with-dynmodules="%dynmodules" \
    --with-modules="" \
    --with-mysql=%_prefix \
    --with-pgsql=%_prefix \
    --with-sqlite=%_prefix \
    --with-sqlite-includes=%_includedir \
    --with-sqlite3=%_prefix \
    --with-sqlite3-includes=%_includedir

# why is this nessesary all of a sudden?
#find . -type f -name "Makefile" | xargs %__subst "s|-pthread|-lpthread|g"

# parallell build's broken now?
%make_build

# this might work someday..., meanwhile use S1
#pushd pdns/docs
#    make
#popd

%install
# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%makeinstall

%__install -d %buildroot{%socketdir,%statedir}

# fix the config
%__rm %buildroot%_sysconfdir/pdns.conf-dist

cat >> %buildroot%_sysconfdir/pdns.conf << __EOF__
#
#   /etc/powerdns/pdns.conf
#
#   Settings for PowerDNS server under ALTLinux
#

chroot=%statedir

module-dir=%mylibdir
socket-dir=%socketdir

setuid=powerdns
setgid=powerdns

launch=bind
#Note: bind-config path is relative to chroot
#bind-config=/namedb/named.conf

#recursor=127.0.0.1:5300

## EOF ##
__EOF__

# **** Restore back original values of builtin macros! ****
%{expand:%%global _sysconfdir %sysconfdir0}
%{expand:%%global     _libdir     %libdir0}

# Install sysv scripts..
%__install -d %buildroot%_initrddir
%__install -m755 pdns/pdns %buildroot%_initrddir/powerdns

%add_verify_elf_skiplist %mylibdir/*

%pre
if test -z "$(%__id -u powerdns 2>/dev/null)"; then
    useradd -r \
	-c 'Pseudo-user for running PowerDNS service' \
	-d %statedir \
	-s /bin/false \
	powerdns
else :
fi

%post
%post_service powerdns

%preun
%preun_service powerdns


%files
%doc ChangeLog HACKING INSTALL README TODO pdns/pdns.conf-dist
%config(noreplace) %attr(0600,root,root) %_sysconfdir/powerdns/pdns.conf
%_initrddir/powerdns
%dir %_sysconfdir/powerdns
%dir %mylibdir/
%dir %attr(0755,powerdns,powerdns) %socketdir
%dir %attr(0750,root,powerdns) %statedir
%_bindir/pdns_control
%_bindir/zone2sql
%_bindir/zone2ldap
%_sbindir/pdns_server
%_man8dir/pdns_control.8*
%_man8dir/pdns_server.8*
%_man8dir/zone2sql.8*

%files backend-pipe
%mylibdir/libpipebackend.so

%if_with mysql
%files backend-mysql
%mylibdir/libgmysqlbackend.so
%endif

%if_with pgsql
%files backend-pgsql
%mylibdir/libgpgsqlbackend.so
%endif

%if_with tdb
%files backend-tdb
%_bindir/xdb-fill
%mylibdir/libxdbbackend.so
%endif

%if_with ldap
%files backend-ldap
%mylibdir/libldapbackend.so
%endif

%if_with sqlite
%files backend-sqlite
%mylibdir/libgsqlitebackend.so
%endif

%if_with sqlite3
%files backend-sqlite3
%mylibdir/libgsqlite3backend.so*
%endif

%if_with geo
%files backend-geo
%doc modules/geobackend/README
%mylibdir/libgeobackend.so
%endif

%files devel
#mylibdir/*.so
%exclude %mylibdir/*.la
%mylibdir/*.a

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.9.22-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Thu Mar 25 2010 Pavel Shilovsky <piastry@altlinux.org> 2.9.22-alt1
- Import 2.9.22 sources
- Patch work
  + Rewrite patch #6
  + Delete patches #1, #3, #4
  + Change patch numbers (#2, #5, #6) to (#1, #2, #3)
- Change .gear-rules according to deleted patches

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 2.9.21.2-alt5.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon May 25 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt5
- fixed build errors on gcc 4.4

* Wed Mar  4 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt4
- fixed some bugs in patch #5

* Tue Mar  3 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt3
- bugfix #18871: added patch #5

* Sat Jan 24 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt2
- fixed missing backend-mysql package requires

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.2-alt1
- updated to new version 2.9.21.2

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.1-alt3
- fixed instaltions problems with devel package requires
- built pgsql backend

* Wed Oct 29 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt2
- fixed problems with g++ 4.3
   + add patch to support g++ 4.3

* Sun Oct 19 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt1
- updated to new version 2.9.21.1
   + add patch to support boost 1.36
   + add backend sqlite3

* Sun Apr 29 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.21-alt1
- updated to new version 2.9.21
   + remove patch #3
   + boost 1.33 or later is required now

* Fri Jan 12 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt3
- bugfix #10650: added patch #3

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt2
- bugfix #10138

* Wed Sep 13 2006 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt1
- initial build for ALTLinux, based on 2.9.20-2mdk

## EOF ##
