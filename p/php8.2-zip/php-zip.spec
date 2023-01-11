%define		php_extension	zip

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release
Summary:	ZIP functions
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.2-version

BuildRequires: libzip-devel zlib-devel
BuildRequires: php-devel = %php_version

%description
This module enables you to transparently read ZIP compressed archives and the files inside them.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .
# drop internal zip
rm -rf lib

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
export PHP_RPATH=no
export LDFLAGS="-lphp-%_php_version" ### Stupid PHP not understand LDLIBS
%add_optflags -fPIC -L%_libdir
%configure --with-%php_extension --with-libzip=%_prefix
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
echo n | make test

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

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.3-alt1
- initial build for ALT Sisyphus
