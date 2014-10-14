%define		php5_extension	pdo_mysql

Name:	 	php5-mysqlnd-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	MySQL driver for PHP5 Data Objects Interface (mysqlnd build)

Group:		System/Servers
License:	PHP Licence
URL:		http://www.php.net/manual/en/ref.pdo-mysql.php
#		http://pecl.php.net/package/PDO_MYSQL

#Source0:	standart PHP module
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: gcc-c++
BuildRequires: php5-devel = %php5_version
Conflicts: php5-%php5_extension
Provides: php5-%php5_extension = %php5_version-%php5_release

Requires: php5-pdo = %php5_version-%release
Requires: php5-mysqlnd = %php5_version-%release
Provides: php5-pdo-driver


%description
PHP5 PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
This package contains a MySQL driver for PDO.

%prep
%setup -T -c
cp -pr -- %php5_extsrcdir/%php5_extension/* .

# Fix path to pdo*.h
subst 's@php/ext@php/%_php5_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php5_version/ext@g' configure

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Tue Oct 14 2014 Anton Farygin <rider@altlinux.ru> 5.5.17.20140916-alt1
- first build for Sisyphus
