%define		php7_extension	imagick
%define 	real_name	imagick
%define		real_version	3.4.3

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 wrapper to the ImageMagick library

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/imagick

# Source0-url: http://pecl.php.net/get/imagick-%real_version.tgz
Source0:	%name-%real_version.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version
BuildRequires: libImageMagick-devel

%description
Imagick is a native PHP extension to create and modify images
using the ImageMagick API.

%prep
%setup -n %name-%real_version
mv -- %real_name-%real_version/* .
rm -fr -- %real_name-%real_version

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
%doc CREDITS
%doc examples*

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Sun Sep 03 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.7-alt1
- initial build 3.4.3 with php7

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 5.6.31.20170607-alt1.S1.2
- updated to 3.4.3
