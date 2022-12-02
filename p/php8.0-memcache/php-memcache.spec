%define		php_extension	memcache
Name:	 	php%_php_suffix-%php_extension
Version:	8.0.1
Release:	alt%php_version.%php_release
Summary:	memcached extension for php%_php_suffix
License:	PHP-3.0
Group:		System/Servers
URL:		https://github.com/websupport-sk/pecl-memcache

BuildRequires(pre): rpm-build-php8.0-version
BuildRequires: php-devel = %php_version zlib-devel
BuildRequires: php%_php_suffix = %php_version memcached /proc

# Source0-url:	https://pecl.php.net/get/memcache-%version.tgz
Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Patch:		php7-memcache-alt-inc.patch

%description 
The php%_php_suffix-%php_extension package contains a dynamic shared object (DSO) for php. The
php%_php_suffix-%php_extension module allows you to work with memcached through handy OO
and procedural interfaces. If you need memcached(1) support for php
applications, you will need to install this package and php.

%prep
%setup -n php-%php_extension-%version
%patch -p2

%build
phpize

export LDFLAGS=-lphp-%_php_version

%configure --enable-memcache --with-zlib-dir=/usr
%php_make

%install
%php_make_install
%__install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
%__install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%ifnarch %ix86
%check
# remove online test
rm -f tests/056.phpt
# run memcached for tests
memcached -d -s /tmp/memcached.sock
memcached -d -p 11212
memcached -d
NO_INTERACTION=1 make test
%endif

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS README

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Mon Oct 03 2022 Anton Farygin <rider@altlinux.ru> 8.0.1-alt1
- 4.0.5.2 -> 8.0.1

* Thu Feb  6 2020 Anton Farygin <rider@altlinux.ru> 4.0.5.2-alt1 
- 4.0.4 -> 4.0.5.2

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 4.0.4-alt1
- updated to 4.0.4 with php-7.3 support
- turned on tests

* Sat Jan 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0.8-alt1
- new version (3.0.8) with rpmgs script

* Sat Jan 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- initial build 2.2.7 for ALT Sisyphus
