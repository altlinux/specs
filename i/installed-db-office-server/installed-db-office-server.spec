Name: installed-db-office-server
Version: 1.3
Release: alt9
Summary: Databases and config files for moodled, mediawiki and rujel
License: GPL
Group: Editors
Source: %name.tar.gz
BuildArch: noarch
Requires: mediawiki mediawiki-apache2 mediawiki-ldap
Requires: moodle-install-tools moodle2.2 

%description
Databases and config files for moodle, mediawiki and rujel

%prep
%setup -q -c

%build

%install

mkdir -p %buildroot/usr/share/%name
install -Dp -m755 %name/80-office-server %buildroot/usr/share/install2/preinstall.d/80-office-server
install -Dp -m755 %name/root.d %buildroot/usr/lib/alterator/hooks/root.d/installed-db
install -Dp -m755 %name/httpd2-office-server %buildroot%_sysconfdir/firsttime.d/httpd2-office-server
install -Dp -m755 %name/moodle %buildroot/etc/hooks/hostname.d/94-moodle-ldap
install -Dp -m755 %name/mediawiki %buildroot/etc/hooks/hostname.d/95-mediawiki-ldap
install -Dp -m755 %name/owncloud %buildroot/etc/hooks/hostname.d/96-owncloud-ldap
install -Dp -m755 %name/rujel %buildroot/usr/lib/alterator/hooks/firsttime.d/rujel-ldap
install -Dp -m755 %name/gpm %buildroot/usr/lib/alterator/hooks/firsttime.d/gpm

cp -r %name %buildroot/usr/share
mkdir -p %buildroot/var/www/webapps/mediawiki
# ln -s /usr/share/doc/alt-docs/indexhtml/img/project-logo.png %buildroot/var/www/webapps/mediawiki/project-logo.png

%files
# /var/www/webapps/mediawiki/project-logo.png
/usr/share/%name
/etc/firsttime.d/*-office-server
/usr/share/install2/preinstall.d/*
/usr/lib/alterator/hooks/root.d/*
/usr/lib/alterator/hooks/firsttime.d/*
/etc/hooks/hostname.d/*

%changelog
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
