%define		php5_extension	libevent
%define 	real_name	libevent
%define		real_version	0.1.0

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 extension for event notification via libevent library

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/libevent

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libevent-devel zlib-devel

%description
php5-libevent provides a wrapper for libevent - event notification
library.

Libevent is a library that provides a mechanism to execute
a callback function when a specific event occurs on a file
descriptor or after a timeout has been reached.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-libevent \
	%nil

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Fri Jun 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 5.5.13.20140626-alt0.1
- Initial build for ALT Linux Sisyphus

