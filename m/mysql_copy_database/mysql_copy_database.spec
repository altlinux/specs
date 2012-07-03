Name: mysql_copy_database
Version: 1.1.0
Release: alt1.1

Summary: A python script used to copy a MySQL database from one host to another

License: GPLv3
Group: Development/Tools
Url: http://code.google.com/p/mysql-copy-database/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

%description
A python script used to copy a MySQL database (including all relevant privileges)
from one host to another, used as a wrapper around mysql and mysqldump.

%prep
%setup

%install
install -D %name.py %buildroot%_bindir/%name.py

%files
%doc README.ru.utf8
%_bindir/%name.py

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus
