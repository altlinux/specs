%define php_extension	bz2

Name: php%_php_suffix-%php_extension
Version: %php_version
Release: %php_release

Summary: A Bzip2 management extension
Group: System/Servers
License: PHP-3.01

Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: bzlib-devel

%description
%name is an extension to create and parse bzip2 compressed data.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-php-config=%_bindir/php-config \
	--with-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
# for tests/with_strings.php need a file from the PHP build tree
rm -f tests/with_strings.phpt
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
