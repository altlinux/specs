%define php_extension	snmp

Name: php%_php_suffix-snmp
Version: %php_version
Release: %php_release

Summary: SNMP module for PHP
Group: System/Servers
License: PHP-3.01


Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

Requires: net-snmp-mibs
BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version

# Automatically added by buildreq on Mon Jan 01 2007
BuildRequires: libnet-snmp-devel

%description
The php-snmp package includes a dynamic shared object (DSO) that adds 
NET-SNMP software support to PHP.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
  --with-snmp=%_usr \
  --with-openssl-dir=%_usr
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
