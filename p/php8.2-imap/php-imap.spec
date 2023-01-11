%define php_extension	imap
%{?optflags_lto:%global optflags_lto %nil}

Name: php%_php_suffix-%php_extension
Version: %php_version
Release: %php_release

Summary: IMAP module for PHP
Group: System/Servers
License: PHP-3.01

Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

Patch: php-imap.patch

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libpam-devel libssl-devel pkgconfig uw-imap-devel

%description
The %name package contains a dynamic shared object (DSO) for PHP. The
%name module adds IMAP (Internet Message Access Protocol) support to
PHP. IMAP is a protocol for retrieving and uploading e-mail messages on
mail servers. PHP is an HTML-embedded scripting language for use with
Apache.  If you need IMAP support for PHP applications, you will need to
install this package and PHP.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .
%patch -p1

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	PHP_OPENSSL=no \
	--with-kerberos=no \
	--with-imap-ssl=yes \
	--with-libdir=%_lib \
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
- Rebuild with php-devel = %php_version-%php_release

