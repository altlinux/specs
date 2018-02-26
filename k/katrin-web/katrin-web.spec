%define major_version 1.5
Name: katrin-web
Version: %major_version.0
Release: alt3.1

%define installdir /var/www/webapps/%name
%add_python_lib_path %installdir

Summary: Web interface for Katrin billing system
License: GPL
Group: Networking/WWW
Requires: python-module-flup
Requires: python-module-django1.1-dbbackend-mysql
Requires: python-module-django-command-extensions

URL: http://katrin.sf.net
Packager: Denis Klimov <zver@altlinux.ru>
BuildArch: noarch

Source: katrin-web.tar
Source11: apache.katrin-web.conf
Source12: apache2.katrin-web.conf
Source14: apache2_python.katrin-web.conf
Source2: katrin-cli
Source3: katrin-lightsquid
Source4: katrin-web-cron-tasks
Source5: katrin-web-db-service

%description
Web interface for Katrin billing system.
%description -l ru_RU.UTF8
Web-интерфейс для биллинговой системы Katrin

%package apache
Summary: Apache conf files for katrin-web
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache
Requires: mod_fastcgi

%description apache
This package provides Apache config files for katrin-web.
%description -l ru_RU.UTF8 apache
Конфигурационные файлы katrin-web для Apache

%package apache2
Summary: Apache2 conf files for katrin-web
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2
Requires: apache2-mod_fcgid

%description apache2
This package provides Apache2 config files for katrin-web.
%description -l ru_RU.UTF8 apache2
Конфигурационные файлы katrin-web для Apache2

%package apache2-python
Summary: Apache2 conf files for deploying katrin-web with mod_python
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2
Requires: apache2-mod_python
Requires: python-module-django1.1-mod_python

%description apache2-python
Apache2 config files for deploying katrin-web with mod_python
%description -l ru_RU.UTF8 apache2-python
Конфигурационные файлы katrin-web для Apache2+mod_python

%package -n katrin-cli
Summary: CLI for katrin-web
Group: Networking/WWW
Requires: %name = %version-%release

%description -n katrin-cli
Command line interface (CLI) for katrin.
It use katrin-web. For run it katrin-web must be correctly config.
%description -l ru_RU.UTF8 -n katrin-cli
CLI интфейс для katrin. Для верной работы необходимо чтобы в katrin-web
файл settings.py был верно настроен.

%package -n katrin-lightsquid
Summary: Katrin lightsquid utils
Group: Networking/WWW
Requires: katrin-cli = %version-%release

%description -n katrin-lightsquid
Katrin lightsquid script output pairs IP LOGIN all katrin users, which
use traff service. This output may be used for feel lightsquid realname
config file before call lightsquid by cron.
%description -l ru_RU.UTF8 -n katrin-lightsquid
Скрипт, выводящий пары значений IP LOGIN для каждого пользователя
katrin, который пользуется traff услугой. Этот вывод может
использоваться для заполнения lightsquid realname конфигурационного
файла перед вызовом lightsquid по cron.

%package user
Summary: User web page module of Katrin billing system
Group: Networking/WWW
Requires: katrin-web >= %major_version.0
%description user
Katrin module which add user web page for show balance

%package traff
Summary: Traff web module of Katrin billing system
Group: Networking/WWW
Provides: katrin-traff = %version-%release
Requires: katrin-web >= %major_version.0
%description traff
Traffic web module of Katrin billing system

%package tel
Summary: Tel web module of Katrin billing system
Group: Networking/WWW
Provides: katrin-tel = %version-%release
Requires: katrin-web >= %major_version.0
%description tel
Tel web module of Katrin billing system

%package ve
Summary: VE web module of Katrin billing system
Group: Networking/WWW
Provides: katrin-ve = %version-%release
Requires: katrin-web >= %major_version.0
%description ve
VE rent module of Katrin billing system


%prep
%setup -n katrin-web

%build

%install

mkdir -p %buildroot%_sysconfdir/httpd/conf/addon-modules.d/
install -pD %SOURCE11 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/
mkdir -p %buildroot%_sysconfdir/httpd2/conf/sites-available/
install -pD %SOURCE12 %SOURCE14 %buildroot%_sysconfdir/httpd2/conf/sites-available/

mkdir -p %buildroot%_sysconfdir/httpd2/conf/sites-enabled
ln -s %_sysconfdir/httpd2/conf/sites-available/{`basename %SOURCE12`,`basename %SOURCE14`} %buildroot%_sysconfdir/httpd2/conf/sites-enabled/

install -pD %SOURCE2 %buildroot%_sbindir/katrin
install -pD %SOURCE3 %buildroot%_sbindir/katrin-lightsquid
install -pD -m 750 %SOURCE5 %buildroot%_sbindir/katrin-web-db-service
install -pD -m 640 %SOURCE4 %buildroot%_sysconfdir/cron.d/katrin-web-db-service

mkdir -p %buildroot%installdir
cp -pR katrin-web/* %buildroot%installdir/
sed -i -e 's/^DEBUG = True/DEBUG = False/g' %buildroot%installdir/settings_default.py

%post
chown -R root:_webserver %installdir
chmod -R g+rw %installdir
chmod -R o-rwx %installdir

%post user
chown -R root:_webserver %installdir/user
chmod -R g+rw %installdir/user
chmod -R o-rwx %installdir/user

%post traff
chown -R root:_webserver %installdir/traff
chmod -R g+rw %installdir/traff
chmod -R o-rwx %installdir/traff

%post tel
chown -R root:_webserver %installdir/tel
chmod -R g+rw %installdir/tel
chmod -R o-rwx %installdir/tel

%post ve
chown -R root:_webserver %installdir/ve
chmod -R g+rw %installdir/ve
chmod -R o-rwx %installdir/ve

%post apache
chmod a-x %_sysconfdir/httpd/conf/addon-modules.d/apache.katrin-web.conf
%post_service httpd

%postun apache
%post_service httpd

%post apache2
a2enmod fcgid
a2enmod rewrite
chmod a-x %_sysconfdir/httpd2/conf/sites-available/apache2.katrin-web.conf
%post_service httpd2

%postun apache2
%post_service httpd2

%post apache2-python
a2enmod python
a2enmod env
chmod a-x %_sysconfdir/httpd2/conf/sites-available/apache2_python.katrin-web.conf
%post_service httpd2

%postun apache2-python
%post_service httpd2

%files
%doc Changelog
%installdir/initial_data.json*
%installdir/manage.py
%installdir/urls.py
%installdir/dispatch.fcgi
%installdir/dispatch.wsgi
%installdir/katrin
%installdir/templates/*.html
%installdir/templates/locale
%installdir/templates/admin
%installdir/settings_default.py
%installdir/__init__.py
%installdir/userbills/*
%_sbindir/katrin-web-db-service
%_sysconfdir/cron.d/katrin-web-db-service
%config(noreplace) %installdir/settings.py

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/apache.katrin-web.conf

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/sites-available/apache2.katrin-web.conf
%config(noreplace) %_sysconfdir/httpd2/conf/sites-enabled/apache2.katrin-web.conf

%files apache2-python
%config(noreplace) %_sysconfdir/httpd2/conf/sites-available/apache2_python.katrin-web.conf
%config(noreplace) %_sysconfdir/httpd2/conf/sites-enabled/apache2_python.katrin-web.conf

%files -n katrin-cli
%_sbindir/katrin

%files -n katrin-lightsquid
%_sbindir/katrin-lightsquid

%files user
%installdir/user
%installdir/templates/user

%files traff
%installdir/traff
%installdir/templates/traff

%files tel
%installdir/tel
%installdir/templates/tel

%files ve
%installdir/ve


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt3.1
- Rebuild with Python-2.7

* Wed Oct 05 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt3
- fix git inherit with ALT gear repo

* Tue Oct 04 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt2
- fix packaging katrin-web-cron-tasks

* Mon Sep 26 2011 Denis Klimov <zver@altlinux.org> 1.5.0-alt1
- new version

* Thu Aug 04 2011 Denis Klimov <zver@altlinux.org> 1.4.1.0-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Rebuilt with python 2.6

* Fri Nov 27 2009 Denis Klimov <zver@altlinux.org> 1.4.0-alt4
- change require to python-module-django1.1-mod_python

* Sun Nov 22 2009 Denis Klimov <zver@altlinux.org> 1.4.0-alt3
- change require to python-module-django1.1-dbbackend-mysql

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.4.0-alt2
- exclude needless files from taxi subpackage

* Fri Nov 20 2009 Denis Klimov <zver@altlinux.org> 1.4.0-alt1
- new version

* Sat Feb 14 2009 Denis Klimov <zver@altlinux.org> 1.3.0-alt2
- turn off debug mode in settings file
- use sysconfdir macros in install section

* Tue Feb 03 2009 Denis Klimov <zver@altlinux.org> 1.3.0-alt1
- new version

* Tue Dec 23 2008 Denis Klimov <zver@altlinux.org> 1.2.6-alt1
- new version

* Wed Nov 19 2008 Denis Klimov <zver@altlinux.ru> 1.2.5-alt1
- new version
- add katrin-lightsquid subpackage

* Tue Nov 18 2008 Denis Klimov <zver@altlinux.ru> 1.2.4-alt1
- new version

* Sat Nov 01 2008 Denis Klimov <zver@altlinux.ru> 1.2.3-alt1
- new version

* Mon Oct 27 2008 Denis Klimov <zver@altlinux.ru> 1.2.2-alt1
- add russian description for packages
- add Changelog file to katrin-web package

* Fri Oct 10 2008 Denis Klimov <zver@altlinux.ru> 1.2.1-alt1
- more compact select user in traff menu
- fix show summary user stats by year

* Sun Oct 05 2008 Denis Klimov <zver@altlinux.ru> 1.2.0-alt1
- support 1.2.0 katrin db scheme
- change structure of traff stats pages

* Fri Oct 03 2008 Denis Klimov <zver@altlinux.ru> 1.1.4-alt1
- add katrin-cli subpackage

* Thu Oct 02 2008 Denis Klimov <zver@altlinux.ru> 1.1.3-alt1
- show title in filter page

* Sat Sep 06 2008 Denis Klimov <zver@altlinux.org> 1.1.2-alt1
- modify for work with first django release

* Wed May 28 2008 Denis Klimov <zver@altlinux.ru> 1.1.1-alt1
- check admin auth in custom views
- add refill page

* Sun May 04 2008 Denis Klimov <zver@altlinux.ru> 1.1.0-alt1
- add statistics by filters feature

* Tue Apr 29 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt2
- add store stat field in models

* Tue Mar 11 2008 Denis Klimov <zver@altlinux.ru> 1.0.0-alt1.RC0
- make separate django applications
- support 1.0.0-RC1 katrin database schema

* Tue Dec 25 2007 Denis Klimov <zver@altlinux.ru> 0.4-alt1
- modify models
- add menu in stat pages
- add define encoding

* Thu Dec 13 2007 Denis Klimov <zver@altlinux.ru> 0.3-alt1
- show traffic bytes as float
- add cost in stats of month and order by it
- add RequestContext in return functions for show userlink

* Wed Dec 05 2007 Denis Klimov <zver@altlinux.ru> 0.2-alt1
- build for 0.2 version

* Thu Nov 29 2007 Denis Klimov <zver@altlinux.ru> 0.1-alt1
- init build for ALT Linux


