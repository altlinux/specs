%define realname stg
Name: stargazer
Version: 2.407.cvs20100811
Release: alt3.2
License: GPLv2
Group: System/Servers
Source0: %realname-%version.src.tgz
Source1: %name
Source4: %name-examples.tar.bz2
Source5: sgauth
Source6: mod_config.tgz
Source9: mod_store_files.tgz

Patch0: %name-alt_local.patch
Patch1: %name-alt_auth.diff
Patch2: %name-alt_install.diff
Patch3: %name-2.405.9.8-alt_default.diff
Patch4: %name-auth-lib.patch
Patch5: %name-stgconf-lib.patch
Patch6: %name-clean_db.diff
Patch7: %name-rscriptd-install.patch
Patch8: %name-wildcards_dotconfpp.patch
Patch9: %name-2.407-alt-DSO.patch

Summary: Stargazer billing system
Summary(ru_RU.UTF8): Биллинг-система Stargazer
Url: http://stargazer.dp.ua
Packager: Dmitriy Kulik <lnkvisitor@altlinux.ru>
Requires: iptables lib%name = %version-%release %name-mod_store >= %version-%release
BuildRequires: gcc-c++ libMySQL-devel libexpat-devel iconv firebird-devel postgresql-devel zlib-devel

%description
Stargazer billing system

%description -l ru_RU.UTF8
Биллинг-система Stargazer

%files
%_libdir/%realname/libscript_executer.so
%_libdir/%realname/libstg_logger.so
%_libdir/%realname/libstg_locker.so
%_sbindir/stargazer.bin
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/available-conf.d
%dir %_sysconfdir/%name/enabled-conf.d
%_initdir/%name
%dir %_localstatedir/%name/monitor
%_localstatedir/%name/monitor
%config(noreplace,missingok) %_sysconfdir/%name/*
%_sysconfdir/%name/mod_store.conf
%exclude %_sysconfdir/%name/available-conf.d/*
%exclude %_sysconfdir/%name/enabled-conf.d/*
%exclude %_sysconfdir/%name/rscriptd.conf

%post
[ -e %_sysconfdir/%name/mod_store.conf ] || echo "#Please install a storage module." > %_sysconfdir/%name/mod_store.conf

%preun
%_initdir/%name condstop

###############################################################################

%package doc
Summary: Stargazer billing system manual and live example
Group: Books/Other
BuildArch: noarch

%description doc
Stargazer billing system manual and live example

%files doc
%doc stargazer-examples stargazer*.pdf projects/stargazer/BUGS projects/stargazer/TODO projects/stargazer/inst/var/*.sql

###############################################################################

%package -n lib%name
Summary: The library files needed for stargazer
Group: Networking/Other

%description -n lib%name
The lib%name package contains the necessary library for %name

%files -n lib%name
%_libdir/%realname/*
%exclude %_libdir/%realname/mod_*
%exclude %_libdir/%realname/libia_auth_c.so
%exclude %_libdir/%realname/libsrvconf.so
%exclude %_libdir/%realname/libscript_executer.so
%exclude %_libdir/%realname/libstg_logger.so
%exclude %_libdir/%realname/libstg_locker.so
%exclude %_libdir/%realname/libhostallow.so
%exclude %_libdir/%realname/libibpp.so

###############################################################################

%package sgauth
Summary: Console authorization utility for the Stargazer billing system
Group: System/Libraries
Requires: lib%name = %version-%release

%description sgauth
This package contains an utility to authorize in networks with Stargazer billing system.

%preun sgauth
%_initdir/sgauth condstop

%files sgauth
%doc projects/sgauth/readme
%_bindir/sgauth
%_libdir/%realname/libia_auth_c.so
%dir %_initdir/sgauth
%config(noreplace,missingok) %_sysconfdir/sgauth.conf

###############################################################################

%package sgconf
Summary: Console configuration utility for the Stargazer billing syste
Group: System/Configuration/Networking
Requires: lib%name = %version-%release

%description sgconf
This package contains a configuration tool for the Stargazer billing system

%files sgconf
%_bindir/sgconf
%_libdir/%realname/libsrvconf.so

###############################################################################

%package mod_store_files
Summary: Stargazer filesystem storage plugin
Group: System/Libraries
Requires: %name = %version-%release
Conflicts: %name-mod_store_mysql %name-mod_store_postgresql %name-mod_store_firebird
Provides: %name-mod_store = %version-{%release}.1

%description mod_store_files
Stargazer filesystem storage plugin allows to store user's information in separate files

%post mod_store_files
[ -e %_sysconfdir/%name/mod_store.conf ] && rm %_sysconfdir/%name/mod_store.conf
ln -s ../available-conf.d/mod_store_files.conf %_sysconfdir/%name/mod_store.conf
%_initdir/%name condrestart

%files mod_store_files
%_libdir/%realname/mod_store_files.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_store_files.conf
%config(noreplace,missingok) %_localstatedir/%name/tariffs/*
%config(noreplace,missingok) %_localstatedir/%name/admins/*
%config(noreplace,missingok) %_localstatedir/%name/users/test/*
%dir %_localstatedir/%name
%dir %_localstatedir/%name/tariffs
%dir %_localstatedir/%name/admins
%dir %_localstatedir/%name/users
%dir %_localstatedir/%name/users/test

###############################################################################

%package mod_store_mysql
Summary: Stargazer MySQL storage plugin
Group: System/Libraries
Requires: %name = %version-%release
Conflicts: %name-mod_store_files %name-mod_store_postgresql %name-mod_store_firebird
Provides: %name-mod_store = %version-%release

%description mod_store_mysql
Stargazer MySQL storage plugin allows to store user's information in MySQL database

%post mod_store_mysql
[ -e %_sysconfdir/%name/mod_store.conf ] && rm %_sysconfdir/%name/mod_store.conf
ln -s ../available-conf.d/mod_store_mysql.conf %_sysconfdir/%name/mod_store.conf
%_initdir/%name condrestart

%files mod_store_mysql
%_libdir/%realname/mod_store_mysql.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_store_mysql.conf

###############################################################################

%package mod_store_postgresql
Summary: Stargazer PostgreSQL storage plugin
Group: System/Libraries
Requires: %name = %version-%release postgresql
Conflicts: %name-mod_store_files %name-mod_store_files %name-mod_store_firebird
Provides: %name-mod_store = %version-%release

%description mod_store_postgresql
Stargazer PostgreSQL storage plugin allows to store user's information in PostgreSQL database

%post mod_store_postgresql
echo Please import database from %_localstatedir/%name/postgresql.sql
[ -e %_sysconfdir/%name/enabled-conf.d/mod_store.conf ] && rm %_sysconfdir/%name/enabled-conf.d/mod_store.conf
ln -s ../available-conf.d/mod_store_postgresql.conf %_sysconfdir/%name/enabled-conf.d/mod_store.conf
%_initdir/%name condrestart

%files mod_store_postgresql
%_libdir/%realname/mod_store_postgresql.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_store_postgresql.conf
%_localstatedir/%name/postgresql.sql

###############################################################################

%package mod_store_firebird
Summary: Stargazer Firebird/Interbase storage plugin
Group: System/Libraries
Requires: %name = %version-%release firebird
Conflicts: %name-mod_store_files %name-mod_store_postgresql %name-mod_store_mysql
Provides: %name-mod_store = %version-%release

%description mod_store_firebird
Stargazer Firebird/Interbase storage plugin allows to store user's information in Firebird/Interbase database

%post mod_store_firebird
echo Please import database from %_localstatedir/%name/firebird.sql
[ -e %_sysconfdir/%name/mod_store.conf ] && rm %_sysconfdir/%name/mod_store.conf
ln -s ../available-conf.d/mod_store_firebird.conf %_sysconfdir/%name/mod_store.conf
%_initdir/%name condrestart

%files mod_store_firebird
%_libdir/%realname/libibpp.so
%_libdir/%realname/mod_store_firebird.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_store_firebird.conf
%_localstatedir/%name/firebird.sql

###############################################################################

%package rscriptd
Summary: Stargazer remote script executer server
Group: System/Servers
Requires: %name = %version-%release

%description rscriptd
Stargazer remote script executer intended to separate NAS'es and billing system itself to different physical servers 

%post rscriptd

%files rscriptd
%_bindir/rscriptd
%config(noreplace,missingok) %_sysconfdir/%name/rscriptd.conf

###############################################################################

%package mod_auth_ao
Summary: Stargazer's plugin for AlwaysOnline authorization mode
Group: System/Libraries
Requires: %name = %version-%release

%description mod_auth_ao
This plugin allows to use "always online" authorization mode for users

%post mod_auth_ao
%_initdir/%name condrestart

%files mod_auth_ao
%_libdir/%realname/mod_auth_ao.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_auth_ao.conf
%_sysconfdir/%name/enabled-conf.d/mod_auth_ao.conf

###############################################################################

%package mod_auth_ia
Summary: Stargazer's plugin for InetAccess authorization
Group: System/Libraries
Requires: %name = %version-%release

%description mod_auth_ia
This plugin allows to use InetAccess (or console utility sgauth) to authorize in the Stargazer billing system

%post mod_auth_ia
%_initdir/%name condrestart

%files mod_auth_ia
%_libdir/%realname/mod_auth_ia.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_auth_ia.conf
%_sysconfdir/%name/enabled-conf.d/mod_auth_ia.conf

###############################################################################

%package mod_conf_sg
Summary: Stargazer's plugin for remote system configuration using GUI or CLI configuration utility
Group: System/Libraries
Requires: %name = %version-%release

%description mod_conf_sg
This plugin allows to use sgconf or sgconfig for remote system configuration

%post mod_conf_sg
%_initdir/%name condrestart

%files mod_conf_sg
%_libdir/%realname/mod_conf_sg.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_conf_sg.conf
%_sysconfdir/%name/enabled-conf.d/mod_conf_sg.conf

###############################################################################

%package mod_cap_ipq
Summary: Stargazer's plugin for traffic capturing via IP_QUEUE
Group: System/Libraries
Requires: %name = %version-%release

%description mod_cap_ipq
This plugin allows to use iptables QUEUE target to collect traffic

%post mod_cap_ipq
%_initdir/%name condrestart

%files mod_cap_ipq
%_libdir/%realname/mod_cap_ipq.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_cap_ipq.conf
%_sysconfdir/%name/enabled-conf.d/mod_cap_ipq.conf

###############################################################################

%package mod_cap_ether
Summary: Stargazer's plugin for traffic capturing via raw sockets
Group: System/Libraries
Requires: %name = %version-%release

%description mod_cap_ether
This plugin captures traffic for the Stargazer billing system using raw socket

%post mod_cap_ether
%_initdir/%name condrestart

%files mod_cap_ether
%_libdir/%realname/mod_cap_ether.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_cap_ether.conf
%_sysconfdir/%name/enabled-conf.d/mod_cap_ether.conf

###############################################################################

%package mod_cap_nf
Summary: Stargazer's plugin for traffic capturing via NetFlow protocol
Group: System/Libraries
Requires: %name = %version-%release

%description mod_cap_nf
This plugin allows to use Stargazer with hardware or software traffic sensors working via NetFlow protocol

%post mod_cap_nf
%_initdir/%name condrestart

%files mod_cap_nf
%_libdir/%realname/mod_cap_nf.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_cap_nf.conf
%_sysconfdir/%name/enabled-conf.d/mod_cap_nf.conf

###############################################################################

%package mod_ping
Summary: Stargazer's plugin for regular pinging online users
Group: System/Libraries
Requires: %name = %version-%release

%description mod_ping
This plugin pings all online users and store the time of last ICMP reply for each user

%post mod_ping
%_initdir/%name condrestart

%files mod_ping
%_libdir/%realname/mod_ping.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_ping.conf
%_sysconfdir/%name/enabled-conf.d/mod_ping.conf

###############################################################################

%package mod_radius
Summary: Stargazer's plugin for working with FreeRADIUS as a back-end
Group: System/Libraries
Requires: %name = %version-%release

%description mod_radius
This plugin allows to control accessing services with FreeRADIUS and the Stargazer billing system

%post mod_radius
%_initdir/%name condrestart

%files mod_radius
%_libdir/%realname/mod_radius.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_radius.conf
%_sysconfdir/%name/enabled-conf.d/mod_radius.conf

###############################################################################

%package mod_remote_script
Summary: Strgazer's plugin to communicate with remote script executor
Group: System/Libraries
Requires: %name = %version-%release

%description mod_remote_script
This plugin sends commands to remote script executer

%post mod_remote_script
%_initdir/%name condrestart

%files mod_remote_script
%_libdir/%realname/mod_remote_script.so
%config(noreplace,missingok) %_sysconfdir/%name/available-conf.d/mod_remote_script.conf
%_sysconfdir/%name/enabled-conf.d/mod_remote_script.conf

%prep 
%add_findprov_lib_path %_libdir/%realname
%setup -q -n %realname-%version
tar -xjf %SOURCE4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p2

find -name 'Makefile*' -print0 | xargs -r0 -- sed -i 's@-rpath.*@-rpath,%_libdir/%realname -Wl,-rpath-link,'`pwd`'/lib@'

%build
# x86_64
%__subst 's|usr/lib|usr/%_lib|g' projects/stargazer/build projects/sgauth/build
%__subst 's|lib/stg|%_lib/stg|g' projects/rscriptd/Makefile \
    projects/stargazer/Makefile projects/stargazer/plugins/Makefile.in \
    projects/stargazer/inst/linux/etc/stargazer/stargazer.conf \
    projects/sgconf/Makefile projects/sgauth/Makefile \
    stglibs/Makefile.in

# optflags
%__subst 's|CFLAGS="$CFLAGS -O2"|CFLAGS="$CFLAGS %optflags"|g' projects/stargazer/build
%__subst 's|CFLAGS="-O2"|CFLAGS="%optflags"|g' projects/sgauth/build
%__subst 's|CFLAGS="-O2"|CFLAGS="%optflags"|g' projects/sgconf/build

cd projects/sgauth
./build
cd ../sgconf
./build
cd ../rscriptd
./build
cd ../stargazer
%__subst 's|PREFIX=""|PREFIX="%buildroot"|g' ./build
%__subst 's|install -m|install -Dp -m|g' ./Makefile
%__subst 's|-m $(DATA_MODE)||g' ./Makefile
%__subst 's|-o $(OWNER) ||g' ./Makefile ../../stglibs/Makefile.in plugins/Makefile.in
%__subst 's|/var/stargazer|%_localstatedir/%name|g' ./Makefile ./scripts/monitor ./scripts/clean_db
%__subst 's|/usr/sbin/$(PROG)|/usr/sbin/stargazer.bin|g' ./Makefile
./build

%install
cd projects/sgauth
make PREFIX=%buildroot install
cd ../sgconf
make PREFIX=%buildroot install
cd ../rscriptd
make PREFIX=%buildroot install
cd ../stargazer
make PREFIX=%buildroot install-bin
cd ../..

#Services
%__install -Dp -m700 %SOURCE1 %buildroot%_initdir/%name
%__install -Dp -m700 %SOURCE5 %buildroot%_initdir/sgauth

#configs
%__mkdir -p %buildroot%_sysconfdir/%name
%__tar -xf %SOURCE6
cp -r mod_config/*  %buildroot%_sysconfdir/%name/
#libs
%__mkdir -p %buildroot%_libdir/%realname && cp lib/*.so %buildroot%_libdir/%realname/

#Data
%__mkdir -p %buildroot%_localstatedir/%name/monitor
cp projects/stargazer/inst/var/00-base-00.postgresql.sql %buildroot%_localstatedir/%name/postgresql.sql
cp projects/stargazer/inst/var/00-base-00.sql %buildroot%_localstatedir/%name/firebird.sql
#mod_store_files data
%__tar -xf %SOURCE9 
cp -R mod_store_files/* %buildroot%_localstatedir/%name/

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.407.cvs20100811-alt3.2
- Fixed build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.407.cvs20100811-alt3.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Sun Sep 19 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.407.cvs20100811-alt3
- Descriptions fix
- Fix requires

* Thu Aug 19 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.407.cvs20100811-alt2
- Added wildcards path
- Subpackages
  * mod_auth_ao
  * mod_auth_ia
  * mod_cap_ether
  * mod_cap_ipq
  * mod_cap_nf
  * mod_conf_sg
  * mod_ping
  * mod_radius
  * mod_remote_script


* Tue Aug 17 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.407.cvs20100811-alt1
- ->4.0.7 CVS20100817
- FIX #18733
- Subpackages
  * mod_store_files
  * mod_store_mysql
  * mod_store_postgresql
  * mod_store_firebird

* Sun Dec 28 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.6
- FIX #18322

* Wed Dec 10 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.5
- fixed stargazer deamon

* Sat Nov 15 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.4
- fixed cleandb script

* Wed Nov 12 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.3
- relocation data files
- added cleandb script

* Mon Nov 10 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.2
- fixed stargazer deamon
- added sgauth deamon

* Fri Nov 07 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2.1
- add configuration file for sgauth

* Tue Oct 28 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.405.9.8-alt2
- pick up from Orphaned
- fix bug inetaccess module
- fix bug utime 
- fix bug include cstring
- fix bug including netfilter
- separate to subpackages libstargazer & sgautch & sgconf

* Tue May 20 2008 Motsyo Gennadi <drool@altlinux.ru> 2.405.9.8-alt1
- new 2.405.9.8 release
- fix unpackaged directory (new sisyphus_check)
- fix #15505

* Tue Mar 11 2008 Motsyo Gennadi <drool@altlinux.ru> 2.404.9.7-alt1
- test build for Sisyphus

* Mon Feb 11 2008 Motsyo Gennadi <drool@altlinux.ru> 2.404.9.7-alt0.M40.1
- new 2.404.9.7 release

* Thu Dec 27 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.2007.12.25.M40.1
- fix bug inetaccess module

* Wed Dec 26 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.2007.12.25.M40.0
- new development snapshot

* Mon Dec 24 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.2007.12.21.M40.2
- fix unmets (thanks to Legion for help)

* Sun Dec 23 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.2007.12.21.M40.1
- new development snapshot (thanks to Madf for hints)
	* x86_64 build now fixed

* Sun Dec 16 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.2007.01.06.M40.2
- fix TEXTREL (add -fPIC to optflags)

* Sat Aug 18 2007 Motsyo Gennadi <drool@altlinux.ru> 2.4-alt0.M40.1
- new snapshot

* Mon Nov 20 2006 Motsyo Gennadi <drool@altlinux.ru> 2.402.9.7-alt0.M24.2
- update live example by alliance.dmitriy at rambler dot ru (support squid+cbq)
- add branded manual in PDF format
- separate example and manual to %name-doc package

* Sun Nov 12 2006 Motsyo Gennadi <drool@altlinux.ru> 2.402.9.7-alt0.M24.1
- new version
    -> upsream fix error with charge to the user of the prepaid traffic
- fix URL
- disable autostart after install/upgrade

* Fri Nov 03 2006 Motsyo Gennadi <drool@altlinux.ru> 2.401.9.7-alt0.M24.1
- new version
- fix license
- add firewall script by default and fix daemon for this
- add live example by alliance.dmitriy at rambler dot ru

* Wed Oct 11 2006 Motsyo Gennadi <drool@altlinux.ru> 2.4.8.6-alt0.M24.1
- new version
- fix URL
- add ALT Linux 2.4 Master compatible daemon

* Tue Oct 10 2006 Motsyo Gennadi <drool@altlinux.ru> 2.016.7.6-alt0.M24.1
- initial build for ALT Linux 2.4 Master
