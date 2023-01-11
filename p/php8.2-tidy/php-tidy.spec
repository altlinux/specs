%define		php_extension	tidy

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	PHP binding for the Tidy HTML clean and repair utility

Group:		System/Servers
License:	PHP-3.01
Url:		https://secure.php.net/manual/en/book.tidy.php

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: libtidy-devel

BuildRequires: gcc-c++
BuildRequires: php-devel = %php_version

%description
Tidy is a binding for the Tidy HTML clean and repair utility
which allows you to not only clean and otherwise manipulate
HTML, XHTML, and XML documents, but also traverse the  document
tree, including ones with embedded scripting languages such as
PHP or ASP within them using object oriented constructs.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension=%_usr
%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

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
- Rebuild with php-devel = %php_version-%php_release

* Thu Jul 5  2018 Nikolay A. Fetisov <naf@altlinux.org> 7.2.6-alt1.S1
- Initial build for ALT Linux Sisyphus
