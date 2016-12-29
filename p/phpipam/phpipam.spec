
Name: phpipam
Version: 1.26.050
Release: alt1
Summary: PHP-based virtual machine control tool
Group: Networking/WWW
License: GPLv3
Url: http://phpipam.net
Source: %name-%version.tar
Source2: php-saml.tar
Source3: PHPMailer.tar
Source11: %name-apache.conf

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
tar -xf %SOURCE2 -C functions/php-saml
tar -xf %SOURCE3 -C functions/PHPMailer
#%patch -p1

%install
mkdir -p %buildroot%webserver_webappsdir
cp -r ../%name-%version %buildroot%webserver_webappsdir/%name
#cleaup
#rm -rf %buildroot%webserver_webappsdir/%name/misc
rm -f %buildroot%webserver_webappsdir/%name/{INSTALL.txt,README,UPDATE}
rm -f %buildroot%webserver_webappsdir/%name/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/.gitmodules

install -pDm644 %SOURCE11 %buildroot%apache2_extra_available/%name.conf
%__subst 's|--dir--|%webserver_webappsdir/%name|g' %buildroot%apache2_extra_available/%name.conf

chmod 644 INSTALL.txt README UPDATE misc/CHANGELOG misc/Roadmap

# Cleanup PHPMailer
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.scrutinizer.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.travis.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/travis.phpunit.xml.dist
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/docs
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/examples
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/test

%files
%doc INSTALL.txt README UPDATE misc/CHANGELOG misc/Roadmap
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
%webserver_webappsdir/%name/.htaccess

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%changelog
* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.26.050-alt1
- git snapshot of master branch b99412648829471f3a336036f5cd138b8f131721
- install PHPMailer from upstream (fixed CVE-2015-8476,CVE-2016-10033,CVE-2016-10045)

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt2
- git snapshot of branch 1.2 - 7a5cb1a2ea065096d1d393ccc5b52a5bb7983c39

* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
