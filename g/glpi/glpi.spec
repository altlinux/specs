%define installdir %webserver_webappsdir/%name

Name: glpi
Version: 10.0.5
Release: alt1

Summary: IT and asset management software
License: GPLv3
Group: Networking/Other

URL: http://www.glpi-project.org
Packager: Pavel Zilke <zidex at altlinux dot org>
BuildArch: noarch

Source0: http://www.glpi-project.org/IMG/gz/%name-%version.tar.gz
Source1: apache2.conf
Source2: README.ALT
Source3: UPGRADE.ALT
#Patch: patch0.patch

Requires: webserver-common php-engine curl lynx
BuildRequires(pre): rpm-macros-webserver-common

%description
GLPI is the Information Resource-Manager with an additional Administration-
Interface.
You can use it to build up a database with an inventory for your company
(computer, software, printers...).
It has enhanced functions to make the daily life for the administrators easier,
like a job-tracking-system with mail-notification and methods to build a
database with basic information about your network-topology.

%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/Other
Requires: %name = %version-%release, apache2
%description apache2
Apache 2.x web-server configuration for %name

%package php7
Summary: PHP7 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release
Requires: php7 >= 7.4
Requires: php7-curl, php7-fileinfo, php7-gd2, php7-json, php7-mbstring, php7-mysqlnd-mysqli, php7-session, php7-zlib, php7-simplexml, php7-xml, php7-intl
Requires: php7-apcu, php7-bz2, php7-exif, php7-ldap, php7-opcache, php7-openssl, php7-sodium, php7-xmlrpc, php7-zip

%description php7
PHP7 dependencies for %name

%package php8.0
Summary: PHP8.0 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release
Requires: php8.0
Requires: php8.0-curl, php8.0-fileinfo, php8.0-gd2, php8.0-json, php8.0-mbstring, php8.0-mysqlnd-mysqli, php8.0-session, php8.0-zlib, php8.0-simplexml, php8.0-xml, php8.0-intl
Requires: php8.0-apcu, php8.0-bz2, php8.0-exif, php8.0-ldap, php8.0-opcache, php8.0-openssl, php8.0-sodium, php8.0-xmlrpc, php8.0-zip

%description php8.0
php8.0 dependencies for %name

%package php8.1
Summary: PHP8.1 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release
Requires: php8.1
Requires: php8.1-curl, php8.1-fileinfo, php8.1-gd2, php8.1-json, php8.1-mbstring, php8.1-mysqlnd-mysqli, php8.1-session, php8.1-zlib, php8.1-simplexml, php8.1-xml, php8.1-intl
Requires: php8.1-apcu, php8.1-bz2, php8.1-exif, php8.1-ldap, php8.1-opcache, php8.1-openssl, php8.1-sodium, php8.1-zip

%description php8.1
php8.1 dependencies for %name


%prep
%setup

%build

%install
# install apache config
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

# install glpi
mkdir -p %buildroot%installdir
cp -rp * %buildroot%installdir/

#install README.ALT and UPGRADE.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT
install -pD -m0644 %_sourcedir/UPGRADE.ALT UPGRADE.ALT

# remove .htaccess files - we're use apache config instead
find %buildroot%installdir -name .htaccess -delete

# remove files
find %buildroot%installdir/files -type f -delete
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete
find %buildroot%installdir -name *.py -delete
rm -rf %buildroot%installdir/vendor/sabre/dav/bin

%post
echo "If you upgrade from previous version (less than 9.5) then read /usr/share/doc/%name-%version/UPGRADE.ALT"

%post apache2
if [ "$1" = "1" ]; then
  a2ensite %name
  %_initdir/httpd2 condreload
fi

%preun apache2
if [ "$1" = "0" ]; then
  a2dissite %name ||:
fi

%postun apache2
if [ "$1" = "0" ]; then
  %_initdir/httpd2 condreload
fi

%files
%dir %installdir
%dir %attr(2770,root,%webserver_group) %installdir/config
%dir %attr(2770,root,%webserver_group) %installdir/files
%attr(0770,root,%webserver_group) %installdir/files/*
%dir %attr(2770,root,%webserver_group) %installdir/marketplace
%installdir/ajax
%installdir/bin
%installdir/config
%installdir/css
%installdir/css_compiled
%installdir/files
%installdir/front
%installdir/inc
%installdir/install
%installdir/js
%installdir/lib
%installdir/locales
%installdir/marketplace
%installdir/pics
%installdir/plugins
%installdir/public
%installdir/sound
%installdir/src
%installdir/templates
%installdir/vendor
%installdir/*.js
%installdir/*.php
%installdir/LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc SUPPORT.md
%doc SECURITY.md
%doc apirest.md
%doc README.ALT
%doc UPGRADE.ALT

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files php7

%files php8.0

%files php8.1

%changelog
* Fri Nov 04 2022 Pavel Zilke <zidex@altlinux.org> 10.0.5-alt1
- New version 10.0.4
- This release fixes several security issues that has been recently discovered. Update is recommended!
- Security fixes:
 + CVE-2022-39276 : Blind SSRF in RSS feeds and planning
 + CVE-2022-39372 : Stored XSS in user information
 + CVE-2022-39373 : Stored XSS in entity name
 + CVE-2022-39376 : Improper input validation on emails links
 + CVE-2022-39370 : Improper access to debug panel
 + CVE-2022-39234 : User's session persist after permanently deleting his account
 + CVE-2022-39262 : Stored XSS on login page
 + CVE-2022-39277 : XSS in external links
 + CVE-2022-39375 : XSS through public RSS feed
 + CVE-2022-39323 : SQL Injection on REST API
 + CVE-2022-39371 : Stored XSS through asset inventory

* Wed Sep 14 2022 Pavel Zilke <zidex@altlinux.org> 10.0.3-alt1
- New version 10.0.3
- This release fixes several critical security issues that has been recently discovered. Update is strongly recommended!
- Security fixes:
 + CVE-2022-35945 : XSS through registration API
 + CVE-2022-31143 : Leak of sensitive information through login page error
 + CVE-2022-31187 : Stored XSS through global search (CVE-2022-31187)
 + CVE-2022-35914 : [critical] Command injection using a third-party library script
 + CVE-2022-35946 : SQL injection through plugin controller
 + CVE-2022-35947 : [critical] Authentication via SQL injection
 + CVE-2022-36112 : Blind Server-Side Request Forgery (SSRF) in RSS feeds and planning

* Fri Jul 22 2022 Pavel Zilke <zidex@altlinux.org> 10.0.2-alt1
- New version 10.0.2
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2022-31061 : Unauthenticated SQL injection on login page
 + CVE-2022-31056 : SQL injection on actor part in assistance forms
 + CVE-2022-31068 : Unauthenticated Sensitive Data Exposure on Refused Inventory Files

* Fri Jun 10 2022 Pavel Zilke <zidex@altlinux.org> 10.0.1-alt1
- New version 10.0.1
- This is a security release, upgrading is recommended
- The GLPI licence has been moved to GPLv3+

* Wed Apr 20 2022 Pavel Zilke <zidex@altlinux.org> 10.0.0-alt1
- New version 10.0.0
- Added glpi-php8.0
- Added glpi-php8.1

* Thu Jan 27 2022 Pavel Zilke <zidex at altlinux dot org> 9.5.7-alt1
- New version 9.5.7
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2022-21720 : SQL injection using custom CSS administration form
 + CVE-2022-21719 : Reflected XSS using reload button

* Tue Oct 12 2021 Pavel Zilke <zidex at altlinux dot org> 9.5.6-alt1
- New version 9.5.6
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2021-39211 : Disclosure of GLPI and server informations in telemetry endpoint
 + CVE-2021-39210 : Autologin cookie accessible by scripts
 + CVE-2021-39209 : Bypassable CSRF protection on ajax endpoints
 + CVE-2021-39213 : Bypassable IP restriction on GLPI API using custom header injection

* Thu May 13 2021 Pavel Zilke <zidex at altlinux dot org> 9.5.5-alt1
- New version 9.5.5
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2021-3486 : Stored XSS in plugins information

* Wed Mar 31 2021 Pavel Zilke <zidex at altlinux dot org> 9.5.4-alt1
- New version 9.5.4
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2021-21326 : Horizontal Privilege Escalation
 + CVE-2021-21255 : entities switch IDOR
 + CVE-2021-21258 : XSS injection in ajax/kanban
 + CVE-2021-21314 : XSS injection on ticket update
 + CVE-2021-21312 : Stored XSS on documents
 + CVE-2021-21313 : XSS on tabs
 + CVE-2021-21325 : Stored XSS in budget type
 + CVE-2021-21327 : Unsafe Reflection in getItemForItemtype()
 + CVE-2021-21324 : Insecure Direct Object Reference (IDOR) on "Solutions"

* Sat Dec 05 2020 Pavel Zilke <zidex at altlinux dot org> 9.5.3-alt1
- New version 9.5.3
- This is a security release, upgrading is recommended
- Security fixes:
 + CVE-2020-27662 : Insecure Direct Object Reference on ajax/comments.php
 + CVE-2020-27663 : Insecure Direct Object Reference on ajax/getDropdownValue.php
 + CVE-2020-26212 : Any CalDAV calendars is read-only for every authenticated user

* Thu Oct 29 2020 Pavel Zilke <zidex at altlinux dot org> 9.5.2-alt3
- Changed PHP7 dependencies

* Tue Oct 27 2020 Pavel Zilke <zidex at altlinux dot org> 9.5.2-alt2
- Fixed spec

* Mon Oct 26 2020 Pavel Zilke <zidex at altlinux dot org> 9.5.2-alt1
- New version 9.5.2
- Security fixes:
 + CVE-2020-15176 : SQL injection with a query parameter of user form
 + CVE-2020-15175 : Removal of .htaccess file in the files folder via a plugin endpoint
 + CVE-2020-15217 : Leakage issue with knowledge base
 + CVE-2020-15177 : Stored XSS in install script
 + CVE-2020-15226 : Minor SQL Injection in Search API

* Fri Jul 24 2020 Pavel Zilke <zidex at altlinux dot org> 9.5.1-alt1
- New version 9.5.1

* Sun Jun 07 2020 Pavel Zilke <zidex at altlinux dot org> 9.4.6-alt1
- New version 9.4.6
- This is a security release, upgrading is highly recommended

* Sun Dec 29 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.5-alt1
- New version 9.4.5

* Sun Dec 29 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.4-alt1
- New version 9.4.4
- This is a security release, upgrading is highly recommended

* Tue Jun 25 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.3-alt1
- New version 9.4.3
- This is a security release, upgrading is highly recommended

* Wed Apr 17 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.2-alt1
- New version 9.4.2
- This is a security release, upgrading is highly recommended

* Tue Apr 09 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.1-alt1
- New version 9.4.1

* Tue Mar 05 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.0-alt2
- Deleted glpi-php5

* Thu Feb 28 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.0-alt1
- New version 9.4.0

* Wed Feb 06 2019 Pavel Zilke <zidex at altlinux dot org> 9.3.3-alt2
- Fixed glpi-apache2 postun

* Sun Dec 30 2018 Pavel Zilke <zidex at altlinux dot org> 9.3.3-alt1
- New verion 9.3.3
- PHP7 support

* Thu Sep 21 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.6-alt2
- Delete glpi-apache

* Thu Sep 21 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.6-alt1
- New version 9.1.6

* Fri Apr 28 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.3-alt1
- New version 9.1.3

* Fri Apr 14 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.2-alt1
- New version 9.1.2

* Wed Sep 28 2016 Pavel Zilke <zidex at altlinux dot org> 9.1-alt1
- New version 9.1

* Thu Aug 25 2016 Pavel Zilke <zidex at altlinux dot org> 0.90.5-alt2
- Conf for Apache2 moved to sites-available

* Thu Aug 25 2016 Pavel Zilke <zidex at altlinux dot org> 0.90.5-alt1
- New version 0.90.5

* Fri Dec 25 2015 Pavel Zilke <zidex at altlinux dot org> 0.90.1-alt1
- Include bugfixes and some minor features

* Fri Dec 25 2015 Pavel Zilke <zidex at altlinux dot org> 0.90-alt1
- New version 0.90

* Sun Oct 11 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.5-alt1
- This is maintenance release to fix several minor bugs.

* Sat Jun 20 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.4-alt1
- This version correct several minor bugs.

* Sat Jun 20 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.3-alt1
- This version fix several minor bugs and a security bug

* Thu Jan 22 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.2-alt1
- This version correct several minor bugs.

* Wed Jan 07 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.1-alt1
- This version fix several minor bugs and a security bug

* Wed Jan 07 2015 Pavel Zilke <zidex at altlinux dot org> 0.85-alt1
- New version 0.85

* Mon Oct 20 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.8-alt1
- This version fix several minor bugs and a security bug.

* Sat Aug 09 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.7-alt1
- New version 0.84.5 This version correct several minor bugs.

* Thu Mar 13 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.5-alt1
- New version 0.84.5 This version correct several minor bugs.

* Fri Feb 07 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.4-alt1
- New version 0.84.4 This version correct several minor bugs.

* Fri Nov 15 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.3-alt1
- New version 0.84.3

* Fri Sep 20 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.2-alt1
- Security fixes:
 + CVE-2013-5696 : SQL Injection, PHP Code Execution, CSRF 

* Tue Sep 10 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.1-alt1
- New version 0.84.1

* Sat Aug 17 2013 Pavel Zilke <zidex at altlinux dot org> 0.84-alt1
- New version 0.84

* Sun Jul 21 2013 Pavel Zilke <zidex at altlinux dot org> 0.83.9.1-alt1
- Security fixes:
 + CVE-2013-2225 + CVE-2013-2227 : Security fix ( serialize + filter classname for autoload) (ALT #29189)

* Tue Apr 16 2013 Pavel Zilke <zidex at altlinux dot org> 0.83.8-alt1
- New version 0.83.8

* Sun Dec 16 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.7-alt1
- New version 0.83.7

* Wed Oct 17 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.6-alt1
- New version 0.83.6

* Thu Aug 16 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.4-alt1
- New version 0.83.4 

* Sat Jun 09 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.2-alt1
- New version 0.83.2

* Thu Apr 19 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.1-alt1
- New version 0.83.1

* Fri Apr 06 2012 Pavel Zilke <zidex at altlinux dot org> 0.83-alt1
- New version 0.83

* Mon Feb 13 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.7-alt1
- New version 0.80.7

* Wed Jan 11 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.61-alt1
- New version 0.80.61

* Tue Oct 25 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.5-alt1
- New version 0.80.5

* Wed Sep 28 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.4-alt1
- New version 0.80.4

* Thu Jul 07 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.1-alt1
- New version 0.80.1 This version correct several bugs.

* Thu Jun 02 2011 Pavel Zilke <zidex at altlinux dot org> 0.80-alt1
- New version 0.80

* Sun Mar 13 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.3-alt1
- New version 0.78.3

* Tue Jan 18 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.2-alt1
- New version 0.78.2

* Tue Nov 23 2010 Pavel Zilke <zidex at altlinux dot org> 0.78.1-alt1
- New version 0.78.1

* Wed Oct 13 2010 Pavel Zilke <zidex at altlinux dot org> 0.78-alt1
- New version 0.78

* Fri Apr 02 2010 Pavel Zilke <zidex at altlinux dot org> 0.72.4-alt1
- New version 0.72.4

* Tue Nov 10 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt2
- remove Thumbs.db files

* Tue Nov 03 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt1
- New version 0.72.3

* Wed Oct 07 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt2
- spec bugfix

* Thu Sep 17 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt1
- New version 0.72.21
- fixed export to pdf
- fixed import from OCS Inventory NG

* Wed Aug 12 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.1-alt1
- New version 0.72.1-alt1

* Thu Jun 04 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt2
- Fixed README.ALT location

* Tue Jun 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt1
- New version 0.71.6-alt1

* Mon Feb 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.5-alt1
- First build for ALT Linux

