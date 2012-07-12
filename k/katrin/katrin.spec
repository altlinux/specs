%define katrin_user _katrin
%define katrin_group _katrin

# Uncomment this for enable debug
#%%set_strip_method none

Name: katrin
Version: 1.5.0
Release: alt4.2

Summary: Modular billing system

License: GPL
Group: Monitoring
Url: http://katrin.sf.net

Source: %name-%version.tar
Packager: Denis Klimov <zver@altlinux.org>

BuildRequires: libconfuse-devel libmysqlclient-devel ppp-devel postgresql-devel
BuildPreReq: chrpath
Requires: libMySQL net-tools sudo

%description
Modular billing system Katrin.
%description -l ru_RU.UTF8
Модульная биллинговая система Katrin.

%package devel
Summary: Development katrin header files
Group: Development/C
Requires: %name = %version-%release
%description devel
Development katrin header files
%description -l ru_RU.UTF8 devel
Заголовочные файлы языка C для библиотек katrin

%package monit
Summary: Monit config file for Katrin
Group: Monitoring
Requires: %name = %version-%release
Requires: monit
%description monit
Monit config file for Katrin
%description -l ru_RU.UTF8 monit
Конфигурационный файл monit для Katrin

%package -n kcdr-sender
Summary: Utility for send tel info by KCDR protocol
Group: Networking/Other
%description -n kcdr-sender
Utility for send tel info by KCDR protocol.
%description -l ru_RU.UTF8 -n kcdr-sender
Утилита для отправки информации о телефонных звонках по протоколу KCDR.

%package core
Summary: Core of Katrin billing system
Group: Networking/Other
%description core
Core of Katrin billing system
%description -l ru_RU.UTF8 core
Ядро биллинговой системы Katrin

%package traff
Summary: Traff module of Katrin billing system
Group: Networking/Other
%description traff
Traff module of Katrin billing system
%description -l ru_RU.UTF8 traff
Traff модуль биллинговой системы Katrin

%package tel
Summary: Tel module of Katrin billing system
Group: Networking/Other
%description tel
Traff module of Katrin billing system
%description -l ru_RU.UTF8 tel
Traff модуль биллинговой системы Katrin

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--with-pppd-auth
%make_build 

%install
%make_install DESTDIR=%buildroot install
install -pD -m 644 upgrade1.1_1.2.sql %buildroot%_datadir/%name/upgrade1.1_1.2.sql
install -pD -m 755 src/auth/katrin-auth-example %buildroot%_datadir/%name/katrin-auth-example
install -pD -m 744 src/init.d/katrind %buildroot%_initdir/katrind
install -pD -m 744 src/init.d/katrin-dropd %buildroot%_initdir/katrin-dropd
install -pD -m 744 src/tc/ppp/katrin-tc-ppp.sh %buildroot%_sysconfdir/ppp/ip-up.d/katrin-tc-ppp.sh
install -pD -m 0400 sudoers.d/katrin %buildroot%_sysconfdir/sudoers.d/katrin

install -pD -m 644 monitrc.d/katrind %buildroot%_sysconfdir/monitrc.d/katrind
mkdir -p %buildroot%_var/run/katrin

chrpath -r %_libdir/katrin \
	%buildroot%_libdir/pppd/libppp-auth-katrin.so.*
for i in %buildroot%_bindir/*
do
	chrpath -r %_libdir/katrin $i ||:
done

%pre
groupadd -r -f %katrin_group 2>/dev/null ||:
useradd -g %katrin_group -c 'Katrin billing system' -d /var/empty -s '/dev/null' \
-r %katrin_user 2>/dev/null || :

%post
%post_service katrind
%post_service katrin-dropd

%preun
%preun_service katrind
%preun_service katrin-dropd

%post monit
%post_service monit

%postun monit
%post_service monit

%files
%doc AUTHORS THANKS ChangeLog
%_bindir/*
%attr(710,root,%katrin_group) %_bindir/*-enable.sample
%attr(710,root,%katrin_group) %_bindir/*-drop.sample
%attr(740,root,%katrin_group) %_bindir/katrin-functions
%exclude %_bindir/kcdr-sender
%dir %_libdir/katrin
%_libdir/katrin/*.so*
%_libdir/*.so*
%_libdir/pppd/libppp-auth-katrin*.so*
%_datadir/%name/
%_initdir/*
%_sysconfdir/ppp/ip-up.d/*
%_sysconfdir/sudoers.d/katrin

%dir %_sysconfdir/%name
%config(noreplace) %attr(640,root,%katrin_group) %_sysconfdir/%name/*
%exclude %_sysconfdir/%name/kcdr-sender.conf
%dir %attr(1770,root,%katrin_group) %_var/run/katrin

%files devel
%_includedir/libkatrin*.h

%files monit
%_sysconfdir/monitrc.d/katrind

%files -n kcdr-sender
%_bindir/kcdr-sender
%config(noreplace) %attr(640,root,root) %_sysconfdir/%name/kcdr-sender.conf

%changelog
* Thu Jul 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt4.2
- move sudo config to /etc/sudoers.d

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt4.1
- Removed bad RPATH

* Wed Oct 05 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt4
- fix inherit with ALT gear repo

* Wed Oct 05 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt3
- update BuildRequires

* Wed Oct 05 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt2
- fix BuildRequires

* Mon Sep 26 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt1
- new version

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1.1
- rebuild with new libmysqlclient

* Fri Nov 12 2010 Denis Klimov <zver@altlinux.org> 1.4.2-alt1
- new version

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.4.1-alt1
- new version

* Fri Nov 20 2009 Denis Klimov <zver@altlinux.org> 1.4.0-alt1
- new version

* Sun Feb 22 2009 Denis Klimov <zver@altlinux.org> 1.3.0-alt1
- new version

* Wed Nov 26 2008 Denis Klimov <zver@altlinux.ru> 1.2.13-alt1
- new version

* Mon Nov 24 2008 Denis Klimov <zver@altlinux.ru> 1.2.12-alt1
- new version

* Tue Nov 18 2008 Denis Klimov <zver@altlinux.ru> 1.2.11-alt1
- new version

* Thu Nov 13 2008 Denis Klimov <zver@altlinux.ru> 1.2.10-alt1
- new version

* Wed Nov 12 2008 Denis Klimov <zver@altlinux.ru> 1.2.9-alt1
- new version

* Fri Nov 07 2008 Denis Klimov <zver@altlinux.ru> 1.2.8-alt1
- new version
- add subpackage devel
- separate libs from modules (move libs to %_libdir)
- add katrin-auth-example prog

* Wed Nov 05 2008 Denis Klimov <zver@altlinux.ru> 1.2.7-alt1
- new version

* Wed Oct 29 2008 Denis Klimov <zver@altlinux.ru> 1.2.6-alt1
- new version

* Tue Oct 28 2008 Denis Klimov <zver@altlinux.ru> 1.2.5-alt1
- new version

* Tue Oct 28 2008 Denis Klimov <zver@altlinux.ru> 1.2.4-alt1
- change Changelog to ChangeLog filename

* Mon Oct 27 2008 Denis Klimov <zver@altlinux.ru> 1.2.3-alt1
- add upgrade sql script
- set %_libdir/katrin as dir in files section
- add Changelog file to package

* Fri Oct 10 2008 Denis Klimov <zver@altlinux.ru> 1.2.2-alt1
- add %_libdir/katrin/ in files section
- change reconnect method in mysql db lib
- change type some fields in katrin.sql

* Fri Oct 10 2008 Denis Klimov <zver@altlinux.ru> 1.2.1-alt1
- fix crontab rules
- add new crontab rules for update today stats

* Sun Oct 05 2008 Denis Klimov <zver@altlinux.ru> 1.2.0-alt1
- new sheme of work with stats

* Tue Sep 30 2008 Denis Klimov <zver@altlinux.ru> 1.1.3-alt1
- fix wrong ip's in netflow info module for x86_64

* Tue Aug 19 2008 Denis Klimov <zver@altlinux.ru> 1.1.2-alt1
- fix memory leak in mysql db module

* Mon May 19 2008 Denis Klimov <zver@altlinux.ru> 1.1.1-alt1
- fix table names in sql stored procedures

* Sun May 04 2008 Denis Klimov <zver@altlinux.ru> 1.1.0-alt1
- add statistics by filters feature

* Mon Apr 28 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt2
- add store stat switch feature
- fix small memory leak

* Thu Mar 27 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC4
- add monit subpackage
- call drop and enable scripts with sudo
- add fee support
- add ip type access for traff service

* Tue Mar 18 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC3
- fix memory leak
- add --with-pppd-auth option
- add store_null_cost_stat param to service

* Thu Mar 13 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC2
- fix work with service filters
- fix wrong asserts
- small fixes sql schema

* Tue Mar 04 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC1
- add autotools support

* Thu Feb 07 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC0
- build for RC version

* Tue Dec 25 2007 Denis Klimov <zver@altlinux.ru> 0.12-alt1
- add config for netflow ti module
- add check blocked field in user struct
- add check netflow version

* Tue Dec 11 2007 Denis Klimov <zver@altlinux.ru> 0.11-alt1
- build with pkg-config
- add block for user which was drop

* Wed Dec 05 2007 Denis Klimov <zver@altlinux.ru> 0.10-alt1
- change db structure
- remove needless functions in code

* Tue Nov 27 2007 Denis Klimov <zver@altlinux.ru> 0.9.3-alt1
- fix Makefile and spec for build in x86_64 arch
- remove attr for libdir and bindir files

* Mon Nov 26 2007 Denis Klimov <zver@altlinux.ru> 0.9.2-alt1
- fix init scripts
- fix home dir for _katrin user

* Mon Nov 26 2007 Denis Klimov <zver@altlinux.ru> 0.9.1-alt1
- add _katrin user and group

* Thu Nov 22 2007 Denis Klimov <zver@altlinux.ru> 0.9-alt1
- change db structure
- add sumstats_month stored procedure

* Tue Nov 13 2007 Denis Klimov <zver@altlinux.ru> 0.8.2-alt1
- add stored procedure in db
- modify function sumstats in db module
- delete id field from stats table
- add new stats_cache table

* Fri Nov 09 2007 Denis Klimov <zver@altlinux.ru> 0.8.1-alt1
- build for 0.8.1

* Thu Nov 08 2007 Denis Klimov <zver@altlinux.ru> 0.8-alt1
- add auth by day of week
- fix memory leak

* Wed Oct 24 2007 Denis Klimov <zver@altlinux.ru> 0.7.3-alt1
- build for 0.7.3

* Thu Oct 18 2007 Denis Klimov <zver@altlinux.ru> 0.7.2-alt1
- build for 0.7.2

* Wed Oct 17 2007 Denis Klimov <zver@altlinux.ru> 0.7.1-alt1
- build for 0.7.1

* Sun Oct 07 2007 Denis Klimov <zver@altlinux.org> 0.7-alt1
- build for 0.7

* Thu Sep 06 2007 Denis Klimov <zver@altlinux.ru> 0.6-alt1
- add katrin-dropd daemon instead libkatrin-drop.so
- build for 0.6

* Wed Aug 22 2007 Denis Klimov <zver@altlinux.ru> 0.5.5-alt1
- build for 0.5.5

* Sun Aug 19 2007 Denis Klimov <zver@altlinux.org> 0.5.4-alt1
- build for 0.5.4

* Sun Aug 19 2007 Denis Klimov <zver@altlinux.org> 0.5.3-alt1
- build for 0.5.3

* Sat Aug 18 2007 Denis Klimov <zver@altlinux.org> 0.5.2-alt1
- build for 0.5.2

* Sat Aug 18 2007 Denis Klimov <zver@altlinux.org> 0.5.1-alt1
- build for 0.5.1

* Tue Aug 14 2007 Denis Klimov <zver@altlinux.ru> 0.5-alt1
- build for 0.5

* Fri Jul 13 2007 Denis Klimov <zver@altlinux.ru> 0.4.14-alt1
- install sql file into dir without version
- build for 0.4.14

* Thu Jul 12 2007 Denis Klimov <zver@altlinux.ru> 0.4.13-alt1
- build for 0.4.13

* Wed Jul 11 2007 Denis Klimov <zver@altlinux.ru> 0.4.12-alt1
- fix mode of init script
- build for 0.4.12

* Wed Jul 11 2007 Denis Klimov <zver@altlinux.ru> 0.4.11-alt1
- build for 0.4.11

* Fri Jul 06 2007 Denis Klimov <zver@altlinux.ru> 0.4.10-alt2
- change /etc/init.d to %%_initdir

* Wed Jul 04 2007 Denis Klimov <zver@altlinux.ru> 0.4.10-alt1
- add %%post and %%preun
- install init script

* Wed Jul 04 2007 Denis Klimov <zver@altlinux.ru> 0.4.9-alt1
- build for 0.4.9

* Fri Jun 29 2007 Denis Klimov <zver@altlinux.ru> 0.4.4-alt1
- build for 0.4.4

* Mon Jun 25 2007 Denis Klimov <zver@altlinux.ru> 0.4.3-alt1
- add config(noreplace) in files section
- build for 0.4.3

* Mon Jun 25 2007 Denis Klimov <zver@altlinux.ru> 0.4.2-alt1
- build for 0.4.2

* Thu Jun 21 2007 Denis Klimov <zver@altlinux.ru> 0.4-alt2
- fix install katrin.sql

* Tue Jun 19 2007 Denis Klimov <zver@altlinux.ru> 0.4-alt1
- build for 0.4

* Sun Jun 17 2007 Denis Klimov <zver@altlinux.org> 0.3.7-alt1
- build for 0.3.7

* Sat Jun 09 2007 Denis Klimov <zver@altlinux.org> 0.3.6-alt1
- build for 0.3.6

* Fri Jun 08 2007 Denis Klimov <zver@altlinux.ru> 0.3.4-alt1
- build for 0.3.4

* Thu May 31 2007 Denis Klimov <zver@altlinux.ru> 0.2.2-alt1
- add requires
- add katrin.sql

* Thu May 31 2007 Denis Klimov <zver@altlinux.ru> 0.2-alt1
- build for 0.2 version

* Wed Mar 28 2007 Denis Klimov <zver@altlinux.org> 0.1-alt1
- initial build

