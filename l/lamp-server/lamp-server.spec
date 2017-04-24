Name: 	 lamp-server
Version: 1.1
Release: alt1

Summary: Metapackage to install LAMP server (Linux+Apache+MariaDB+PHP)
Summary(ru_RU.UTF-8): Метапакет для установки сервера LAMP (Linux+Apache+MariaDB+PHP) 
License: System/Servers
Group:   Graphics
URL: 	 http://www.altlinux.org/ApacheMariaDBPHP 

BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %name-%version.tar

Requires: apache2-base 
Requires: mariadb-server
Requires: apache2-mod_php5
Requires: php5-mysql 
Requires: php5-mysqli

%description
This is to help people setup and install a LAMP
(Linux+Apache+MariaDB+PHP) server, including Apache 2, PHP 5 and
MariaDB.

%prep
%setup 

%files
%doc README

%changelog
* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Change mysql-server to mariadb-server (ALT #33416)

* Tue Nov 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Require mysql-server for compatiblity with mariadb-server

* Sat Apr 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build

