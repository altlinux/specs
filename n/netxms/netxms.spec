Name: netxms
Version: 1.2.1
Release: alt1

Summary: Open source network monitoring system
License: GPL
Group: System/Servers
URL: http://http://www.netxms.org
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar
Source1: netxmsd.init
Source2: nxagentd.init

BuildRequires: flex gcc-c++ zlib-devel libexpat-devel libssl-devel libgd2-devel libreadline-devel libsqlite3-devel libMySQL-devel postgresql-devel libunixODBC-devel

%set_verify_elf_method unresolved=relaxed

%description
NetXMS is an enterprise grade multi-platform open source network management and monitoring system.

%package common
Summary: NetXMS common libraries
Group: System/Libraries
%description common
%summary

%package server
Summary: NetXMS server
Group: System/Libraries
%description server
%summary

%package client
Summary: NetXMS client
Group: Networking/Remote access
%description client
%summary

%package agent
Summary: NetXMS agent
Group: Networking/Remote access
%description agent
%summary

%package mysql
Summary: MySQL resources for NetXMS server
Group: System/Servers
%description mysql
%summary

%package pgsql
Summary: PostgreSQL resources for NetXMS server
Group: System/Servers
%description pgsql
%summary

%package sqlite
Summary: SQLite resources for NetXMS server
Group: System/Servers
%description sqlite
%summary

%package odbc
Summary: ODBC resources for NetXMS server
Group: System/Servers
%description odbc
%summary

%prep
%setup

%build
subst 's|$(DESTDIR)$(bindir)/nxmibc|LD_LIBRARY_PATH=%buildroot/%_libdir $(DESTDIR)$(bindir)/nxmibc|g' Makefile.am
subst 's|/var/opt/netxms|/var/lib/netxms|g' src/agent/core/nxagentd.h
./reconf
%configure      \
  --with-server \
  --with-snmp   \
  --with-mysql  \
  --with-pgsql  \
  --with-sqlite \
  --with-odbc   \
  --with-client \
  --with-agent
%make

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot/%_initdir/netxmsd
cp %SOURCE2 %buildroot/%_initdir/nxagentd
mkdir -p %buildroot/%_sysconfdir
cp contrib/netxmsd.conf-dist %buildroot/%_sysconfdir/netxmsd.conf
cp contrib/nxagentd.conf-dist %buildroot/%_sysconfdir/nxagentd.conf
subst 's|^# LogFile = {syslog}|LogFile = {syslog}|g' %buildroot/%_sysconfdir/*.conf
subst 's|/var/nxagentd|/var/lib/netxms|g' %buildroot/%_sysconfdir/nxagentd.conf
mkdir -p %buildroot/%_localstatedir/%name/agent

%files common
%_libdir/libnetxms.so
%_libdir/libnetxms.so.1
%_libdir/libnetxms.so.1.0.0
%_libdir/libnxdb.so
%_libdir/libnxdb.so.1
%_libdir/libnxdb.so.1.0.0
%_libdir/libnxlp.so
%_libdir/libnxlp.so.1
%_libdir/libnxlp.so.1.0.0
%_libdir/libnxmap.so
%_libdir/libnxmap.so.1
%_libdir/libnxmap.so.1.0.0
%_libdir/libnxsqlite.so
%_libdir/libnxsqlite.so.1
%_libdir/libnxsqlite.so.1.0.0
%_libdir/libnxtre.so
%_libdir/libnxtre.so.5
%_libdir/libnxtre.so.5.0.0

%files server
%_bindir/netxmsd
%_bindir/nxaction
%_bindir/nxadm
%_bindir/nxap
%_bindir/nxdbmgr
%_bindir/nxencpasswd
%_bindir/nxget
%_bindir/nxmibc
%_bindir/nxscript
%_bindir/nxsnmpget
%_bindir/nxsnmpset
%_bindir/nxsnmpwalk
%_bindir/nxupload
%_libdir/libavaya-ers.so
%_libdir/libcisco.so
%_libdir/libnxcore.so
%_libdir/libnxcore.so.1
%_libdir/libnxcore.so.1.0.0
%_libdir/libnxsl.so
%_libdir/libnxsl.so.1
%_libdir/libnxsl.so.1.0.0
%_libdir/libnxsms_generic.so
%_libdir/libnxsms_generic.so.1
%_libdir/libnxsms_generic.so.1.0.0
%_libdir/libnxsms_nxagent.so
%_libdir/libnxsms_nxagent.so.1
%_libdir/libnxsms_nxagent.so.1.0.0
%_libdir/libnxsms_portech.so
%_libdir/libnxsms_portech.so.1
%_libdir/libnxsms_portech.so.1.0.0
%_libdir/libnxsnmp.so
%_libdir/libnxsnmp.so.1
%_libdir/libnxsnmp.so.1.0.0
%_libdir/libnxsrv.so
%_libdir/libnxsrv.so.1
%_libdir/libnxsrv.so.1.0.0
%dir %_libdir/%name
%dir %_libdir/%name/dbdrv
%dir %_libdir/%name/ndd
%_libdir/%name/ndd/baystack.ndd
%_libdir/%name/ndd/cat2900xl.ndd
%_libdir/%name/ndd/catalyst.ndd
%_libdir/%name/ndd/ers8000.ndd
%_libdir/%name/ndd/netscreen.ndd
%dir %_datadir/%name
%_datadir/%name/mibs
%dir %_datadir/%name/sql
%dir %_datadir/%name/images
%_datadir/%name/images/*
%dir %_localstatedir/%name
%_initdir/netxmsd
%config(noreplace) %_sysconfdir/netxmsd.conf
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO doc/manuals/*.odt doc/manuals/*.doc

%files client
%_bindir/nxalarm
%_bindir/nxevent
%_bindir/nxpush
%_bindir/nxsms
%_libdir/libnxcl.so
%_libdir/libnxcl.so.1
%_libdir/libnxcl.so.1.0.0

%files agent
%_bindir/nxagentd
%_initdir/nxagentd
%_libdir/libnsm_ecs.so
%_libdir/libnsm_linux.so
%_libdir/libnsm_logwatch.so
%_libdir/libnsm_ping.so
%_libdir/libnsm_portcheck.so
%_libdir/libnsm_odbcquery.so
%_libdir/libnsm_sms.so
%_libdir/libnsm_ups.so
%_libdir/%name/ecs.nsm
%_libdir/%name/linux.nsm
%_libdir/%name/logwatch.nsm
%_libdir/%name/odbcquery.nsm
%_libdir/%name/ping.nsm
%_libdir/%name/portcheck.nsm
%_libdir/%name/sms.nsm
%_libdir/%name/ups.nsm
%dir %_localstatedir/%name/agent
%config(noreplace) %_sysconfdir/nxagentd.conf

%files mysql
%_libdir/libnxddr_mysql.so
%_libdir/%name/dbdrv/mysql.ddr
%_datadir/%name/sql/dbinit_mysql.sql

%files pgsql
%_libdir/libnxddr_pgsql.so
%_libdir/%name/dbdrv/pgsql.ddr
%_datadir/%name/sql/dbinit_pgsql.sql

%files sqlite
%_libdir/libnxddr_sqlite.so
%_libdir/%name/dbdrv/sqlite.ddr
%_datadir/%name/sql/dbinit_sqlite.sql

%files odbc
%_libdir/libnxddr_odbc.so
%_libdir/%name/dbdrv/odbc.ddr

%changelog
* Thu Jun 21 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.1-alt1
- new version

* Fri Apr 27 2012 Eugene Prokopiev <enp@altlinux.ru> 1.2.0-alt1
- first build for Sisyphus
