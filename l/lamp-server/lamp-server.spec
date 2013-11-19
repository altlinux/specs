Name: 	 lamp-server
Version: 1.0
Release: alt2

Summary: Metapackage to install LAMP server (Linux+Apache+MySQL+PHP)
Summary(ru_RU.UTF-8): Метапакет для установки сервера LAMP (Linux+Apache+MySQL+PHP) 
License: System/Servers
Group:   Graphics
URL: 	 http://www.altlinux.org/ApacheMySQLPHP 

BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %name-%version.tar

Requires: apache2-base 
Requires: mysql-server
Requires: apache2-mod_php5
Requires: php5-mysql 
Requires: php5-mysqli

%description
This is to help people setup and install a LAMP (Linux+Apache+MySQL+PHP)
server, including Apache 2, PHP 5 and MySQL 5.0.

%prep
%setup 

%files
%doc README

%changelog
* Tue Nov 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Require mysql-server for compatiblity with mariadb-server

* Sat Apr 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build

