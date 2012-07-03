%define priority 50

Name: dspam
Version: 3.9.0
Release: alt1.beta2.1
Summary: DSPAM is an open-source, freely available anti-spam solution
License: GPL
Group:	 Networking/Mail
Source0: %name-%version.tar
Source1: %name.init
Source2: %name-clean
Source3: %name.http
Source4: dspam_corpus
Source5: train.pl
Source6: %name.logrotate

URL: http://dspam.sourceforge.net/
Packager: Alexey Shentzev <ashen@altlinux.ru>
Requires: %name-storage = %version-%release

#hash storage always enabled
%def_with    mysql
%def_with    pgsql
%def_with    sqlite3
%def_with    hash

%def_without libdb3
%def_without libdb4

BuildPreReq: zlib-devel
BuildPreReq: gcc-c++
BuildPreReq: libstdc++-devel

%{?_with_libdb3:BuildPreReq: libdb3-devel}
%{?_with_libdb4:BuildPreReq: libdb4-devel}
%{?_with_sqlite3:BuildPreReq: libsqlite3-devel}
%{?_with_mysql:BuildPreReq: libMySQL-devel}
%{?_with_pgsql:BuildPreReq: libpq-devel postgresql-devel}

BuildRequires: glibc-devel-static

%description
DSPAM is an open-source, freely available anti-spam solution designed to combat
unsolicited commercial email using advanced statistical analysis. In short,
DSPAM filters spam by learning what spam is and isn't by learning
each user's individual mail behavior. This allows DSPAM to provide
highly-accurate, personalized filtering for each user on even a large system
and provides an administratively maintenance free solution capable of learning
each user's email behaviors with very few false positives.

You need to install one of storage package (%name-*).

%if_with hash
%package hash
Summary: DSPAM is an open-source, freely available anti-spam solution (hash storage)
Group: Networking/Mail
Requires: %name = %version-%release
Provides: %name-storage = %version-%release
%description hash
DSPAM is an open-source, freely available anti-spam solution designed to combat
unsolicited commercial email using advanced statistical analysis. In short,
DSPAM filters spam by learning what spam is and isn't by learning
each user's individual mail behavior. This allows DSPAM to provide
highly-accurate, personalized filtering for each user on even a large system
and provides an administratively maintenance free solution capable of learning
each user's email behaviors with very few false positives.
%endif #with hash

%if_with sqlite3
%package sqlite3
Summary: DSPAM is an open-source, freely available anti-spam solution (SQLite3 storage)
Group: Networking/Mail
Requires: %name = %version-%release
Provides: %name-storage = %version-%release
%description sqlite3
DSPAM is an open-source, freely available anti-spam solution designed to combat
unsolicited commercial email using advanced statistical analysis. In short,
DSPAM filters spam by learning what spam is and isn't by learning
each user's individual mail behavior. This allows DSPAM to provide
highly-accurate, personalized filtering for each user on even a large system
and provides an administratively maintenance free solution capable of learning
each user's email behaviors with very few false positives.
%endif #with sqlite3

%if_with pgsql
%package pgsql
Summary: DSPAM is an open-source, freely available anti-spam solution (PostgreSQL storage)
Group: Networking/Mail
Requires: %name = %version-%release
Provides: %name-storage = %version-%release
%description pgsql
DSPAM is an open-source, freely available anti-spam solution designed to combat
unsolicited commercial email using advanced statistical analysis. In short,
DSPAM filters spam by learning what spam is and isn't by learning
each user's individual mail behavior. This allows DSPAM to provide
highly-accurate, personalized filtering for each user on even a large system
and provides an administratively maintenance free solution capable of learning
each user's email behaviors with very few false positives.
%endif #with pgsql

%if_with mysql
%package mysql
Summary: DSPAM is an open-source, freely available anti-spam solution (MySQL storage)
Group: Networking/Mail
Requires: %name = %version-%release
Provides: %name-storage = %version-%release
%description mysql
DSPAM is an open-source, freely available anti-spam solution designed to combat
unsolicited commercial email using advanced statistical analysis. In short,
DSPAM filters spam by learning what spam is and isn't by learning
each user's individual mail behavior. This allows DSPAM to provide
highly-accurate, personalized filtering for each user on even a large system
and provides an administratively maintenance free solution capable of learning
each user's email behaviors with very few false positives.
%endif #with mysql

%package -n lib%name
Summary: The DSPAM core processing engine
Group: Development/C
%description -n lib%name
The DSPAM core processing engine, also known as libdspam, provides all primary
spam filtering functions.  The engine is linked to other dspam components (or
shells) to provide functionality. libdspam is capable of being linked
in with any other application as a "drop-in" to provide spam filtering to
mail clients, other anti-spam tools, and other such type projects that
would benefit from its use.  Both static and shared versions are built by
libtool and installed upon 'make install'.

%package -n lib%name-devel
Summary: The DSPAM core processing engine
Group: Development/C
Requires: lib%name = %version-%release
%description -n lib%name-devel
The DSPAM core processing engine, also known as libdspam, provides all primary
spam filtering functions.  The engine is linked to other dspam components (or
shells) to provide functionality. libdspam is capable of being linked
in with any other application as a "drop-in" to provide spam filtering to
mail clients, other anti-spam tools, and other such type projects that
would benefit from its use.  Both static and shared versions are built by
libtool and installed upon 'make install'.

%package webui
Summary: The DSPAM core processing engine
Group: Development/C
BuildPreReq: perl-CGI perl-GD-Text perl-GD-Graph3d
Requires: %name = %version-%release webserver perl-CGI perl-GD-Text perl-GD-Graph3d
Provides: perl(configure.pl)
%description webui
The DSPAM core processing engine, also known as libdspam, provides all primary
spam filtering functions. The engine is web user interface.

%prep
%setup -q

%build
STORAGES_LIST="hash_drv"
STORAGES_INCLUDE_LIST=""
%if_with pgsql
STORAGES_LIST="${STORAGES_LIST},pgsql_drv"
STORAGES_INCLUDE_LIST="${STORAGES_INCLUDE_LIST} --with-pgsql-includes=%_includedir/pgsql/"
%endif #with pgsql

%if_with mysql
STORAGES_LIST="${STORAGES_LIST},mysql_drv"
STORAGES_INCLUDE_LIST="${STORAGES_INCLUDE_LIST} --with-mysql-includes=%_includedir/mysql/"
%endif #with mysql

%if_with sqlite3
STORAGES_LIST="${STORAGES_LIST},sqlite3_drv"
%endif #with sqlite3

%if_with libdb4
STORAGES_LIST="${STORAGES_LIST},libdb4_drv"
%endif #with libdb4

%autoreconf -fisv
%configure --with-storage-driver=${STORAGES_LIST} ${STORAGES_INCLUDE_LIST} \
           --disable-dependency-tracking \
	   --enable-daemon \
           --enable-neural-networking \
	   --enable-preferences-extension \
           --enable-virtual-users \
	   --enable-long-usernames \
	   --enable-large-scale \
	   --with-gnu-ld \
	   --with-pic \
	   --enable-homedir \
	   --with-dspam-home=%_localstatedir/%name \
	   --enable-clamav \
	   --enable-syslog \
	   --sysconfdir=%_sysconfdir/%name \
	   --with-logdir=%_logdir/%name \
	   --with-logfile=%_logdir/%name/%name.log

%make CFLAGS="%optflags %optflags_shared"

%install
%__mkdir_p %buildroot%_localstatedir/%name
%make DESTDIR=%buildroot install
%__mkdir_p %buildroot/%_initdir
%__install -m 0755 %SOURCE1 %buildroot%_initdir/%name
%__mkdir_p %buildroot%_sysconfdir/cron.daily
%__install -m 0755 %SOURCE2 %buildroot%_sysconfdir/cron.daily
%__mkdir_p %buildroot/var/lib/%name
%__mkdir_p %buildroot/%_logdir/%name

%__mkdir_p %buildroot/%_docdir/%name-%version
cp CHANGELOG %buildroot/%_docdir/%name-%version/
cp LICENSE %buildroot/%_docdir/%name-%version/
cp README.* %buildroot/%_docdir/%name-%version/
cp UPGRADING %buildroot/%_docdir/%name-%version/
cp src/%name.conf %buildroot%_sysconfdir/%name/%name.conf
%__mkdir_p %buildroot%_docdir/%name-%version/doc
cp doc/*.txt %buildroot%_docdir/%name-%version/doc
%__install -m 0755 %SOURCE4 %buildroot/%_bindir/

%__mkdir_p %buildroot/%_datadir/%name-%version/txt
cp txt/*.txt %buildroot/%_datadir/%name-%version/txt
%__install -m 0755 %SOURCE5 %buildroot/%_datadir/%name-%version


%__mkdir_p %buildroot/%_datadir/%name-%version/sql/mysql
cp src/tools.mysql_drv/*.sql %buildroot/%_datadir/%name-%version/sql/mysql/
%__mkdir_p %buildroot/%_datadir/%name-%version/sql/pgsql
cp src/tools.pgsql_drv/*.sql %buildroot/%_datadir/%name-%version/sql/pgsql/
%__mkdir_p %buildroot/%_datadir/%name-%version/sql/sqlite
cp src/tools.sqlite_drv/*.sql %buildroot/%_datadir/%name-%version/sql/sqlite/

%__mkdir_p %buildroot%_datadir/%name-%version/webui/cgi-bin
cp webui/cgi-bin/*.cgi %buildroot%_datadir/%name-%version/webui/cgi-bin/
cp webui/cgi-bin/*.pl %buildroot%_datadir/%name-%version/webui/cgi-bin/
cp webui/cgi-bin/*.prefs %buildroot%_datadir/%name-%version/webui/cgi-bin/
cp webui/cgi-bin/*.txt %buildroot%_datadir/%name-%version/webui/cgi-bin/
cp webui/cgi-bin/admins %buildroot%_datadir/%name-%version/webui/cgi-bin/
%__mkdir_p %buildroot%_datadir/%name-%version/webui/cgi-bin/templates
cp webui/cgi-bin/templates/*.html %buildroot%_datadir/%name-%version/webui/cgi-bin/templates/
%__mkdir_p %buildroot%_datadir/%name-%version/webui/htdocs
cp webui/htdocs/base.css %buildroot%_datadir/%name-%version/webui/htdocs/
cp webui/htdocs/dspam-logo-small.gif %buildroot%_datadir/%name-%version/webui/htdocs/
%__install -m 0644 %SOURCE3 %buildroot%_datadir/%name-%version/

install -pD %SOURCE6 %buildroot%_sysconfdir/logrotate.d/%name

%files
%_bindir/*
%exclude %_bindir/css*
%exclude %_bindir/dspam_pg2int8
%config(noreplace) %_sysconfdir/%name/%name.conf
%_initdir/%name
%attr(0750,root,mail) %config(noreplace) %_sysconfdir/cron.daily/%name-clean
%attr(0640,root,mail) %config(noreplace) %_sysconfdir/logrotate.d/%name
%_datadir/%name-%version/txt/*
%_datadir/%name-%version/train.pl
%_man1dir/*
%doc %_docdir/%name-%version/*
%attr(0750,root,mail) %_bindir/%name
%attr(0770,root,mail) /var/lib/%name
%attr(0770,root,mail) %_logdir/%name
%dir %_docdir/dspam-%version

%files -n lib%name
%_libdir/lib%name.so.*
%exclude %_libdir/lib*.a

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*
%_man3dir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%if_with hash
%files hash
%_bindir/css*
%_libdir/%name/libhash_drv.so*
%endif #with hash

%if_with sqlite3
%files sqlite3
%_libdir/%name/libsqlite3_drv.so
%_libdir/%name/libsqlite3_drv.so.*
%_datadir/%name-%version/sql/sqlite/*

%endif #with sqlite3

%if_with pgsql
%files pgsql
%_bindir/dspam_pg2int8
%_libdir/%name/libpgsql_drv.so
%_libdir/%name/libpgsql_drv.so.*
%_datadir/%name-%version/sql/pgsql/*
%endif #with pgsql

%if_with mysql
%files mysql
%_libdir/%name/libmysql_drv.so
%_libdir/%name/libmysql_drv.so.*
%_datadir/%name-%version/sql/mysql/*
%endif #with mysql

%files webui
%_datadir/%name-%version/webui/cgi-bin/*.cgi 
%_datadir/%name-%version/webui/cgi-bin/*.pl
%_datadir/%name-%version/webui/cgi-bin/*.prefs
%_datadir/%name-%version/webui/cgi-bin/*.txt
%_datadir/%name-%version/webui/cgi-bin/admins
%_datadir/%name-%version/webui/cgi-bin/templates/*.html
%_datadir/%name-%version/webui/htdocs/base.css
%_datadir/%name-%version/webui/htdocs/dspam-logo-small.gif
%_datadir/%name-%version/dspam.http

%changelog
* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 3.9.0-alt1.beta2.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Fri Sep 18 2009 Aleksey Avdeev <solo@altlinux.ru> 3.9.0-alt1.beta2
- NMU
- 3.9.0-BETA2 build
- Fix dspam.init for use condrestart
- Use logrotate for %%_logdir/%%name/%%name.log (Closes: #13576)
- Set %%config(noreplace) for %%_sysconfdir/cron.daily/%%name-clean

* Thu Aug 20 2009 Alexey Shentzev <ashen@altlinux.ru> 3.9.0-alt1.alpha2
- new version build

* Mon Sep 29 2008 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.9
- add BuildRequires: glibc-devel-static

* Thu Mar 20 2008 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.8
- disable ldap support
- set attribute 750 root:mail on /usr/bin/dspam
- add changes train.pl from http://devnull.com/kyler/dspam.20040512.html

* Fri Feb 01 2008 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.7
- fix bug #13576 
- bug #13575 is invalid, ignored
- build with --enable-ldap, --enable-syslog, --with-logfile=%_logdir/%name/%name.log

* Tue Dec 04 2007 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.5
- modify file locations and persmissions
- add default configuration file
- change dspam-clean
- add dspam_corpus from dspam 3.6.x
- thanks Eugene Prokopiev <enp@altlinux.ru> for help

* Thu Aug 30 2007 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.4
- closed bugs #12112, #11228, #11243, #7531 of https: // bugzilla.altlinux.org/

* Mon Aug 27 2007 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.3
- add init-scripts, thanks enp@altlinux.ru
- add documentation, sql-scripts for sqlite, postgresql, mysql

* Tue Aug 07 2007 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.2
- fixx BuildRequires

* Sun May 20 2007 Alexey Shentzev <ashen@altlinux.ru> 3.8.0-alt1.1
- new version build
- fix build with --as-needed
- build with --enable-clam options
- thanks Vyacheslav Dubrovsky <slava@tangramltd.com> for the help

* Wed Dec 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 3.6.8-alt1
- return from orphaned
- new version 3.6.8
- fix build with --as-needed

* Sat Dec 10 2005 Ivan Fedorov <ns@altlinux.ru> 3.6.2-alt1
- 3.6.2
- fixed #7531

* Thu Sep 15 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.9-alt2
- add virtual users support to mysql and pgsql drivers

* Tue Aug 09 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.9-alt1
- 3.4.9

* Fri Jul 22 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.8-alt1
- 3.4.8
- Fix #7247

* Sun May 15 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.6-alt1
- 3.4.6

* Fri Apr 29 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.0-alt3
- Rebuilt with postgresql 8.0

* Sat Apr 09 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.0-alt1
- Spec rewritten.
- Added alternatives

* Sat Apr 09 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.0-alt0.2
- Enable daemon mode

* Sat Mar 26 2005 Ivan Fedorov <ns@altlinux.ru> 3.4.0-alt0.1
- 3.4.0

* Fri Jan 07 2005 Ivan Fedorov <ns@altlinux.ru> 3.2.3-alt0.1
- Initial build
