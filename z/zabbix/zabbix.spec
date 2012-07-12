%define zabbix_user	zabbix
%define zabbix_group	zabbix
%define	zabbix_home	/dev/null
%define svnrev 16759

%def_with pgsql

Name: zabbix
Version: 1.8.12
Release: alt2.prerc1
#Release: alt1.svn.%svnrev.1

Serial: 1

Summary: A network monitor
License: GPL
Group: Monitoring

Url: http://www.zabbix.com

# http://heanet.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.gz
Source0: %name-%version.tar

BuildPreReq: /proc
BuildPreReq: libelf-devel
BuildRequires(pre): rpm-build-webserver-common

# Automatically added by buildreq on Fri Feb 27 2009 (-bi)
BuildRequires: libMySQL-devel libcurl-devel libiksemel-devel libldap-devel libnet-snmp-devel libsqlite3-devel perl-Switch libopenipmi-devel

%if_with pgsql
BuildRequires: postgresql-devel
%endif

%package common
Summary: %name network monitor (common stuff)
Group: Monitoring
Provides: %_sysconfdir/%name
Provides: %_logdir/%name
BuildArch: noarch

%package server-common
Summary: %name network monitor (server common stuff)
Group: Monitoring
Requires: %_sysconfdir/%name
Requires: %_logdir/%name

%package server-mysql
Summary: %name network monitor (server, compiled with MySQL support)
Group: Monitoring
Requires: %name-server-common = %serial:%version-%release
Requires: %_sbindir/fping
Obsoletes: %name-mysql < 1:1.1.7-alt1

%if_with pgsql
%package server-pgsql
Summary: %name network monitor (server, compiled with PostgreSQL support)
Group: Monitoring
Requires: %name-server-common = %serial:%version-%release
Requires: %_sbindir/fping
Obsoletes: %name-pgsql < 1:1.1.7-alt1
%endif

%package agent
Summary: %name agent
Group: Monitoring
Requires: %_sysconfdir/%name
Requires: %_logdir/%name

%package agent-sudo
Summary: sudo entry for %name agent
Group: Monitoring
BuildArch: noarch
Requires: %name-agent

%package proxy
Summary: %name proxy
Group: Monitoring
Requires: %_sysconfdir/%name
Requires: %_logdir/%name
Requires: %_sbindir/fping

%package phpfrontend-engine
Summary: zabbix web frontend (php)
Group: Monitoring
Requires: php-engine
Obsoletes: %name-phpfrontend < 1:1.1.7-alt1
BuildArch: noarch

%package phpfrontend-php5
Summary: zabbix web frontend, edition for php5
Group: Monitoring
Requires: php5-gd2 php5-mysql php5-pgsql php5-sockets php5-mbstring php5-dom
BuildArch: noarch

%package phpfrontend-apache
Summary: %name-phpfrontend's apache config files
Group: Monitoring
Requires: %name-phpfrontend-engine = %serial:%version-%release, apache-base
BuildArch: noarch

%package phpfrontend-apache2
Summary: %name-phpfrontend's apache2 config files
Group: Monitoring
Requires: %name-phpfrontend-engine = %serial:%version-%release, apache2-base
BuildArch: noarch

%package phpfrontend-apache2-mod_php5
Summary: Requirements for the use of apache2-mod_php5
Group: Monitoring
Requires: %name-phpfrontend-apache2
Requires: apache2-httpd-prefork-like
Requires: apache2-mod_php5
BuildArch: noarch

%package doc
Summary: %name network monitor documentation (README, ChangeLog, Manual)
Group: Monitoring
BuildArch: noarch

%package contrib
Summary: %name network monitor (additional scripts)
Group: Monitoring
BuildArch: noarch

%description
ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description common
Common files and docs for zabbix network monitor

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description server-common
common stuff for zabbix server

%description server-mysql
zabbix server, compiled with MySQL support

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%if_with pgsql
%description server-pgsql
zabbix server, compiled with PostgreSQL support
%endif

%description proxy
zabbix network monitor proxy daemon.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description agent
zabbix network monitor agent.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%description agent-sudo
Sudo entry for zabbix agent.

%description phpfrontend-apache
zabbix's apache config files

%description phpfrontend-apache2
zabbix's apache2 config files

%description phpfrontend-apache2-mod_php5
Contains requirements for the use of apache2-mod_php5
in to zabbix phpfrontend

%description phpfrontend-engine
a php frontend for zabbix - core

%description phpfrontend-php5
zabbix web frontend, edition for php5

%description doc
%name network monitor (README, ChangeLog)

%description contrib
%name network monitor (additional scripts)

%prep
%setup

%build
# fix ZABBIX_REVISION
sed -i -e "s,{ZABBIX_REVISION},%svnrev," include/common.h

%autoreconf

# we must call this for produce dbsync.h
pushd create/schema
./gen.pl c >../../include/dbsync.h
popd

%configure --with-mysql \
	--with-net-snmp \
	--enable-server \
	--enable-ipv6 \
	--with-ldap \
	--with-libcurl \
	--with-jabber \
	--with-openipmi
%make dbschema
%make

mv src/%{name}_server/%{name}_server src/%{name}_server/%{name}_mysql
%make clean

%if_with pgsql
%configure --with-pgsql \
	--with-net-snmp \
	--enable-server \
	--enable-ipv6 \
	--with-ldap \
	--with-libcurl \
	--with-jabber \
	--with-openipmi
%make dbschema
%make

mv src/%{name}_server/%{name}_server src/%{name}_server/%{name}_pgsql
%make clean
%endif

%configure --with-sqlite3 \
	--enable-proxy \
	--enable-ipv6 \
	--with-libcurl \
	--with-net-snmp \
	--with-ldap \
	--enable-agent \
	--with-jabber \
	--with-openipmi
%make

# create database upgrades
pushd upgrades
mkdir dbpatches-final
%make dist-hook distdir=dbpatches-final
popd

# adjust in several files /home/zabbix
find misc/conf -type f -print0 | xargs -0 sed -i \
	-e "s,/home/zabbix/bin,/usr/sbin,g" \
	-e "s,PidFile=/tmp,PidFile=%_var/run/zabbix,g" \
	-e "s,LogFile=/tmp,LogFile=%_logdir/zabbix,g" \
	-e "s,/home/zabbix/lock,%_var/lock/subsys/zabbix,g" \
	-e "s,/tmp/mysql.sock,%_localstatedir/mysql/mysql.sock,g" --

%install
%makeinstall

# create directory structure
install -dm1775 %buildroot%_logdir/%name
install -dm0755 %buildroot%_sbindir
install -dm0750 %buildroot%_sysconfdir/%name
install -dm0750 %buildroot%_sysconfdir/%name/zabbix_agentd.conf.d
install -dm0755 %buildroot%webserver_webappsdir/%name

# binaries
install -m0755 src/%{name}_*/%{name}_{mysql,agentd} %buildroot%_sbindir
%if_with pgsql
install -m0755 src/%{name}_server/%{name}_pgsql %buildroot%_sbindir
%endif

# conf files
install -m0640 misc/conf/%{name}_{server,agentd,proxy}.conf %buildroot%_sysconfdir/%name
#install -m0640 misc/conf/%{name}_agentd/userparameter_{examples,mysql}.conf %buildroot%_sysconfdir/%name

# frontends
cp -r frontends %buildroot%webserver_webappsdir/%name/

# apache config
install -pDm0644 sources/%name.conf %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

# apache2 config
install -pDm0644 sources/%name.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

# start scripts
install -pDm0755 sources/%{name}_agentd.init %buildroot%_initdir/%{name}_agentd
install -pDm0755 sources/%{name}_mysql.init %buildroot%_initdir/%{name}_mysql
%if_with pgsql
install -pDm0755 sources/%{name}_pgsql.init %buildroot%_initdir/%{name}_pgsql
%endif
install -pDm0644 sources/zabbix_server %buildroot%_sysconfdir/sysconfig/zabbix_server
install -pDm0755 sources/%{name}_proxy.init %buildroot%_initdir/%{name}_proxy

# migrator
install -m0755 sources/zabbix.migrate.sh migrate.sh

# sudo entry
install -pDm0400 sources/%name.sudo %buildroot%_sysconfdir/sudoers.d/%name

# database upgrades
mkdir -p upgrades-{mysql,postgresql}
mv upgrades/dbpatches-final/dbpatches/1.6/mysql upgrades-mysql/1.6
mv upgrades/dbpatches-final/dbpatches/1.8/mysql upgrades-mysql/1.8
mv upgrades/dbpatches-final/dbpatches/1.6/postgresql upgrades-postgresql/1.6
mv upgrades/dbpatches-final/dbpatches/1.8/postgresql upgrades-postgresql/1.8

# UPGRADING
cp sources/UPGRADING.ALT .

# ChangeLog
bzip2 ChangeLog

%pre common
/usr/sbin/groupadd -r -f %zabbix_group ||:
/usr/sbin/useradd -g %zabbix_group -G proc -c 'Zabbix' \
	-d %zabbix_home -s /dev/null -r %zabbix_user >/dev/null 2>&1 ||:

%post server-mysql
%post_service zabbix_mysql

%preun server-mysql
%preun_service zabbix_mysql

%if_with pgsql
%post server-pgsql
%post_service zabbix_pgsql

%preun server-pgsql
%preun_service zabbix_pgsql
%endif

%post proxy
%post_service zabbix_proxy

%preun proxy
%preun_service zabbix_proxy

%post agent
%post_service zabbix_agentd
if [ $1 -eq 1 ]; then
	sed -i -e "s,Hostname=Zabbix server,Hostname=$HOSTNAME,g" \
	%_sysconfdir/%name/%{name}_agentd.conf
fi

%post agent-sudo
if [ $1 -eq 1 ]; then
	gpasswd -a %zabbix_user wheel
fi

%preun agent
%preun_service zabbix_agentd

%post phpfrontend-apache
%_initdir/httpd reload >/dev/null 2>&1 ||:

%postun phpfrontend-apache
%_initdir/httpd reload >/dev/null 2>&1 ||:

%post phpfrontend-apache2
%_initdir/httpd2 reload >/dev/null 2>&1 ||:

%postun phpfrontend-apache2
%_initdir/httpd2 reload >/dev/null 2>&1 ||:

%files common
%dir %attr(1775,root,%zabbix_group) %_logdir/%name
%dir %_sysconfdir/%name

%files server-common
%_bindir/%{name}_get
%config(noreplace) %_sysconfdir/sysconfig/zabbix_server
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_server.conf
%_man1dir/%{name}_get.*

%files server-mysql
%_sbindir/%{name}_mysql
%_initdir/%{name}_mysql
%doc create/schema/mysql.sql create/data/data.sql create/data/images_mysql.sql
%doc upgrades-mysql
%doc UPGRADING.ALT

%if_with pgsql
%files server-pgsql
%_sbindir/%{name}_pgsql
%_initdir/%{name}_pgsql
%doc create/schema/postgresql.sql create/data/data.sql create/data/images_pgsql.sql
%doc upgrades-postgresql
%doc UPGRADING.ALT
%endif

%files proxy
%_sbindir/%{name}_proxy
%_initdir/%{name}_proxy
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_proxy.conf
%_man8dir/%{name}_proxy.*

%files agent
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_agentd.conf
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/%name/zabbix_agentd.conf.d
%_initdir/%{name}_agentd
%_sbindir/%{name}_agentd
%_bindir/%{name}_sender
%_man8dir/%{name}_agentd.*
%_man1dir/%{name}_sender.*
%exclude %_sbindir/%{name}_agent

%files agent-sudo
%config(noreplace) %attr(0400,root,root) %_sysconfdir/sudoers.d/%name

%files phpfrontend-engine
%webserver_webappsdir/%name
%exclude %webserver_webappsdir/%name/frontends/php/conf/COPYING

%files phpfrontend-php5

%files phpfrontend-apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files phpfrontend-apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%files phpfrontend-apache2-mod_php5

%files doc
%doc AUTHORS NEWS README UPGRADING.ALT INSTALL ChangeLog.bz2

%files contrib
%doc misc/snmptrap/* migrate.sh

%changelog
* Thu Jul 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.8.12-alt2.prerc1
- move sudo config to /etc/sudoers.d

* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.12-alt1.prerc1
- Update to 1.8.12 pre-rc1 (Closes: #26865).
- Revert e54e00bf8c2bcee6659222d2beee7cace69749c0 (buggy).
- Revert solo@ patches (need rediff):
  + db343c66258f4e6738e9df1c0888774b0fa3f397
  + 04887ca7ba0e4433ab398e2ee4700f9ee3640f28
  + 94e0757eeb1fb25c66d7562164e7f48560c7765f
  + f9d9e34c96212ce0c14bf315525225a0ef76038f
  + d5eebe23f9c596b30468ce3b27bd2b62b074292d
  + e8105b55f4e8797a3dd9d1ad9e205885e54fe122
  + e947d0e6601b5c52010d68974452c5e2c2507df2
  + 168d58665ead31efd018492ab86a0aeeb3596573
  + f94ee213a79f9a6a93aeb631d8981a0688e7521a

* Wed Jan 12 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.5-alt1.rc1
- Update to 1.8.5 rc1.

* Tue Nov 23 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.4-alt3.rc2
- Update to 1.8.4 rc2+, rev 15637.
- Introduce zabbix-agent-sudo subpackage.

* Tue Nov 09 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.4-alt2.rc2
- Update to 1.8.4 rc2+, rev 15345.
- phpfrontend: fix maps display when using postgresql9.

* Mon Oct 25 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.4-alt1.rc2
- Update to 1.8.4 rc2.
- zabbix_proxy, zabbix_server: fix default interface binding behavior.
- Drop previously introduced patch for not showing triggers with unknown
  state on the map (needs to be rediffed / reviewed).
- Package upstream ChangeLog into -doc subpackage.

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt2.svn.13936.1
- Fix priority triggers an unknown state (thanks manowar@). (Closes: #24289)

* Thu Oct 07 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.3-alt2.svn.13936
- zabbix_agentd: fix default interface binding behavior.
- Fix updating default Hostname in zabbix_agentd.conf

* Fri Sep 10 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt1.svn.13936.3
- Added missing requires for phpfrontend (php-dom).

* Tue Sep 07 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt1.svn.13936.2
- Set requires apache*-base for to phpfrontend-apache* subpackages.
- Add phpfrontend-apache2-mod_php5 subpackage

* Wed Sep 01 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt1.svn.13936.1
- Update to 13936 svn rev. of 1.8.3 tag.

* Sun Aug 15 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc4.svn.13927.1
- Update to 13927 svn rev. of 1.8 branch.

* Fri Aug 06 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc3.svn.13816.1
- Fixed problem of implicit cast with PostgreSQL 8.3
  (thanks to Fernando Ike de Oliveira). (Closes: ZBX-416,ZBX-986)

* Fri Aug 06 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc2.svn.13687.4
- Fixed calculated items using.

* Fri Jul 30 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc2.svn.13687.3
- Update to 13687 svn rev. of 1.8 branch.
- Fixed undefined variable config[...] in many forms. (Fixed upstream
  in rev:13675, see ZBX-2783)
- Fixed allow reading files with dots from zabbix_agentd.conf.d (thanks vvk@).

* Thu Jul 29 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc2.svn.13659.1
- Update to 13659 svn rev. of 1.8 branch.

* Sat Jul 24 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.3-alt0.rc1.svn.13556.1
- Update to 13556 svn rev. of 1.8 branch.

* Thu Jul 08 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.2-alt1.svn.11296.1
- Add the ability to use the item children nodes as arguments of functions
  computed items on the master. (Closes: ZBXNEXT-451)
- Fixed return the empty string as the hostname when parsing.
  (Closes: ZBX-2751)

* Mon Apr 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.2-alt1.svn.11296
- Update to 11296 svn rev. of 1.8 branch.
- Security fix: CVE-2010-1144 Zabbix PHP Frontend "user" SQL Injection
  Vulnerability. See http://secunia.com/advisories/39119/ for datails.
- Enable ipv6 support.

* Fri Mar 19 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.1-alt1.svn.10921
- Update to 10921 svn rev. of 1.8 branch.
- Add BuildPreReq: libelf-devel.
- Use on file Provides/Requires for %%name-common subpackages.
- Use on file Requires %%_sbindir/fping in server and proxy subpackages.

* Wed Mar 17 2010 Aleksey Avdeev <solo@altlinux.ru> 1:1.8.1-alt1.svn.10892
- Update to 10892 svn rev. of 1.8 branch.

* Fri Mar 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8.1-alt1.svn.10592
- Update to 10592 svn rev. of 1.8 branch (Closes: #23064).
- Enable openipmi support.

* Tue Jan 12 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8-alt1.svn.9232
- Update to 9232 svn rev. of 1.8 branch.

* Thu Dec 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.8-alt1.svn.8618
- Update to 8618 svn rev. of 1.8 branch.
- Add UPGRADING.ALT.
- Do not package /var/run/zabbix. It's created from initscripts now.
- Add dependency on fping in server and proxy subpackages.

* Wed Dec 09 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.8-alt1.svn.8544
- 1.6.8 release.

* Thu Dec 03 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.7-alt1.svn.8427
- Updated to 8427 svn rev. of 1.6 branch.
- Allow reading files with dots from /etc/zabbix/zabbix_agentd.conf.d/
- Change Group to Monitoring.
- Add hack for setting ZABBIX_REVISION.

* Thu Oct 29 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.6-alt1.svn.8136
- Updated to 8136 svn rev. of 1.6 branch. Security fixes:
  + [ZBX-1031] fixed security vulnerability in server, allowing remote
  unauthenticated users to execute arbitrary SQL queries. Thanks to
  Nicob (Sasha).

* Thu Aug 20 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.5-alt1.svn.7782
- Updated to 7782 svn rev. of 1.6 branch

* Fri Jun 05 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.4-alt1.svn.7369
- Updated to 7369 svn rev. of 1.6 branch

* Wed May 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.4-alt1.svn.7269
- Updated to 7269 svn rev. of 1.6 branch
- Supress output of apache reloads at post stage of -phpfrontend-apache{2}

* Thu Apr 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.4-alt1.svn.7186
- Updated to 7186 svn rev. of 1.6 branch
- Add dependency on php5-sockets in phpfrontend subpackage

* Fri Feb 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.2-alt1.svn.6838
- Updated to 6838 svn rev. of 1.6 branch
- Added /etc/zabbix/zabbix_agentd.conf.d support (thresh) (Closes: #13182)
- Build zabbix-proxy with sqlite support (Closes: #18980)

* Tue Dec 16 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.1-alt1.svn.6455
- Updated to 6455 rev of 1.6 branch
- Disabled ipv6 support

* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.1-alt1.svn.6431
- Updated to 6431 rev of 1.6 branch
- Dropped php4 subpackage
- Package some subpackages as noarch (doc, contrib, frontend)

* Thu Nov 06 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6.1-alt1.svn.6254
- Updated to 6254 rev of 1.6 branch

* Tue Oct 28 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6-alt2.svn.6212
- Fixed sql-upgrades packaging (reported by hiddenman)

* Thu Oct 23 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6-alt1.svn.6212
- Updated to 6212 rev of 1.6 branch

* Thu Sep 25 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1:1.6-alt1.svn.6080
- Updated to 6080 rev of 1.6 branch
- Added zabbix-proxy subpackage
- Web frontend packaging corrected according to WebPolicy
- Dropped third-party patches not merged by upstream

* Thu Apr 10 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.4.5-alt1
- 1.4.5 release

* Fri Jan 18 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.4.4-alt1
- 1.4.4 release

* Wed Dec 05 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.4.2-alt2.svn.5128
- Security fix: CVE-2007-6210
- Updated to 5128 rev of refs/remotes/1.4

* Tue Aug 21 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.4.2-alt1
- 1.4.2 release
- Implemented sysconfig file for have ability to pass startup arguments to
  zabbix server
- Package docs directory (contains zabbix manual in pdf format)
- Drop some phpfrontend patches, not included by upstream
- Enable jabber support
- Apply two patches from sauron:
  + zabbix-sms.fix - fix infinite waith read loop at zero step in SMS sender
  + zabbix-jabber.fix - fix working with Openfire

* Tue Apr 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.7-alt1
- 1.1.7
- Split phpfrontend to 3 parts:
  + phpfrontend-engine
  + phpfrontend-php4
  + phpfrontend-php5
- Separate common part of zabix-{my,pg}sql packages to zabix-server-common
- Rename zabix-{my,pg}sql to zabbix-server-{my,pg}sql
- Use %%preun_service, don't %%post_service in %%preun zabbix-server-pgsql
  (bugfix)
- Set Hostname to $HOSTNAME in agentd config after first package install
  (suggested by Konstantin Pavlov <thresh@altlinux>)
- Better drop /proc/XXX-avaibility checks at build-time
- Add russian translation from Andrew Kornilov <hiddenman@altlinux>
- Add phpfrontend-apache2 subpackage
- Switch to use .gear-tags

* Mon Feb 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.6-alt1
- 1.1.6

* Tue Jan 30 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.5-alt1
- 1.1.5

* Fri Jan 12 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.4-alt3
- Added some useful patches:
  + Create trigger button on item form, see
  http://www.zabbix.com/forum/showthread.php?t=4858
  + Add Hostname Colum To Trigger Status Page, see
  http://www.zabbix.com/forum/showthread.php?t=4912
  + Add hyperlinks to the Monitoring/Overview page
    + secondary sort by hosts (the primary sort order is still by trigger, but
    hosts with the same triggers are sorted alphabetically now)
    + clicking on one of the (vertical) hostnames will take you to the latest data
    obtained from this host
    + clicking on a (green or red) field in the matrix will take you to the
    simple graph of this data item
  see http://www.zabbix.com/forum/showthread.php?t=4105
  + Variable {ITEM.NAME} for alert messages, see
  http://www.zabbix.com/forum/showthread.php?t=4806

* Wed Dec 13 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.4-alt2
- Reworked subpackaging schema (Closes: #10400):
  + Move .sql-files for MySQL into %name-mysql package
  + Move .sql-files for PostgreSQL into %name-pgsql package
  + Move contrib-scripts into %name-contrib
  + Move win32 agent into %name-contrib-agent-win32
  + Move win64 agent into %name-contrib-agent-win64
- Integrate these patches into source-tree:
  + zabbix-1.1.1-alt-config.h.chroot_build.patch
  + zabbix-1.1.2-alt-daemon.patch
  + zabbix-1.1.2-alt-diskio.c_kernelcheck.patch
  + zabbix-1.1beta9-alt-check_alive_zabbix_mysql.patch
- Temporary remove dependency on php-gd2 because of bug #10401, be close,
  don't forget to install php-gd2/php5-gd2 by hand
- Rebuild with new libnetsnmp

* Wed Nov 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.4-alt1
- 1.1.4
- Removed zabbix-1.1.3-deb-delta.patch (merged upstream)
- Enabled PostgreSQL support

* Mon Nov 13 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.3-alt1
- 1.1.3
- Removed patches (merged upstream)
  + zabbix-1.1.2-deb-security.patch
  + zabbix-1.1.2-deb-expression.c.patch
  + zabbix-1.1.2-deb-maps.inc.php.patch
  + zabbix-1.1.2-deb-data.sql.patch
- Fix delta problem, see: http://www.zabbix.com/forum/showthread.php?t=4315
  (patch from Debian, zabbix-1.1.3-deb-delta.patch)
- Removed warning-message about "need database upgrade"
- Enhanced initscript of zabbix_agentd also (stale pidfile removing)

* Tue Oct 10 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.2-alt3
- Added zabbix-1.1.2-deb-security.patch for fix security issues discovered by
  the debian-audit project (Debian bug #391388) (Secunia Advisory 22313)
- Added zabbix-1.1.2-deb-expression.c.patch for fix substitution of variables
  in action e-mails, see: http://www.zabbix.com/forum/showthread.php?t=3969
- Added zabbix-1.1.2-deb-maps.inc.php.patch for fix reversed icons issue, see:
  http://www.zabbix.com/forum/showthread.php?t=3986
  http://www.zabbix.com/forum/showthread.php?t=3979
- Added zabbix-1.1.2-deb-data.sql.patch for fix login problem if
  http://localhost/ is used, see
  http://www.zabbix.com/forum/showthread.php?t=4033

* Tue Oct 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.2-alt2
- Added zabbix-1.1.2-alt-daemon.patch for fix handling of file descriptors
  (suggested by hiddenman@)

* Thu Sep 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.2-alt1
- 1.1.2
- zabbix-1.1beta7-alt-diskio.c_kernelcheck.patch rediffed and renamed to
  zabbix-1.1.2-alt-diskio.c_kernelcheck.patch

* Mon Jul 24 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1:1.1.1-alt1
- 1.1.1 release
- Added Serial tag
- Added again zabbix-1.1.1-alt-config.h.chroot_build.patch for disable some
  checks at build-time
- Improved server initscript - added autoremoving of stale pidfile

* Tue Jun 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1rel-alt1
- 1.1 release

* Thu May 04 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta9-alt3
- useradd,groupadd actions moved to %%pre common (reported by hiddenman@)

* Thu Apr 27 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta9-alt2
- Add zabbix-1.1beta9-alt-check_alive_zabbix_mysql.patch for fix wrong name of
  zabbix daemon in phpfrontend (reported by hiddenman@)
- In apache's config AllowOverride directive has been changed from "None" to
  "AuthConfig Limit" (FR by hiddenman@)

* Wed Apr 26 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta9-alt1
- new version (1.1beta9)

* Mon Apr 17 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta8-alt2
- Add migrate.sh script

* Tue Apr 04 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta8-alt1
- Beta 8
- Removed unneeded README.ALT.1
- Added zabbix-1.1beta7-alt-diskio.c_kernelcheck.patch for realtime checking
  of kernel version instead of compilation time
- SQL-data moved to -doc subpackage
- Updated Summary and Description
- Removed zabbix-config.h.in.chroot.patch
- Added /proc to BuildPreReq
- Corrected Requires of subpackages
- Do not use some macros in spec anymore (%%__install, %%__mv)
- Add zabbix pseudouser to 'proc' group

* Fri Dec 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1beta2-alt2.1
- rebuild with libnetsnmp.so.9

* Tue Nov 22 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta2-alt2
- Added missing requires for phpfrontend (php-engine, php-gd2)
- File db.inc.php now packaged as %%config(noreplace) (thanks to hiddenman@ :)
  )
- Package %name-phpfrontend splitted (Closes #8324)
- Changed permissions of /var/log/zabbix/ and /var/run/zabbix due to ALT
  security policy
- Corrected default path to mysql.sock
- Common stuff moved to -common package
- Added zabbix-config.h.in.chroot.patch for disabling some checks in chroot
  (thanks to lakostis@)
- Updated create/data/README.ALT
- Minor spec update

* Wed Oct 19 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta2-alt1
- New version.
- PostgreSQL support still disabled.
- Packaged zabbix_get utility.

* Wed Sep 21 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1beta1-alt1
- New version.
- PostgreSQL support temporary disabled.
- Removed COPYING from package.
- Packaged snmptrap.sh script and agent W32binary.
- Added README.ALT to /usr/share/doc/.../create/data
- fixed package ownership of /etc/%name
- changed permissions of config-files.

* Sat Sep 03 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1alpha10-alt1
- Initial build for Sisyphus.
