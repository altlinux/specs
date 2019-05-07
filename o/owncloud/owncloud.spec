Name: owncloud
Version: 10.1.1
Release: alt1

%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPLv3
Url: https://owncloud.org/

BuildRequires(pre): rpm-macros-webserver-common
BuildArch: noarch

Requires(pre): webserver-common

#https://doc.owncloud.org/server/9.1/admin_manual/installation/source_installation.html
Requires: php7-libs php7-dom php7-gd2 php7-mbstring php7-xmlreader php7-zip php7-curl php7-fileinfo php7-intl
#For SQL DBs:
Requires: php7-pdo-driver

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%description
ownCloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %EVR apache2-mod_php7 apache2-mod_ssl
Requires(post): cert-sh-functions

%description apache2
Apache 2.x web-server default configuration for %name.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %EVR nginx
Requires(post): cert-sh-functions

%description nginx
nginx web-server default configuration for %name.

%prep
%setup

%install
mkdir -p %buildroot%installdir
cp -rp %name/* %buildroot%installdir/
cp %name/.htaccess %buildroot%installdir/
cp %name/.user.ini %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr

mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%installdir/config/ %buildroot%_sysconfdir/%name/.
ln -s %_sysconfdir/%name/config %buildroot%installdir/config

mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

#install apache2
install -pD -m0644 apache2/default.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

#install nginx
install -pD -m0644 nginx/default.conf %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
# Generate SSL key
. cert-sh-functions
ssl_generate "owncloud"
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%post nginx
# Generate SSL key
. cert-sh-functions
ssl_generate "owncloud"

%files
%dir %installdir
%dir %attr(0775,root,_webserver) %installdir/apps
%installdir/apps/*
%installdir/core
%installdir/lib
%installdir/oc*
%installdir/resources
%installdir/settings
%installdir/updater
%dir %attr(0770,root,_webserver) %_sysconfdir/%name/config/
%_sysconfdir/%name
%installdir/config
%dir %attr(0770,root,_webserver) %_localstatedir/%name
%installdir/data
%installdir/*.php
%installdir/.htaccess
%installdir/.user.ini
%doc %installdir/AUTHORS
%doc %installdir/CHANGELOG.md
%doc %installdir/COPYING
%installdir/*.xml
%installdir/index.html
%installdir/robots.txt

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%changelog
* Tue May 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 10.1.1-alt1
- 10.1.1

* Wed Mar 13 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 10.1.0-alt2
- fix deps and conf (apache/nginx)

* Thu Mar 07 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 10.1.0-alt1
- 10.1.0 (closes: #35308, #36099)
- NMU: Generate SSL key diring package installation (by cas@) (closes: #36095)

* Wed Mar 06 2019 Anton Farygin <rider@altlinux.ru> 7.0.9-alt1.1
- dependencies on php5 and old owncloud modules removed due to cleaning sisyphus

* Wed Jun 29 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 7.0.9-alt1
- 7.0.9

* Wed Feb 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.4-alt1
- 7.0.4

* Wed Sep 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.2-alt1
- 7.0.2

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.3-alt1
- 6.0.3

* Wed Jan 29 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Wed Jan 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.14a-alt1
- 5.0.14a

* Wed Nov 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.13-alt1
- 5.0.13

* Thu Sep 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.11-alt1
- 5.0.11

* Mon May 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.6-alt1
- 5.0.6

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.4-alt1
- 5.0.4

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Thu Mar 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.5.8-alt1
- 4.5.8

* Tue Feb 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.5.7-alt1
- 4.5.7 from new upstream git

* Tue Feb 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Fri Aug 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.7-alt2
- an ability to play mp3 without tags added

* Tue Aug 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.7-alt1
- 4.0.7

* Thu Aug 09 2012 Denis Baranov <baraka@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Wed Jun 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Tue May 22 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Thu May 03 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.0.2-alt2
- fix some double utf8 bugs

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt1
- merge upstream v3.0.1-88-g51049d8

* Fri Apr 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Thu Apr 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0-alt2
- add webserver-common to prereq

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0-alt1
- initial

