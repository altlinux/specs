Name:           sp
Version:        4.2
Release:        alt4
Summary:        School Portal
Summary(ru):    Школьный портал
License:        Distributable, non-free
Group:          Education
Url:            http://spcms.ru
Packager:       Andrey Stroganov <dja@altlinux.org>
Vendor:         SP Team
Source:         sp-4.2.tar
Requires:       perl-base perl-CGI perl-CGI-Session perl-Archive-Zip perl-GD perl-GD-Graph perl-CGI-SpeedyCGI perl-Magick perl-Mail-Sender perl-Text-Iconv perl-DBD-InterBase perl-HTML-TagFilter pwgen perl-IO-Compress
Requires(post): apache2 firebird-classic squid-server net-tools apache-common
Autoprov:       0
Autoreq:        0
ExclusiveArch:  %ix86

# -------------------------------------------
# Описание на английском
# -------------------------------------------
%description
Integrated school control system.

# -------------------------------------------
# Описание на русском
# -------------------------------------------
%description -l ru
Комплексная система управления школой.

# add by snejok@
# -------------------------------------------
# Распаковываем
# -------------------------------------------
%prep
%setup

# -------------------------------------------
# Установка. Устанавливаем всё, что нужно в $RPM_BUILD_ROOT как в /
# -------------------------------------------

%install
mkdir -p %buildroot/
mkdir -p %buildroot/var/www/cgi-bin/sp/
mkdir -p %buildroot/var/www/html/sp/

# add by snejok@
cp -r * %buildroot/

# -------------------------------------------
# Список файлов, которые попадут в пакет
# -------------------------------------------
%files
%defattr(440, apache, apache, 755)
%attr(640,apache,apache)     %config(noreplace) /var/www/cgi-bin/sp/sp.conf
%dir /var/lib/firebird/xxi/
%attr(660,firebird,firebird) %config(noreplace) /var/lib/firebird/xxi/*
%attr(440,firebird,firebird) /usr/lib/firebird/UDF/UDFLib.dll
%attr(640,apache,apache)     /var/www/html/.htaccess
%attr(640,apache,apache)     %config /etc/httpd2/conf/sites-available/000-sp.conf
%attr(750,root,root)         /usr/sbin/sp-add-admin
%attr(444,root,root) %doc /usr/share/doc/sp/LICENSE
%attr(444,root,root) %doc /usr/share/doc/sp/LICENSE.alt
%attr(444,root,root) %doc /usr/share/doc/sp/README
%dir /var/www/cgi-bin/sp/
%dir /var/www/html/sp/
%dir /usr/share/doc/sp/
/var/www/cgi-bin/sp/*
/var/www/html/sp/*
%ghost %attr(640,apache,squid) /var/www/sp_htpasswd
%ghost %attr(640,apache,squid) /var/www/sp_users_allowed

# -------------------------------------------
# Команды, выполняющиеся после распаковки файлов из пакета при установке на целевую систему
# -------------------------------------------
%post

# -----------------------------------------------------------
# Firebird классик:
# -----------------------------------------------------------
#chown -R firebird:firebird /var/lib/firebird/xxi/
#chmod 660 /var/lib/firebird/xxi/*.*
#chmod 755 /usr/lib/firebird/UDF/UDFLib.dll

# снимаем ограничение на 5 коннектов к fb
if ! grep -q "per_source = UNLIMITED" /etc/xinetd.d/firebird; then
	perl -i -p -e 's/^\s*disable\s+=\s+no$/disable = no\nper_source = UNLIMITED/' /etc/xinetd.d/firebird
fi

# без этого classic просто не работает, а нужен здесь и сейчас
# boris: если xinetd запущен не был, то его надо запустить руками -- такая идеология
# перезапуск по причинам:
# 1) чтобы xinetd заработал, если не работал
# 2) если xinetd работал, чтобы узнал о том, что теперь у нас есть fb
# 3) если xinetd и fb были установлены до нас и всё работало, ничего страшного
# service xinetd restart

# если xinetd не был стартован, стартуем, делаем своё, опускаем как было

# в каком состоянии xinetd?
#if service xinetd status; then
#    XINETD_WAS_STARTED=1
#else
#    XINETD_WAS_STARTED=0
#fi

# xinetd...
#if [ "$XINETD_WAS_STARTED" -eq "0" ]; then
#    # не был стартован
#    echo Temporary starting xinetd...
#    service xinetd start
#else
#    # был стартован. заставляем подхватить конфиг fb
#    echo xinetd in running, restarting to ensure fb config read...
#    service xinetd restart
#fi

# по умолчанию fb нет в автозапуске, включаем
# chkconfig firebird on

# -----------------------------------------------------------
# Apache
# -----------------------------------------------------------
a2enmod cgi
a2enmod rewrite
a2enmod deflate
a2enmod headers

# Выключем "It Works!"
a2dissite 000-default
# Включаем SP
a2ensite  000-sp

perl -i-original -p -e 's/^ServerTokens Full$/ServerTokens Prod/' /etc/httpd2/conf/extra-available/httpd-default.conf

chown apache2.apache2 /var/www/html/.htaccess

# chkconfig httpd2 on
# service httpd2 restart
service httpd2 condrestart

# в 5.0 уберём
chsh -s /bin/bash apache2

# -----------------------------------------------------------
# SP Setup
# -----------------------------------------------------------

cd /var/www/cgi-bin/sp/

perl setup.pl --yes

# Действие ($1)                     Значение параметра
# ====================================================
# Установка в первый раз            1
# Обновление                        2 или больше
# Удаление последней версии пакета  0

# выполнять только если установка в первый раз
# Експеримент: XXI поставляется опорталенной
#if [ "$1" -eq 1 ]; then
#	perl update_xxi.pl sp.conf sp.sql
#fi


# больше не нужны
rm -f -- update_xxi.pl
rm -f -- sp.sql

chmod 500 /usr/sbin/sp-add-admin

# xinetd не был стартован изначально, укладываем как было
#if [ "$XINETD_WAS_STARTED" -eq "0" ]; then
#    echo xinetd was stopped befor sp. Stopping back...
#    service xinetd stop
#fi

# -----------------------------------------------------------
# Squid: управление доступом в интернет
# -----------------------------------------------------------

if ! grep -q "^acl sp_users_allowed" /etc/squid/squid.conf; then
	# правим конфиг кальмара
	perl -i-original -p -e 's!^icap_enable on!icap_enable off!; s!^auth_param!#auth_param!; s!^acl password proxy_auth REQUIRED!#acl password proxy_auth REQUIRED!; s!^http_access deny all!#http_access deny all!; s!^http_access allow password!#http_access allow password!; s!^htcp_access allow localnet!#htcp_access allow localnet!' /etc/squid/squid.conf
	
	echo '
# ==============================
# School Portal Internet Control
# To disable replace /etc/squid/squid.conf with /etc/squid/squid.conf-original
# ==============================
auth_param basic program /usr/lib/squid/ncsa_auth /var/www/sp_htpasswd
auth_param basic children 5
auth_param basic realm Squid proxy-caching web server
auth_param basic credentialsttl 2 hours
auth_param basic casesensitive on
acl sp_users_allowed proxy_auth "/var/www/sp_users_allowed"
http_access allow sp_users_allowed
http_access deny all
' >> /etc/squid/squid.conf
fi

# в 5.0 уберём
usermod -G wheel,_webserver apache2

# в 5.0 уберём
# чтобы было безопасно поставить второй раз, сначала проверим, потом допишем
APACHE_SUDOER_LINE='apache2      ALL=(ALL)       NOPASSWD: /usr/sbin/smbldap-useradd,/usr/sbin/smbldap-passwd,/usr/sbin/smbldap-usermod,/usr/sbin/smbldap-groupadd,/usr/bin/ldapsearch,/usr/bin/ldapmodify,/bin/touch,/bin/chmod,/etc/init.d/squid reload'
if ! grep -q "$APACHE_SUDOER_LINE" /etc/sudoers; then
	echo "$APACHE_SUDOER_LINE" >> /etc/sudoers
fi

# выполнять только если установка в первый раз
if [ "$1" -eq 1 ]; then

	echo 'auth = basic'                                 >> /var/www/cgi-bin/sp/sp.conf
	echo 'htpasswd = /var/www/sp_htpasswd'              >> /var/www/cgi-bin/sp/sp.conf
	echo 'sp_users_allowed = /var/www/sp_users_allowed' >> /var/www/cgi-bin/sp/sp.conf

fi

#touch /var/www/sp_htpasswd
#touch /var/www/sp_users_allowed

#chown apache2.squid  /var/www/sp_htpasswd  /var/www/sp_users_allowed
#chmod 660            /var/www/sp_htpasswd  /var/www/sp_users_allowed

# выполнять только если установка в первый раз
if [ "$1" -eq 1 ]; then

	# По дефолту никому в инет нельзя
	# для этого добавим юзера с неугадываемым паролем
	SP_HTPASSWD=$(pwgen --secure 32 1)
	/usr/bin/htpasswd -cb /var/www/sp_htpasswd sp_dummy_user $SP_HTPASSWD
	echo 'sp_dummy_user' >> /var/www/sp_users_allowed

fi

# chkconfig squid on
# service squid restart
service squid condrestart

# -----------------------------------------------------------
# Интеграция с LDAP
#
# Сегодня, 12 скн 2011, при установке ALT Linux 6 rc1 как сервера
# LDAP не настроен
#
# в 5.0 уберём в любом случае
# -----------------------------------------------------------

# mv -f /var/www/cgi-bin/sp/smbldap-passwd /usr/sbin/smbldap-passwd
# chown root.root /usr/sbin/smbldap-passwd /sbin/sp-ldap-setup
# chmod 755 /usr/sbin/smbldap-passwd /sbin/sp-ldap-setup

# выполнять только если установка в первый раз
# if [ "$1" -eq 1 ]; then
# 
# 	sp-ldap-setup
# 
# fi

echo ''
echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
echo '!!!                                                              !!!'
echo '!!!       School Portal installed.                               !!!'
echo '!!!       Direct your browser to this server to log in.          !!!'
echo '!!!                                                              !!!'
echo '!!!       Login:    admin                                        !!!'
echo '!!!       password: smenimenya                                   !!!'
echo '!!!                                                              !!!'
echo '!!!       CHANGE PASSWORD NOW!                                   !!!'
echo '!!!                                                              !!!'
echo '!!!       Alphabet book: http://spcms.ru/download#abook          !!!'
echo '!!!       Support:       http://spcms.ru                         !!!'
echo '!!!                                                              !!!'
echo '!!!       Please, read in russian: /usr/share/doc/sp/README      !!!'
echo '!!!                                                              !!!'
echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
echo ''
echo 'If not sure what to type in browser, try:'
ifconfig | awk '/inet addr/ {print $2}' | awk -F ':' '{print "http://" $2}'
echo ''
echo ''

# -------------------------------------------
# Команды, выполняющиеся после при удалении пакета
# -------------------------------------------
%preun

# возвращаем всё как было
a2ensite  default
a2dissite 000-sp

%changelog
* Tue Sep 13 2011 Andrey Stroganov <dja@altlinux.org> 4.2-alt4
- added README, final installation message now shorter
* Mon Sep 12 2011 Andrey Stroganov <dja@altlinux.org> 4.2-alt3
- deps concretized, permissions fixed, spec cleanup and optimization,
- config cleanup, added useful details to installation message,
- postin: removed some warnings, config converted to in utf-8
* Thu Sep 1 2011 Andrey Stroganov <dja@altlinux.org> 4.2-alt2
- license added, spec cleanups
* Mon Jul 18 2011 Andrey Stroganov <dja@altlinux.org> 4.2-alt1
- initial build for alt 6
