%define		php7_extension	gmagick
%define 	real_name	gmagick
%define		real_version	2.0.5RC1

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	php7 extension to work with images using the GraphicsMagick API

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/gmagick/

# FIXME: gear: Extracted archive: php7-gmagick-%php7_version.tar

# Source0-url: https://pecl.php.net/get/gmagick-%real_version.tgz
Source0:	%name-version.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7

BuildRequires: php7-devel = %php7_version-%php7_release
BuildRequires: libGraphicsMagick-devel >= 1.3.20

%description
Gmagick is a PHP extension to create, modify, and obtain meta 
information of images using the GraphicsMagick API. 

Gmagick consists of a main Gmagick class, a GmagickDraw class
that is in effect a drawing wand, and a GmagickPixel class of
which instances represent a single pixel of an image (color,
opacity).

%prep
%setup -n %name-version
mv -- %real_name-%real_version/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	#

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc README.md

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 7.4.12-alt1
- build 2.0.5RC1 for php7

* Sat Sep 05 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Initial build for ALT Linux Sisyphus
