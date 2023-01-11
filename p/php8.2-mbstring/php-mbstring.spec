%define		php_extension	mbstring

Name:	 	php8.2-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	PHP module for support multi-byte strings.
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires:  liboniguruma-devel

%description
This package allows you to handle multiple Japanese encodings (SJIS, EUC,
UTF-8, JIS) in PHP.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%php_version
%configure \
        --enable-mbregex \
	--enable-%php_extension
%php_make

%install
%php_make_install phpincludedir=%includedir
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

%files
%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-%version-%release

