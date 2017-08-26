Name:           sp
Version:        5.2.1
Release:        alt21
Summary:        School Portal
Summary(ru):    Школьный портал
License:        Distributable, non-free
Group:          Education
Url:            http://spcms.ru
Packager:       Andrey Stroganov <dja@altlinux.org>
Source:         sp-5.2.1.tar
BuildRequires:  fpc
Requires:       perl-base perl-CGI perl-CGI-Session perl-Archive-Zip perl-GD perl-GD-Graph perl-CGI-SpeedyCGI perl-Magick perl-Mail-Sender perl-Text-Iconv perl-DBD-InterBase perl-HTML-TagFilter pwgen perl-IO-Compress xinetd mpg123 perl-libwww
Requires: 	apache2 firebird-classic squid-server net-tools apache2-base
Autoprov:       0
Autoreq:        0

# for UDF, because:
# verify-elf: ERROR: ./usr/lib/firebird/UDF/UDFLib.dll: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed

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
# Build UDFlib for Firebird
mkdir -p usr/lib/firebird/UDF/
cd UDFlib-src
fpc -Mdelphi -Xc -Cccdecl UDFLib.dpr -oUDFLib.dll
mv UDFLib.dll ..
cd ..
rm -rf UDFlib-src
# пусть расширение .dll вас не смущает. давным-давно у нас firebird был на винде,
# соответственно UDF собирался для винды, назван был с расширением .dll,
# для Linux название бинарника сохранено из соображений "чтобы не перелопачивать базу",
# бинарник для Linux здесь нативный

# -------------------------------------------
# Установка. Устанавливаем всё, что нужно в $RPM_BUILD_ROOT как в /
# -------------------------------------------
%install
# mkdir -p %buildroot/
mkdir -p %buildroot/var/www/cgi-bin/sp/
mkdir -p %buildroot/var/www/html/sp/
mkdir -p %buildroot/var/www/html/sp/tmp/{img_report_links,img_report_parallel,img_report_school,img_report_teacher,img_subgrp,img_subj}

# add by snejok@
cp -r * %buildroot/

# UDFlib
mkdir -p      %buildroot/%_libdir/firebird/UDF/
mv UDFLib.dll %buildroot/%_libdir/firebird/UDF/UDFLib.dll

# -------------------------------------------
# Список файлов, которые попадут в пакет
# -------------------------------------------
%files
%defattr(440, apache2, apache2, 755)
%attr(640,apache2,mail)      %config(noreplace) /var/www/cgi-bin/sp/sp.conf
%dir /var/lib/firebird/xxi/
%attr(660,firebird,firebird) %config(noreplace) /var/lib/firebird/xxi/*
%attr(440,firebird,firebird) %_libdir/firebird/UDF/UDFLib.dll
%attr(640,apache2,apache2)     /var/www/html/.htaccess
%attr(640,apache2,apache2)     %config /etc/httpd2/conf/sites-available/000-sp.conf
%attr(640,apache2,apache2)     %config /etc/httpd2/conf/mods-start.d/900-sp.conf
%attr(640,apache2,apache2)     %config /etc/httpd2/conf/sites-start.d/000-sp.conf
%attr(750,root,root)         %config /etc/xinetd.d/sphelper
%attr(750,root,root)         /usr/sbin/sp-add-admin
%attr(750,root,root)         /usr/sbin/sphelper.pl
%attr(444,root,root) %doc /usr/share/doc/sp/LICENSE
%attr(444,root,root) %doc /usr/share/doc/sp/LICENSE.alt
%attr(444,root,root) %doc /usr/share/doc/sp/README
%dir /var/www/cgi-bin/sp/
%dir /var/www/html/sp/
%dir /usr/share/doc/sp/
/var/www/cgi-bin/sp/*
/var/www/cgi-bin/sp/.htaccess
/var/www/html/sp/*
/var/www/html/sp/.htaccess
%ghost %attr(640,apache2,squid) /var/www/sp_htpasswd
%ghost %attr(640,apache2,squid) /var/www/sp_users_allowed

# -------------------------------------------
# Команды, выполняющиеся после распаковки файлов из пакета при установке на целевую систему
# -------------------------------------------
%post

# ниже есть команды с относительными путями, для простоты переход делается в первую очередь
cd /var/www/cgi-bin/sp/

# -----------------------------------------------------------
# Firebird классик:
# -----------------------------------------------------------
#chown -R firebird:firebird /var/lib/firebird/xxi/
#chmod 660 /var/lib/firebird/xxi/*.*
#chmod 755 /usr/lib/firebird/UDF/UDFLib.dll

# снимаем ограничение на 5 коннектов к fb
if ! grep -q "per_source = UNLIMITED" /etc/xinetd.d/firebird; then
	echo "Disabling connect count limitation in /etc/xinetd.d/firebir"
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
#echo "Turning on apache modules: cgi rewrite deflate headers"
#APACHE_SP_CONF='/etc/httpd2/conf/mods-start.d/900-sp.conf'
#if ! grep -q 'cgi=yes'        $APACHE_SP_CONF; then
#	echo 'cgi=yes'         >> $APACHE_SP_CONF
#fi

# a2enmod cgi
# a2enmod rewrite
# a2enmod deflate
# a2enmod headers

# echo "Setting School Portal as default site..."

# Выключем "It Works!"
# /usr/sbin/a2dissite 000-default
# if [ -e /etc/httpd2/conf/sites-start.d/000-default.conf ]; then
	# mv -vf /etc/httpd2/conf/sites-start.d/000-default.conf /etc/httpd2/conf/sites-start.d/000-default.conf-disabled
	# # rm -f /etc/httpd2/conf/sites-start.d/000-default.conf
# fi

# Включаем SP
# /usr/sbin/a2ensite 000-sp

# echo "Turning off ServerTokens Full in Apache for better security"
# perl -i-original -p -e 's/^ServerTokens Full$/ServerTokens Prod/' /etc/httpd2/conf/extra-available/httpd-default.conf
# echo "Current Apache config file saved: /etc/httpd2/conf/extra-available/httpd-default.conf-original"

chown apache2.apache2 /var/www/html/.htaccess

# chkconfig httpd2 on
# service httpd2 restart

# не нужно, т. к. в ALT переехали на файлтриггеры
# http://www.altlinux.org/Apache2/modulespec#.D0.A1.D0.BA.D1.80.D0.B8.D0.BF.D1.82.D1.8B_.25post.2F.25preun
# service httpd2 condrestart

# полный перенос функциональности в sp-helper не состоялся, всё ещё нужно как минимум для управления squid-ом
chsh -s /bin/bash apache2


# Действие ($1)                     Значение параметра
# ====================================================
# Установка в первый раз            1
# Обновление                        2 или больше
# Удаление последней версии пакета  0

# -------------------------------
# Базы
# -------------------------------

# Для ALT Linux XXI поставляется предварительно опорталенной

# выполнять только если установка в первый раз
if [ "$1" -eq 1 ]; then
	echo 'Clean databases installed'
	# в альте базы требуют складывать не как принято у нас,
	# конфиг отныне будем класть как для всех, но патчить его после установки в пакетах для альта
	perl -i -p -e 's!/opt/xxi/data/!/var/lib/firebird/xxi/!' /var/www/cgi-bin/sp/sp.conf
else
	# обновление структуры базы
	perl update-db.pl sp.conf
fi

# больше не нужны
rm -f -- update-sql.pl update-db.pl

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
	echo "Setting up internet access control..."
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
	echo "Current Squid config saved: /etc/squid/squid.conf-original"
fi

# полный перенос функциональности в sp-helper не состоялся
# управление squid-ом пока выполняется от имени юзера apache2
usermod -G wheel,_webserver apache2
# чтобы было безопасно поставить второй раз, сначала проверим, потом допишем
# TODO: если допиливание sp-helper затянется, посмотреть в сторону переезда на /etc/sudoers.d
APACHE_SUDOER_LINE='apache2      ALL=(ALL)       NOPASSWD: /usr/sbin/smbldap-useradd,/usr/sbin/smbldap-passwd,/usr/sbin/smbldap-usermod,/usr/sbin/smbldap-groupadd,/usr/bin/ldapsearch,/usr/bin/ldapmodify,/bin/touch,/bin/chmod,/etc/init.d/squid reload'
if ! grep -q "$APACHE_SUDOER_LINE" /etc/sudoers; then
	echo "$APACHE_SUDOER_LINE" >> /etc/sudoers
	echo "/etc/sudoers modified for LDAP integration and Squid control"
	echo "Added line: $APACHE_SUDOER_LINE"
fi

# выполнять только если установка в первый раз
if [ "$1" -eq 1 ]; then
	echo 'auth = basic'                                 >> /var/www/cgi-bin/sp/sp.conf
	echo 'htpasswd = /var/www/sp_htpasswd'              >> /var/www/cgi-bin/sp/sp.conf
	echo 'sp_users_allowed = /var/www/sp_users_allowed' >> /var/www/cgi-bin/sp/sp.conf
fi

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
# SP-Helper
# -----------------------------------------------------------
SPHELPER_SERVICES_LINE='sphelper 7890/tcp'
if ! grep -q "$SPHELPER_SERVICES_LINE" /etc/services; then
	echo "$SPHELPER_SERVICES_LINE" >> /etc/services
fi
# service xinetd restart

# gallery
# выполнять только если нет папки галереи
if [ ! -e /var/www/html/sp/pic/gallery ]; then
	mkdir -p \
	    /var/www/html/sp/pic/gallery \
	    /var/www/html/sp/pic/gallery.thumbs \
	    /var/www/html/sp/pic/gallery.resize

	chown root:root \
	    /var/www/html/sp/pic/gallery
	chmod 777 \
	    /var/www/html/sp/pic/gallery

	chown apache:apache \
	    /var/www/html/sp/pic/gallery.thumbs \
	    /var/www/html/sp/pic/gallery.resize
	chmod 775 \
	    /var/www/html/sp/pic/gallery.thumbs \
	    /var/www/html/sp/pic/gallery.resize
fi

# -----------------------------------------------------------
# SP Setup
# -----------------------------------------------------------
perl setup.pl --yes

# -----------------------------------------------------------
# Интеграция с LDAP
#
# Сегодня, 12 сен 2011, при установке ALT Linux 6 rc1 как сервера
# LDAP не настроен
#
# в 5.0 уберём в любом случае
# upd: теперь у нас есть sp-helper, но в комментах оставляем, вдруг настроенный ldap вернётся в следующих версиях ALT
# -----------------------------------------------------------

# mv -f /var/www/cgi-bin/sp/smbldap-passwd /usr/sbin/smbldap-passwd
# chown root.root /usr/sbin/smbldap-passwd /sbin/sp-ldap-setup
# chmod 755 /usr/sbin/smbldap-passwd /sbin/sp-ldap-setup

# выполнять только если установка в первый раз
# if [ "$1" -eq 1 ]; then
# 	sp-ldap-setup
# fi

if [ "$1" -eq 1 ]; then
	echo
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
	echo 'If not sure what to type in browser, try:'
	ifconfig | awk '/inet addr/ {print $2}' | awk -F ':' '{print "http://" $2}'
	echo
else
	echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
	echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
	echo '!!!                                                                   !!!'
	echo '!!!           School Portal Updated.                                  !!!'
	echo '!!!                                                                   !!!'
	echo '!!!           Support:                                                !!!'
	echo '!!!           http://spcms.ru                                         !!!'
	echo '!!!                                                                   !!!'
	echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
	echo '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
fi

# -------------------------------------------
# Команды, выполняющиеся после при удалении пакета
# -------------------------------------------
%preun

# возвращаем всё как было
# mv /etc/httpd2/conf/sites-start.d/000-default.conf-disabled /etc/httpd2/conf/sites-start.d/000-default.conf
# a2ensite  default
# a2dissite 000-sp

%changelog
* Sat Aug 26 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.1-alt21
- Require apache2-base instead of deprecated apache-common

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt20
add sites.start.d apache config for sp

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt19
fixed clean databases

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt18
rollback default site replacement (2)

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt17
rollback default site replacement

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt16
fix preun script

* Mon May 06 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt15
fix permissions; replace a2dissite with rm symlink

* Sun May 05 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt14
patch paths to DBs in sp.conf for alt reqs

* Sun May 05 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt13
removed user dir from files section

* Sun May 05 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt12
converted SP config part for apache from grep/echo to ready file in repo

* Sat May 04 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt0.M60P.1
- build for p6

* Sat May 04 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt10
- do not scan for updates on install; fix tmp path

* Sat May 04 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt9
- fix tmp dirs creation

* Sat May 04 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt8
- fix: chdir before setup.pl; tmp dirs creation

* Tue Apr 30 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt7
- add dependency: perl-libwww

* Mon Apr 29 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt6
- migrate from a2enmod to mods-start.d/* configs in Apache configuration

* Mon Apr 29 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt5
- added notice for xinetd config modification for firebird, remove connect limit
- remove gallery dirs ownership. photos must stay untouched after sp uninstall

* Mon Apr 29 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt4
- fix ghost dirs for gallery

* Mon Apr 29 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt3
- ghost dirs for gallery

* Mon Apr 29 2013 Andrey V. Stroganov <dja@altlinux.org> 5.2.1-alt2
- removed apache reconf due to filetriggers
- setup dirs for gallery module from 5.2.1
- added notices for Apache, Squid, sudoers config modification
- internal user IDs under 100 now reserved

* Wed Jan 16 2013 Andrey Stroganov <dja@altlinux.org> 5.2.1-alt1
- sp-5.2.1

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 4.2-alt6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * vendor-tag for sp-debuginfo
  * vendor-tag for sp

* Thu Sep 13 2012 Andrey Stroganov <dja@altlinux.org> 4.2-alt6
- /usr/lib replaced with macros

* Thu Sep 5 2012 Andrey Stroganov <dja@altlinux.org> 4.2-alt5
- UDFlib source code

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
