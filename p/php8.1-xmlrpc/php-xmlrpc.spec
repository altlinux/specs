%define		php_extension	xmlrpc

Name:	 	php%_php_suffix-%php_extension
Version:	1.0.0
Release:	alt2.RC3.%php_version

Summary:	PHP module to write XML-RPC servers and clients

Group:		System/Servers
License:	PHP-3.01
URL:		https://pecl.php.net/package/xmlrpc
#URL:		http://php.net/manual/en/book.xmlrpc.php
# "504 Gateway Time-out" too long time.
# The package built from source code tarball available
# at https://pecl.php.net/get/xmlrpc
VCS: http://git.php.net/?p=pecl/networking/xmlrpc.git

Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.1-version
BuildRequires:  libxml2-devel
BuildRequires:	php-devel = %php_version
BuildRequires: rpm-build-php

%description
PHP PECL module XML-RPC can be used to write XML-RPC servers
and clients.

The extension is unbundled from php-src as of PHP 8.0.0,
because the underlying libxmlrpc has obviously been abandoned.
It is recommended to reevaluate using this extension.

These functions can be used to write XML-RPC servers and clients. You can find
more information about XML-RPC at http://www.xmlrpc.com/, and more documentation
on this extension and its functions at http://xmlrpc-epi.sourceforge.net/.

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
NO_INTERACTION=1 php run-tests.php --offline

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS EXPERIMENTAL

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Wed Oct 25 2023 Alexey Shemyakin <alexeys@altlinux.org> 1.0.0-alt1.RC3.%_php_release_version
- Update source code to  1.0.0RC3 version. Package built from source
  tarball available at https://pecl.php.net/get/xmlrpc.

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus

