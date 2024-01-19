%define		php_extension	swoole
%define 	real_name	swoole
%define		real_version	5.1.1

Name:	 	php%_php_suffix-%php_extension
Version:	%real_version
Release:	alt2.%_php_release_version
ExcludeArch: %ix86 armh
Summary:	Coroutine-based concurrency library for PHP
License:	Apache-2.0
Group:		System/Servers
URL:		https://pecl.php.net/package/swoole
VCS:		https://github.com/swoole/swoole-src
#URL:		https://www.swoole.com/coding
Source0:	%real_name-%real_version.tar

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Patch0:	php-swoole-%version.patch

BuildRequires(pre): rpm-build-php8.3-version
BuildRequires(pre): rpm-build-licenses
BuildRequires: php-devel = %php_version

BuildRequires: boost-devel-headers gcc-c++ libbrotli-devel libcurl-devel libpcre-devel libssl-devel zlib-devel

# Using symbols from php-sockets and php-curl:
Requires: php%_php_suffix-sockets php%_php_suffix-curl

%description
php-swoole extension provides an event-driven asynchronous and
coroutine-based concurrency networking communication engine
with high performance written in C++ for PHP.

Swoole main features are includes:
- event-driven
- coroutine
- asynchronous non-blocking
- multi-thread reactor
- multi-process worker
- multi-protocol
- millisecond timer
- built-in tcp/http/websocket/http2 server
- coroutine tcp/http/websocket client
- coroutine mysql client
- coroutine redis client
- coroutine read/write file system
- coroutine dns lookup
- support IPv4/IPv6/UnixSocket/TCP/UDP
- support SSL/TLS encrypted transmission


%prep
%setup -c
%patch0 -p1

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

# For php_sockets.h
ln -nsf -- /usr/src/php%_php_suffix-devel/ext/ .

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-swoole-json \
	--enable-swoole-curl \
	--enable-openssl \
	--enable-http2 \
	--enable-mysqlnd \
	--enable-sockets \
	%nil

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc README.md LICENSE

%php_extconf/%php_extension
%php_extdir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%version-%release

* Fri Jan 19 2024 Anton Farygin <rider@altlinux.ru> 5.1.1-alt2
- added upstream fix against php 8.3 (Closes: #49116)
- removed postscripts (there is a filetrigger)

* Tue Jan 09 2024 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Sun Jun 25 2023 Anton Farygin <rider@altlinux.ru> 4.8.13-alt1
- 4.8.13
- fix License according SPDX
- cleanup buildrequires

* Tue Jan 12 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.8.12-alt1
- New version

* Fri Jan 21 2022 Nikolay A. Fetisov <naf@altlinux.org> 4.8.6-alt1
- Initial build for ALT Linux Sisyphus

