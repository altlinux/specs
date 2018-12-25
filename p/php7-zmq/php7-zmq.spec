%define		php7_extension	zmq
%define 	real_name	php-zmq
%define		real_version	1.1.3

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 bindings for ZeroMQ high-performance asynchronous messaging library

License:	%bsdstyle
Group:		System/Servers
URL:		https://pecl.php.net/package/zmq

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh


BuildRequires(pre): rpm-build-php7 rpm-build-licenses
# Automatically added by buildreq on Tue Dec 25 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl php7-libs pkg-config python-base python-modules python3 python3-base python3-dev ruby ruby-stdlibs sh3
BuildRequires: glibc-devel-static libzeromq-devel

BuildRequires: php7-devel = %php7_version

%description
php7-zmq extension provides bindings for ZeroMQ (0MQ) high-performance
asynchronous messaging library that provides a way to quickly design
and implement a fast message-based applications.

%prep
%setup -c
%patch0 -p1

sed -e 's/@PACKAGE_VERSION@/%real_version/g' -i php_zmq.h
sed -e 's/@PACKAGE_VERSION@/%real_version/g' -i package.xml

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--enable-zmq \
	%nil

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc ChangeLog README.md LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Tue Dec 25 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.2.12-alt1
- Initial build for ALT Linux Sisyphus

