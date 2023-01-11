%define		php_extension	imagick
%define 	real_name	imagick

Name:	 	php%_php_suffix-%{php_extension}
Version:	3.7.0
Epoch:		1
Release:	alt1.%_php_release_version
Summary:	PHP wrapper to the ImageMagick library
License:	PHP-3.01
Group:		System/Servers
URL:		http://pecl.php.net/package/imagick
VCS: 		https://github.com/Imagick/imagick
Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: libImageMagick-devel

%description
Imagick is a native PHP extension to create and modify images
using the ImageMagick API.

%prep
%setup -n php-%php_extension-%version

%build
phpize
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
%doc CREDITS
%doc examples*

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 1:3.7.0-alt1
- 3.6.0 -> 3.7.0
- built from upstream git

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 1:3.6.0-alt1
- 3.5.1 -> 3.6.0

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 1:3.5.1-alt1
- updated to 3.5.1

* Tue Jul 06 2021 Anton Farygin <rider@altlinux.ru> 1:3.5.0
- updated to 3.5.0
- changed versioning theme to mainline (via Epoch)

* Sun Sep 03 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.7-alt1
- initial build 3.4.3 with php7

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 5.6.31.20170607-alt1.S1.2
- updated to 3.4.3
