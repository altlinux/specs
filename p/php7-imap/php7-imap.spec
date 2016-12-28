%define php7_extension	imap

Name: php7-imap
Version: %php7_version
Release: %php7_release.1

Summary: IMAP module for PHP
Group: System/Servers
License: PHP Licence

Source1: php-%php7_extension.ini
Source2: php-%php7_extension-params.sh

Patch: php-imap.patch

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version

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
cp -pr %php7_extsrcdir/%php7_extension/* .
%patch -p1

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	PHP_OPENSSL=no \
	--with-kerberos=no \
	--with-imap-ssl=yes \
	--with-libdir=%_lib \
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
- Rebuild with php7-%php7_version-%php7_release

