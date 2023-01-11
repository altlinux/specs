%define	php_extension	sodium
Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	Sodium library support for PHP
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: libsodium-devel
BuildRequires:	php-devel = %php_version

%description
The %name includes a dynamic shared object (DSO) that adds
sodium support to PHP.

Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more.

It is a portable, cross-compilable, installable, packageable fork of NaCl, with
a compatible API, and an extended API to improve usability even further.

Its goal is to provide all of the core operations needed to build higher-level
cryptographic tools.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-libdir=%_lib \
	--with-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 make test

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS
%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release
