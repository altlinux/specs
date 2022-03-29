%define		php_extension	memcached
Name:	 	php%_php_suffix-%php_extension
Version:	3.2.0
Release:	alt1.%_php_release_version
Epoch:		1
Summary:	php extension for interfacing with memcached via libmemcached library
License:	PHP-3.01
Group:		System/Servers
URL:		http://pecl.php.net/package/memcached
VCS: https://github.com/php-memcached-dev/php-memcached
Source0: php-memcached-%version.tar
Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.1-version
BuildRequires: php-devel = %php_version
BuildRequires: libmemcached-devel zlib-devel
BuildRequires: php%_php_suffix memcached /proc

%description
php-memcached extension uses libmemcached library to provide
API for communicating with memcached servers.

memcached is a high-performance, distributed memory object
caching system, generic in nature, but intended for use in
speeding up dynamic web applications by alleviating database
load.

%prep
%setup -n php-memcached-%version

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-memcached \
	--enable-memcached-json \
	--disable-memcached-sasl \
	%nil
#	--enable-memcached-protocol \
#	--enable-memcached-igbinary \

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
rm -rf tests/experimental
memcached -d
NO_INTERACTION=1 make test

%files
%doc CREDITS README.markdown LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Tue Mar 29 2022 Anton Farygin <rider@altlinux.ru> 1:3.2.0-alt1
- 3.1.5 -> 3.2.0

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.3-alt1
- initial build 3.0.3 for ALT Sisyphus
