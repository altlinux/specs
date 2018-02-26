%define _unpackaged_files_terminate_build 1
%define installdir %webserver_datadir/addon-modules/netams

%define prog_name netams

Name: netams
Version: 3.4.5
Release: alt3

Summary: Network Traffic Accounting and Management Service (NeTAMS)
Summary(ru_RU.UTF-8): NeTAMS - сервис контроля и учета сетевого трафика.

License: GPL
Group: Monitoring

Packager: Boris Savelev <boris@altlinux.org>

Url: http://www.netams.com

Source: http://netams.com/files/%name-%version.tar.gz
Source3: %prog_name-README.ALT.koi8-r
Source4: %prog_name.initd
Source5: %prog_name-stat.conf
Source6: %prog_name.cfg
Source7: %prog_name-stat.htaccess
Source8: %prog_name-Makefile
Source9: %prog_name-logrotate
Source10: %prog_name-mods_enable.conf
Source11: %prog_name-README.ALT.utf-8

Patch1: %prog_name-Makefile-3.4.2.patch
Patch2: %prog_name-doc-3.4.2.patch
Patch3: %prog_name-src-3.4.2.patch
Patch4: %prog_name-x86-64.patch
Patch5: %prog_name-admin-3.4.2.patch
Patch9: %prog_name-html_fix-3.4.2.patch
Patch10: %prog_name-schedule_fix.patch
Patch11: %prog_name-image_fix-3.4.3.patch
Patch12: %prog_name-image_fix2-3.4.5.patch
Patch13: %prog_name-configure_glib-3.4.5.patch

BuildPreReq: webserver-common rpm-macros-apache2 rpm-macros-apache

# Automatically added by buildreq on Thu Dec 11 2008 (-bi)
BuildRequires: gcc-c++ iptables-devel libMySQL-devel libdb1-devel libpam-devel
BuildRequires: perl-CGI perl-Crypt-GeneratePassword perl-DBI perl-GD-Graph
BuildRequires: postgresql-devel rrd-perl libpcap-devel glib2-devel libssl-devel

%add_findreq_skiplist perl(netams_api.pl) perl(statistic.pl)

Requires: %prog_name-server = %version-%release
Requires: %prog_name-apache2 = %version-%release
Requires: %prog_name-common = %version-%release

%package -n %prog_name-apache2
Summary: NeTAMS web configs for apache2
Summary(ru_RU.UTF-8): Настройки NeTAMS для apache2
BuildArch: noarch
Requires: apache2-common

License: GPL
Group: Monitoring

Requires: apache2 >= 2.2.4-alt12
Requires: %prog_name-common = %version-%release
Provides: perl(netams_api.pl) perl(statistic.pl)

%package -n %prog_name-apache
Summary: NeTAMS web configs for apache
Summary(ru_RU.UTF-8): Настройки NeTAMS для apache
BuildArch: noarch
Requires: apache-common

License: GPL
Group: Monitoring

Requires: apache
Requires: %prog_name-common = %version-%release
Provides: perl(netams_api.pl) perl(statistic.pl)

%package -n %prog_name-server
Summary: NeTAMS server
Summary(ru_RU.UTF-8): Сервер NeTAMS

License: GPL
Group: Monitoring

Requires: telnet

%package -n %prog_name-common
Summary: NeTAMS metapackage
Summary(ru_RU.UTF-8): Метапакет NeTAMS
BuildArch: noarch

Requires: webserver-common

License: GPL
Group: Monitoring

%description
NeTAMS is a Network Traffic Accounting and Monitoring Software.
It collects an IP traffic information flowing via your PC/UNIX or Cisco router,
filters it, aggregates, stores onto HASH/SQL database, and makes SMTP/HTML
reports to site administrator. Anoter features are flexible policy targets,
firewalling, access control, quotas, scheduler and much much more.

%description -l ru_RU.UTF-8
NeTAMS - это программа, которая занимается контролем и учетом сетевого траффика,
проходящего через ваш сервер.
Не секрет, что универсального средства учета траффика не существует.
Множество программ, программулек и скриптов, которые можно легко разыскать в
интернете, могут решить ограниченный круг задач, тот который заложил при
создании автор. Такие решения обычно не масштабируемы, легко настраиваются и
трудно управляются. Практически невозможно добиться от такой программы хоть
чуть-чуть большего, чем запланированно конструкцией. Большинство "скриптов" не
переживают перезагрузки сервера и вряд ли могут обеспечить информацию о траффике
за позавчера. NeTAMS пробует сделать для вас то, что было возможно раньше за
большие деньги. Эта программа будет учитывать потоки IP-траффика, проходящие
через Unix-маршрутизатор, в том числе с трансляцией адресов, сохранять
статистику в базе, предоставлять контроль доступа для отдельных машин и для
групп компьютеров.
NeTAMS собирает в себя потоки информации о траффике, IP и не только, например,
путем перехвата проходящих пакетов через сетевой интерфейс (libpcap), divert
socket (ipfw divert), поток NetFlow или любой другой модуль. После обработки и
суммирования данных информация о статистике попадает в БД, откуда любая
статистика может быть запрошена посредством прямого запроса или через
веб-интерфейс. Попутно может осуществляться контроль доступа, квот и прав
пользования. Управление программой осуществляется посредством установления
соединения на некий TCP порт сервера клиентом telnet и ввода соответствующих
команд. Имеется также веб-интерфейс отображения статистики.

%description -n %prog_name-apache2
Apache2 config files nedded to view NeTAMS logs.

%description -n %prog_name-apache2 -l ru_RU.UTF-8
Конфигурационные файлы apache2 для отображения NeTAMS.

%description -n %prog_name-apache
Apache config files nedded to view NeTAMS logs.

%description -n %prog_name-apache -l ru_RU.UTF-8
Конфигурационные файлы apache для отображения NeTAMS.

%description -n %prog_name-server
Server part of package NeTAMS

%description -n %prog_name-server -l ru_RU.UTF-8
Серверная часть установки NeTAMS

%description -n %prog_name-common
Metapackage gives needed provides.

%description -n %prog_name-common -l ru_RU.UTF-8
Метапакет для формирования зависимостей.

%prep
%setup -q

# find . -type f | grep -v Makefile | egrep -v "*\.sh" | xargs %__subst 's/.$//'

%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p2
%patch13 -p1
# cp %SOURCE8 ./Rules.make
chmod -x doc/*

%build
%make_build

%install

mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_docdir/%name-%version/oracle
mkdir -p %buildroot%_docdir/%name-common-%version
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/netams
mkdir -p %buildroot%apache2_addonconfdir
mkdir -p %buildroot%apache2_mods_start
mkdir -p %buildroot%apache_addonconfdir
mkdir -p %buildroot%_sysconfdir/logrotate.d
mkdir -p %buildroot%_logdir/netams
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%installdir/admintool
mkdir -p %buildroot%installdir/stat

install -m600 addon/.netamsctl.rc %buildroot%_sysconfdir/.netamsctl.rc
sed '{s|@APACHE@|%installdir|}' %SOURCE6 > conf
install -m600 conf %buildroot%_sysconfdir/netams/netams.conf
install -m644 addon/ru-networks.txt %buildroot%_sysconfdir/netams/ru-networks
install -m755 %SOURCE4 %buildroot%_initdir/netams
install -m750 src/netamsctl %buildroot%_sbindir
install -m750 src/netams %buildroot%_sbindir
install -m750 src/flowprobe %buildroot%_sbindir
install doc/{flowprobe.8,netams.8,netamsctl.8} %buildroot%_man8dir
install -m644 INSTALL %buildroot%_docdir/%name-%version/
sed '{s|@APACHE@|%installdir|}' %SOURCE5 > apache_conf
install -m644 apache_conf %buildroot%apache2_addonconfdir/A.netams-stat.conf
install -m644 apache_conf %buildroot%apache_addonconfdir/netams-stat.conf
install %SOURCE10 %buildroot%apache2_mods_start/900-netams.conf

install -m644 doc/TODO.txt %buildroot%_docdir/%name-%version/TODO
install -m644 doc/README %buildroot%_docdir/%name-%version/
install -m644 addon/mysql_rotate.pl %buildroot%_docdir/%name-%version/
install -m644 addon/access-script-linux.README %buildroot%_docdir/%name-%version/
install -m644 addon/postgresql_schema.sql %buildroot%_docdir/%name-%version/
install -m644 addon/cardtool_schema.sql %buildroot%_docdir/%name-%version/
install -m644 addon/cardtool_schema-Pg.sql %buildroot%_docdir/%name-%version/
install -m644 addon/ua-networks-get.sh %buildroot%_docdir/%name-%version/
install -m644 addon/oracle/* %buildroot%_docdir/%name-%version/oracle
install -m644 cgi-bin/admin/*.sql %buildroot%_docdir/%name-common-%version/
rm -f cgi-bin/admin/*.sql
cp -R cgi-bin/* %buildroot%installdir/admintool/
chmod  0755 %buildroot%installdir/admintool/*.cgi
chmod  0755 %buildroot%installdir/admintool/admin/*.cgi
ln -s ../admintool/admintool.cgi %buildroot%installdir/stat/admintool.cgi
ln -s ../admintool/admin/ %buildroot%installdir/stat/admin
ln -s ../admintool/images/ %buildroot%installdir/stat/images
cp %SOURCE7 %buildroot%installdir/stat/.htaccess
cp %SOURCE3 %buildroot%_docdir/%name-%version/
cp %SOURCE11 %buildroot%_docdir/%name-%version/
cp %SOURCE9 %buildroot%_sysconfdir/logrotate.d/netams

%files -n %prog_name-server
%_sbindir/*
%_initdir/*
%dir%attr(0700,root,root)%_sysconfdir/netams
%config(noreplace)%attr(0600,root,root)%_sysconfdir/.netamsctl.rc
%config(noreplace)%attr(0600,root,root)%_sysconfdir/netams/netams.conf
%attr(0644,root,root)%_sysconfdir/netams/ru-networks
%_sysconfdir/logrotate.d/*
%attr(0750,root,root)%_logdir/netams
%_man8dir/*
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%files

%files -n %prog_name-common
%dir%attr(0750,root,%webserver_group)%installdir
%dir%attr(0750,root,%webserver_group)%installdir/stat
%dir%attr(0750,root,%webserver_group)%installdir/admintool
%dir%attr(0750,root,%webserver_group)%installdir/admintool/admin
%dir%attr(0750,root,%webserver_group)%installdir/admintool/images
%config(noreplace)%attr(750,root,%webserver_group)%installdir/admintool/config.cgi
%config(noreplace)%attr(750,root,%webserver_group)%installdir/admintool/admin/config.cgi
%attr(-,root,%webserver_group)%installdir/admintool/activate.cgi
%attr(-,root,%webserver_group)%installdir/admintool/activate.tmpl
%attr(-,root,%webserver_group)%installdir/admintool/admintool.cgi
%attr(-,root,%webserver_group)%installdir/admintool/login.cgi
%attr(-,root,%webserver_group)%installdir/admintool/netams_api.pl
%attr(-,root,%webserver_group)%installdir/admintool/netams_example.cgi
%attr(-,root,%webserver_group)%installdir/admintool/netams_graph.cgi
%attr(-,root,%webserver_group)%installdir/admintool/netams_html.cgi
%attr(-,root,%webserver_group)%installdir/admintool/russian.res
%attr(-,root,%webserver_group)%installdir/admintool/statistic.pl
%attr(-,root,%webserver_group)%installdir/admintool/usertool.cgi
%attr(0640,root,%webserver_group)%installdir/admintool/admin/.htaccess
%attr(-,root,%webserver_group)%installdir/admintool/admin/access.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/account.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/cardtool.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/graph.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/index.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/login.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/monitor.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/netams.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/plan.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/policy.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/quota.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/radius.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/rrdgraph.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/russian.res
%attr(-,root,%webserver_group)%installdir/admintool/admin/showusercard.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/showusercard.tmpl
%attr(-,root,%webserver_group)%installdir/admintool/admin/statistic.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/subplan.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/unit.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/user.cgi
%attr(-,root,%webserver_group)%installdir/admintool/admin/view.cgi
%attr(-,root,%webserver_group)%installdir/admintool/images/*
%attr(-,root,%webserver_group)%installdir/stat/admintool.cgi
%attr(-,root,%webserver_group)%installdir/stat/admin
%attr(-,root,%webserver_group)%installdir/stat/images
%attr(0640,root,%webserver_group)%installdir/stat/.htaccess
%_docdir/%name-common-%version/billing_users_table.sql
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/netams-common-%version 

%files -n %prog_name-apache2
%config(noreplace) %apache2_addonconfdir/A.netams-stat.conf
%config(noreplace) %apache2_mods_start/900-netams.conf

%files -n %prog_name-apache
%config(noreplace) %apache_addonconfdir/netams-stat.conf

%post -n %prog_name-server
%post_service %name

%post -n %prog_name-apache2
%post_service httpd2
echo '---------------------------------------------'
echo 'Install needed perl-DBD-* packages before use'
echo '---------------------------------------------'

%post -n %prog_name-apache
%post_service httpd

%preun -n %prog_name-server
%preun_service %name

%postun -n %prog_name-apache2
%post_service httpd2

%postun -n %prog_name-apache
%post_service httpd

%changelog
* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.5-alt3
- fix build

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.5-alt2
- rebuild with new libssl.so.10/libmysqlclient.so.16

* Sun Mar 14 2010 Boris Savelev <boris@altlinux.org> 3.4.5-alt1
- new version

* Wed Dec 30 2009 Boris Savelev <boris@altlinux.org> 3.4.3-alt3
- add webserver-common to requires %prog_name-common (closes #22428)

* Sun Nov 29 2009 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.3-alt2
- Update requirements
- Split README.ALT and and info about web (closes #22391)
- Update image paths (closes #22393)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for netams-common
  * postclean-05-filetriggers for spec file

* Mon Aug 10 2009 Boris Savelev <boris@altlinux.org> 3.4.3-alt1
- new version (3.4.3)

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 3.4.2c-alt1
- new version (3.4.2c)

* Sun Feb 08 2009 Boris Savelev <boris@altlinux.org> 3.4.2-alt1
- new version (3.4.2)

* Thu Dec 11 2008 Boris Savelev <boris@altlinux.org> 3.4.1rc2-alt2
- fix init script (forget new -f option)
- move cgi scripts to common (become noarch)
- fix license to GPL
- add subpackage apache

* Sun Dec 07 2008 Boris Savelev <boris@altlinux.org> 3.4.1rc2-alt1
- new version
- fix x68_64 build

* Sat Dec 06 2008 Boris Savelev <boris@altlinux.org> 3.4.1rc1-alt1
- new version
- fix apache2 macros

* Thu Dec 27 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc2-alt5
- Try to fix scheduler service
- Add install info

* Sat Dec 15 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc2-alt4
- Fix HTML service bug (#13487)
- Fix sHtmlAction (use aMalloc) and sHSafeMkdir (strange creation) functions

* Sun Dec 2 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc2-alt3
- Fix bug #13399
- Fix bug #13423
- Fix bug #13424
- Fix bug #13425
- Fix bug #13426
- Divide NeTAMS in three packages:
  * netams (full install)
  * netams-server (only server)
  * netams-apache2 (only apache2 client)
- Add PosgreSQL card schema and PosgreSQL web access

* Wed Oct 24 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc2-alt2
- copy apache2-devel to BuildPreReq
- change russian description to UTF-8

* Thu Jun 07 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc2-alt1
- New version
- Check used patches

* Fri May 04 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt7
- Fix src patch

* Sat Apr 28 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt6
- Enable apache2 config and fix access (bug #11633)
- Rename apache_webmaster group to apache_group
- Fix 'user' and 'no user' command execution (bug #11636)
- Set 'noreplace' to two files 'config.cgi'
- Add module enabling

* Thu Apr 12 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt5
- Change apache2 config name
- Config for apache2 is now named as needed
- Set 'stat' directory outside apache2 default root directory
  (to /var/www/apache2/addmon-modules/netams)
- Add HASH storage (via libdb1).

* Thu Apr 05 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt4
- Change init script to 'off by default'
- Change start level from 90 to 11

* Wed Apr 04 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt3
- Fix apache2 config due to bug #11329
- Replace internal macros with real names
- Fix doc info
- Fix previous Changelog record

* Tue Apr 03 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt2
- Fix bug #11300 (now name of the config file is %_sysconfdir/netams/netams.conf)
  (thanks to Artem Zolochevskiy)
- Fix bug in netamsctl execution (add ~/.netamsctrl.rc as config file)
- Fix doc due to bug #11300

* Tue Mar 27 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.4.0rc1-alt1
- New version
- Cleanup patches
- Remove ipfw2netflow (not built for linux)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.3.5-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Dec 21 2006 Sergei Epiphanov <serpiph@altlinux.ru> 3.3.5-alt3
- Fix x86_64 build
- Split patche into 2 parts: common patch and x86_64 patch
- Rebuild for apache2

* Tue Dec 19 2006 Sergei Epiphanov <serpiph@altlinux.ru> 3.3.5-alt2
- Fixing build of new version

* Fri Dec 15 2006 Sergei Epiphanov <serpiph@altlinux.ru> 3.3.5-alt1
- New version

* Thu Jan 26 2006 Anton Korbin <ahtoh@altlinux.ru> 3.3.2-alt1
- Bugs fixed, new version

* Mon Dec 05 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.1a-alt1
- Bugs fixed, new version

* Mon Nov 07 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.0-alt4
- Provides fixed

* Fri Nov 04 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.0-alt2
- AdminTool added

* Thu Oct 06 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.0-alt1
- New stable version, but freeradius not supported

* Wed Sep 07 2005 Anton Korbin <ahtoh@altlinux.ru> 3.3.0.rc2-alt1
- New version, but freeradius not supported

* Sat Apr 09 2005 Anton Korbin <ahtoh@altlinux.ru> 3.2.2-alt1
- New version, add billing system, add log-rotate

* Tue Feb 22 2005 Anton Korbin <ahtoh@altlinux.ru> 3.2.1-alt1
- New version

* Tue Feb 22 2005 Anton Korbin <ahtoh@altlinux.ru> 3.2.0-alt1
- New version

* Tue Oct 12 2004 Anton Korbin <ahtoh@altlinux.ru> 3.1.1829-alt1.2
- Add doc in pdf, netams-README.ALT correct, bugfix with postgres

* Fri Jul 30 2004 Anton Korbin <ahtoh@altlinux.ru> 3.1.1829-alt1.1
- netams.rc bug fix.

* Sat Jul 03 2004 Anton Korbin <ahtoh@altlinux.ru> 3.1.1829-alt1
- Included are HTML files permission patch and new russian network prefix table.

* Thu May 13 2004 Anton Korbin <ahtoh@altlinux.ru> 3.1.1828-alt1.1
- Fix changelog problem

* Tue Apr 06 2004 Anton Korbin <ahtoh@altlinux.ru> 3.1.1828-alt1
- First build for ALTLinux Sisyphus
