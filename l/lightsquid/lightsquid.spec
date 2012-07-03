Name: lightsquid
Version: 1.8
Release: alt1

Summary: Lite, small size and fast log analizer for squid proxy
Summary(ru_RU.UTF-8): Легкий, маленький и быстрый анализатор лога для прокси сервера squid
License: GPL
Group: Networking/WWW
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Url: http://lightsquid.sourceforge.net/
Source: http://prdownloads.sourceforge.net/lightsquid/%name-%version.tgz
BuildRequires: perl-CGI perl-GD2
Requires: webserver

BuildArch: noarch

%define apache_home %_var/www/html
%define apache_confdir %_sysconfdir/httpd/conf
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define lightsquid_confdir %_sysconfdir/lightsquid
%define lightdir %apache_home/lightsquid

##%set_strip_method none

%description
%name -- light squid report parser and visualyzer, generate sort of report
        light
        fast
        no database required
        no additional perl modules
        small disk usage
        template html - you can create you own look;

%description -l ru_RU.UTF-8
%name -- легкий, быстрый анализатор лога прокси сервера squid.
	 Не требует базы данных
	 Не требует дополнительных модулей perl
	 Использует шаблоны html

%package apache
Summary: Config %name for apache
Summary(ru_RU.UTF-8): Конфигурационный файл %name для вебсервера apache
License: GPL
Group: System/Servers
Requires: %name = %version-%release
Requires: apache

%description apache
Config %name for apache

%prep
%setup -n %name-%version

%__subst "s|/var/www/html/lightsquid/lang|%_datadir/%name/lang|g"  lightsquid.cfg
%__subst "s|/var/www/html/lightsquid/tpl|%_datadir/%name/tpl|g" lightsquid.cfg
%__subst "s|/var/www/html/lightsquid/ip2name|%_datadir/%name/ip2name|g" lightsquid.cfg
%__subst "s|/var/www/html/lightsquid/report|%_localstatedir/%name|g" lightsquid.cfg
%__subst "s|\$cfgpath             =\"/var/www/html/lightsquid|\$cfgpath             =\"%lightsquid_confdir|g" lightsquid.cfg
%__subst "s|\$lockpath            =\$reportpath|\$lockpath            =\"%_lockdir/%name\"|g" lightsquid.cfg
%__subst 's|require "ip2name|require "$ip2namepath|g' lightparser.pl
%__subst "s|lightsquid.cfg|%lightsquid_confdir/lightsquid.cfg|g" *.cgi *.pl
%__subst "s|common.pl|%_datadir/%name/common.pl|g" *.cgi *.pl
%__subst "s|/etc/squid/users.txt|/etc/lightsquid/users.txt|g" ip2name/ip2name.*

iconv -f WINDOWS-1251 -t UTF8 lang/ru.lng > lang/ru-utf8.lng
%__subst "s|windows-1251|utf8|g" lang/ru-utf8.lng

	
%install
%__mkdir_p %buildroot%_sbindir
%__mkdir_p %buildroot%lightsquid_confdir
%__mkdir_p %buildroot%_sysconfdir/cron.d
%__mkdir_p %buildroot%_datadir/%name/{lang,ip2name,tpl}
%__mkdir_p %buildroot%apache_addonconfdir
%__mkdir_p %buildroot%_localstatedir/%name
%__mkdir_p %buildroot%lightdir
%__mkdir_p %buildroot%_lockdir/%name

# install bin
%__install -p -m 755 lightparser.pl %buildroot%_sbindir/

# install configs
%__install -p -m 644 lightsquid.cfg %buildroot%lightsquid_confdir/lightsquid.cfg
%__install -p -m 644 group.cfg.src %buildroot%lightsquid_confdir/group.cfg
%__install -p -m 644 realname.cfg %buildroot%lightsquid_confdir/realname.cfg
%__cat << EOF > %buildroot%apache_addonconfdir/lightsquid.conf
<Directory "/var/www/html/lightsquid">
    Options FollowSymLinks +ExecCGI
    AddHandler cgi-script .cgi
</Directory>
EOF

# install cron
%__cat << EOF > %buildroot%_sysconfdir/cron.d/lightsquid
55 * * * *     lightsquid /usr/sbin/lightparser.pl today
EOF


# install lib
%__install -p -m 644 common.pl %buildroot%_datadir/%name/
%__install -p -m 755 check-setup.pl %buildroot%_datadir/%name/
%__install -p -m 644 lang/[^A-Z]*.lng %buildroot%_datadir/%name/lang/
%__install -p -m 644 ip2name/[^A-Z]* %buildroot%_datadir/%name/ip2name/
%__cp -aRf tpl/[^A-Z]* %buildroot%_datadir/%name/tpl/
##%__install -p -m 644 tpl/[^A-Z]* %buildroot%_datadir/%name/tpl/

# install web
#%__install -p -m 644 .htaccess %buildroot%apache_home/%name/
%__install -p -m 755 [^A-Z]*.cgi %buildroot%apache_home/%name/

%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:
/usr/sbin/useradd -r -g %name -G squid -d %_localstatedir/%name -c 'Log parser lightsquid' -s /bin/false -n %name &> /dev/null ||:

%post
if [[ -d %lightdir/report ]]; then
    mv %lightdir/report/* %_localstatedir/%name
##    rm -f %lightdir/report
    echo "Reports move from %lightdir/report to %_localstatedir/%name"
fi
find %_localstatedir/%name -print0 | xargs -r0 chown %name:%name

%post apache
%post_service httpd

%files
%doc doc/*
%_sbindir/*
%_datadir/%name
%dir %lightsquid_confdir
%config(noreplace) %verify(not md5 size mtime) %lightsquid_confdir/lightsquid.cfg
%config(noreplace) %verify(not md5 size mtime) %lightsquid_confdir/group.cfg
%config(noreplace) %verify(not md5 size mtime) %lightsquid_confdir/realname.cfg
%config %attr(0644,root,root) %_sysconfdir/cron.d/lightsquid
%dir %attr(1775,root,%name) %_localstatedir/%name
%dir %attr(1775,root,%name) %lightdir
%dir %attr(1775,root,%name) %_lockdir/%name
%attr(0755,%name,%name) %lightdir/*.cgi

%files apache
%config(noreplace) %verify(not md5 size mtime) %apache_addonconfdir/lightsquid.conf

%changelog
* Tue Jul 07 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8-alt1
- Update to 1.8
- Convert spec to UTF-8

* Sun Jan 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.1-alt2
- Fix #13302

* Thu Apr 12 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.1-alt1
- Change Requires: apache-common to apache (#11307)

* Wed Jan 10 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.7.1-alt0
- Update to 1.7.1
- Remove %%set_strip_method none

* Fri Nov 24 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.7-alt0
- Update to 1.7
- Remove postun, preun scripts
- Add "today" in %_sysconfdir/cron.d/lightsquid
- Add %_lockdir\%name

* Wed Apr 26 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6-alt2.beta
- Fix (#9471): Replaced Requires for apache-mod_perl by webserver
  and config for apache separated in package %name-apache
- Fix (#9472): Change rights and owner for %_localstatedir/%name, %lightdir
- Fix (#9474)

* Wed Dec 07 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6-alt1.beta
- Fix (#8592)
  + Add pseudouser & group lightsquid
  + Change rights for *.cgi
  + Move /var/www/html/lightsquid/report to /var/lib/lightsquid
  + Move %_sysconfdir/cron.daily/lightsquid to %_sysconfdir/cron.d/lightsquid

* Fri Nov 25 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6-alt0.beta
- Update to 1.6-beta
- Add BuildRequires & Requires for perl-GD2

* Thu Oct 27 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5-alt2
- Removed requires for squid (#8352)

* Wed Sep 14 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5-alt1
- Fix path to users.txt in ip2name/ip2name.*

* Fri Aug 05 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5-alt0
- built for ALT Linux
