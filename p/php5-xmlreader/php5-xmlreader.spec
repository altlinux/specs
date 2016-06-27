%define		php5_extension	xmlreader

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 module for support XML
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libxml2-devel zlib-devel

Requires: php5-dom = %php5_version-%php5_release

%description
The extension allows you to operate on an XML document with the DOM API.

%prep
%setup -T -c
mkdir ext
cp -pr %php5_extsrcdir/dom ext/
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	PHP_LIBXML_SHARED=yes \
	--enable-%php5_extension
echo "#define HAVE_DOM 1" >>config.h
%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release
