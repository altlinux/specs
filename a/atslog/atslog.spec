%define svn 688
Name: atslog
Version: 2.2.0
Release: alt3.svn%svn
Epoch: 1

Summary: Daemon for collecting info about calls from various types of PBX models. 
Summary(ru_RU.UTF-8): Сервис для сбора информации о звонках с различных типов мини-АТС
License: GPL
Group: System/Servers

URL: http://www.atslog.com
Source: http://download.berlios.de/atslog/%name-%version.tar.gz
Source2: atslogweb.conf
Source3: atsloginit

BuildRequires: libwrap-devel perl-DBI-devel perl-DBD-mysql perl-DBD-Pg
Requires: libwrap
Requires: %name-config


%define atsloginit atslog
%define apache_home %_var/www/html
%define apache_confdir %_sysconfdir/httpd/conf
%define apache_addonconfdir %apache_confdir/addon-modules.d

%description
%name -- daemon for collecting info about calls from various types of PBX (Private Branch eXchange) models and store them into the MySQL or PostgreSQL database.
You can use %name-web to analyse calls via handy and flexible web interface.

%description -l ru_RU.UTF-8
%name -- сервис для сбора информации о звонках с различных типов мини-АТС и сохранения
их в базе данных MySQL или PostgreSQL

%package mysql
Summary: MySQL backend for the %name to store info about calls
Summary(ru_RU.UTF8): Пакет добавляет в %name поддержку баз даных MySQL в качестве хранилища информации о звонках
Group: System/Servers
Requires: perl-DBD-mysql
Conflicts: %name-pgsql
Provides: %name-config

%description mysql
MySQL backend for the %name to store info about calls

%description mysql -l ru_RU.UTF-8
Пакет добавляет в %name поддержку баз даных MySQL в качестве хранилища информации о звонках


%package pgsql
Summary: PostgreSQL backend for the %name to store info about calls
Summary(ru_RU.UTF8): Пакет добавляет в %name поддержку баз даных PostgreSQL в качестве хранилища информации о звонках
Group: System/Servers
Requires: perl-DBD-Pg
Conflicts: %name-mysql
Provides: %name-config

%description pgsql
PostgreSQL backend for the %name to store info about calls

%description pgsql -l ru_RU.UTF-8
Пакет добавляет в %name поддержку баз даных PostgreSQL в качестве хранилища информации о звонках

# -- Web interface--
%package web
Summary: Handy and flexible web interface for analysing info about calls and adminstration of the %name
License: GPL
Group: Networking/WWW
Requires: webserver
Requires: %name-web-config
Obsoletes: atslogweb <= 2.0.78

%description web
%name-web provides a handy and flexible web interface for viewing and analysing
calls info collected by %name

%description web -l ru_RU.UTF-8
%name-web предоставляет удобный и гибкий web интерфейс для просмотра и анализа
информации о звонках, собранной с помощью %name

%package web-mysql
Summary: MySQL support for the %name-web to analyse info about calls
Summary(ru_RU.UTF8): Пакет добавляет в %name-web поддержку баз даных MySQL для анализа информации о звонках
Group: Networking/WWW
Requires: php5-mysql
Requires: %name-web
Conflicts: %name-web-pgsql
Provides: %name-web-config

%description web-mysql
MySQL support for the %name-web to analyse info about calls

%description web-mysql -l ru_RU.UTF-8
Пакет добавляет в %name-web поддержку баз даных MySQL для анализа информации о звонках

%package web-pgsql
Summary: PostgreSQL support for the %name-web to analyse info about calls
Summary(ru_RU.UTF8): Пакет добавляет в %name-web поддержку баз даных PostgreSQL для анализа информации о звонках
Group: Networking/WWW
Requires: php5-pgsql
Requires: %name-web
Conflicts: %name-web-mysql
Provides: %name-web-config

%description web-pgsql
PostgreSQL support for the %name-web to analyse info about calls

%description web-pgsql -l ru_RU.UTF-8
Пакет добавляет в %name-web поддержку баз даных PostgreSQL для анализа информации о звонках


%prep
%setup -n %name-%version

# fix perms
find %_builddir/%name-%version/www -type d -print0 | xargs -r0 chmod 755
find %_builddir/%name-%version/www -type f -print0 | xargs -r0 chmod 644
# fix logdir
##find %_builddir/%name-%version -type f -print0 | xargs -r0 sed -i "s|@localstatedir@/log|@localstatedir@/log/atslog|g"

%build
%autoreconf
%configure --localstatedir=%_var --with-wwwroot=%apache_home
%make_build

%install
%make_install install DESTDIR=%buildroot

# install init
install -pD -T -m 755 %SOURCE3 %buildroot%_initdir/%atsloginit

# install web config
install -pD -m640 %SOURCE2 %buildroot%apache_addonconfdir/atslogweb.conf
	
# install cron
mkdir -p %buildroot%_sysconfdir/cron.daily
cat << EOF > %buildroot%_sysconfdir/cron.daily/atslog
#!/bin/sh
/usr/bin/atslogmaster writedb
EOF
mkdir -p %buildroot%_sysconfdir/cron.monthly
cat << EOF > %buildroot%_sysconfdir/cron.monthly/atslog
#!/bin/sh
/usr/bin/atslogmaster rotate
EOF

# install sql data
mkdir -p %buildroot%_datadir/%name/sql
install -pD -m 644 data/sql/[^A-Z]* %buildroot%_datadir/%name/sql
install -p -m 644 data/textlogs/* %buildroot%_datadir/%name/

%post
%post_service %atsloginit

%preun
%preun_service %atsloginit

%post mysql
sed -i "s|sqltype=PostgreSQL|sqltype=MySQL|g" %_sysconfdir/%name.conf

%post pgsql
sed -i "s|sqltype=MySQL|sqltype=PostgreSQL|g" %_sysconfdir/%name.conf


%pre web
if [[ -e %apache_home/atslog/include/set/conf.inc.php ]]; then
    mv -u %apache_home/atslog/include/set/conf.inc.php %apache_home/atslog/include/config.inc.php
    echo "Config move from %apache_home/atslog/include/set/conf.inc.php  to %apache_home/atslog/include/config.inc.php"
fi

%post web
/sbin/service httpd reload ||:

%post web-mysql
sed -i "s|sqltype='pgsql'|sqltype='mysql'|g" %apache_home/atslog/include/config.inc.php

%post web-pgsql
sed -i "s|sqltype='mysql'|sqltype='pgsql'|g" %apache_home/atslog/include/config.inc.php
				
%files
%_bindir/*
%_libexecdir/%name
%config %_initrddir/%name
%attr(0755,root,root) %config %_sysconfdir/cron.daily/*
%attr(0755,root,root) %config %_sysconfdir/cron.monthly/*

%_datadir/%name
%exclude %_datadir/%name/sql/createsqltables*

%doc CHANGES DEINSTALL INSTALL UPDATING USAGE ChangeLog
%doc atslogd/api.draft.txt
%doc include/{atslog.conf.default,atslog.conf.default.rus}
%_man8dir/atslog*
%_mandir/ru/*/*
%dir %_mandir/ru/
%dir %_mandir/ru/man8

%attr(3770,root,root) %_logdir/%name

%files mysql
%_datadir/%name/sql/*.mysql.*
%dir %_datadir/%name
%dir %_datadir/%name/sql
%config(noreplace) %_sysconfdir/%name.conf

%files pgsql
%_datadir/%name/sql/*.Pg.*
%dir %_datadir/%name
%dir %_datadir/%name/sql
%config(noreplace) %_sysconfdir/%name.conf

%files web
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/atslogweb.conf
%apache_home/atslog
%exclude %apache_home/atslog/include/config.inc.php

%files web-mysql
%config(noreplace) %attr(0640,root,apache) %apache_home/atslog/include/config.inc.php

%files web-pgsql
%config(noreplace) %attr(0640,root,apache) %apache_home/atslog/include/config.inc.php

%changelog
* Thu Mar 17 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1:2.2.0-alt3.svn688
- Add filter for avaya PBX
- Cleanup spec
- Avoid post-install unowned files
- Don't use %%post_service for non-own services

* Mon Dec 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1:2.2.0-alt2.svn688
- Fixes for rebuild

* Tue Apr 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 1:2.2.0-alt1.svn688
- Latest SVN version

* Fri Feb 09 2007 Andrew Kornilov <hiddenman@altlinux.ru> 1:2.2.0-alt1.svn648
- Latest version from SVN
- There're some new subpackages now (support PostgreSQL and so on)
- Spec cleanups

* Fri Jan 12 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1:2.0.0-alt0
- New version: release
  + Update spec
  + Add Epoch: 1
  + Remove all patches (in upstream)
  + Add %%__autoreconf
- Rename and replase %apache_home/atslog/include/set/conf.inc.php to 
  %apache_home/atslog/include/config.inc.php in %%pre script

* Thu Dec 28 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0.0pre4-alt1
- Update %atsloginit for new policy (off in level 345)

* Mon Dec 25 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0.0pre4-alt0
- New version: pre4

* Fri Dec 22 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0.0pre3-alt0
- New version: pre3 thanks to Andrew Kornilov (hiddenman@)

* Thu Oct 26 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0-alt4
- Fix "s|decimal(100|decimal(65|g"

* Fri Jun 16 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0-alt3
- New version: pre2 thanks to Andrew Kornilov (hiddenman@)
  + Update spec
  + Remove all patches (in upstream)
  + Add support MySQL 5

* Thu Mar 09 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0-alt2
- Patch3 is added (fix --as-needed)

* Fri Jun 10 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0-alt1
- Patch1 (fix bag #4233) & patch2 (fix bag #4234) is added
- Fix group for config /atslog/include/set/conf.inc

* Thu May 05 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0-alt0
- Update to 2.0
- Buildrequires libwrap-devel perl-DBI is added
- Many bugs are fixed; thanks to Andrew Kornilov (hiddenman@)

* Wed Feb 16 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.4-alt0
- Built for Master 2.4
