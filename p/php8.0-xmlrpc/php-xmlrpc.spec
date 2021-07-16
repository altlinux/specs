%define		php_extension	xmlrpc

Name:	 	php%_php_suffix-%php_extension
Version:	1.0.0
Release:	alt1.%_php_release_version

Summary:	PHP module to write XML-RPC servers and clients

Group:		System/Servers
License:	PHP-3.01
URL:		https://pecl.php.net/package/xmlrpc
#URL:		http://php.net/manual/en/book.xmlrpc.php

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.0-version
BuildRequires:  libxml2-devel

BuildRequires:	php-devel = %php_version

%description
PHP PECL module XML-RPC can be used to write XML-RPC servers
and clients.

The extension is unbundled from php-src as of PHP 8.0.0,
because the underlying libxmlrpc has obviously been abandoned.
It is recommended to reevaluate using this extension.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	PHP_ICONV=yes \
	PHP_LIBXML_SHARED=yes \
	--with-libxml-dir=%_usr \
	--with-expat-dir=%_usr \
	--with-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus
