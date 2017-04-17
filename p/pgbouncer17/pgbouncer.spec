%define         pgb_runtimedir   /var/run/%name
Name:		pgbouncer17 
Version:	1.7.2
Release:        alt5 
Summary:	Lightweight connection pooler for PostgreSQL	
License: 	BSD
Group: 		Databases
Url:		https://github.com/pgbouncer/pgbouncer
Source:		%name-%version.tar
Source1:        pgbouncer.init
Source2:        pgbouncer.ini
Source3:	users.txt	
Source4:	pgbouncer.conf

BuildRequires:	libevent-devel libssl-devel
Provides: pgbouncer
Conflicts: pgbouncer < 1.7


%prep
%setup -q
%build
touch lib/mk/install-sh
./autogen.sh
%configure 

%make

%install
%make DESTDIR=%buildroot install
%__install -d -m 1770 %buildroot%pgb_runtimedir
%__install -p -m755 -D %SOURCE1 %buildroot%_initdir/pgbouncer
%__install -p -m755 -D %SOURCE2 %buildroot%_sysconfdir/pgbouncer.ini
%__install -p -m750 -D %SOURCE3 %buildroot%_sysconfdir/users.txt
%__install -p -m750 -D %SOURCE4 %buildroot%_sysconfdir/tmpfiles.d/pgbouncer.conf


%files
%_bindir/pgbouncer
%_sysconfdir/pgbouncer.ini
%attr(750,root,postgres) %_sysconfdir/users.txt
%_initdir/pgbouncer
%attr(1770,root,postgres) %pgb_runtimedir
%doc doc/*
%_defaultdocdir/*
/etc/tmpfiles.d/pgbouncer.conf

%description
Several levels of brutality when rotating connections:
Session pooling - Most polite method. When client connects, a server connection will be assigned to it for the whole duration it stays connected. When client disconnects, the server connection will be put back into pool. 
Transaction pooling - Server connection is assigned to client only during a transaction. When PgBouncer notices that transaction is over, the server will be put back into pool. This is a hack as it breaks application expectations of backend connection. You can use it only when application cooperates with such usage by not using features that can break. See the table below for breaking features. 
Statement pooling - Most aggressive method. This is transaction pooling with a twist - multi-statement transactions are disallowed. This is meant to enforce "autocommit" mode on client, mostly targeted for PL/Proxy. 

%changelog
* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt5
- fix perms for pid file and its location

* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt4
- fix typo

* Mon Apr 17 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt3
- fix tmpfiles place

* Fri Apr 14 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt2
- conflicts with open's pgbouncer

* Thu Apr 13 2017 Denis Medvedev <nbr@altlinux.org> 1.7.2-alt1
- bumped to 1.7.2

* Thu Jul 28 2011 Alexander V Openkin <open@altlinux.ru> 1.4.2-alt1
- 1.4.2 

* Fri Apr 30 2010 Alexander V Openkin <open@altlinux.ru> 1.3.2-alt0.M50p.1
- 1.3.2 

* Thu Oct 15 2009 Alexander V Openkin <open@altlinux.ru> 1.3.1-alt1
- 1.3.1 release 

* Wed Apr 15 2009 Alexander V Openkin <open@altlinux.ru> 1.3-alt1
- 1.3 release 

* Tue Apr 14 2009 Alexander V Openkin <open@altlinux.ru> 1.2.3-alt2
- init script fixed

* Tue Sep 23 2008 Alexander V Openkin <open@altlinux.ru> 1.2.3-alt1
-  1.2.3 release. 

* Sat Feb 16 2008 Alexander V Openkin <open@altlinux.ru> 1.1.2-alt1
-  1.1.2 release.
