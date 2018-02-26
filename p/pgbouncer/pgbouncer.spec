%define         pgb_runtimedir   /var/run/%name
Name:		pgbouncer 
Version:	1.4.2
Release:        alt1 
Summary:	Lightweight connection pooler for PostgreSQL	
License: 	BSD
Group: 		Databases
Url:		https://developer.skype.com/SkypeGarage/DbProjects/PgBouncer
Source:		%name-%version.tgz
Source1:        pgbouncer.init
Source2:        pgbouncer.ini
Source3:	users.txt	

BuildRequires:	libevent-devel



%prep
%setup -q

%configure 

%build
%make

%install
%make DESTDIR=%buildroot install
%__install -d -m 1770 %buildroot%pgb_runtimedir
%__install -p -m755 -D %SOURCE1 %buildroot%_initdir/pgbouncer
%__install -p -m755 -D %SOURCE2 %buildroot%_sysconfdir/pgbouncer.ini
%__install -p -m750 -D %SOURCE3 %buildroot%_sysconfdir/users.txt


%files
%_bindir/pgbouncer
%_man1dir/*
%_man5dir/*

%_sysconfdir/pgbouncer.ini
%attr(750,root,postgres) %_sysconfdir/users.txt
%_initdir/pgbouncer
%attr(1770,root,postgres) %pgb_runtimedir


%description
Several levels of brutality when rotating connections:
Session pooling - Most polite method. When client connects, a server connection will be assigned to it for the whole duration it stays connected. When client disconnects, the server connection will be put back into pool. 
Transaction pooling - Server connection is assigned to client only during a transaction. When PgBouncer notices that transaction is over, the server will be put back into pool. This is a hack as it breaks application expectations of backend connection. You can use it only when application cooperates with such usage by not using features that can break. See the table below for breaking features. 
Statement pooling - Most aggressive method. This is transaction pooling with a twist - multi-statement transactions are disallowed. This is meant to enforce "autocommit" mode on client, mostly targeted for PL/Proxy. 

%changelog
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
