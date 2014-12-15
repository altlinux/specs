Name: nginx-webapps
Version: 0.2.0
Release: alt1

Summary: Config file for multiple locations
License: Public Domain
Group: System/Configuration/Other

Source1: webapps.conf
Source2: webapps-indexhtml.conf
Source3: webapps-ssl.conf
BuildArch: noarch

Requires: nginx

%description
This package contains configuration file for
nginx that includes multiple configuration files
from specified directory. It is simplifies the usage of
several 'locations' in the single 'server' section.

%package ssl
Summary: Config file for multiple locations (HTTPS server)
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: cert-sh-functions

%description ssl
This package contains configuration file for
nginx that includes multiple configuration files
from specified directory. It is simplifies the usage of
several 'locations' in the single 'server' section.

This configuration file implements HTTPS server.

%install
mkdir -p %buildroot%_sysconfdir/nginx/webapps-available.d/
mkdir -p %buildroot%_sysconfdir/nginx/webapps-enabled.d/
mkdir -p %buildroot%_sysconfdir/nginx/webapps-ssl-enabled.d/
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/nginx/sites-available.d/webapps.conf
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/nginx/webapps-available.d/indexhtml.conf
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/nginx/sites-available.d/webapps-ssl.conf

%post ssl
# Create SSL certificate for HTTPS server
cert-sh generate %name ||:

%files
%dir %_sysconfdir/nginx/webapps-available.d/
%dir %_sysconfdir/nginx/webapps-enabled.d/
%config(noreplace) %_sysconfdir/nginx/sites-available.d/webapps.conf
%config(noreplace) %_sysconfdir/nginx/webapps-available.d/indexhtml.conf

%files ssl
%dir %_sysconfdir/nginx/webapps-ssl-enabled.d/
%config(noreplace) %_sysconfdir/nginx/sites-available.d/webapps-ssl.conf

%changelog
* Mon Dec 15 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Add nginx-webapps-ssl subpackage.

* Mon Aug 18 2014 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

