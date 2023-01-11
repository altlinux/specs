%define		php_extension	intl

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	Internationalization extension is a wrapper for ICU library
Group:		System/Servers
License:	PHP-3.01
URL: http://php.net/manual/en/book.intl.php

#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: gcc-c++ libicu-devel

BuildRequires:	php-devel = %php_version


%description
Internationalization extension (further is referred as Intl) is a wrapper
for ICU library, enabling PHP programmers to perform UCA-conformant
collation and date/time/number/currency formatting in their scripts.

It tends to closely follow ICU APIs, so that people having experience
working with ICU in either C/C++ or Java could easily use the PHP
API. Also, this way ICU documentation would be useful to understand
various ICU functions.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
%ifarch %e2k
# lcc-1.23.12: char16_t is undefined otherwise; see also mcst#4060
%add_optflags -std=gnu++11
%endif
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-php-config=%_bindir/php-config \
	--with-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

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

* Sun May 12 2019 Michael Shigorin <mike@altlinux.org> 7.1.8-alt1.1
- Fixed build with lcc 1.23 on e2k

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus
