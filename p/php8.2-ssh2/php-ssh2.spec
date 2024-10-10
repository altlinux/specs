%define php_extension	ssh2
Name: php%_php_suffix-%php_extension
Version: 1.4.1
Epoch: 1
Release: alt1.%_php_release_version
Summary: PHP bindings for the libssh2 library
License: PHP-3.01
Group: System/Servers
Url: https://pecl.php.net/package/ssh2
VCS: https://github.com/php/pecl-networking-ssh2
Source0: php-%php_extension-%version.tar
Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh
Patch0: php-ssh2-alt-%version.patch
BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: libssh2-devel
BuildRequires: php-devel = %php_version php%_php_suffix

%description
php-ssh extension provides bindings to the functions of libssh2
which implements the SSH2 protocol.

%prep
%setup -n php-%php_extension-%version
%patch0 -p1

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
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

* Thu Oct 10 2024 Anton Farygin <rider@altlinux.ru> 1:1.4.1-alt1
- 1.3.1 -> 1.4.1
- added patch from php bugtracker 79702 (closes: #51645)

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 1:1.3.1
- 1.3.1

* Tue Jun 16 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1.1
- Fix module configuration

* Mon Jun 15 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.18-alt1
- Initial build for ALT Linux Sisyphus

