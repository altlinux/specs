%define	php7_extension	gd
%define	gd_ver	2

Name:	 	php7-%php7_extension%gd_ver
Version:	%php7_version
Release:	%php7_release

Summary:	GD library support for PHP
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension%gd_ver.ini
Source2:	php-%php7_extension%gd_ver-params.sh

BuildRequires(pre): rpm-build-php7
# Automatically added by buildreq on Thu Jan 28 2010
BuildRequires: glibc-devel-static libfreetype-devel libjpeg-devel libpng-devel php7-devel t1lib-devel

BuildRequires:	php7-devel = %php7_version

%description
The %name includes a dynamic shared object (DSO) that adds
GD support to PHP. GD is a library that enables you to create PNG,
JPEG, XPM, and WBMP graphics. It is linked with freetype and t1lib so
you can use TrueType fonts. PHP is an HTML-embedded scripting language.
If you need GD support for PHP applications, you will need to install
this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--enable-gd-native-ttf \
	--without-xpm \
	--with-jpeg-dir=%_prefix \
	--with-t1lib \
	--with-ttf=%_prefix \
	--with-png-dir=%_prefix \
	--with-zlib-dir=%_prefix \
	--with-freetype-dir=%_prefix \
	--with-libdir=%_lib \
	--enable-exif \
	--with-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release
