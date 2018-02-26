%define majver 2.01
%define minver 10
%define suff	RB23

Name: webalizer
Version: %majver.%minver.%suff
Release: alt2

Summary: Web/ftp/proxy server log analyser
License: GPL
Group: Monitoring

Url: http://www.patrickfrei.ch/webalizer/%name
Source0: %name-%majver-%minver-%suff-src.tar.bz2
Source1: %name.conf
Source2: README.ALT-webalizer

Patch1:  %name-alt-configure.patch

%define apache_group apache
%define apache_log %_logdir/httpd/access_log
%define vsftpd_log %_logdir/vsftpd.log
%define dns_cache  /var/lib/%name/dns_cache.db
%define webalizer_user webalizer
%define webalizer_group webalizer
%define webalizer_home %_localstatedir/%name
%define webalizer_html %_var/www/html/%name
%define geoip_data /usr/share/GeoIP/GeoIP.dat

Summary(ru_RU.UTF-8): Анализатор логов web/ftp/proxy-серверов

# Automatically added by buildreq on Sat Aug 16 2008
BuildRequires: rpm-macros-apache rpm-macros-apache2 bzlib-devel libGeoIP-devel libdb4-devel libgd2-devel libpng-devel

BuildRequires: zlib-devel bzlib-devel

Requires: db4.7-utils

%description
The Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser.  The results
are presented in both columnar and graphical format, which facilitates
interpretation.  Yearly, monthly, daily and hourly usage statistics are
presented, along with the ability to display usage by site, URL, referrer,
user agent (browser) and country (user agent and referrer are only
available if your web server produces combined log format files).
Webalizer Xtended is especially useful for all those users who would like 
to have detailed HTML-404-statistics (i.e. about broken links and visitors 
trying to look-up folders and files containing potentionally vulnerable 
software). As further features, all colors of the statistics can be 
defined by the user and the country resp. traffic statistics are more 
reliable due to the implementation of Geolizer resp. 


%description -l ru_RU.UTF-8
The Webalizer -- программа для анализа лог-файлов web-сервера Apache и
некоторых других, представляющая результаты в виде HTML (таблицы и диаграммы).
Собирается годичная, помесячная, ежедневная и почасовая статистика с
возможностью просмотра по сайтам, URL, реферрерам, браузерам, странам. В этой версии
также собирается детальная статистика ошибок 404 (неправильные линки)
Webalizer Xtended полезен тем, кому необходима детальная статистика по 404-ошибкам
(неправильные ссылки, попытки пользователей просмотреть каталоги и файлы, содержащие
потенциально опасные приложения). Дополнительно есть возможность определить цветовые 
гаммы статистики и включена поддержка Geolizer.

%prep
%setup -n %name-%majver-%minver-%suff
%patch1 -p1

%build
CFLAGS="%optflags -fsigned-char"
%configure \
	--with-db \
	--with-dblib \
	--enable-dns \
	--enable-geoip \
	--with-bzlib \
	--with-bz-inc


# patch the template; keep common data in HOME, distinct in DATA
sed -e "s,__HTML__,%webalizer_html,g" \
    -e "s,__HOME__,%webalizer_home,g" \
    -e "s,__DATA__,%webalizer_home,g" \
    -e "s,__LOGFILE__,%apache_log,g" \
    -e "s,__GEOIPDATA__,%geoip_data,g" \
    -e "s,__LOGTYPE__,clf,g" \
< %SOURCE1 \
> apache.conf

sed -e "s,__HTML__,%webalizer_html/ftp,g" \
    -e "s,__HOME__,%webalizer_home,g" \
    -e "s,__DATA__,%webalizer_home/ftp,g" \
    -e "s,__LOGFILE__,%vsftpd_log,g" \
    -e "s,__GEOIPDATA__,%geoip_data,g" \
    -e "s,__LOGTYPE__,ftp	# xferlog_std_format=YES to /etc/vsftpd.conf,g" \
< %SOURCE1 \
> vsftpd.conf

%make_build

%install
install -d %buildroot%_sysconfdir/{,%name,cron.d}
install -d %buildroot%_bindir
install -d %buildroot%_docdir
install -d %buildroot%webalizer_home
install -d %buildroot%webalizer_html
install -d %buildroot%_mandir/man1
install -m644 sample.conf %buildroot%_docdir/
install -m644 apache.conf %buildroot%_sysconfdir/%name/
install -m644 vsftpd.conf %buildroot%_sysconfdir/%name/
install -m755 webalizer %buildroot%_bindir
install -m644 webalizer.1 %buildroot%_man1dir
install -m644 webalizer.png %buildroot%webalizer_html
install -m644 msfree.png %buildroot%webalizer_html
touch %buildroot%_sysconfdir/%name.conf

cat << EOF > %buildroot%_sysconfdir/cron.d/%name
#!/bin/sh
15 03 * * * %webalizer_user %_bindir/%name -c %_sysconfdir/%name/apache.conf
#25 03 * * * %webalizer_user %_bindir/%name -c %_sysconfdir/%name/vsftpd.conf
EOF

ln -s webalizer %buildroot/%_bindir/webasolve

install -m644 %SOURCE2 README.ALT

%pre
grep -q "^%webalizer_group:" %_sysconfdir/group \
|| %_sbindir/groupadd -r -f %webalizer_group ||:
grep -q "^%webalizer_user:" %_sysconfdir/passwd \
|| %_sbindir/useradd -g %webalizer_group -G %apache_group -c 'The Webalizer' \
	-d %webalizer_home -s /dev/null -r %webalizer_user ||: 
if LANG=C %_bindir/id -Gn %apache2_user >/dev/null 2>&1;then \
	 %_sbindir/usermod -G %apache_group,%apache2_group %webalizer_user ||:
fi

%post
# get hostname.  This way till we have a macro.
W_HOST=`hostname`
[ $? = 0 ] || W_HOST=localhost
[ $? = 0 ] && {
	sed -i "s,__HOST__,$W_HOST,g" %_sysconfdir/%name/apache.conf ||:
}
[ $? = 0 ] && {
	sed -i "s,__HOST__,$W_HOST,g" %_sysconfdir/%name/vsftpd.conf ||:
}
[ -f "%_sysconfdir/%name.conf" ] && \
echo "NB: default webalizer configuration place is under %_sysconfdir/%name/ now
to allow for easier management of .conf files; you may want to look there
and/or update your setup." ||:

# we don't need no db_upgrade
rm -f %dns_cache ||:

#postun
#_sbindir/userdel webalizer <-- don't do it!

# fix awful user/group deletion in previous spec versions :(
%triggerpostun -- webalizer < 2.01.10-alt3
echo "Fixing permissions after faulty previous package:"
%_sbindir/groupadd -r -f %webalizer_group ||:
%_sbindir/useradd -g %webalizer_group -G %apache_group -c 'The Webalizer' \
	-d %webalizer_home -s /dev/null -r %webalizer_user ||: 
for i in %webalizer_home %webalizer_html; do
	find $i -group %apache_webmaster \( -type f -o -type d \) -print0 \
	| xargs -r0 -- chown -Rv root:%webalizer_group
done

%files
%doc CHANGES DNS.README INSTALL README* country-codes.txt sample.conf
%config(noreplace) %_sysconfdir/cron.d/*
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name/*
%ghost %config(noreplace,missingok) %verify(not size mtime md5) %_sysconfdir/%name.conf
%_bindir/*
%_man1dir/*
%dir %attr(775,root,%webalizer_group) %webalizer_home
%dir %attr(775,root,%webalizer_group) %webalizer_html
%attr(644,root,%webalizer_group) %webalizer_html/*

# FIXME:
# - wait for pseudouser naming/mgmt policy and fix the package (finally)
# - bak-around userdel -r in early packages?

%changelog
* Fri Nov 25 2011 Michael Shigorin <mike@altlinux.org> 2.01.10.RB23-alt2
- upgraded db_upgrade to rm -f (closes: #26620)

* Mon Sep 15 2008 Veaceslav Grecea <slavutich@altlinux.org> 2.01.10.RB23-alt1
- RB22 -> RB23

* Sat Aug 16 2008 Veaceslav Grecea <slavutich@altlinux.org> 2.01.10.RB22-alt2
- fixed #15371
- upgrade DNS cache in postinstall
- update BuildReq

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.10.RB22-alt1.1
- Automated rebuild with libdb-4.7.so.

* Tue Apr 01 2008 Veaceslav Grecea <slavutich@altlinux.org> 2.01.10.RB22-alt1
- RB21 -> RB22

* Thu Feb 21 2008 Veaceslav Grecea <slavutich@altlinux.org> 2.01.10.RB21-alt3
- Moved packager name to slavutich@altlinux.org
  Updated description

* Thu Dec 13 2007 Veaceslav Grecea <slavutich@grecea.net> 2.01.10.RB21-alt2
- Added GeoIP related stuff to config

* Tue Dec 11 2007 Veaceslav Grecea <slavutich@grecea.net> 2.01.10.RB21-alt1
- RB20 -> RB21

* Fri Oct 12 2007 Veaceslav Grecea <slavutich@grecea.net> 2.01.10.RB20-alt6.1.0
- Moved to RB20

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.10-alt6.1.0
- Automated rebuild.

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.10-alt6.1
- Rebuilt with libdb4.4.

* Mon Oct 17 2005 Michael Shigorin <mike@altlinux.org> 2.01.10-alt6
- (re?)added apache-devel to buildreqs: unexpanded macro was there,
  thanks Alexey Tourbin (at@) and Dmitry Levin (ldv@) for patiently
  helping me get over it being missing...

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.10-alt5.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Mon Nov 08 2004 Serge A. Volkov <vserge@altlinux.ru> 2.01.10-alt5
- Update BuildReq
- Rebuild with libgd2
 
* Mon Jun 28 2004 Michael Shigorin <mike@altlinux.ru> 2.01.10-alt4
- fixed #2977 (in a stylish manner: stuffed ||: all over the place)
- fixed #2623 (userdel issue)
- #2945 (perms on /var/log/httpd) also resolved, so no changes
  on webalizer part needed
- more secure permissions fixup
- minor spec cleanup

* Thu Jul 31 2003 Michael Shigorin <mike@altlinux.ru> 2.01.10-alt3
- removed userdel/groupdel as per proposal; closes #0002623
- moved configuration file(s) to %%_sysconfdir/%%name/
  (default webalizer.conf became webalizer/apache.conf, you
   may need to update cronjob)
- added vsftpd.conf
- reshuffled data dir somewhat (shouldn't touch legacy data)

* Tue Oct 29 2002 Michael Shigorin <mike@altlinux.ru> 2.01.10-alt2
- rebuilt with gcc 3.2

* Tue Jul 09 2002 Michael Shigorin <mike@altlinux.ru> 2.01.10-alt1
- built for ALT Linux (based on Cooker package)
- cronjob and fs permissions adjusted to run webalizer as user
- s/cron.weekly/cron.d/ seems sane to me (more freedom, less hassle)
- more out-of-box tuning introduced (mainly webalizer.conf tweaks)
