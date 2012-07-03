%define dist_tag %(cut -d" " -f3 < /etc/altlinux-release)
%define apache_group apache
%define apache_user apache
%define apache2_group apache2
%define lighttpd_group lighttpd
%define maillog_group adm
%define mailgraph_user mailgraph
%define mailgraph_group mailgraph
%define mailgraph_data %_localstatedir/%name

Name: mailgraph
Version: 1.13
Release: alt3

Summary: Simple mail statistics for Postfix
License: GPL
Group: Monitoring

Url: http://mailgraph.schweikert.ch
Source0: %name-%version.tar
Source1: %name.conf
Source2: %name.htaccess
Source3: %name.init-Master
Source4: %name.init-Sisyphus
Source5: %name.sysconfig
Source6: A.%name.conf
Source7: %name.control
Source8: 100-mailgraph.conf
Patch0: %name-%version-%release.patch

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2005 (-bi)
BuildRequires: freetype2 perl-File-Tail rrd-perl

Summary(ru_RU.KOI8-R): Простая статистика для Postfix
Summary(uk_UA.KOI8-U): Проста статистика для Postfix
Summary(pl): Proste statystyki dla Postfiksa

# should be looking whether /etc/init.d/functions-compat exists...
%if_with Master
  %define dist_tag Master
%endif

%if_with Sisyphus
  %define dist_tag Sisyphus
%endif

#%if "%dist_tag" == ""
#  %define dist_tag %(cut -d" " -f3 < /etc/altlinux-release)
#%endif

%description
Mailgraph is a very simple mail statistics RRDtool frontend for
Postfix that produces daily, weekly, monthly and yearly graphs of
received/sent and bounced/rejected mail.

%description -l ru_RU.KOI8-R
Mailgraph -- простой интерфейс для сбора статистики по лог-файлам
Postfix, основанный на RRDtool.  Производит суточные, недельные,
месячные и годовые графики по полученной/отосланной и отвергнутой по
разным причинам почте.

%description -l uk_UA.KOI8-U
Mailgraph -- простий ╕нтерфейс для збирання статистики з лог-файл╕в
Postfix, що базу╓ться на RRDtool.  Робить граф╕ки за добу, тиждень,
м╕сяць та р╕к по отриман╕й/в╕д╕слан╕й та в╕дкинут╕й з р╕зних причин
пошт╕.

%description -l pl
Mailgraph to prosty frontend na RRDtool do statystyk pocztowych dla
Postfiksa. Produkuje wykresy dzienne, tygodniowe, miesiЙczne i roczne
poczty wysЁanej/odebranej i odbitej/odrzuconej.

%package common
Summary: Simple mail statistics for Postfix
Group: Monitoring
Requires: postfix, perl-File-Tail, rrd-perl
Obsoletes: mailgraph < 1.12-alt2

%description common
Mailgraph is a very simple mail statistics RRDtool frontend for
Postfix that produces daily, weekly, monthly and yearly graphs of
received/sent and bounced/rejected mail.

Don't forget to install %name-apache package for get working mailgraph
with Apache 1.3.x webserver.

%package apache
Summary: apache-related config and control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, apache

%description apache
%summary

%package apache2
Summary: apache2-related config and control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, apache2

%description apache2
%summary

%package lighttpd
Summary: lighttpd-related control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, lighttpd

%description lighttpd
%summary

%package nginx
Summary: nginx-related control(8) call
Group: Monitoring
Requires: %name-common = %version-%release, nginx

%description nginx
%summary


%prep
%if "%dist_tag" == ""
  echo "*** Unable to determine target distribution"
  echo "*** use --with Master or --with Sisyphus"
  exit 1
%endif
%setup	-q
%patch0 -p1

%install
subst "s,'mailgraph.cgi','index.cgi'," %name.cgi

install -d -m1775 %buildroot{%mailgraph_data/tmp,%_var/run/%name,%_logdir/%name}
install -d %buildroot{%_sbindir,%_initdir,%_var/www/cgi-bin/%name}

# install control file
install -pDm0755 %SOURCE7 %buildroot%_controldir/%name

install %name.cgi %buildroot%_var/www/cgi-bin/%name/index.cgi
install %name.pl %buildroot%_sbindir/%name.pl

install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -pD -m0644 %SOURCE6 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
install -pD -m0644 %SOURCE8 %buildroot%_sysconfdir/httpd2/conf/mods-start.d/100-%name.conf
install -pD -m0644 %SOURCE2 %buildroot%_var/www/cgi-bin/%name/.htaccess
install -pD -m0644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name

%if "%dist_tag" == "Master"
  install %SOURCE3 %buildroot%_initdir/%name
%else
  install %SOURCE4 %buildroot%_initdir/%name
%endif

%pre common
%_sbindir/groupadd -r -f %mailgraph_group 2>/dev/null ||:
%_sbindir/useradd -g %mailgraph_group -G %maillog_group \
	-c 'Mailgraph the Postfix Logfile Analyzer' \
	-d %mailgraph_data -s /dev/null -r %mailgraph_user \
	2>/dev/null ||:
[ ! -d %_var/run/mailgraph ] || find %mailgraph_data -type f -iname \*.rrd -print0 \
	|xargs -0 chown -f %mailgraph_user -- >/dev/null 2>&1 ||:
# dump facility state before upgrading package
if [ $1 -eq 2 ]; then
        %_sbindir/control-dump %name >/dev/null 2>&1 ||:
fi

%post common
%_sbindir/usermod -G adm$(groups %mailgraph_user | cut -d ':' -f 2 | sed 's/ /,/g') %mailgraph_user ||:
%post_service %name
# restore facility state after upgrading package
if [ $1 -eq 2 ]; then
        %_sbindir/control-restore %name >/dev/null 2>&1 ||:
fi

%preun common
%preun_service %name

%post apache
%_sbindir/apxs -e -a -n expires %_libdir/apache/mod_expires.so >/dev/null 2>&1 ||:
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name apache
fi
%_initdir/httpd condrestart 1>&2
find %mailgraph_data/tmp -mindepth 1 -type d -print0 \
	|xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%postun apache
%_initdir/httpd reload >/dev/null 2>&1 ||:

%post apache2
a2chkconfig
%_initdir/httpd2 reload >/dev/null 2>&1 ||:
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name apache2
fi
find %mailgraph_data/tmp -mindepth 1 -type d -print0 \
	|xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%postun apache2
if [ $1 -eq 0 ]; then
	a2chkconfig
	%_initdir/httpd2 reload >/dev/null 2>&1 ||:
fi

%post lighttpd
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name lighttpd
fi
find %mailgraph_data/tmp -mindepth 1 -type d -print0 \
	|xargs -0 rm -rf -- >/dev/null 2>&1 ||:

%post nginx
# set facility at first package install
if [ $1 -eq 1 ]; then
        %_sbindir/control %name nginx
fi

%triggerun -n %name-apache -- %name-apache < 1.13-alt1
%_sbindir/control %name apache

%triggerun -n %name-apache2 -- %name-apache2 < 1.13-alt1
%_sbindir/control %name apache2

%triggerun -n %name-lighttpd -- %name-lighttpd < 1.13-alt1
%_sbindir/control %name lighttpd

%triggerpostun -- %name <= 1.12-alt1
# fix stale actions
subst "/Include conf\/addon-modules\/mailgraph.conf/d" %_sysconfdir/httpd/conf/httpd.conf

%triggerpostun -- %name <= 1.2-alt1
# work around update problem caused by postun script deleting user/group
%_sbindir/groupadd -r -f %mailgraph_group 2>/dev/null ||:
%_sbindir/useradd -g %mailgraph_group -G %maillog_group \
	-c 'Mailgraph the Postfix Logfile Analyzer' \
	-d %mailgraph_data -s /dev/null -r %mailgraph_user \
	2>/dev/null ||:
find %_var/run/mailgraph %mailgraph_data %_var/www/cgi-bin/%name -nouser -print0 \
	-exec chown %mailgraph_user -- \{\} \;

%files common
%_sbindir/%name.pl
%_initdir/%name
%config %_controldir/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(1771,root,%mailgraph_group) %_logdir/%name
%dir %attr(1771,root,%mailgraph_group) %_var/run/%name
%dir %attr(1771,root,%mailgraph_group) %mailgraph_data
%dir %attr(1770,root,root) %mailgraph_data/tmp
%dir %attr(0755,root,root) %_var/www/cgi-bin/%name
%attr(0755,%mailgraph_user,root) %_var/www/cgi-bin/%name/index.cgi
%config(noreplace) %_var/www/cgi-bin/%name/.htaccess
%doc README CHANGES

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf
%_sysconfdir/httpd2/conf/mods-start.d/100-%name.conf

%files lighttpd

%files nginx

%changelog
* Wed Apr 18 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.13-alt3
- Fix group name of nginx http server in control(8) file (reported by
  Dmitry V. Levin)
- Supress output of apxs in %%post apache (Closes: #11544)
- Supress output of httpd2 reload in %%post apache2 (Closes: #11545)
- Also supress same output in %%postun
- Supress output of control-restore(8) call

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.13-alt2
- Do not start on any runlevel by default

* Mon Apr 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.13-alt1
- Updated to 1.13
- Change mod_expires activation way accordind to new apache2 scheme
- Also activate mod_cgi after %name-apache2 package installation
- Fix filename of apache2-related config
- Implemented control(8) support for switching permissions of tmp-dir between
  webserwers

* Fri Feb 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.12-alt4
- Force add mailgraph pseudouser to %%maillog_group
- Silently discard warning if .rrd files wasn't found
- Don't use %%__ macroses
- Intergate patches

* Wed Feb 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.12-alt3
- Added -apache2 and -lighttpd packages
- Relaxed permissions of cgi-script
- Corrected %%pre-script (Closes: #8943)

* Thu Jan 19 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.12-alt2
- Fix ownership of rrd-files (since 1.12-alt1 we do't run as root)
- Added mailgraph-1.12-alt-default_maillog.patch:
  + monitor /var/log/maillog instead of /var/log/syslog by default
- MAIL_LOG and DAEMON_LOG initscript variables moved to
  /etc/sysconfig/mailgraph
- Default daemon log changed to /var/log/mailgraph/mailgraph.log
- Changed permissions of /var/run/mailgraph/, /var/lib/mailgraph/,
  /var/www/cgi-bin/mailgraph/ due to ALT Security Policy
- Don't package unneeded directory /var/lib/mailgraph/imgs/
- Packaging changes:
  + apache-related config and temp dir for images moved to -apache subpackage
  + other stuff moved to -common (and it don't contains dependency on
  apache)
- WARNING: if you upgrading from previos version and use Apache
  web-server, DON'T FORGET to install mailgraph-apache!
- Spec update

* Wed Oct 26 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.12-alt1
- Updated to version 1.12
- .htaccess packaged as %%config(noreplace)
- Some spec fixes
- Init-script fixes (warning! initscript for Master 2.4 still broken!)
- Some configution parameters placed into /etc/sysconfig/mailgraph
- Apache's mailgraph.conf moved to /etc/httpd/conf/addon-modules.d
- mailgraph-1.3-alt.patch replaced with mailgraph-1.12-alt.patch
- Added dependency on apache

* Tue Apr 20 2004 Serge A. Volkov <vserge@altlinux.ru> 1.8-alt1
- Update to new version 1.8

* Fri Jan 30 2004 Michael Shigorin <mike@altlinux.ru> 1.6-alt1
- 1.6
- removed my silly {user,group}del from %%preun; new trigger :(
- auto-select Master/Sisyphus initscripts (not ideal though)
- added mod_expires activation
- BuildArch: noarch
- spec cleanup

* Wed Jun 11 2003 Nick Fedchik <nick@fedchik.org.ua> 1.3-alt1
- Updated sources to version 1.3
- Changed place of mailgraph.conf to /etc/httpd/conf/addon-modules
- Changed place of mailgraph.cgi to /var/www/cgi-bin/mailgraph
- Other minor fixes

* Tue Jun 10 2003 Michael Shigorin <mike@altlinux.ru> 1.2-alt2
- added empty %%mailgraph_data/mailgraph.rrd
- IfModule'ized mod_expire statements in mailgraph.conf
- thanks Nick Fedchik <nick at fedchik org ua> for reminding me :)

* Sun Mar 09 2003 Michael Shigorin <mike@altlinux.ru> 1.2-alt1
- built for ALT Linux
- spec adapted from PLD <feedback@pld.org.pl> (0.20)
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  blues, grzegorz, kloczek, qboosh 
- heavy spec cleanup
- mailgraph.pl no longer runs as root
- access from localhost only by default
