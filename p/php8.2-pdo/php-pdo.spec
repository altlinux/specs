%define		php_extension	pdo

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	PHP Data Objects Interface

License:	PHP-3.01
Group:		System/Servers
URL:		http://www.php.net/manual/en/book.pdo.php
#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Patch1: 	php7-pdo-7.4-re2c-require.patch


BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: gcc-c++ 
BuildRequires: re2c

BuildRequires: php%_php_suffix

Requires: php%_php_suffix-pdo-driver

%description
PHP PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
PDO drivers are dynamically loadable and may be developed independently from the 
core, but still accessed using the same API.


%prep
%setup -T -c
cp -pr -- %php_extsrcdir/%php_extension/* .
%patch1 -p1

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

%check
NO_INTERACTION=1 make test

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS
%exclude %php_includedir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release
