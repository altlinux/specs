%define		php_extension	swoole
%define 	real_name	swoole
%define		real_version	4.8.12

Name:	 	php%_php_suffix-%php_extension
Version:	%real_version
Release:	alt1.%_php_release_version

Summary:	Coroutine-based concurrency library for PHP

License:	%asl 2.0
Group:		System/Servers
URL:		https://pecl.php.net/package/swoole
#URL:		https://github.com/swoole/swoole-src
#URL:		https://www.swoole.com/coding

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.1-version
BuildRequires(pre): rpm-build-licenses
BuildRequires: php-devel = %php_version

BuildRequires: boost-devel-headers gcc-c++ glibc-devel-static libbrotli-devel libcurl-devel libpcre-devel libssl-devel valgrind-devel zlib-devel

# Using symbols from php-sockets:
Requires: php%_php_suffix-sockets


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
%doc README.md README-CN.md SUPPORTED.md LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%version-%release

* Tue Jan 12 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.8.12-alt1
- New version

* Fri Jan 21 2022 Nikolay A. Fetisov <naf@altlinux.org> 4.8.6-alt1
- Initial build for ALT Linux Sisyphus

