%define full_ver %(pkg-config --modversion libpq)
%define pg_ver %(c=%{full_ver}; echo ${c%%.*})
%define sname pgpool

Name: pgpool-II
Version: 4.2.7
Release: alt1
Summary: Pgpool is a connection pooling/replication server for PostgreSQL
License: BSD
Group: Databases
Url: http://www.pgpool.net
Source: %name-%version.tar

Source1: pgpool.service
Source2: pgpool.tmpfiles
Source3: pgpool.init
Source4: pgpool.sysconfig

Patch: 0001-Update-path-for-socket-and-log.patch

BuildRequires: flex
BuildRequires: postgresql-devel
BuildRequires: pam-devel
BuildRequires: libmemcached-devel
BuildRequires: libssl-devel
BuildRequires: setproctitle-devel

Provides: pgpool2 = %EVR

Requires: postgresql-common

%description
pgpool-II is a inherited project of pgpool (to classify from
pgpool-II, it is sometimes called as pgpool-I). For those of
you not familiar with pgpool-I, it is a multi-functional
middle ware for PostgreSQL that features connection pooling,
replication and load balancing functions. pgpool-I allows a
user to connect at most two PostgreSQL servers for higher
availability or for higher search performance compared to a
single PostgreSQL server.

%package -n libpcp
Summary: lib files for  %name
Group: System/Libraries
Provides: %name-lib = %EVR
Obsoletes: %name-lib < %EVR

%description -n libpcp
lib files for %name.

%package -n libpcp-devel
Summary: The development files for pgpool-II
Group: Development/C
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR
Requires: libpcp = %EVR

%description -n libpcp-devel
Development headers and libraries for pgpool-II.

%package -n postgresql%pg_ver-%name
Summary: Postgresql extensions for pgpool-II
Group: Databases
Requires: postgresql%pg_ver-server

%description -n postgresql%pg_ver-%name
Postgresql extensions libraries and sql files for pgpool-II.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --with-pam \
    --with-openssl \
    --disable-rpath \
    --with-memcached=%_includedir/libmemcached \
    --sysconfdir=%_sysconfdir/%sname

%make_build
%make_build -C src/sql/pgpool-recovery
%make_build -C src/sql/pgpool-regclass

%install
%make DESTDIR=%buildroot install
%make DESTDIR=%buildroot install -C src/sql/pgpool-recovery
%make DESTDIR=%buildroot install -C src/sql/pgpool-regclass

mkdir -p %buildroot{{%_logdir,%_datadir}/%sname,%_unitdir,%_initdir,%_tmpfilesdir,%_man1dir,%_man8dir}

install -p -m644 %SOURCE1 %buildroot%_unitdir/%sname.service
install -p -m644 %SOURCE2 %buildroot%_tmpfilesdir/%sname.conf
install -p -m755 %SOURCE3 %buildroot%_initdir/%sname
install -p -m644 -D %SOURCE4 %buildroot%_sysconfdir/sysconfig/%sname

mv %buildroot%_sysconfdir/%sname/pcp.conf.sample %buildroot%_sysconfdir/%sname/pcp.conf
mv %buildroot%_sysconfdir/%sname/pgpool.conf.sample %buildroot%_sysconfdir/%sname/pgpool.conf
mv %buildroot%_sysconfdir/%sname/pool_hba.conf.sample  %buildroot%_sysconfdir/%sname/pool_hba.conf
mv %buildroot%_sysconfdir/%sname/failover.sh.sample %buildroot%_sysconfdir/%sname/failover.sh
mv %buildroot%_sysconfdir/%sname/follow_primary.sh.sample %buildroot%_sysconfdir/%sname/follow_primary.sh
mv %buildroot%_sysconfdir/%sname/pgpool_remote_start.sample %buildroot%_sysconfdir/%sname/pgpool_remote_start
mv %buildroot%_sysconfdir/%sname/recovery_1st_stage.sample %buildroot%_sysconfdir/%sname/recovery_1st_stage
mv %buildroot%_sysconfdir/%sname/pgpool.conf.sample-* %buildroot%_datadir/%sname/

# Copy man pages
cp doc/src/sgml/man1/* %buildroot%_man1dir/
cp doc/src/sgml/man8/* %buildroot%_man8dir/

rm -f %buildroot%_libdir/*.{a,la}

%post
# Migrate configs from pgpool < 4.2.1
if [ $1 -eq 2 ]; then
    [ ! -f %_sysconfdir/pcp.conf ] || mv -f %_sysconfdir/pcp.conf %_sysconfdir/%sname/pcp.conf
    [ ! -f %_sysconfdir/pgpool.conf ] || mv -f %_sysconfdir/pgpool.conf %_sysconfdir/%sname/pgpool.conf
    [ ! -f %_sysconfdir/pool_hba.conf ] || mv -f %_sysconfdir/pool_hba.conf %_sysconfdir/%sname/pool_hba.conf
    chown root:postgres %_sysconfdir/%sname/*
    chmod 640 %_sysconfdir/%sname/*
fi

%post_service %sname

%preun
%preun_service %sname

%files
%doc NEWS COPYING src/sample
%_bindir/*
%_datadir/%name
%_datadir/%sname
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
%dir %attr(750,root,postgres) %_sysconfdir/%sname
%config(noreplace) %attr(640,root,postgres) %_sysconfdir/%sname/*
%config(noreplace) %_sysconfdir/sysconfig/%sname
%_man1dir/*
%_man8dir/*

%attr(1775,root,%sname) %dir %_logdir/%sname

%files -n libpcp-devel
%_includedir/*
%_libdir/libpcp.so

%files -n libpcp
%_libdir/libpcp.so.*

%files -n postgresql%pg_ver-%name
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%changelog
* Tue Feb 08 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.7-alt1
- 4.2.7

* Thu Mar 11 2021 Alexey Shabalin <shaba@altlinux.org> 4.2.2-alt2
- Fixed config files permissions.

* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 4.2.2-alt1
- 4.2.2
- Execute service as postgres system user.
- Move old configs to /etc/pgpool dir.

* Sun Feb 07 2021 Alexey Shabalin <shaba@altlinux.org> 4.2.1-alt1
- 4.2.1
- Execute service as pgpool system user.
- Move configs to /etc/pgpool dir.

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.2-alt1
- 4.0.2
- build for postgresql11

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.7.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Jul 24 2018 Alexey Shabalin <shaba@altlinux.org> 3.7.4-alt1
- 3.7.4
- rename package pgpool-II-lib to libpcp
- rename package pgpool-II-devel to libpcp-devel
- add package postgresql10-pgpool-II with postgresql extension

* Mon Feb 06 2012 Alexander V Openkin <open@altlinux.ru> 3.1.2-alt2
- 3.1.2 init script fixed

* Thu Feb 02 2012 Alexander V Openkin <open@altlinux.ru> 3.1.2-alt1
- 3.1.2 release

* Thu Jul 28 2011 Alexander V Openkin <open@altlinux.ru> 3.0.4-alt1
- 3.0.4 release

* Wed Mar 09 2011 Alexander V Openkin <open@altlinux.ru> 3.0.3-alt1
- 3.0.3 release

* Fri Sep 24 2010 Konstantin Pavlov <thresh@altlinux.org> 2.3.3-alt0.M40.7
- Apply patch fixing EINTR problem with pgpool health check.
- Log to /var/log/pgpool instead of slow syslog.

* Fri Jul 30 2010 Alexander V Openkin <open@altlinux.ru> 2.2.5-alt0.M40.2
- 2.3.3 release 

* Wed Oct 14 2009 Alexander V Openkin <open@altlinux.ru> 2.2.5-alt1
- 2.2.5 release

* Fri May 22 2009 Alexander V Openkin <open@altlinux.ru> 2.2.2-alt2
- New init script read the /etc/pgpool.d directory and running many pgpool instance 

* Tue May 05 2009 Alexander V Openkin <open@altlinux.ru> 2.2.2-alt1
- 2.2.2 release, new init script. 

* Wed Oct 22 2008 Alexander V Openkin <open@altlinux.ru> 2.1-alt1
- 2.1 release 

* Wed Sep 05 2007 Alexander V Openkin <open@altlinux.ru> 1.2-alt1
- changed init script (logging to syslog) 

* Tue Aug 28 2007 Alexander V Openkin <open@altlinux.ru> 1.2-alt0.4
- 1.2 release 

* Fri Jul 20 2007 Alexander V Openkin <open@altlinux.ru> 1.1.1-alt0.2
- pool_process_query.c: Fix kind mismatch error when load_balance_mode is true

