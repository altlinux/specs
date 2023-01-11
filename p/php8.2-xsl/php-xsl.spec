%define		php_extension	xsl

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release.1

Summary:	Sablotron XSLT support for PHP
Group:		System/Servers
License:	PHP-3.01

Prereq:		php%_php_suffix-dom

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires:	php-devel = %php_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libxml2-devel libxslt-devel zlib-devel

%description
The %name includes a dynamic shared object (DSO) that adds
XSLT support to PHP. Sablotron is a fast, compact and portable XSLT processor.
If you need XSLT support for PHP applications, you will need
to install this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .
mkdir -p ./ext
cp -pr %php_extsrcdir/dom ./ext/
# use external header for dom from php-devel
sed -i 's,../dom/,dom/,' php_xsl.h

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	PHP_DOM=yes \
	PHP_LIBXML_SHARED=yes \
	--with-%php_extension=%_usr
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

* Tue May 16 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.3-alt0
- initial build for ALT Sisyphus
