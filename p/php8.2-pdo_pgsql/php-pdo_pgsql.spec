%define		php_extension	pdo_pgsql

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	PostgreSQL driver for PHP Data Objects Interface

Group:		System/Servers
License:	PHP-3.01
URL:		http://www.php.net/manual/en/ref.pdo-pgsql.php
#		http://pecl.php.net/package/PDO_PGSQL

#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: gcc-c++ postgresql-devel
BuildRequires: php-devel = %php_version

PreReq: php%_php_suffix-pdo = %php_version
Provides: php%_php_suffix-pdo-driver

%description
PHP PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
This package contains a PostgreSQL driver for PDO.

%prep
%setup -T -c
cp -pr -- %php_extsrcdir/%php_extension/* .

# Fix path to pdo*.h
subst 's@php/ext@php/%_php_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php_version/ext@g' configure

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	#

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release
