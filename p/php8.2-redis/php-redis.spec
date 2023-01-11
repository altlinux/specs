# TODO:
#    --enable-redis-igbinary \
#    --enable-redis-msgpack \

%define		php_extension	redis
%define 	real_name	redis
Name:	 	php%_php_suffix-%php_extension
Version:	5.3.7
Release:	alt1.%php_version
Summary:	Client extension for Redis key-value store
License:	PHP-3.01
Group:		System/Servers
URL:		https://github.com/nicolasff/phpredis
Source:		php-%php_extension-%version.tar

Source1: redis.ini
Source2: php-redis-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: liblzf-devel libzstd-devel liblz4-devel

%description
The phpredis extension provides an API for communicating with the Redis key-value store.

%prep
%setup -n php-%php_extension-%version

%build
phpize

%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
    --with-libdir=%_lib \
    --enable-redis-lzf \
    --with-liblzf \
    --enable-redis-zstd \
    --with-libzstd \
    --enable-redis-lz4 \
    --with-liblz4

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc CREDITS *.markdown
%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 5.3.7-alt1
- 5.3.6 -> 5.3.7
- built from upstream git

* Wed Feb 02 2022 Anton Farygin <rider@altlinux.ru> 5.3.6-alt1
- 5.3.5 -> 5.3.6

* Mon Dec 20 2021 Anton Farygin <rider@altlinux.ru> 5.3.5-alt1
- 5.3.4 -> 5.3.5

* Mon Jul 05 2021 Anton Farygin <rider@altlinux.ru> 5.3.4-alt1
- update to 5.3.4

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3.1-alt1
- new version 5.3.1
- build with liblzf, libzstd, liblz4 support

* Fri Dec 13 2019 Anton Farygin <rider@altlinux.org> 5.1.1-alt1
- 3.1.2 -> 5.1.1

* Wed May 17 2017 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt7.1.3.alt1.0
- initial build for ALT Sisyphus
