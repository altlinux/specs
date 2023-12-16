%define php_version 8.2
%define system_requires apache2-base, apache2-mod_php%php_version, apache2-mod_ssl, mariadb-server
%define deploy_requires deploy >= 0.4
%define rule_requires   python3-module-pymysql, pwgen, curl

Name: installed-db-office-server
Version: 1.5.4
Release: alt1
Summary: Databases and config files for moodle, mediawiki and nextcloud
License: GPL-2.0+
Group: System/Configuration/Other
Source: %name-%version.tar
BuildArch: noarch

Requires: %name-mediawiki = %EVR
Requires: %name-nextcloud = %EVR
Requires: %name-moodle = %EVR

%description
Databases and config files for moodle, mediawiki and nextcloud

%package mediawiki
Summary: Databases and config files for mediawiki
Group: System/Configuration/Other
Requires: %system_requires
Requires: %deploy_requires
Requires: %rule_requires
Requires: mediawiki
Requires: mediawiki-apache2
Requires: mediawiki-mysql
Requires: python3-module-pymysql
Requires: pwgen
Requires: curl

%description mediawiki
Databases and config files for mediawiki

%package moodle
Summary: Databases and config files for moodle
Group: System/Configuration/Other
Requires: %system_requires
Requires: %deploy_requires
Requires: %rule_requires
Requires: moodle
Requires: moodle-apache2
Requires: moodle-base
Requires: moodle-local-mysql
Requires: python3-module-pymysql
Requires: pwgen
Requires: curl

%description moodle
Databases and config files for moodle

%package nextcloud
Summary: Databases and config files for nextcloud
Group: System/Configuration/Other
Requires: %system_requires
Requires: %deploy_requires
Requires: %rule_requires
Requires: nextcloud
Requires: nextcloud-apache2
Requires: php%php_version-pcntl
Requires: php%php_version-pdo_mysql
Requires: python3-module-pymysql
Requires: pwgen
Requires: curl
Provides: %name-owncloud = %EVR
Obsoletes: %name-owncloud < %EVR

%description nextcloud
Databases and config files for nextcloud

%prep
%setup

%build

%install
for service in mediawiki nextcloud moodle; do
    install -Dp -m755 $service %buildroot%_sysconfdir/firsttime.d/80-office-server-$service
    install -Dp -m755 ${service}-password %buildroot%_libexecdir/alterator/hooks/root.d/$service
done

%files

%files mediawiki
%_sysconfdir/firsttime.d/80-office-server-mediawiki
%_libexecdir/alterator/hooks/root.d/mediawiki

%files moodle
%_sysconfdir/firsttime.d/80-office-server-moodle
%_libexecdir/alterator/hooks/root.d/moodle

%files nextcloud
%_sysconfdir/firsttime.d/80-office-server-nextcloud
%_libexecdir/alterator/hooks/root.d/nextcloud

%changelog
* Sat Dec 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- Use PHP 8.2.
- Add python3-module-pymysql, pwgen and curl.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt2
- Use PHP 8.0.

* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- Remove empty configuration file of nextcloud.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- Disable debug mediawiki deploy.

* Tue Oct 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Wait 30s before first deploy (mediawiki).
- Debug mediawiki deploy.

* Wed Jul 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Remove deprecated mediawiki-ldap from requirements.

* Fri Jul 16 2021 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Use deploy for installation and password change.

* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.8-alt1
- Set strong password during mediawiki deploy.
- Do not set password for MySQL during root password change.
- Set License to GPL-2.0+.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.7-alt1
- Fix set admin password for nextcloud.

* Wed Oct 09 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.6-alt1
- Remove 95-office-server-postinstall as sp package is unsupported.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- Open pages after deploy to pass cache errors
- Fix write all output include stderr to log

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Fix run chkconfig under systemd for httpd2 enable
- Fix arguments passed for nextcloud deploy
- Replace installed-db-office-server-owncloud for -nextcloud

* Mon Jun 24 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- Set shell for su in nextcloud deploy.
- Fix warning about memory_limit for nextcloud deploy.

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Fix Moodle wwwroot.
- Fix admin password change.
- Add hostname to trusted domains for Nextcloud.

* Mon Jun 17 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Requires all needed packages.
- Supports nextcloud and moodle 3.6.
- Move all deploy actions to firsttime.d.
- Log deploy to /root/.install-log/office-server-deploy.log.

* Mon Jul 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt13
- Support moodle2.5 instead of moodle2.2
- Enable mod_filter

* Tue Apr 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.4-alt12
- New hook in postinstall.d/95-office-server-postinstall
- Fix path to School Portal in DocumentRoot
- Update MediaWiki database
- Remove trusted domains and leave maintenance mode for Owncloud
- Update initial database settings for Owncloud 7.0.4

* Tue Dec 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt11
- owncloud with ldap integration fixed

* Thu Apr 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt10
- unconditional chkconfig httpd2 on

* Wed Mar 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt9
- owncloud with ldap integration fixed

* Tue Mar 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt6
- owncloud installation without wiki fixed

* Fri Mar 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt4
- premature exit fixed
- data files placement fixed

* Fri Mar 01 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt3
- lost script re-added into package

* Wed Feb 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt2
- interpackage requires added

* Wed Feb 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt1
- split on mediawiki, moodle, owncloud and rujel packages

* Thu Aug 30 2012 Andrey Cherepanov <cas@altlinux.org> 1.3-alt10
- updated rujel user access privileges for MySQL (thanks Gennady Kushnir)

* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt9
- moodle domain changing fixed

* Thu May 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt8
- passwords changing fixed
- moodle language setting fixed

* Wed May 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt7
- hardcoded russian language for moodle

* Mon May 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt6
- moodle siteurl fixed

* Thu May 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt5
- moodle-install-tools support

* Mon Apr 23 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt4
- fixed for owncloud 3.0.2

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt3
- owncloud ldap connection fixed

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt2
- owncloud setup fixed

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt1
- owncloud setup added

* Thu Apr 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2-alt1
- set root password for services

* Thu Dec 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt3
- setup user-visible domain name on mediawiki config

* Wed Dec 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt2
- mediawiki-ldap run priority fixed

* Tue Dec 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- dependences on mediawiki packages added
- new mediawiki database dump
- mediawiki config and config place fixed
- mediawiki script moved to hostname.d

* Thu Dec 23 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt11
- fix RUJEL deployment script

* Tue Dec 14 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt10
- don't create empty database 'rujel'

* Wed Dec 08 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt9
- fix RUJEL grant statements
- enable gpm by default

* Tue Dec 07 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt8
- fix RUJEL database creation
- add files for RUJEL LDAP authentication

* Wed Dec 01 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt7
- Completely fixed access denided messages while mysqld configuration
- Added rujel database

* Mon Nov 29 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt6
- Fixed access denided messages in mysqld configuration

* Thu Mar 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt5
- Enable mod_rewrite (ALT #23075)

* Wed Oct 14 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt4
- specify httpd2 runlevels

* Thu Aug 13 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3
- Change first day of the week to monday in moodle

* Fri Jul 31 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2
- Update

* Thu Jul 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- Initial based on installed-db-school-server
