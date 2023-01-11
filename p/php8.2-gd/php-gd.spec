%define	php_extension	gd
Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	GD library support for PHP
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: glibc-devel-static libfreetype-devel libjpeg-devel libpng-devel t1lib-devel libwebp-devel
BuildRequires:	php-devel = %php_version
Provides: php%_php_suffix-gd2 = %EVR
Obsoletes: php%_php_suffix-gd2 < %EVR

%description
The %name includes a dynamic shared object (DSO) that adds
GD support to PHP. GD is a library that enables you to create PNG,
JPEG, XPM, and WBMP graphics. It is linked with freetype and t1lib so
you can use TrueType fonts. PHP is an HTML-embedded scripting language.
If you need GD support for PHP applications, you will need to install
this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-jpeg \
	--with-t1lib \
	--with-webp \
	--with-png \
	--with-zlib \
	--with-freetype \
	--with-libdir=%_lib \
	--with-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS
%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Fri Oct 23 2020 Anton Farygin <rider@altlinux.org>
- fix for building with external libs for internal libgd (closes: #39116)

* Mon Dec 16 2019 Anton Farygin <rider@altlinux.org>
- renamed from php7-gd2 to php7-gd
- built with libwebp (closes: #37626)
- cleanup buildrequires
