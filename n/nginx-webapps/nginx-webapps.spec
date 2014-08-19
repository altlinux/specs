Name: nginx-webapps
Version: 0.1.0
Release: alt1

Summary: Config file for multiple locations
License: Public Domain
Group: System/Configuration/Other

Source1: webapps.conf
Source2: webapps-indexhtml.conf
BuildArch: noarch

Requires: nginx

%description
This package contains configuration file for
nginx that includes multiple configuration files
from specified directory. It is simplifies the usage of
several 'locations' in the single 'server' section.

%install
mkdir -p %buildroot%_sysconfdir/nginx/webapps-available.d/
mkdir -p %buildroot%_sysconfdir/nginx/webapps-enabled.d/
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/nginx/sites-available.d/webapps.conf
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/nginx/webapps-available.d/indexhtml.conf

%files
%dir %_sysconfdir/nginx/webapps-available.d/
%dir %_sysconfdir/nginx/webapps-enabled.d/
%config(noreplace) %_sysconfdir/nginx/sites-available.d/webapps.conf
%config(noreplace) %_sysconfdir/nginx/webapps-available.d/indexhtml.conf

%changelog
* Mon Aug 18 2014 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

