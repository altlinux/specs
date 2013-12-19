#./configure --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/lib --localstatedir=/var/lib --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info --disable-dependency-tracking --disable-rpath

#./configure --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/lib --localstatedir=/var/lib --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info --disable-dependency-tracking --disable-rpath


%define modname sql
%define name0 pgpool
%define name1 pgpool-II

Name:		%modname-webguard
Version:	1.3
Release:	alt1

Summary:	Proxy server for PostgreSQL - modules
License:	non-exclusive
Group:		Databases

Packager: Lenar Shakirov <snejok@altlinux.org>

BuildRequires: libpq, webguard 
Requires: libpq, postgresql9.1, webguard

Conflicts: pgpool-II, pgpool-II-devel, pgpool-II-lib

Source0:	%name-%version.tar.gz

ExclusiveArch: x86_64 %ix86

%ifarch x86_64
%define dir_arch 64bit
%endif
%ifarch %ix86
%define dir_arch 32bit
%endif

%description
The product is a software data protection designed to protect against unauthorized access to the Web-server queuing system. The product is responsible for the authentication and authorization of users, and makes registration of user activity in the system (audit), filtering SQL- user requests.
Web-guard system is designed for external differentiation of user rights in the application due to:
- restricting access the database using SQL-queries;
- restricting access when calling stored procedures in the database.

%prep
%setup

%install

install -d %buildroot%_datadir/%name0

install -d %buildroot%_sysconfdir
cp -r %dir_arch/etc/* %buildroot%_sysconfdir
mv %buildroot%_sysconfdir/pcp.conf.sample %buildroot%_sysconfdir/pcp.conf
mv %buildroot%_sysconfdir/pgpool.conf.sample %buildroot%_sysconfdir/pgpool.conf
mv %buildroot%_sysconfdir/pool_hba.conf.sample %buildroot%_sysconfdir/pool_hba.conf

cd %dir_arch/usr/

install -d %buildroot%_bindir
cp -r bin/* %buildroot%_bindir

install -d %buildroot%_mandir
cp -r share/man/* %buildroot%_mandir

install -d %buildroot%_datadir/%name1
cp -r share/pgpool-II %buildroot%_datadir

install -d %buildroot%_includedir
cp -r include/* %buildroot%_includedir

cd -

install -d %buildroot%_libdir
cp -r %dir_arch/%_libdir/* %buildroot%_libdir


# nuke libtool archive and static lib
#rm -f %buildroot%_libdir/libpcp.a,la

%pre
install -p -d -m 0755 /var/run/%name0

#%post 
#/sbin/ldconfig
#chkconfig --add pgpool

#%preun
#if [ $1 = 0 ] ; then
#	/sbin/service pgpool condstop >/dev/null 2>&1
#	chkconfig --del pgpool
#fi

#%postun -p /sbin/ldconfig

%files
%dir %_datadir/%name0
%doc doc/basebackup.sh doc/pgpool-en.html doc/pgpool-ja.css doc/pgpool-ja.html doc/pgpool.css doc/pgpool_remote_start doc/recovery.conf.sample doc/tutorial-en.html doc/tutorial-ja.html doc/tutorial-zh_cn.html doc/where_to_send_queries.odg doc/where_to_send_queries.pdf
%_bindir/pgpool
%_bindir/pcp_attach_node
%_bindir/pcp_detach_node
%_bindir/pcp_node_count
%_bindir/pcp_node_info
%_bindir/pcp_pool_status
%_bindir/pcp_proc_count
%_bindir/pcp_proc_info
%_bindir/pcp_promote_node
%_bindir/pcp_stop_pgpool
%_bindir/pcp_recovery_node
%_bindir/pcp_systemdb_info
%_bindir/pg_md5
%_bindir/pcp_watchdog_info
%_mandir/man8/pgpool*
%_datadir/%name1/insert_lock.sql
%_datadir/%name1/system_db.sql
%_libdir/libpcp.so.*
%_datadir/%name1/pgpool.pam
%attr(644,root,root) %config(noreplace) %_sysconfdir/*.conf
%attr(644,root,root) %_sysconfdir/pgpool.conf.*
#%_initrddir/pgpool
#%config(noreplace) %_sysconfdir/sysconfig/pgpool

#%_includedir/libpcp_ext.h
#%_includedir/pcp.h
#%_includedir/pool_process_reporting.h
#%_includedir/pool_type.h
#%_libdir/libpcp.so

%exclude %_includedir/libpcp_ext.h
%exclude %_includedir/pcp.h
%exclude %_includedir/pool_process_reporting.h
%exclude %_includedir/pool_type.h


%changelog
* Thu Dec 12 2013 Lenar Shakirov <snejok@altlinux.org> 1.3-alt1
- initial build for ALT Linux Sisyphus
