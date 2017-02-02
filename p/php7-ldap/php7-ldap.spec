%define php7_extension	ldap

Name: php7-%php7_extension
Version: %php7_version
Release: %php7_release

Summary: LDAP module for PHP
Group: System/Servers
License: PHP Licence

Source1: php-%php7_extension.ini
Source2: php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version

BuildRequires: libldap-devel libsasl2-devel

Requires: php7-libs = %php7_version-%php7_release

%description
The %name includes a dynamic shared object (DSO) that adds
Lightweight Directory Access Protocol (LDAP) support to PHP. LDAP is a
set of protocols for accessing directory services over the Internet.
PHP is an HTML-embedded scripting language. If you need LDAP support
for PHP applications, you will need to install this package in addition
to the php package.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build

phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDLIBS=-lphp-%_php7_version
%configure \
	--with-%php7_extension=%_usr \
	--with-ldap-sasl=%prefix \
	--with-libdir=$(echo "%_libdir" | cut -d '/' -f3)
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
- Rebuild with php7-%php7_version-%php7_release