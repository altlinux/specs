Name: 	 lamp-server
Version: 1.3
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
Requires: apache2-mod_php8.0
Requires: php8.0-mysqlnd 
Requires: php8.0-mysqlnd-mysqli

%description
This is to help people setup and install a LAMP
(Linux+Apache+MariaDB+PHP) server, including Apache 2, PHP  and
MariaDB.

%prep
%setup 

%files
%doc README

%changelog
* Thu Dec 15 2022 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- switch to php8.0

* Wed Mar 06 2019 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- switch to php7

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Change mysql-server to mariadb-server (ALT #33416)

* Tue Nov 19 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Require mysql-server for compatiblity with mariadb-server

* Sat Apr 28 2012 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build

