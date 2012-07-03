Name: web-cyradm
Version: 0.5.5e1
Release: alt2

Summary: Web Based Management tool for Postfix, Cyrus IMAP, and MySQL or PostgreSQL
License: GPL
Group: System/Servers

Url: http://www.web-cyradm.org
Source0: %url/%name-%version.tar

Source1: web-cyradm.apache.conf
Source2: web-cyradm.htaccess
Source3: web-cyradm.README.ALT
Source4: web-cyradm.logrotate

BuildArch: noarch

BuildRequires(pre): rpm-macros-apache2

Requires: php-engine php5-mysql php5-mbstring php5-imap

Requires: pear-DB

%package apache2
Summary: %name's apache2 config file
Group: System/Servers
Requires: %name = %version-%release, apache2

%description apache2
%name's apache2 config file


%description
Web-cyradm is a software that glues topnotch mailing technologies together.
The focus is on administrating small and large mailing environments.

Features:
- Administer multiple virtual domains
- Manage user-accounts
- Map useraccounts to emailadresses
- Create, delete and rename cyrus-imap mailboxes
- Setting of quotas for users and domains
- Delegation of some tasks to domain adminstrators
- Resetting password for accountusers by its domainadmins and superusers
- Sieve functions like forwarding single e-mail adresses and out-of-office replies
- Enable/Disable different services like imap, pop, sieve and stmp for particular users
- Support for MySQL and PostgreSQL databases
- Storing passwords in crypt, md5 or MySQL passwd compatible format
- i18n (internationalisation) support 
- Available in 18 Languages (see the translation statistics )

%description apache2
%name's apache2 config file

%prep
%setup

%install
rm -f COPYRIGHT
mkdir -p %buildroot%webserver_webappsdir/%name/
cp -ar *.php %buildroot%webserver_webappsdir/%name/
cp -ar css images lib locale %buildroot%webserver_webappsdir/%name/

install -pD -m0640 config/conf.php.dist \
	%buildroot%webserver_webappsdir/%name/config/conf.php

install -pD -m0644 %SOURCE1 %buildroot%apache2_confdir/addon.d/A.%name.conf
install -pD -m0644 %SOURCE2 %buildroot%webserver_webappsdir/%name/.htaccess
install -pD -m0644 %SOURCE3 README.ALT
install -pD -m0644 %SOURCE4 %buildroot%_sysconfdir/logrotate.d/%name

install -d -m1770 %buildroot%_var/log/%name

%files
%webserver_webappsdir/%name/*.php
%dir %attr(0750,root,%apache2_user) %webserver_webappsdir/%name/config
%config(noreplace) %attr(0640,root,%apache2_user) %webserver_webappsdir/%name/config/conf.php
%webserver_webappsdir/%name/css
%webserver_webappsdir/%name/images
%webserver_webappsdir/%name/lib
%webserver_webappsdir/%name/locale
%dir %webserver_webappsdir/%name/
%dir %attr(1770,root,%apache2_user) %_var/log/%name/
%_sysconfdir/logrotate.d/%name
%doc ChangeLog README* TO-BE-DONE INSTALL doc scripts

%files apache2
%webserver_webappsdir/%name/.htaccess
%config(noreplace) %apache2_confdir/addon.d/A.%name.conf

%changelog
* Tue Jun 14 2011 Vitaly Lipatov <lav@altlinux.ru> 0.5.5e1-alt2
- add missed requires pear-DB
- fix apache config

* Tue Jun 14 2011 Vitaly Lipatov <lav@altlinux.ru> 0.5.5e1-alt1
- build 0.5.5 with Etersoft's patches
- build subpackage for Apache2

* Fri Jun 16 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.4-alt2
- $%%$%%! Set BuildArch: noarch

* Thu Jun 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.4-alt1
- Initial build for Sisyphus
