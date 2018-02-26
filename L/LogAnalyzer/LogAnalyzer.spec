%define wwwdir %_datadir/%name

Summary: A syslog data viewer for the web
Name: LogAnalyzer
Version: 3.4.1
Release: alt1
License: GPLv3+
Group: Monitoring
Url: http://loganalyzer.adiscon.com/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch
Provides: phplogcon

Requires: webserver webserver-common
Requires: php5-gd2 php5-jpgraph fonts-ttf-vera

BuildPreReq: rpm-macros-webserver-common

%description
LogAnalyzer project provides an easy to use but powerful front end for
searching, reviewing and analyzing network event data, including
syslog, windows event log and many other event sources.

%prep
%setup -n %name-%version
%patch -p1

%build
rm -rf src/classes/jpgraph
rm -rf src/BitstreamVeraFonts

%install
mkdir -p %buildroot{%_sysconfdir/cron.d,%wwwdir,%_sysconfdir/%name}
cp -aRf src/* %buildroot%wwwdir/

touch             %buildroot%_sysconfdir/%name/config.php
ln -s ../../..%_sysconfdir/%name/config.php %buildroot%wwwdir/config.php


%files
%doc COPYING INSTALL ChangeLog LogAnalyzer-apache.conf doc
%dir %attr(750,root,%webserver_group) %_sysconfdir/%name
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/%name/config.php
%dir %wwwdir
%wwwdir/*

%changelog
* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Fri Jun 10 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- initial build for ALT Linux Sisyphus
