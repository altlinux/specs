%define wwwdir %_datadir/%name
%define phpver 8.1

Summary: A syslog data viewer for the web
Name: LogAnalyzer
Version: 4.1.13
Release: alt1
License: GPLv3+
Group: Monitoring
Url: http://loganalyzer.adiscon.com/
VCS: https://github.com/rsyslog/loganalyzer.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch
Provides: phplogcon

Requires(pre): webserver-common
Requires: fonts-ttf-vera

BuildPreReq: rpm-macros-webserver-common rpm-macros-apache2

%description
LogAnalyzer project provides an easy to use but powerful front end for
searching, reviewing and analyzing network event data, including
syslog, windows event log and many other event sources.

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %EVR
Requires: %name-php%phpver
Requires: apache2-httpd-prefork-like php-engine

%description apache2
%summary

%package php%phpver
Group: Networking/WWW
BuildArch: noarch
Summary: php virtual package  for %name
Provides: %name-php
Requires: %name = %EVR
Requires: php%phpver-mysqli
Requires: php%phpver-ldap php%phpver-pdo php%phpver-mbstring
Requires: php%phpver-gd2

%description php%phpver
%summary

%prep
%setup -n %name-%version
%patch -p1

%build
#rm -rf src/classes/jpgraph
rm -rf src/BitstreamVeraFonts

%install
mkdir -p %buildroot{%_sysconfdir/cron.d,%wwwdir,%_sysconfdir/%name}
cp -aRf src/* %buildroot%wwwdir/

touch %buildroot%_sysconfdir/%name/config.php
ln -s ../../..%_sysconfdir/%name/config.php %buildroot%wwwdir/config.php

install -pDm644 LogAnalyzer-apache.conf %buildroot%apache2_extra_available/%name.conf

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete


%files
%doc COPYING INSTALL ChangeLog LogAnalyzer-apache.conf doc
%dir %attr(750,root,%webserver_group) %_sysconfdir/%name
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/%name/config.php
%dir %wwwdir
%wwwdir/*

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%files php%phpver

%changelog
* Tue Aug 08 2023 Anton Farygin <rider@altlinux.ru> 4.1.13-alt1
- update to 4.1.13
- use php 8.1 as default php for LogAnalyzer

* Tue Dec 15 2020 Alexey Shabalin <shaba@altlinux.org> 4.1.11-alt1
- new version 4.1.11

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 4.1.7-alt2
- drop php5 package

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 4.1.7-alt1
- 4.1.7

* Wed Apr 11 2018 Alexey Shabalin <shaba@altlinux.ru> 4.1.6-alt1
- 4.1.6
- add php5, php7, apache2 packages

* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.5-alt1
- 4.1.5
- use bundled jpgraph

* Tue Oct 22 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.5-alt1
- 3.6.5

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.4-alt1
- 3.6.4

* Thu Jul 11 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.3-alt1
- 3.6.3

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.4-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * windows-thumbnail-database-in-package for LogAnalyzer

* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Fri Jun 10 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- initial build for ALT Linux Sisyphus
