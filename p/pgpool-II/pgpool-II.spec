%def_with	devel
%def_with       lib
%define		pgpool_configdir    %_sysconfdir/pgpool.d
%define		pgpool_piddir    %_var/run/pgpool
%define		pgpool_logdir    %_logdir/pgpool
%define		PGSQL   pgsql

Name:		pgpool-II 
Version:	3.1.2
Release:    	alt2
Summary:	pgpool is a connection pool/replication server for PostgreSQL	
License: 	BSD
Group: 		Databases
Url:		http://pgfoundry.org/projects/pgpool
Source:		%name-%version.tar.gz
Source1:    pgpool.init
Source2:	pgpool.conf

BuildRequires: flex gcc-c++ postgresql-devel


%package        devel
Summary:        header files for  %name.
Group:          Databases

%package        lib
Summary:        lib files for  %name.
Group:          Databases



%prep
%setup -q
%autoreconf

%build
%configure   --includedir=/usr/include/pgsql 
%make_build

%install
/usr/sbin/groupadd -g 46 postgres || :
/usr/sbin/useradd -M -o -r -d %_localstatedir/%PGSQL -s /dev/null \
        -c "PostgreSQL Server, slony1, pgpool daemon" -u 46 postgres -g postgres || :

%make DESTDIR=%buildroot install
%__install -p -m755 -D %SOURCE1 %buildroot%_initdir/pgpool
%__install -p -m755 -D %SOURCE2 %buildroot%_sysconfdir/pgpool.conf 
%__mkdir_p %buildroot{%pgpool_piddir,%pgpool_logdir}


mv %buildroot%_sysconfdir/pcp.conf.sample %buildroot%_sysconfdir/pcp.conf
mv %buildroot%_sysconfdir/pool_hba.conf.sample  %buildroot%_sysconfdir/pool_hba.conf

mkdir %buildroot%_sysconfdir/cron.d
/bin/cat << __EOF__ > %buildroot%_sysconfdir/cron.d/pgpool
20	10	*	*	*	root	find /var/log/pgpool/ -type f -mtime +90 -delete
__EOF__

%pre
/usr/sbin/groupadd -g 46 postgres || :
/usr/sbin/useradd -M -o -r -d %_localstatedir/%PGSQL -s /dev/null \
	-c "PostgreSQL Server and slony1 daemon" -u 46 postgres -g postgres || :

%post
%post_service pgpool

%files
%attr(0755,root,root) %_bindir/*

%_man8dir/*
%_datadir/%name
%_initdir/pgpool
%config(noreplace) %_sysconfdir/pgpool.conf
%config(noreplace) %_sysconfdir/pcp.conf
%config(noreplace) %_sysconfdir/pool_hba.conf

%config %_sysconfdir/cron.d/pgpool

%attr(770,root,postgres) %dir %pgpool_piddir
%attr(770,root,postgres) %dir %pgpool_logdir

%files devel
%_includedir/%PGSQL

%files lib
%_libdir/libpcp.so
%_libdir/libpcp.so.0
%_libdir/libpcp.so.0.0.0


%description
pgpool-II is a middleware that works between PostgreSQL servers and a PostgreSQL database client
%description    devel
header files for %name.
%description    lib
lib files for %name.

%changelog
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

