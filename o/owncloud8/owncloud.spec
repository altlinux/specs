%define major 8

Name: owncloud%major
Version: 8.0.9
Release: alt1

%define installdir %webserver_webappsdir/%name
%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPLv3
Url: http://www.owncloud.org/

BuildRequires(pre): rpm-macros-webserver-common
BuildArch: noarch

Requires(pre): webserver-common
Requires: php5-dom
Requires: %name-apps
Requires: %name-3rdparty

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/WWW
Requires: %name = %version-%release apache2 php5-gd2 php5-zip php5-mbstring php5-pdo_mysql
%description apache2
Apache 2.x web-server configuration for %name

%prep
%setup

%install
# install apache config
install -pD -m0644 alt/apache2.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
# install owncloud
mkdir -p %buildroot%installdir

cp -rp * %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr

mv %buildroot%installdir/config %buildroot%_sysconfdir/%name
ln -s %_sysconfdir/%name %buildroot%installdir/config

	mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

rm -rf %buildroot%installdir/alt
rm -f %buildroot%installdir/l10n/l10n.pl

%post apache2
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%doc AUTHORS
%doc COPYING-AGPL
%doc COPYING-README
#%installdir/3rdparty
%dir %attr(0775,root,_webserver) %installdir/apps
%installdir/apps/*
%dir %attr(0770,root,_webserver) %_sysconfdir/%name
%installdir/config
%_sysconfdir/%name/*.php
%installdir/core
%installdir/l10n
%installdir/lib
%installdir/ocs
%installdir/settings
%installdir/*.php
%installdir/*.html
%installdir/*.xml
%dir %attr(0770,root,_webserver) %_localstatedir/%name
%installdir/data
%installdir/robots.txt

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%changelog
* Thu Jun 30 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0.9-alt1
- 8.0.9

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

