%define		php7_extension	xsl

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Sablotron XSLT support for PHP7
Group:		System/Servers
License:	PHP Licence

Prereq:		php7-dom

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

Patch: php-xsl-dom.patch

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libxml2-devel libxslt-devel zlib-devel

%description
The %name includes a dynamic shared object (DSO) that adds
XSLT support to PHP. Sablotron is a fast, compact and portable XSLT processor.
If you need XSLT support for PHP applications, you will need
to install this package in addition to the php package.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .
mkdir -p ./ext
cp -pr %php7_extsrcdir/dom ./ext/
%patch -p1

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	PHP_DOM=yes \
	PHP_LIBXML_SHARED=yes \
	--with-%php7_extension=%_usr
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
- Rebuild with php5-%version-%release

* Tue May 16 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.3-alt0
- initial build for ALT Sisyphus
