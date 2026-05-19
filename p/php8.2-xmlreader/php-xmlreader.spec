%define		php_extension	xmlreader

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	PHP module for support XML
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

# Fix tests for libxml2 2.13+ compatibility
# See: https://github.com/php/php-src/issues/18009
%if "%_php_suffix" == "8.4"
Patch1:		php8.4-%php_extension-alt-libxml2-2.13-tests.patch
%else
Patch1:         php8.3-%php_extension-alt-libxml2-2.13-tests.patch
%endif


BuildRequires(pre): rpm-build-php8.2-version
BuildRequires:	php-devel = %php_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libxml2-devel zlib-devel

Requires: php%_php_suffix-dom = %php_version

%description
The extension allows you to operate on an XML document with the DOM API.

%prep
%setup -T -c
mkdir ext
cp -pr %php_extsrcdir/dom ext/
cp -pr %php_extsrcdir/%php_extension/* .
%patch1 -p1

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	PHP_LIBXML_SHARED=yes \
	--enable-%php_extension
echo "#define HAVE_DOM 1" >>config.h
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

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
