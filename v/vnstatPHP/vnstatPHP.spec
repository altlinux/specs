Name: vnstatPHP
Version: 1.5.1
Release: alt2
Packager: Alex Negulescu <alecs@altlinux.org>
Summary: PHP fronted end to vnStat, a network traffic logger
License: GPL
Group: Monitoring
Url: http://www.sqweek.com/sqweek/index.php?p=1
Source: vnstat_php_frontend-1.5.1.tar.bz2
BuildArch: noarch
Requires: vnstat, fonts-ttf-vera, php5 >= 5.0

%description
This is a PHP fronted end to vnStat, a network traffic logger.
This script requires a working PHP setup with GD image libraries. 
vnStat must be properly installed and collecting data.
For information about how to set those up please check
http://humdi.net/vnstat/

%prep
%setup -q -n vnstat_php_frontend-1.5.1

%install
%__mkdir -p %buildroot/var/www/html
%__cp -r %_builddir/vnstat_php_frontend-1.5.1 %buildroot/var/www/html/vnstat

%post

%clean

%files
/var/www/html/vnstat/COPYING
/var/www/html/vnstat/README
/var/www/html/vnstat/config.php
/var/www/html/vnstat/graph.php
/var/www/html/vnstat/graph_svg.php
/var/www/html/vnstat/index.php
/var/www/html/vnstat/localize.php
/var/www/html/vnstat/vnstat.php
/var/www/html/vnstat/lang/*
/var/www/html/vnstat/themes/*

%changelog
* Sun Apr 03 2011 Alex Negulescu <alecs@altlinux.org> 1.5.1-alt2
- removed VeraBd, closes #25331
* Wed Jan 12 2011 Alex Negulescu <alecs@altlinux.org> 1.5.1-alt1
- version up
* Wed Apr 01 2009 Alex Negulescu <alecs@altlinux.org> 1.4.1-alt1
- created rpm for vnstatPHP
