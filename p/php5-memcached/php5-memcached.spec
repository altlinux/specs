%define		php5_extension	memcached
%define 	real_name	memcached
%define		real_version	2.1.0

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release.1

Summary:	PHP5 extension for interfacing with memcached via libmemcached library

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/memcached

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

Patch0:		php-memcached-2.1.0-debian-fix_symbols.patch

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libmemcached-devel zlib-devel

%description
php5-memcached extension uses libmemcached library to provide
API for communicating with memcached servers.

memcached is a high-performance, distributed memory object
caching system, generic in nature, but intended for use in
speeding up dynamic web applications by alleviating database
load.

%prep
%setup -c
%patch0 -p2

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-memcached \
	--enable-memcached-json \
	%nil
#	--enable-memcached-igbinary \

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS README.markdown LICENSE

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.18.20121017-alt1.1
- rebuild with php5-5.3.18.20121017-alt1.1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- rebuild with php5-5.3.18.20121017-alt1

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.17.20120913-alt1
- Initial build for ALT Linux Sisyphus

