
Name: phpipam
Version: 1.2.1
Release: alt1
Summary: PHP-based virtual machine control tool
Group: Networking/WWW
License: GPLv3
Url: http://phpipam.net
Source: %name-%version.tar
Source2: %name-apache.conf
# Patch: %name-%version-%release.patch

BuildArch: noarch
Requires: webserver-common
Requires: php5-gmp php5-pdo php5-pdo_mysql php5-ldap php5-pcntl pear-core

BuildPreReq: rpm-macros-webserver-common rpm-macros-apache2

%description
phpipam is an open-source web IP address management application. Its goal is to provide light and simple IP address management application.
It is ajax-based using jQuery libraries, it uses php scripts and javascript and some HTML5/CSS3 features, so some modern browser is preferred
to be able to display javascript quickly and correctly.

Features and tools:
- Section / Subnet separation
- Subnet nesting
- IPv4/IPv6 support
- REST API
- Subnet ICMP/telnet scanning and automatic status updates
- Displays free range and number of clients
- Subnet statistics
- User management
- AD/LDAP/OpenLDAP/NetIQ/Radius authentication support (multiple servers)
- E-Mail notification with IP details
- Import IP addresses from XLS / CSV file
- Export IP database to XLS file
- IPv4/IPv6 calculator
- Search IP database
- IP request module
- Custom IP address fields
- and much more...
- PowerDNS integration (3.4+);

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %version-%release
Requires: apache2-httpd-prefork-like php-engine

%description apache2
%summary

%prep
%setup
#%patch -p1

%install
mkdir -p %buildroot%webserver_webappsdir
cp -r ../%name-%version %buildroot%webserver_webappsdir/%name
#cleaup
rm -rf %buildroot%webserver_webappsdir/%name/misc
rm -f %buildroot%webserver_webappsdir/%name/{INSTALL.txt,README,UPDATE}
rm -f %buildroot%webserver_webappsdir/%name/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/.gitignore

install -pDm644 %SOURCE2 %buildroot%apache2_extra_available/%name.conf
%__subst 's|--dir--|%webserver_webappsdir/%name|g' %buildroot%apache2_extra_available/%name.conf

%files
%doc INSTALL.txt README UPDATE misc/CHANGELOG misc/Roadmap
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
%webserver_webappsdir/%name/.htaccess

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%changelog
* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
