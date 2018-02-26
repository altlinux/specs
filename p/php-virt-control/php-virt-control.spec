
Name: php-virt-control
Version: 0.0.4
Release: alt1
Summary: PHP-based virtual machine control tool
Group: Networking/Remote access
License: GPLv3
Url: http://www.php-virt-control.org
Source: %name-%version.tar
Source2: %name-apache.conf
Patch: %name-%version-%release.patch

Requires: %name-tools = %version-%release
Requires: %name-common = %version-%release

BuildPreReq: rpm-macros-webserver-common

%define wwwdir %_datadir/%name

%description
php-virt-control is a virtual machine control tool written in PHP language
to allow virtual machine management using libvirt-php extension.
For more details see: http://www.php-virt-control.org

%package tools
Summary: PHP-based virtual machine control tool
Group: Networking/Remote access

%description tools
php-virt-control is a virtual machine control tool written in PHP language
to allow virtual machine management using libvirt-php extension.
For more details see: http://www.php-virt-control.org

This package contain apache-key-copy for copy ssh key to remote server.

%package common
Summary: PHP-based virtual machine control tool
Group: Networking/Remote access
BuildArch: noarch
Requires: webserver-common
Requires: php5-libvirt php5-gd2 php5-mysql
Requires: %name-tools = %version-%release

%description common
php-virt-control is a virtual machine control tool written in PHP language
to allow virtual machine management using libvirt-php extension.
For more details see: http://www.php-virt-control.org

This package as noarch and contain php files.

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name-common = %version-%release, apache2

%description apache2
%summary

%prep
%setup
%patch -p1

%install
mkdir -p %buildroot{%_bindir,%wwwdir,%_sysconfdir/%name}
gcc -o %buildroot/%_bindir/apache-key-copy tools/apache-key-copy.c

cp -af *.php %buildroot%wwwdir/
cp -af *.css %buildroot%wwwdir/
cp -af classes/ data/ graphics/ lang/ logs/ pages/ %buildroot%wwwdir/
cp -af config/connection.php %buildroot/%_sysconfdir/%name/connection.php
cp -af config/mysql-connection.php %buildroot/%_sysconfdir/%name/mysql-connection.php
install -Dp -m0644 auth/50-org.libvirt-remote-access.pkla %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/50-org.libvirt-remote-access.pkla
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%post apache2
/sbin/service httpd2 condreload

%postun apache2
/sbin/service httpd2 condreload


%files common
%doc AUTHORS COPYING README INSTALL
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/%name/connection.php
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/%name/mysql-connection.php
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/polkit-1/localauthority/50-local.d/50-org.libvirt-remote-access.pkla
%dir %wwwdir
%wwwdir/*

%files tools
%_bindir/apache-key-copy

%files apache2 
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%changelog
* Tue Mar 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.0.4-alt1
- 0.0.4

* Wed Dec 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.0.3-alt1
- initial build for ALT Linux Sisyphus
