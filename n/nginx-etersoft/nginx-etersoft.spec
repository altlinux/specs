Name: nginx-etersoft
Version: 0.2.20
Release: alt1

Summary: Additional Nginx templates and functions

License: AGPLv3
Group: Development/Other
Url: http://www.altlinux.org/Nginx-etersoft

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/%name.git
# git-clone http://git.etersoft.ru/people/lav/packages/%name.git
Source: %name-%version.tar

BuildArchitectures: noarch

# error: File must begin with "/": %webserver_htdocsdir/maintenance/
BuildRequires: rpm-macros-webserver-common

Requires: nginx >= 1.8.1

%description
Additional Nginx templates and functions.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/nginx/include/limits/
install -m644 include/*.conf %buildroot%_sysconfdir/nginx/include/
install -m644 include/*.inc %buildroot%_sysconfdir/nginx/include/
install -m644 include/limits/* %buildroot%_sysconfdir/nginx/include/limits/

mkdir -p %buildroot%_sysconfdir/nginx/httpconf-enabled.d/

mkdir -p %buildroot%_sysconfdir/nginx/httpconf-available.d/
install -m644 httpconf-available.d/* %buildroot%_sysconfdir/nginx/httpconf-available.d/

mkdir -p %buildroot%_sysconfdir/nginx/sites-available.d/
install -m644 sites-available.d/* %buildroot%_sysconfdir/nginx/sites-available.d/

mkdir -p %buildroot%_sysconfdir/nginx/examples/
install -m644 examples/* %buildroot%_sysconfdir/nginx/examples/

mkdir -p %buildroot%_datadir/%name/images/
install -m644 share/images/* %buildroot%_datadir/%name/images/

mkdir -p %buildroot%webserver_htdocsdir/maintenance/
install -m644 www/* %buildroot%webserver_htdocsdir/maintenance/

%files
%dir %_sysconfdir/nginx/include/
%config(noreplace) %_sysconfdir/nginx/include/*
%dir %_sysconfdir/nginx/httpconf-available.d/
%dir %_sysconfdir/nginx/httpconf-enabled.d/
%config(noreplace) %_sysconfdir/nginx/httpconf-available.d/*
%config(noreplace) %_sysconfdir/nginx/sites-available.d/
%_sysconfdir/nginx/examples/
%_datadir/%name/
%dir %webserver_htdocsdir/maintenance/
%config(noreplace) %webserver_htdocsdir/maintenance/*

%changelog
* Thu Jan 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.20-alt1
- fix static-stub-* conf
- add static-stub404.conf
- ssl.conf: improve cookie security
- separate hsts to sslhsts.conf

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.19-alt1
- static-fallback.conf: drop double fonts list
- mediawiki: fix for trailing slash
- fix duplicate $uri $uri/ in try_files
- cors*.conf: drop if (https://trac.nginx.org/nginx/ticket/234)

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.18-alt1
- separate locations by file types
- add CORS wide-open rules
- add CORS with http_referer

* Thu Apr 20 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.17-alt1
- letsencrypt: add allow all
- ssl: improve comment
- extent static extensions

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.16-alt1
- set Accept-Encoding to empty (force disabling gzip on apache side)
- add OCSP stapling (eterbug #11621)

* Sat Sep 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.15-alt1
- log.conf: add some logs formats
- add nosslonly.conf script
- store-proxy: add X-Powered-By
- add ip-server config for ignore ip based requests
- add HSTS example
- add stop-cms.conf against requests to a popular CMS urls

* Thu Apr 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.14-alt1
- set required nginx version to 1.8.1
- use default proxy_cache_key value
- use scheme for proxy_cache_key
- make proxy_cache_lock really works
- add store-week-proxy.conf
- add proxy_*_timeout example

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.13-alt1
- allow permanent trans-repoxy
- add letsencrypt.conf
- create_nginx: add check

* Thu Mar 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.12-alt1
- set X-Forwarded-Proto for static proxy too

* Thu Mar 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.11-alt1
- add woff2 support
- improve TLS security (eterbug #10599)
- add comment about ssl detection on the server side

* Thu Nov 12 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt1
- stop-injection: replace 401 with 406 error code
- stop-injection: fix against sleep
- do not wait so long for login to admin part

* Fri Oct 30 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2.9-alt1
- update limits
- stop-crack: add rules for Joomla xmlrpc.php and Bitrix admin
- add hostreq limit for per site restriction
- add log write to deny rules
- fix anti injection rules and add write to log
- stop-crack: fix bitrix rule, add phpbb rule

* Thu Aug 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2.8-alt1
- log.conf: add logdata
- mediawiki: improve
- store-proxy: cache lock on
- store-proxy: ignore Set-Cookie

* Mon Mar 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2.7-alt1
- fix limit name
- improve stop-injection
- static-fallback: remove json and xml from rules
- add static-icons and disable nocache for first pages
- static-fallback: update video formats
- add stat-apache file
- ssl fixes

* Sat Oct 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt1
- use /var/lib/vz/private
- fix expires
- add mediateproxy, fix other configs
- rewrite trans conf via main trans-proxy.inc

* Sun Oct 06 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- rename config, add techalias
- rewrite the rewrite checking code
- create_nginx: add support for mediawiki engine
- static-fallback: add support for yandex auth file

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- improve stop-injection.conf
- stop-crack: catch /edit requests
- admin pages: do log access-admin.log
- static-stub: make log
- stop-crack: stop wp-admin control
- add maintenance page

* Sat Mar 23 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- add trans-admin-proxy.conf
- deny.conf: forbids sql and .hg
- stop-crack.conf: slow login pages for WordPress and Joomla
- add limits for media
- move admin limits to separate files

* Fri Jan 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- add static-stub and images for it
- add no_cache example
- create_nginx_from_apache: do not update config if not changed

* Sat Nov 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- add nodelay to limit_req
- add initial stop-injection.conf

* Wed Mar 21 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- moved to nginx >= 1.1.8
- too many incompatible changes

* Thu Mar 15 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- add subst-site.conf for site.ru/subdir -> some.site.ru proxying

* Mon Nov 07 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- add static-fallback.conf, mark as obsoleted static, static-images

* Thu Oct 20 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- add logdefine.conf
- add reproxy.conf for internal redirect
- small static update

* Thu Jun 09 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- add static-images.conf

* Thu Nov 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- fix robots.txt rewrite for set-mainhost

* Thu Nov 11 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- correct ignore www rewrite for robots.txt
- hold scheme when set main host
- set proxy_buffer_size in all proxy
- use relate path instead full

* Sun Mar 07 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- add examples, add ssl configs

* Sat Mar 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build

