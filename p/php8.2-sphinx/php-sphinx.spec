%define		php_extension	sphinx
%define 	real_name	sphinx
%define		real_version	1.4.0-dev

Name:	 	php%_php_suffix-%{php_extension}
Version:	%php_version
Release:	alt2.%_php_release_version

Summary:	PHP bindings for Sphinx search client library

License:	PHP-3.01
Group:		System/Servers
URL:		https://pecl.php.net/package/sphinx

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: libsphinxclient-devel

%description
php-sphinx extension provides bindings for Sphinx search client
library. Sphinx is a standalone search engine meant to provide
fast, size-efficient and relevant fulltext search functions
to other applications. Sphinx was specially designed to integrate
well with SQL databases and scripting languages.

%prep
%setup -c
%patch0 -p1


%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-sphinx \
	%nil

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc CREDITS LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.ru> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus

