%define		php_extension	sqlsrv
Name:	 	php%_php_suffix-%php_extension
Version:	5.12.0
Release:	alt1.%_php_release_version
Epoch:		1
Summary:	Microsoft Drivers for PHP for SQL Server

License:	%mit
Group:		System/Servers
URL:		https://pecl.php.net/package/sqlsrv
#URL: https://github.com/Microsoft/msphpsql
#URL: https://docs.microsoft.com/ru-ru/sql/connect/php/microsoft-php-driver-for-sql-server

# This extension can't be used on 32bit or ARM systems - there are no support for 32bit or ARM systems from Microsoft.
ExclusiveArch: x86_64
#BuildArch: x86_64

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%php_extension.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

Source3:	README.ALT

BuildRequires(pre): rpm-build-php8.2-version rpm-build-licenses
BuildRequires: gcc-c++ libunixODBC-devel

BuildRequires: php-devel = %php_version

%description
The php-sqlsrv package contains the Microsoft Drivers for PHP for SQL Server
are PHP extensions that allow for the reading and writing of SQL Server data
from within PHP scripts. The SQLSRV extension provides a procedural interface
while the PDO_SQLSRV extension implements PDO for accessing data in all editions
of SQL Server 2008 R2 and later (including Azure SQL DB). These drivers rely
on the Microsoft ODBC Driver for SQL Server to handle the low-level
communication with SQL Server.

This package contains only the SQLSRV driver. Microsoft ODBC Driver 13 must be
installed for this extension to work.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
export CXX=c++
%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	#

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

install -D -m 644 -- %SOURCE3  README.ALT

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS README.ALT

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel %php_version-%php_release

* Thu Mar 28 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1:5.12.0-alt1
- 5.12.0

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 1:5.9.0
- 5.9.0

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 7.4.14-alt1
- update to 5.8.1

* Thu Feb 13 2020 Anton Farygin <rider@altlinux.org> 7.3.14-alt1
- update to 5.8.0

* Tue Jul 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.2.6-alt1
- Initial build for ALT Linux Sisyphus

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.9-alt1
- Initial build
