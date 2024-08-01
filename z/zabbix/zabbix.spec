%define zabbix_user	zabbix
%define zabbix_group	zabbix
%define zabbix_home	/dev/null
%define svnrev		d1b0c3308ce

%def_with pgsql
%def_enable java
%def_with ssh2
%def_with unixodbc

%def_enable ipv6
%def_enable agent2
%def_enable webservice

%ifndef _unitdir
%define _unitdir %systemd_unitdir
%endif

Name: zabbix
Version: 7.0.2
Release: alt1
Epoch: 1

Summary: A network monitor
License: AGPL-3.0-only
Group: Monitoring

Url: http://www.zabbix.com

# http://heanet.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.gz
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): libelf-devel rpm-build-webserver-common rpm-macros-apache2
%{?_enable_agent2:BuildRequires(pre): rpm-build-golang}
%{?_enable_webservice:BuildRequires(pre): rpm-build-golang}

# Automatically added by buildreq on Thu Nov 02 2017 (-bi)
# optimized out: elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libcom_err-devel libkrb5-devel libnet-snmp30 libp11-kit libpq-devel libsasl2-3 libssl-devel net-snmp-config perl pkg-config python-base python3 rpm-build-python3 xz
BuildRequires: libcurl-devel libelf-devel libevent-devel libiksemel-devel libldap-devel libmysqlclient-devel libnet-snmp-devel libopenipmi-devel libpcre-devel libsqlite3-devel libxml2-devel python3-base
BuildRequires: perl-Switch zlib-devel /proc
%if_with ssh2
BuildRequires: libssh2-devel
%endif
%if_with unixodbc
BuildRequires: libunixODBC-devel
%endif

%{?_enable_java:BuildRequires: java-devel rpm-build-java}

%if_with pgsql
BuildRequires: libpq-devel
%endif

%package common
Summary: %name network monitor (common stuff)
Group: Monitoring
Provides: %_sysconfdir/%name
Provides: %_logdir/%name
BuildArch: noarch

%package common-database-sqlite3
Summary: %name common database stuff (for sqlite3)
Group: Monitoring
BuildArch: noarch

%package common-database-mysql
Summary: %name common database stuff (for mysql)
Group: Monitoring
BuildArch: noarch

%if_with pgsql
%package common-database-pgsql
Summary: %name common database stuff (for postgresql)
Group: Monitoring
BuildArch: noarch
%endif

%package server-common
Summary: %name network monitor (server common stuff)
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1

%package server-mysql
Summary: %name network monitor (server, compiled with MySQL support)
Group: Monitoring
Requires: %name-server-common >= 1:2.0.4-alt1
Requires: %name-common-database-mysql = %EVR
Requires: %_sbindir/fping

%if_with pgsql
%package server-pgsql
Summary: %name network monitor (server, compiled with PostgreSQL support)
Group: Monitoring
Requires: %name-server-common >= 1:2.0.4-alt1
Requires: %name-common-database-pgsql = %EVR
Requires: %_sbindir/fping
%endif

%package agent
Summary: %name agent
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1
Requires: %name-agent-sudo

%if_enabled agent2
%package agent2
Summary: %name agent2
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1
Requires: %name-agent-sudo
%endif

%if_enabled webservice
%package web-service
Summary: %name web service
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1
%endif

%package agent-sudo
Summary: sudo entry for %name agent
Group: Monitoring
BuildArch: noarch
Requires: %name-common >= 1:2.0.4-alt1

%package proxy
Summary: %name proxy with Sqlite3 support
Group: Monitoring
Requires: %name-proxy-common = %EVR
Requires: %name-common-database-sqlite3 = %EVR
Conflicts: %name-proxy-pgsql

%if_with pgsql
%package proxy-pgsql
Summary: %name proxy with PostgreSQL support
Group: Monitoring
Requires: %name-proxy-common = %EVR
Requires: %name-common-database-pgsql = %EVR
Conflicts: %name-proxy
%endif

%package proxy-common
Summary: %name proxy common files
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1
Requires: %_sbindir/fping
BuildArch: noarch

%if_enabled java
%package java-gateway
Summary: %name java gateway
Group: Monitoring
Requires: %name-common >= 1:2.0.4-alt1
Requires: jre-openjdk >= 1.7.0
%filter_from_requires /^\/etc\/sysconfig\/network/d
%filter_from_requires /^\/etc\/sysconfig\/zabbix-java-gateway/d
%endif

%package phpfrontend-engine
Summary: zabbix web frontend (php)
Group: Monitoring
Requires: php-engine
BuildArch: noarch

%package phpfrontend-php8.1
Summary: zabbix web frontend, edition for php8.1
Group: Monitoring
Requires: php8.1-gd php8.1-libs php8.1-mbstring php8.1-mysqli php8.1-openssl php8.1-pgsql php8.1-sockets
Requires: zabbix-phpfrontend-engine = %EVR
BuildArch: noarch

%package phpfrontend-php8.2
Summary: zabbix web frontend, edition for php8.2
Group: Monitoring
Requires: php8.2-gd php8.2-libs php8.2-mbstring php8.2-mysqli php8.2-openssl php8.2-pgsql php8.2-sockets
Requires: zabbix-phpfrontend-engine = %EVR
BuildArch: noarch

%package phpfrontend-php8.3
Summary: zabbix web frontend, edition for php8.3
Group: Monitoring
Requires: php8.3-gd php8.3-libs php8.3-mbstring php8.3-mysqli php8.3-openssl php8.3-pgsql php8.3-sockets
Requires: zabbix-phpfrontend-engine = %EVR
BuildArch: noarch

%package phpfrontend-apache2
Summary: %name-phpfrontend's apache2 config files
Group: Monitoring
Requires: apache2-base
BuildArch: noarch

%package phpfrontend-apache2-mod_php8.1
Summary: Requirements for the use of apache2-mod_php8.1
Group: Monitoring
Requires: %name-phpfrontend-apache2
Requires: apache2-httpd-prefork-like
Requires: apache2-mod_php8.1
BuildArch: noarch

%package phpfrontend-apache2-mod_php8.2
Summary: Requirements for the use of apache2-mod_php8.2
Group: Monitoring
Requires: %name-phpfrontend-apache2
Requires: apache2-httpd-prefork-like
Requires: apache2-mod_php8.2
BuildArch: noarch

%package phpfrontend-apache2-mod_php8.3
Summary: Requirements for the use of apache2-mod_php8.3
Group: Monitoring
Requires: %name-phpfrontend-apache2
Requires: apache2-httpd-prefork-like
Requires: apache2-mod_php8.3
BuildArch: noarch

%package phpfrontend-nginx
Summary: %name-phpfrontend's nginx config files
Group: Monitoring
Requires: nginx
Requires: %name-common
BuildArch: noarch

%package phpfrontend-nginx-php8.1-fpm-fcgi
Summary: Requirements for the use of php8.1-fpm-fcgi
Group: Monitoring
Requires: %name-phpfrontend-nginx
Requires: %name-phpfrontend-php8.1
Requires: php8.1-fpm-fcgi
BuildArch: noarch

%package phpfrontend-nginx-php8.2-fpm-fcgi
Summary: Requirements for the use of php8.2-fpm-fcgi
Group: Monitoring
Requires: %name-phpfrontend-nginx
Requires: %name-phpfrontend-php8.2
Requires: php8.2-fpm-fcgi
BuildArch: noarch

%package phpfrontend-nginx-php8.3-fpm-fcgi
Summary: Requirements for the use of php8.3-fpm-fcgi
Group: Monitoring
Requires: %name-phpfrontend-nginx
Requires: %name-phpfrontend-php8.3
Requires: php8.3-fpm-fcgi

BuildArch: noarch

%package doc
Summary: %name network monitor documentation (README, ChangeLog, Manual)
Group: Monitoring
BuildArch: noarch

%package contrib
Summary: %name network monitor (additional scripts)
Group: Monitoring
BuildArch: noarch

%package source
Summary: %name network monitor (files for zabbix modules)
Group: Development/C
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

%description common-database-sqlite3
common stuff for zabbix sqlite3 databases.

%description common-database-mysql
common stuff for zabbix mysql databases.

%if_with pgsql
%description common-database-pgsql
common stuff for zabbix postgresql databases.
%endif

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

%if_with pgsql
%description proxy-pgsql
zabbix network monitor proxy daemon with PostgreSQL support.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.
%endif

%description proxy-common
zabbix network monitor proxy daemon.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.

%if_enabled java
%description java-gateway
Zabbix java gateway
%endif

%description agent
zabbix network monitor agent.

%if_enabled agent2
%description agent2
zabbix network monitor agent2.

ZABBIX is software for monitoring of your applications, network and servers.
ZABBIX supports both polling and trapping techniques to collect data from
monitored hosts. A flexible notification mechanism allows easy and quickly
configure different types of notifications for pre-defined events.
%endif

%if_enabled webservice
%description web-service
Zabbix web servce for performing various tasks using headless web browser.
%endif

%description agent-sudo
Sudo entry for zabbix agent.

%description phpfrontend-apache2
zabbix's apache2 config files

%description phpfrontend-apache2-mod_php8.1
Contains requirements for the use of apache2-mod_php8.1
in to zabbix phpfrontend

%description phpfrontend-apache2-mod_php8.2
Contains requirements for the use of apache2-mod_php8.2
in to zabbix phpfrontend

%description phpfrontend-apache2-mod_php8.3
Contains requirements for the use of apache2-mod_php8.3
in to zabbix phpfrontend

%description phpfrontend-nginx
zabbix's nginx config files

%description phpfrontend-nginx-php8.1-fpm-fcgi
Contains requirements for the use of php8.1-fpm-fcgi
in to zabbix phpfrontend

%description phpfrontend-nginx-php8.2-fpm-fcgi
Contains requirements for the use of php8.2-fpm-fcgi
in to zabbix phpfrontend

%description phpfrontend-nginx-php8.3-fpm-fcgi
Contains requirements for the use of php8.3-fpm-fcgi
in to zabbix phpfrontend

%description phpfrontend-engine
a php frontend for zabbix - core

%description phpfrontend-php8.1
zabbix web frontend, edition for php8.1

%description phpfrontend-php8.2
zabbix web frontend, edition for php8.2

%description phpfrontend-php8.3
zabbix web frontend, edition for php8.3

%description doc
%name network monitor (README, ChangeLog)

%description contrib
%name network monitor (additional scripts)

%description source
%name network monitor (files for zabbix modules)

%prep
%setup
%patch0 -p1

%build
%ifarch armh
export CFLAGS=-fPIC
%endif
# fix ZABBIX_REVISION
sed -i -e "s,{ZABBIX_REVISION},%svnrev," include/version.h src/zabbix_java/src/com/zabbix/gateway/GeneralInformation.java src/go/pkg/version/version.go

%autoreconf

%configure --with-mysql \
	--with-net-snmp \
	--enable-server \
	%{subst_enable ipv6} \
	--with-ldap \
	--with-libcurl \
	--with-libxml2 \
	--with-openipmi \
	--with-openssl \
	%{subst_with ssh2} \
	%{subst_with unixodbc} \
	--sysconfdir=/etc/zabbix
%make dbschema
%make

mv src/%{name}_server/%{name}_server src/%{name}_server/%{name}_mysql
%make clean

%if_with pgsql
%configure --with-postgresql \
	--with-net-snmp \
	--enable-server \
	%{subst_enable ipv6} \
	--with-ldap \
	--with-libcurl \
	--with-libxml2 \
	--with-openipmi \
	--with-openssl \
	%{subst_with ssh2} \
	%{subst_with unixodbc} \
	--sysconfdir=/etc/zabbix
%make dbschema
%make

mv src/%{name}_server/%{name}_server src/%{name}_server/%{name}_pgsql
%make clean

%configure --with-postgresql \
	--enable-proxy \
	%{subst_enable ipv6} \
	--enable-agent \
	%{subst_enable java} \
	--with-libcurl \
	--with-libxml2 \
	--with-net-snmp \
	--with-ldap \
	--with-openipmi \
	--with-openssl \
	%{subst_with ssh2} \
	%{subst_with unixodbc} \
	--sysconfdir=/etc/zabbix
%make

mv src/%{name}_proxy/%{name}_proxy src/%{name}_proxy/%{name}_proxy_pgsql
%make clean
%endif

export GOFLAGS="-mod=vendor"

%configure --with-sqlite3 \
	--enable-proxy \
	%{subst_enable ipv6} \
	--enable-agent \
	%{subst_enable agent2} \
	%{subst_enable webservice} \
	%{subst_enable java} \
	--with-libcurl \
	--with-libxml2 \
	--with-net-snmp \
	--with-ldap \
	--with-openipmi \
	--with-openssl \
	%{subst_with ssh2} \
	%{subst_with unixodbc} \
	--sysconfdir=/etc/zabbix
%make dbschema
%make

# adjust in several files /home/zabbix
find conf src/go/conf -type f -print0 | xargs -0 sed -i \
	-e "s,/home/zabbix/bin,/usr/sbin,g" \
	-e "s,PidFile=/tmp,PidFile=%_var/run/zabbix,g" \
	-e "s,LogFile=/tmp,LogFile=%_logdir/zabbix,g" \
	-e "s,/home/zabbix/lock,%_var/lock/subsys/zabbix,g" \
	-e "s,/tmp/mysql.sock,%_localstatedir/mysql/mysql.sock,g" \
	-e "s,Include=/usr/local/etc/zabbix_agentd.conf.d/,Include=%_sysconfdir/%name/zabbix_agentd.conf.d/,g" --

%install
# Generate *.mo files
for pofile in `find ui/locale -type f -name '*.po'`
do
    msgfmt --use-fuzzy -c -o ${pofile%%po}mo $pofile
done

export GOFLAGS="-mod=vendor"
%makeinstall

# create directory structure
install -dm1775 %buildroot%_logdir/%name
install -dm0755 %buildroot%_sbindir
install -dm0750 %buildroot%_sysconfdir/%name
install -dm0750 %buildroot%_sysconfdir/%name/zabbix_agentd.conf.d
install -dm0755 %buildroot%webserver_webappsdir/%name
install -dm0755 %buildroot%_unitdir
install -dm0755 %buildroot%_includedir/%name

# binaries
install -m0755 src/%{name}_*/%{name}_{mysql,agentd} %buildroot%_sbindir
%if_with pgsql
install -m0755 src/%{name}_server/%{name}_pgsql %buildroot%_sbindir
install -m0755 src/%{name}_proxy/%{name}_proxy_pgsql %buildroot%_sbindir
%endif

# conf files
install -m0640 conf/%{name}_{server,agentd,proxy}.conf %buildroot%_sysconfdir/%name
install -Dpm 644 sources/%name-tmpfiles.conf %buildroot/lib/tmpfiles.d/%name.conf
%if_enabled agent2
install -dm0750 %buildroot%_sysconfdir/%name/zabbix_agent2.conf.d
install -m0640 src/go/conf/zabbix_agent2.conf %buildroot%_sysconfdir/%name/
install -dm0750 %buildroot%_sysconfdir/%name/zabbix_agent2.conf.d/plugins.d
install -m0640 src/go/conf/zabbix_agent2.d/plugins.d/*.conf %buildroot%_sysconfdir/%name/zabbix_agent2.conf.d/plugins.d/
%endif

# frontends
mv ui/locale/*.sh .
cp -r ui %buildroot%webserver_webappsdir/%name/

# apache2 config
install -pDm0644 sources/%name.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

# nginx config
install -pDm0644 sources/%name.nginx %buildroot%_sysconfdir/%name/%{name}_nginx.conf

# start scripts
install -pDm0755 sources/%{name}_agentd.init %buildroot%_initdir/%{name}_agentd
install -pDm0644 sources/%{name}_agentd.service %buildroot%_unitdir/%{name}_agentd.service
install -pDm0644 sources/zabbix_server %buildroot%_sysconfdir/sysconfig/zabbix_server
%if_enabled agent2
install -pDm0755 sources/%{name}_agent2.init %buildroot%_initdir/%{name}_agent2
install -pDm0644 sources/%{name}_agent2.service %buildroot%_unitdir/%{name}_agent2.service
%endif
%if_with pgsql
install -pDm0755 sources/%{name}_pgsql.init %buildroot%_initdir/%{name}_pgsql
install -pDm0644 sources/%{name}_pgsql.service %buildroot%_unitdir/%{name}_pgsql.service
install -pDm0755 sources/%{name}_proxy_pgsql.init %buildroot%_initdir/%{name}_proxy_pgsql
install -pDm0644 sources/%{name}_proxy_pgsql.service %buildroot%_unitdir/%{name}_proxy_pgsql.service
%endif
install -pDm0755 sources/%{name}_mysql.init %buildroot%_initdir/%{name}_mysql
install -pDm0644 sources/%{name}_mysql.service %buildroot%_unitdir/%{name}_mysql.service
install -pDm0755 sources/%{name}_proxy.init %buildroot%_initdir/%{name}_proxy
install -pDm0644 sources/%{name}_proxy.service %buildroot%_unitdir/%{name}_proxy.service
%if_enabled java
install -pDm0755 sources/%{name}_java_gateway.init %buildroot%_initdir/%{name}_java_gateway
install -pDm0644 sources/%{name}_java_gateway.service %buildroot%_unitdir/%{name}_java_gateway.service
%endif
%if_enabled webservice
install -m0640 src/go/conf/zabbix_web_service.conf %buildroot%_sysconfdir/%name/
install -pDm0755 sources/%{name}_web_service.init %buildroot%_initdir/%{name}_web_service
install -pDm0644 sources/%{name}_web_service.service %buildroot%_unitdir/%{name}_web_service.service
%endif

# sudo entry
install -pDm0400 sources/%name.sudo %buildroot%_sysconfdir/sudoers.d/%name

# include files
cp -r include/* %buildroot%_includedir/%name

%if_enabled java
# delete unnecessary files from java gateway
rm %buildroot%_sbindir/zabbix_java/settings.sh
rm %buildroot%_sbindir/zabbix_java/startup.sh
rm %buildroot%_sbindir/zabbix_java/shutdown.sh

mv %buildroot%_sbindir/zabbix_java/lib/logback.xml %buildroot%_sysconfdir/zabbix/zabbix_java_gateway_logback.xml
rm %buildroot%_sbindir/zabbix_java/lib/logback-console.xml

mkdir -p %buildroot%_javadir
mv %buildroot%_sbindir/zabbix_java %buildroot%_javadir/zabbix-java-gateway
install -m 0755 -p sources/zabbix_java_gateway-sysd %buildroot%_sbindir/zabbix_java_gateway

cat src/zabbix_java/settings.sh | sed \
        -e 's|^PID_FILE=.*|PID_FILE="/var/run/zabbix/zabbix_java.pid"|g' \
        -e '/^# TIMEOUT=/a \\nTIMEOUT=3' \
        > %buildroot%_sysconfdir/zabbix/zabbix_java_gateway.conf
%endif

# ChangeLog
bzip2 ChangeLog

# remove Makefile* files from database/*
find ./database/postgresql  -name 'Makefile*' -exec rm '{}' ';'

%pre common
/usr/sbin/groupadd -r -f %zabbix_group ||:
/usr/sbin/useradd -g %zabbix_group -G proc -c 'Zabbix' \
	-d %zabbix_home -s /dev/null -r %zabbix_user >/dev/null 2>&1 ||:

%pre server-mysql
echo "########################################################################"
echo "              Attention! Zabbix upgrade to %version"
echo "########################################################################"
echo " Notice:"
echo " On MySQL and MariaDB, this requires GLOBAL"
echo " log_bin_trust_function_creators = 1 to be set if binary logging is"
echo " enabled and there is no superuser privileges and"
echo " log_bin_trust_function_creators = 1 is not set in MySQL configuration"
echo " file. To set the variable using MySQL console, run:"
echo ""
echo " mysql> SET GLOBAL log_bin_trust_function_creators = 1;"
echo ""
echo " Once the upgrade has been successfully completed,"
echo " log_bin_trust_function_creators can be disabled:"
echo ""
echo " mysql> SET GLOBAL log_bin_trust_function_creators = 0;"
echo ""
echo "########################################################################"

%post server-mysql
%post_service zabbix_mysql

%preun server-mysql
%preun_service zabbix_mysql
%if_with pgsql
%pre server-pgsql
echo "########################################################################"
echo "              Attention! Zabbix upgrade to %version"
echo "########################################################################"
echo "# Notice: zabbix-server-pgsql require PostgreSQL 13 or newer!          #"
echo "########################################################################"

%post server-pgsql
%post_service zabbix_pgsql

%preun server-pgsql
%preun_service zabbix_pgsql
%endif

%post proxy
%post_service zabbix_proxy

%preun proxy
%preun_service zabbix_proxy

%if_with pgsql
%pre proxy-pgsql
echo "########################################################################"
echo "              Attention! Zabbix upgrade to %version"
echo "########################################################################"
echo "# Notice: zabbix-server-pgsql require PostgreSQL 13 or newer!          #"
echo "########################################################################"

%post proxy-pgsql
%post_service zabbix_proxy_pgsql

%preun proxy-pgsql
%preun_service zabbix_proxy_pgsql
%endif

%if_enabled java
%post java-gateway
%post_service zabbix_java_gateway

%preun java-gateway
%preun_service zabbix_java_gateway
%endif

%post agent
if [ $1 -eq 1 ]; then
	sed -i -e "s,Hostname=Zabbix server,Hostname=$HOSTNAME,g" \
	%_sysconfdir/%name/%{name}_agentd.conf
fi
%post_service zabbix_agentd

%post agent-sudo
if [ $1 -eq 1 ]; then
	gpasswd -a %zabbix_user wheel
fi

%preun agent
%preun_service zabbix_agentd


%if_with agent2
%post agent2
if [ $1 -eq 1 ]; then
	sed -i -e "s,Hostname=Zabbix server,Hostname=$HOSTNAME,g" \
	%_sysconfdir/%name/%{name}_agent2.conf
fi
%post_service zabbix_agent2

%preun agent2
%preun_service zabbix_agent2
%endif

%post phpfrontend-engine
if [ -f %webserver_webappsdir/%name/frontends/php/conf/zabbix.conf.php -a ! -f %webserver_webappsdir/%name/ui/conf/zabbix.conf.php ]
then
    cp -p %webserver_webappsdir/%name/frontends/php/conf/zabbix.conf.php %webserver_webappsdir/%name/ui/conf/
fi

%files common
%dir %attr(1775,root,%zabbix_group) %_logdir/%name
%dir %_sysconfdir/%name
/lib/tmpfiles.d/*

%files common-database-sqlite3
%doc database/sqlite3/*.sql

%files common-database-mysql
%doc database/mysql/*.sql
%doc database/mysql/option-patches/*.sql

%if_with pgsql
%files common-database-pgsql
%doc database/postgresql/*.sql database/postgresql/timescaledb
%endif

%files server-common
%_bindir/%{name}_get
%_bindir/%{name}_js
%config(noreplace) %_sysconfdir/sysconfig/zabbix_server
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_server.conf
%_man1dir/%{name}_get.*

%files server-mysql
%_sbindir/%{name}_mysql
%_initdir/%{name}_mysql
%_unitdir/*mysql*

%if_with pgsql
%files server-pgsql
%_sbindir/%{name}_pgsql
%_initdir/%{name}_pgsql
%_unitdir/*pgsql*
%exclude %_unitdir/*proxy_pgsql*
%endif

%files proxy-common
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_proxy.conf
%_man8dir/%{name}_proxy.*

%files proxy
%_sbindir/%{name}_proxy
%_initdir/%{name}_proxy
%_unitdir/*proxy*
%if_with pgsql
%exclude %_unitdir/*proxy_pgsql*
%endif

%if_with pgsql
%files proxy-pgsql
%_sbindir/%{name}_proxy_pgsql
%_initdir/%{name}_proxy_pgsql
%_unitdir/*proxy_pgsql*
%endif

%if_enabled java
%files java-gateway
%_sbindir/%{name}_java_gateway
%_initdir/%{name}_java_gateway
%_unitdir/*java_gateway*
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_java_gateway.conf
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_java_gateway_logback.xml
%_javadir/*
%endif

%files agent
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_agentd.conf
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/%name/zabbix_agentd.conf.d
%_initdir/%{name}_agentd
%_unitdir/*agentd*
%_sbindir/%{name}_agentd
%_bindir/%{name}_sender
%_man8dir/%{name}_agentd.*
%_man1dir/%{name}_sender.*

%if_enabled agent2
%files agent2
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_agent2.conf
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/%name/zabbix_agent2.conf.d
%dir %attr(0750,root,%zabbix_group) %_sysconfdir/%name/zabbix_agent2.conf.d/plugins.d
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/zabbix_agent2.conf.d/plugins.d/*
%_initdir/%{name}_agent2
%_unitdir/*agent2*
%_sbindir/%{name}_agent2
%_man8dir/%{name}_agent2.*
%endif

%if_enabled webservice
%files web-service
%config(noreplace) %attr(0640,root,%zabbix_group) %_sysconfdir/%name/%{name}_web_service.conf
%_initdir/%{name}_web_service
%_unitdir/*_web_service*
%_sbindir/%{name}_web_service
%_man8dir/%{name}_web_service.*
%endif

%files agent-sudo
%config(noreplace) %attr(0400,root,root) %_sysconfdir/sudoers.d/%name

%files phpfrontend-engine
%webserver_webappsdir/%name
%doc add_new_language.sh make_mo.sh update_po.sh

%files phpfrontend-php8.1
%files phpfrontend-php8.2
%files phpfrontend-php8.3

%files phpfrontend-apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%files phpfrontend-apache2-mod_php8.1
%files phpfrontend-apache2-mod_php8.2
%files phpfrontend-apache2-mod_php8.3

%files phpfrontend-nginx
%config(noreplace) %_sysconfdir/%name/%{name}_nginx.conf

%files phpfrontend-nginx-php8.1-fpm-fcgi
%files phpfrontend-nginx-php8.2-fpm-fcgi
%files phpfrontend-nginx-php8.3-fpm-fcgi

%files doc
%doc AUTHORS NEWS README INSTALL ChangeLog.bz2

%files contrib
%doc misc/snmptrap/*

%files source
%_includedir/%name

%changelog
* Thu Aug 01 2024 Alexei Takaseev <taf@altlinux.org> 1:7.0.2-alt1
- 7.0.2

* Tue Jul 23 2024 Alexei Takaseev <taf@altlinux.org> 1:7.0.1-alt1
- 7.0.1

* Tue Jun 04 2024 Alexei Takaseev <taf@altlinux.org> 1:7.0.0-alt1
- 7.0.0
- Change license to AGPL-3.0-only
- Add support nginx frontend

* Tue May 21 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.30-alt1
- 6.0.30

* Tue Apr 23 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.29-alt1
- 6.0.29

* Fri Apr 12 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.28-alt2
- Add support php 8.3 (ALT #46487)

* Thu Mar 28 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.28-alt1
- 6.0.28
- Revert changes from 6.0.26-alt2 and 6.0.27-alt2, no need more.
- java-gateway now arch-depended

* Tue Mar 19 2024 Michael Shigorin <mike@altlinux.org> 1:6.0.27-alt2
- E2K: use whatever java is available

* Tue Feb 27 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.27-alt1
- 6.0.27 (Fixes: CVE-2023-32725, CVE-2023-32726, CVE-2023-32727
                 CVE-2023-32728, CVE-2024-22119)

* Wed Jan 31 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.26-alt2
- Change BR java-devel to java-11-devel

* Tue Jan 30 2024 Alexei Takaseev <taf@altlinux.org> 1:6.0.26-alt1
- 6.0.26

* Wed Dec 20 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.25-alt2
- Add zabbix-web-service subpackage

* Thu Dec 14 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.25-alt1
- 6.0.25

* Thu Nov 02 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.23-alt1
- 6.0.23
- Remove deprecate --with-jabber

* Mon Oct 09 2023 Ivan A. Melnikov <iv@altlinux.org> 1:6.0.22-alt1.1
- NMU: add riscv64 and loongarch64 support

* Tue Sep 26 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.22-alt1
- 6.0.22

* Mon Sep 11 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.21-alt2
- Remove subpackages phpfrontend-php8.0 and phpfrontend-apache2-mod_php8.0

* Wed Aug 23 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.21-alt1
- 6.0.21

* Mon Aug 21 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.20-alt1
- 6.0.20

* Wed Jun 28 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.19-alt1
- 6.0.19
- Add Requires: zabbix-phpfrontend-engine to phpfrontend-php* subpackages (ALT #46487)

* Wed May 31 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.18-alt1
- 6.0.18

* Tue Apr 25 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.17-alt1
- 6.0.17
- Remove subpackages phpfrontend-php7 and phpfrontend-apache2-mod_php7

* Tue Apr 18 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.16-alt1
- 6.0.16

* Mon Apr 17 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.15-alt2
- Pack tsdb_history_pk_upgrade_*_compression/*.sql files

* Mon Apr 03 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.15-alt1
- 6.0.15

* Thu Mar 09 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.14-alt2
- Add support php 8.2
- Fix typo Summary for phpfrontend-php8.1

* Thu Mar 09 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.14-alt1
- 6.0.14

* Thu Feb 02 2023 Alexei Takaseev <taf@altlinux.org> 1:6.0.13-alt1
- 6.0.13

* Wed Dec 28 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.12-alt2
- Add notice fo use MySQL 8.0.x
- Pack history_pk_prepare.sql (ALT #44523)

* Wed Dec 07 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.12-alt1
- 6.0.12

* Tue Nov 29 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.11-alt1
- 6.0.11

* Thu Nov 03 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.10-alt1
- 6.0.10

* Thu Sep 22 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.9-alt1
- 6.0.9

* Mon Aug 29 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.8-alt0.rc2.1
- Fix path to zabbix-agent2 configs and plugins (ALT #43640)

* Sun Aug 28 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.8-alt0.rc2
- 6.0.8 rc2

* Thu Aug 18 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.7-alt2
- Remove unneeded Obsoletes
- Add notice fo use Postgresql 13 or newer

* Tue Jul 26 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.7-alt1
- 6.0.7

* Tue Jun 28 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.6-alt1
- 6.0.6

* Tue May 31 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.5-alt1
- 6.0.5

* Wed May 04 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.4-alt1
- 6.0.4

* Wed Apr 06 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.3-alt1
- 6.0.3

* Fri Mar 18 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.2-alt1
- 6.0.2

* Wed Mar 02 2022 Alexei Takaseev <taf@altlinux.org> 1:6.0.1-alt1
- 6.0.1

* Wed Mar 02 2022 Alexei Takaseev <taf@altlinux.org> 1:5.4.11-alt1
- 5.4.11

* Thu Feb 03 2022 Alexei Takaseev <taf@altlinux.org> 1:5.4.10-alt1
- 5.4.10

* Fri Dec 24 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.9-alt1
- 5.4.9
    * [ZBX-20388] fixed XSS vulnerability in multiselect
    * [ZBX-20278] fixed XSS attack vulnerability in scheduled report configuration form

* Thu Dec 23 2021 Michael Shigorin <mike@altlinux.org> 1:5.4.8-alt2
- fix build with disabled agent2

* Tue Nov 30 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.8-alt1
- 5.4.8

* Fri Oct 29 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.7-alt1
- 5.4.7

* Tue Oct 19 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.6-alt1
- 5.4.6

* Fri Oct 01 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.5-alt1
- 5.4.5

* Fri Sep 03 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.4-alt2
- Add Req: to php7-openssl for -phpfrontend-php7 subpackage
  (ALT #40841)

* Tue Aug 31 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.4-alt1
- 5.4.4

* Fri Aug 20 2021 Alexei Takaseev <taf@altlinux.org> 1:5.4.3-alt1
- 5.4.3

* Sat Jul 17 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.14-alt1
- 5.0.14

* Tue Jun 29 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.13-alt1
- 5.0.13
- Disable build agent2 on Elbrus arch

* Tue Jun 01 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.12-alt3
- (ALT #40122)

* Mon May 31 2021 Alexey Shabalin <shaba@altlinux.org> 1:5.0.12-alt2
- Add agent2 package

* Tue May 25 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.12-alt1
- 5.0.12

* Tue Apr 27 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.11-alt1
- 5.0.11

* Thu Apr 01 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.10-alt1
- 5.0.10

* Wed Feb 24 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.9-alt1
- 5.0.9

* Tue Feb 02 2021 Alexei Takaseev <taf@altlinux.org> 1:5.0.8-alt1
- 5.0.8

* Thu Dec 03 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.6-alt1
- 5.0.6
- Edit Apache config file (ALT #37494)

* Thu Nov 19 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.5-alt3
- Add lost double.sql (ALT #39311)

* Mon Nov 16 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.5-alt2
- Copy old zabbix.conf.php from pre-5.0 version (ALT #39282)

* Tue Oct 27 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.5-alt1
- 5.0.5

* Tue Sep 29 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.4-alt1
- 5.0.4

* Wed Sep 02 2020 Alexei Takaseev <taf@altlinux.org> 1:5.0.3-alt1
- 5.0.3

* Fri Jul 03 2020 Alexei Takaseev <taf@altlinux.org> 1:4.4.10-alt1
- 4.4.10

* Tue May 26 2020 Alexei Takaseev <taf@altlinux.org> 1:4.4.9-alt1
- 4.4.9

* Mon Mar 30 2020 Alexei Takaseev <taf@altlinux.org> 1:4.4.7-alt1
- 4.4.7

* Tue Feb 25 2020 Alexei Takaseev <taf@altlinux.org> 1:4.4.6-alt1
- 4.4.6

* Sat Feb 01 2020 Alexei Takaseev <taf@altlinux.org> 1:4.4.5-alt1
- 4.4.5
- Cleanup spec

* Fri Dec 20 2019 Alexei Takaseev <taf@altlinux.org> 1:4.4.4-alt1
- 4.4.4

* Thu Nov 28 2019 Alexei Takaseev <taf@altlinux.org> 1:4.4.3-alt1
- 4.4.3

* Wed Nov 27 2019 Alexei Takaseev <taf@altlinux.org> 1:4.4.2-alt1
- 4.4.2

* Fri Nov 01 2019 Alexei Takaseev <taf@altlinux.org> 1:4.4.1-alt1
- 4.4.1

* Thu Oct 03 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.7-alt1
- 4.2.7

* Thu Sep 26 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.6-alt2
- Add BR /proc

* Tue Aug 27 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.6-alt1
- 4.2.6

* Tue Jul 30 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.5-alt1
- 4.2.5

* Wed Jun 26 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.4-alt1
- 4.2.4

* Fri May 17 2019 Alexei Takaseev <taf@altlinux.org> 1:4.2.1-alt1
- 4.2.1

* Fri Apr 19 2019 Alexei Takaseev <taf@altlinux.org> 1:4.0.7-alt1
- 4.0.7
- Change path to traceroute (ALT #36439)

* Fri Mar 29 2019 Alexei Takaseev <taf@altlinux.org> 1:4.0.6-alt1
- 4.0.6

* Tue Mar 05 2019 Alexei Takaseev <taf@altlinux.org> 1:4.0.5-alt2
- Remove support PHP5

* Tue Feb 26 2019 Alexei Takaseev <taf@altlinux.org> 1:4.0.5-alt1
- 4.0.5

* Tue Feb 05 2019 Alexei Takaseev <taf@altlinux.org> 1:4.0.4-alt1
- 4.0.4

* Fri Dec 21 2018 Alexei Takaseev <taf@altlinux.org> 1:4.0.3-alt1
- 4.0.3

* Wed Nov 28 2018 Alexei Takaseev <taf@altlinux.org> 1:4.0.2-alt1
- 4.0.2

* Tue Oct 30 2018 Alexei Takaseev <taf@altlinux.org> 1:4.0.1-alt1
- 4.0.1
- Add support PHP7

* Wed Oct 03 2018 Alexei Takaseev <taf@altlinux.org> 1:4.0.0-alt1
- 4.0.0

* Fri Sep 21 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.14-alt2
- Add re-check apache2 config while
  install/de-install zabbix-phpfrontend-apache2

* Tue Sep 18 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.14-alt1
- 3.4.14

* Tue Sep 04 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.13-alt2
- Rebuild with OpenSSL 1.1.x

* Tue Aug 28 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.13-alt1
- 3.4.13

* Thu Aug 02 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.12-alt1
- 3.4.12

* Tue Jun 26 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.11-alt1
- 3.4.11

* Tue Jun 05 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.10-alt1
- 3.4.10

* Thu May 10 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.9-alt1
- 3.4.9

* Tue Apr 03 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.8-alt1
- 3.4.8

* Mon Feb 19 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.7-alt2
- 3.4.7 r77720

* Wed Feb 07 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.7-alt1
- 3.4.7

* Fri Jan 19 2018 Alexei Takaseev <taf@altlinux.org> 1:3.4.6-alt1
- 3.4.6

* Wed Dec 27 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.5-alt1
- 3.4.5

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.4-alt2
- Added support for libssh2, unixODBC.
- Built proxy with PostgreSQL support.

* Wed Nov 08 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.4-alt1
- 3.4.4

* Fri Nov 03 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.3-alt2
- introduce java knob (on by default) (closes: #34122)
- buildreq again

* Thu Oct 19 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.3-alt1
- 3.4.3

* Thu Sep 28 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.2-alt1
- 3.4.2

* Tue Aug 29 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.1-alt1
- 3.4.1

* Fri Aug 25 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.1-alt0.rc1
- 3.4.1rc1

* Tue Aug 22 2017 Alexei Takaseev <taf@altlinux.org> 1:3.4.0-alt1
- 3.4.0

* Wed Jul 19 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.7-alt1
- 3.2.7

* Mon Jun 19 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.6-alt2
- Remove phpfrontend-apache subpackage

* Sat May 06 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.6-alt1
- 3.2.6

* Wed Apr 26 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.5-alt2
- Change default LOAD_MODULE_PATH from %%_libdir/modules to
  %%_libdir/zabbix/modules (ALT#33418)

* Fri Apr 21 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.5-alt1
- 3.2.5

* Mon Mar 06 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.4-alt2
- Enable Zabbix Java gateway

* Tue Feb 28 2017 Alexei Takaseev <taf@altlinux.org> 1:3.2.4-alt1
- 3.2.4

* Thu Dec 29 2016 Alexei Takaseev <taf@altlinux.org> 1:3.2.3-alt1
- 3.2.3

* Fri Dec 09 2016 Alexei Takaseev <taf@altlinux.org> 1:3.2.2-alt1
- 3.2.2

* Mon Oct 03 2016 Alexei Takaseev <taf@altlinux.org> 1:3.2.1-alt1
- 3.2.1

* Fri Sep 16 2016 Alexei Takaseev <taf@altlinux.org> 1:3.2.0-alt1
- 3.2.0

* Tue Jul 26 2016 Alexei Takaseev <taf@altlinux.org> 1:3.0.4-alt1
- 3.0.4

* Thu May 19 2016 Alexei Takaseev <taf@altlinux.org> 1:3.0.3-alt1
- 3.0.3

* Thu Apr 21 2016 Alexei Takaseev <taf@altlinux.org> 1:3.0.2-alt1
- 3.0.2

* Sat Feb 27 2016 Alexei Takaseev <taf@altlinux.org> 1:3.0.1-alt1
- 3.0.1
- Enable SSL (ALT#31828)

* Wed Feb 17 2016 Alexei Takaseev <taf@altlinux.org> 1:3.0.0-alt1
- 3.0.0
- Remove deprecated script and docs.
- Add group setting for zabbix-agent (ALT#31627)
- Add subpackage -source (ALT#31340)

* Fri Nov 13 2015 Alexei Takaseev <taf@altlinux.org> 1:2.4.7-alt1
- 2.4.7

* Tue Aug 11 2015 Alexei Takaseev <taf@altlinux.org> 1:2.4.6-alt1
- 2.4.6

* Sat Jun 20 2015 Alexei Takaseev <taf@altlinux.org> 1:2.4.5-alt2
- Support macros in URL map elements (ALT#31084)
- ALT#31021

* Wed Apr 22 2015 Alexei Takaseev <taf@altlinux.org> 1:2.4.5-alt1
- 2.4.5

* Tue Feb 24 2015 Alexei Takaseev <taf@altlinux.org> 1:2.4.4-alt1
- 2.4.4

* Tue Dec 16 2014 Alexei Takaseev <taf@altlinux.org> 1:2.4.3-alt1
- 2.4.3

* Thu Nov 06 2014 Alexei Takaseev <taf@altlinux.org> 1:2.4.2-alt1
- 2.4.2

* Wed Oct 08 2014 Alexei Takaseev <taf@altlinux.org> 1:2.4.1-alt1
- 2.4.1

* Sat Sep 20 2014 Alexei Takaseev <taf@altlinux.org> 1:2.4.0-alt1
- 2.4.0

* Thu Aug 28 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.6-alt1
- 2.2.6

* Fri Jul 18 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.5-alt1
- 2.2.5
- Removed executable permission bits on *.service (ALT#30177)

* Tue Jun 24 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.4-alt1
- 2.2.4

* Wed May 21 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.3-alt2
- build with --with-libxml2 (ALT#30086)
- change Requires: php5-mysqli for zabbix-phpfrontend-php5 (ALT#30105)

* Thu Apr 10 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.3-alt1
- 2.2.3 release

* Thu Feb 13 2014 Alexei Takaseev <taf@altlinux.org> 1:2.2.2-alt1
- 2.2.2 release

* Mon Dec 09 2013 Alexei Takaseev <taf@altlinux.org> 1:2.2.1-alt1
- 2.2.1 release

* Thu Nov 21 2013 Alexei Takaseev <taf@altlinux.org> 1:2.2.0-alt1
- 2.2.0 release

* Wed Oct 09 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.9-alt1
- 2.0.9 release

* Thu Aug 22 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.8-alt1
- 2.0.8 release

* Sat Jul 27 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.7-alt1
- 2.0.7 release

* Tue Apr 23 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.6-alt1
- 2.0.6 release

* Wed Apr 03 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.5-alt2
- change buildreq 'libMySQL-devel' to 'libmysqlclient-devel'

* Wed Feb 13 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.5-alt1
- 2.0.5 release

* Wed Jan 23 2013 Alexei Takaseev <taf@altlinux.org> 1:2.0.4-alt3
- (Fixes: CVE-2013-1364)

* Tue Dec 25 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.4-alt2
- Add define %%_unitdir macro for compatible with P6/T6 branches
- Change requires on -commons's pkg to "soft"

* Mon Dec 17 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.4-alt1
- 2.0.4 release

* Sat Nov 24 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.3-alt3
- Fix name unit files

* Thu Nov 22 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.3-alt2
- Remove httpd2 restart/reload calls in its post/un scripts,
  deprecated by httpd2.filetrigger
- Add systemd unit files

* Tue Oct 02 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.3-alt1
- 2.0.3 release

* Thu Jul 26 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.2-alt3
- Generate *.mo files

* Sun Jul 22 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.2-alt2
- Fix default pidfile location

* Fri Jul 20 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.2-alt1
- 2.0.2 release

* Mon Jul 16 2012 Alexei Takaseev <taf@altlinux.org> 1:2.0.2-alt0.rc1.2
- 2.0.2rc1

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
