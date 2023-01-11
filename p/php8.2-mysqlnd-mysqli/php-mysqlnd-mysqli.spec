%define		php_extension	mysqli

Name:	 	php%_php_suffix-mysqlnd-%php_extension
Version:	%php_version
Release:	%php_release.1

Summary:	MySQL Improved Extension for PHP with Native Driver

License:	PHP-3.01
Group:		System/Servers
URL:		http://www.php.net/manual/en/ref.mysqli.php

#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
Conflicts: php%_php_suffix-%php_extension
Provides: php%_php_suffix-%php_extension = %EVR
%if "%_php_suffix" == "7"
Provides: php%_php_suffix-mysqli = %EVR
Obsoletes: php%_php_suffix-mysqli < %EVR
%endif
Requires: php%_php_suffix-mysqlnd = %php_version

%description
MySQLi (improved) - new MySQL interface for PHP and MySQL 4.1.3+

%prep
%setup -T -c
cp -pr -- %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
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
- Rebuild with php-devel = %version-%release

