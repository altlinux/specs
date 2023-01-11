%define		php_extension	ssh2
Name:	 	php%_php_suffix-%php_extension
Version:	1.3.1
Epoch:		1
Release:	alt3.%_php_release_version

Summary:	PHP bindings for the libssh2 library

License:	PHP-3.01
Group:		System/Servers
URL:		https://pecl.php.net/package/ssh2
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	php-%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.2-version

BuildRequires: libssh2-devel

BuildRequires: php-devel = %php_version

%description
php-ssh extension provides bindings to the functions of libssh2
which implements the SSH2 protocol.

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
	--enable-zmq \
	%nil

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc README.md
%doc --no-dereference LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 1:1.3.1
- 1.3.1

* Tue Jun 16 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1.1
- Fix module configuration

* Mon Jun 15 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1
- Initial build for ALT Linux Sisyphus

