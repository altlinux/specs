%define php_extension	ldap

Name: php%_php_suffix-%php_extension
Version: %php_version
Release: %php_release

Summary: LDAP module for PHP
Group: System/Servers
License: PHP-3.01

Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version

BuildRequires: libldap-devel libsasl2-devel

%description
The %name includes a dynamic shared object (DSO) that adds
Lightweight Directory Access Protocol (LDAP) support to PHP. LDAP is a
set of protocols for accessing directory services over the Internet.
PHP is an HTML-embedded scripting language. If you need LDAP support
for PHP applications, you will need to install this package in addition
to the php package.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build

phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDLIBS=-lphp-%_php_version
%configure \
	--with-%php_extension=%_usr \
	--with-ldap-sasl=%prefix \
	--with-libdir=$(echo "%_libdir" | cut -d '/' -f3)
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
- Rebuild with php-devel = %php_version-%php_release
