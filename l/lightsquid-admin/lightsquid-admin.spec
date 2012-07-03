Name: lightsquid-admin
Version: 1.8.0.1

%define branch_switch 
%define branch_release_num 1

%if "%{?branch_switch}" == "M40" || "%{?branch_switch}" == "M41"
  %define tree 1
%else
  %define tree 0
%endif

Summary: Lite, small size and fast log analizer for squid proxy
Summary(ru_RU.UTF-8): Легкий, маленький и быстрый анализатор лога для прокси сервера squid
License: GPL
Group: Networking/WWW
Packager: Dmitry Kharitonov <kharpost@altlinux.ru>

Url: http://lightsquid.sourceforge.net/
Source: http://prdownloads.sourceforge.net/lightsquid/%name-%version.tgz
BuildRequires(pre): rpm-macros-branch
BuildRequires: perl-CGI perl-GD2 apache apache2 coreutils webserver-common rpm-macros-webserver-common
Requires: coreutils perl-CGI webserver-common perl-GD2
Requires(pre): shadow-groups
Release: %branch_release alt2.13

BuildArch: noarch

%define applname lightsquid
%define webserver_datadir %_var/www
%define webserver_htdocsdir %webserver_datadir/html
%define apache_home %webserver_htdocsdir
%if %{tree} > 0
  %define apache2_home %webserver_datadir/apache2/html
%else
  %define apache2_home %apache_home
%endif
%define apache_confdir %_sysconfdir/httpd/conf
%define apache2_confdir %_sysconfdir/httpd2/conf
%define apache_addonconfdir %apache_confdir/addon-modules.d
%define apache2_siteanav %apache2_confdir/sites-available
%define apache2_sitestart %apache2_confdir/sites-start.d
%define apache2_modsstart %apache2_confdir/mods-start.d
%define apache2_portsstart %apache2_confdir/ports-start.d
%define lightsquid_confdir %_sysconfdir/%applname
%define lightdir %apache_home/%applname
%define lightdir2 %apache2_home/%applname
%define blockerurl %_localstatedir/%applname/blockerurl
%define blockerip %_localstatedir/%applname/blockerip


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
Summary: Config %name for apache (do not work bug #15691)
Summary(ru_RU.UTF-8): Конфигурационный файл %name для вебсервера apache (не работает bug #15691)
License: GPL
Group: System/Servers
Requires: %name = %version-%release
Requires: apache coreutils mod_auth_pam grep apache-mod_perl
Requires(pre): shadow-groups

%description apache
Config %name for apache

%package apache2
Summary: Config %name for apache2
Summary(ru_RU.UTF-8): Конфигурационный файл %name для вебсервера apache2
License: GPL
Group: System/Servers
Requires: %name = %version-%release
Requires: apache2 coreutils grep apache2-mod_perl apache2-common
Requires(pre): shadow-groups

%description apache2
Config %name for apache2

%prep
%setup -n %name-%version
#$langpath="/var/www/html/lightsquid/lang";
subst "s|\$langpath[[:space:]]*=.*;|\$langpath=\"%_datadir/%applname/lang\";|g"  lightsquid.cfg

#$tplpath="/var/www/html/lightsquid/tpl";
subst "s|\$tplpath[[:space:]]*=.*;|\$tplpath=\"%_datadir/%applname/tpl\";|g" lightsquid.cfg

#$ip2namepath="/var/www/html/lightsquid/ip2name";
subst "s|\$ip2namepath[[:space:]]*=.*;|\$ip2namepath=\"%_datadir/%applname/ip2name\";|g" lightsquid.cfg

#$badurl="$reportpath/badurl";
subst "s|\$badurl[[:space:]]*=.*;|\$badurl=\"%_localstatedir/%applname/badurl\";|g" lightsquid.cfg

#$badip="$reportpath/badip";
subst "s|\$badip[[:space:]]*=.*;|\$badip=\"%_localstatedir/%applname/badip\";|g" lightsquid.cfg

#$cmdurl="$reportpath/blockerurl";
subst "s|\$cmdurl[[:space:]]*=.*;|\$cmdurl=\"%blockerurl\";|g" lightsquid.cfg

#$cmdip="$reportpath/blockerip";
subst "s|\$cmdip[[:space:]]*=.*;|\$cmdip=\"%blockerip\";|g" lightsquid.cfg

#$reportpath="/var/www/html/lightsquid/report";
subst "s|\$reportpath[[:space:]]*=.*;|\$reportpath=\"%_localstatedir/%applname\";|g" lightsquid.cfg

#$cfgpath="/var/www/html/lightsquid";
subst "s|\$cfgpath[[:space:]]*=.*;|\$cfgpath=\"%lightsquid_confdir\";|g" lightsquid.cfg

#$lockpath=$reportpath;
subst "s|\$lockpath[[:space:]]*=.*;|\$lockpath=\"%_lockdir/%applname\";|g" lightsquid.cfg

#$logpath="/var/log/squid";
subst "s|\$logpath[[:space:]]*=.*;|\$logpath=\"/var/log/squid\";|g" lightsquid.cfg

#require "ip2name";
subst "s|require[[:space:]]*\"ip2name\";|require \"\$ip2namepath/ip2name.\$ip2name\";|g" lightparser.pl

subst "s|require[[:space:]]*\"lightsquid.cfg\";|require \"%lightsquid_confdir/lightsquid.cfg\";|g" {,admin/}*.cgi *.pl
subst "s|require[[:space:]]*\"common.pl\";|require \"%_datadir/%applname/common.pl\";|g" {,admin/}*.cgi *.pl
subst "s|/etc/squid/users.txt|/etc/lightsquid/users.txt|g" ip2name/ip2name.*

iconv -f WINDOWS-1251 -t UTF8 lang/ru.lng > lang/ru-utf8.lng
subst "s|windows-1251|utf8|g" lang/ru-utf8.lng

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%lightsquid_confdir
mkdir -p %buildroot%_sysconfdir/cron.d
mkdir -p %buildroot%_datadir/%applname/{lang,ip2name,tpl}
mkdir -p %buildroot%apache_addonconfdir
mkdir -p %buildroot%apache2_home
%if %{tree} > 0
  ln -snf $(relative %buildroot%lightdir %buildroot%lightdir2) %buildroot%lightdir2
%endif
mkdir -p %buildroot%_localstatedir/%applname
mkdir -p %buildroot%lightdir/admin
mkdir -p %buildroot%_lockdir/%applname
mkdir -p %buildroot%apache2_siteanav
mkdir -p %buildroot%apache2_sitestart
mkdir -p %buildroot%apache2_modsstart
mkdir -p %buildroot%apache2_portsstart

# install bin
install -p -m 755 lightparser.pl %buildroot%_sbindir/

# install configs
install -p -m 644 lightsquid.cfg %buildroot%lightsquid_confdir/lightsquid.cfg
install -p -m 644 group.cfg.src %buildroot%lightsquid_confdir/group.cfg
install -p -m 644 realname.cfg %buildroot%lightsquid_confdir/realname.cfg

# install cron
cat > %buildroot%_sysconfdir/cron.d/lightsquid << EOF
55 * * * * lightsquid %_sbindir/lightparser.pl today
EOF

cat > %buildroot%_sysconfdir/cron.d/lightsquidip << EOF
#*/5 * * * * root flag="%blockerip"; if [ -f "\$flag" ]; then rm -f "\$flag"; firewall 2>&1 1>/dev/null; fi
EOF

cat > %buildroot%_sysconfdir/cron.d/lightsquidurl << EOF
#*/5 * * * * root flag="%blockerurl"; if [ -f "\$flag" ]; then rm -f "\$flag"; /usr/sbin/squid -k reconfigure 2>&1 1>/dev/null; fi
EOF

cat > admin/.htaccess << EOF
AuthType Basic
AuthName "%applname administrator mode"
AuthUserFile %lightdir/admin/.htpasswd
Require user admin

EOF


#Default password admin
/bin/touch admin/.htpasswd

# install lib
install -p -m 644 common.pl %buildroot%_datadir/%applname/
install -p -m 755 check-setup.pl %buildroot%_datadir/%applname/
install -p -m 644 lang/[^A-Z]*.lng %buildroot%_datadir/%applname/lang/
install -p -m 644 ip2name/[^A-Z]* %buildroot%_datadir/%applname/ip2name/
cp -aRf tpl/[^A-Z]* %buildroot%_datadir/%applname/tpl/
##install -p -m 644 tpl/[^A-Z]* %buildroot%_datadir/%applname/tpl/

# install web
#install -p -m 644 .htaccess %buildroot%apache_home/%applname/
install -p -m 755 [^A-Z]*.cgi %buildroot%apache_home/%applname/
cp -aRf admin/[^A-Z]*.cgi %buildroot%lightdir/admin
cp -aRf admin/.h* %buildroot%lightdir/admin
#/bin/cp -aRf admin/. admin/.. admin/.htaccess admin/.htpasswd /usr/src/tmp/lightsquid-admin-buildroot/var/www/apache2/html/lightsquid/admin

#apache
cat << EOF > %buildroot%apache_addonconfdir/lightsquid.conf
<Directory "%lightdir">
    Options FollowSymLinks +ExecCGI
    AddHandler cgi-script .cgi
    AllowOverride AuthConfig
    DirectoryIndex index.cgi
</Directory>

EOF

#apache2
cat << EOF > %buildroot%apache2_modsstart/110-lightsquid.conf
perl=yes
cgi=yes
dir=yes
auth_basic=yes
authn_file=yes
authz_user=yes

EOF

cat << EOF > %buildroot%apache2_siteanav/lightsquid.conf
ScriptAlias "/cgi-bin/" "%lightdir2/"
<Directory "%lightdir2/">
    Options FollowSymLinks +ExecCGI
    AddHandler cgi-script .cgi
    AllowOverride AuthConfig
    DirectoryIndex index.cgi
</Directory>

EOF

cat << EOF > %buildroot%apache2_sitestart/110-lightsquid.conf
lightsquid=yes

EOF

cat << EOF > %buildroot%apache2_portsstart/110-lightsquid.conf
http=yes

EOF

%pre
/usr/sbin/groupadd -r -f %applname &> /dev/null ||:
/usr/sbin/useradd -r -g %applname -d %_localstatedir/%applname -c 'Log parser lightsquid' -s /bin/false -n %applname &> /dev/null ||:
gpasswd -a %applname squid
gpasswd -a %applname _webserver

%pre apache
#groups user | sed "s/.*://;s/^[[:space:]]\+//;s/[[:space:]]\+$//;s/[[:space:]]\+/,/g;"
gpasswd -a %applname apache
gpasswd -a %applname _webserver
gpasswd -a %applname squid
gpasswd -a apache _webserver

%pre apache2
gpasswd -a %applname apache2
gpasswd -a %applname _webserver
gpasswd -a %applname squid
gpasswd -a apache2 _webserver

%post
if [[ -d %lightdir/report ]]; then
    mv %lightdir/report/* %_localstatedir/%applname
##    rm -f %lightdir/report
    echo "Reports move from %lightdir/report to %_localstatedir/%applname"
fi
#find %_localstatedir/%applname -print0 | xargs -r0 chown %applname:_webserver
#find %_localstatedir/%applname -print0 | xargs -r0 chmod a-xw+Xr,ug+w
chown -R %applname:_webserver %_localstatedir/%applname
chmod -R a-xw+Xr,ug+w %_localstatedir/%applname
echo "Please, edit the %_sysconfdir/cron.d/lightsquidip for your own IP blocker procedure."
echo "Please, edit the %_sysconfdir/cron.d/lightsquidurl for your own URL blocker procedure."

%post apache
cat > %lightdir/admin/.htaccess << EOF
AuthType Basic
AuthName "%applname administrator mode"
AuthUserFile %lightdir/admin/.htpasswd
Require user admin

EOF
touch %lightdir/admin/.htpasswd
chown %applname:_webserver %lightdir/admin/.ht*
chmod 640 %lightdir/admin/.htpasswd
if ! grep -q "admin" %lightdir/admin/.ht*; then
    /usr/bin/htpasswd -bm %lightdir/admin/.htpasswd admin admin
    echo "Default administrator login:admin password:admin to change it use"
else
    echo "For change your password use"
fi
echo "# htpasswd -m %lightdir/admin/.htpasswd admin"
%post_service httpd

%post apache2
cat > %lightdir2/admin/.htaccess << EOF
AuthType Basic
AuthName "%applname administrator mode"
AuthBasicProvider file
AuthUserFile %lightdir/admin/.htpasswd
Require user admin

EOF
touch %lightdir2/admin/.htpasswd
chown %applname:_webserver %lightdir2/admin/.h*
chmod 640 %lightdir2/admin/.h*
if ! grep -q "admin" %lightdir2/admin/.htpasswd; then
    /usr/bin/htpasswd2 -bm %lightdir2/admin/.htpasswd admin admin
    echo "Default administrator login:admin password:admin to change it use"
else
    echo "For change your password use"
fi
echo "# htpasswd2 -m %lightdir/admin/.htpasswd admin"
a2chkconfig
%post_service httpd2

%files
%doc doc/*
%_sbindir/*
%_datadir/%applname
%dir %attr(1755,root,root) %lightsquid_confdir
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %lightsquid_confdir/lightsquid.cfg
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %lightsquid_confdir/group.cfg
%config(noreplace) %attr(0644,root,root) %verify(not md5 size mtime) %lightsquid_confdir/realname.cfg
%config(noreplace) %attr(0644,root,root) %_sysconfdir/cron.d/lightsquid
%config(noreplace) %attr(0644,root,root) %_sysconfdir/cron.d/lightsquidurl
%config(noreplace) %attr(0644,root,root) %_sysconfdir/cron.d/lightsquidip
%dir %attr(1775,%applname,_webserver) %_localstatedir/%applname
%dir %attr(1755,%applname,_webserver) %lightdir
%dir %attr(1755,%applname,_webserver) %lightdir/admin
%dir %attr(1775,%applname,_webserver) %_lockdir/%applname
%attr(0755,%applname,_webserver) %lightdir/*.cgi
%attr(0755,%applname,_webserver) %lightdir/admin/*.cgi
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htpasswd
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htaccess

%files apache
%config(noreplace) %verify(not md5 size mtime) %attr(0644,root,root) %apache_addonconfdir/lightsquid.conf
#%dir %attr(1775,%applname,_webserver) %lightdir
#%dir %attr(1775,%applname,_webserver) %lightdir/admin
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htpasswd
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htaccess

%files apache2
#%dir %attr(1755,%applname,_webserver) %lightdir
#%dir %attr(1755,%applname,_webserver) %lightdir/admin
#%dir %attr(1755,root,_webserver) %apache2_home
%if %{tree} > 0
# Store the link
  %lightdir2
%endif
%config(noreplace) %verify(not md5 size mtime) %attr(0644,root,root) %apache2_siteanav/lightsquid.conf
%config(noreplace) %verify(not md5 size mtime) %attr(0644,root,root) %apache2_modsstart/110-lightsquid.conf
%config(noreplace) %verify(not md5 size mtime) %attr(0644,root,root) %apache2_sitestart/110-lightsquid.conf
%config(noreplace) %verify(not md5 size mtime) %attr(0644,root,root) %apache2_portsstart/110-lightsquid.conf
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htpasswd
%config(noreplace) %attr(0440,%applname,_webserver) %lightdir/admin/.htaccess

%changelog
* Mon Nov 02 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.13
- Autocommit for branch sisyphus

* Mon Nov 02 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.11.M40.4
- Fix lightparser path (ALT #22093)

* Mon Oct 12 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.10.M40.4
- Fix shadow-groups require

* Sun Oct 11 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.9.M40.1
- Fix perms for password

* Sat Oct 10 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.8.M40.1
- Fix group for lightsquid

* Wed Oct 07 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.7.M40.1
- Fix symlink for !M40

* Wed Oct 07 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.4.sisyphus.1
- Disable filetriggers (fix for branch 4.0)

* Mon Oct 05 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt2.2.sisyphus.1
- Add shadow-groups (fix for branch 4.0)

* Tue Aug 18 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8.0.1-alt1
- Fix units
- Fix site filter
- Add doc for admin mode
- Fix graph scale
- Fix apache config

* Sun Jul 26 2009 Kharitonov A. Dmitry <kharpost@altlinux.ru> 1.8-alt2
- Add administrators mode

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
- Add %_lockdir\%applname

* Wed Apr 26 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6-alt2.beta
- Fix (#9471): Replaced Requires for apache-mod_perl by webserver
  and config for apache separated in package %applname-apache
- Fix (#9472): Change rights and owner for %_localstatedir/%applname, %lightdir
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
