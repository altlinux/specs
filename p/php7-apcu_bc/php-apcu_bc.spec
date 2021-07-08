%define		php_extension	apcu_bc
%define 	real_name	apcu_bc
%define		real_version	1.0.5

Name:	 	php%_php_suffix-%{php_extension}
Version:	%php_version
Release:	%php_release

Summary:	PHP7 extension apcu_bc - APCu Backwards Compatibility Module

License:	PHP-3.01
Group:		System/Servers
URL:		https://pecl.php.net/package/apcu_bc
#URL:		https://github.com/krakjoe/apcu-bc

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Source3:	apcu-headers.tar

BuildRequires(pre): rpm-build-php7-version
BuildRequires: php-devel = %php_version

Requires: php%_php_suffix-apcu

%description
PHP extension apcu_bc provides a backwards APC compatible
API using APCu.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-apc \
	--enable-apc-mmap \
	#

# We need APCu headers - put them into current directory
sed -e 's#ext/apcu/#apcu/#' -i php_apc.c
tar xvf %SOURCE3

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc README.md LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- updated to 1.0.5

* Mon Jan 22 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.1.12-alt1.S1
- Initial build for ALT Linux Sisyphus
