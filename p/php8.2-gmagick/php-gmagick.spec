%define		php_extension	gmagick

Name:	 	php%_php_suffix-%php_extension
Version:	2.0.6
Epoch:		1
Release:	alt3.%_php_release_version.rc1

Summary:	php extension to work with images using the GraphicsMagick API

License:	PHP-3.01
Group:		System/Servers
URL:		http://pecl.php.net/package/gmagick/

# Source0-url: https://pecl.php.net/get/gmagick-%real_version.tgz
Source0:	%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version

BuildRequires: php-devel = %php_version
BuildRequires: libGraphicsMagick-devel >= 1.3.20

%description
Gmagick is a PHP extension to create, modify, and obtain meta 
information of images using the GraphicsMagick API. 

Gmagick consists of a main Gmagick class, a GmagickDraw class
that is in effect a drawing wand, and a GmagickPixel class of
which instances represent a single pixel of an image (color,
opacity).

%prep
%setup -n %php_extension-%version

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	#

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc README.md

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 7.4.12-alt1
- build 2.0.5RC1 for php7

* Sat Sep 05 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Initial build for ALT Linux Sisyphus
