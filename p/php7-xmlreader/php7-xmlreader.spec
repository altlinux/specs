%define		php7_extension	xmlreader

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	PHP module for support XML
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libxml2-devel zlib-devel

Requires: php7-dom = %php7_version-%php7_release

%description
The extension allows you to operate on an XML document with the DOM API.

%prep
%setup -T -c
mkdir ext
cp -pr %php7_extsrcdir/dom ext/
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	PHP_LIBXML_SHARED=yes \
	--enable-%php7_extension
echo "#define HAVE_DOM 1" >>config.h
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
