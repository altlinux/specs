%define php_extension	xdebug

Name: php%_php_suffix-%php_extension
Version: 3.2.0
Epoch: 1
Release: alt1.%_php_release_version
Summary: xdebug extensions
Group: System/Servers
License: Xdebug-1.02
URL: https://xdebug.org/download#releases
VCS: https://github.com/xdebug/xdebug
Source: php-%php_extension-%version.tar
Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.0-version
BuildRequires: php-devel = %php_version
BuildRequires: php%_php_suffix = %php_version

%description
Xdebug is an extension for PHP to assist with debugging and development.
It contains a single step debugger to use with IDEs;
it upgrades PHP's var_dump() function;
it adds stack traces for Notices, Warnings, Errors and Exceptions;
it features functionality for recording every function call and
variable assignment to disk; it contains a profiler;
and it provides code coverage functionality for use with PHPUnit.

%prep
%setup -n php-%php_extension-%version
%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension=%_usr
%php_make

%install
install -D -m 644 modules/xdebug.so %buildroot%php_extdir/xdebug.so
install -D -m 644 %SOURCE1 %buildroot%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot%php_extconf/%php_extension/params

%files
%php_extconf/%php_extension
%php_extdir/xdebug.so

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel %php_version-%php_release

* Tue Jan 10 2023 Anton Farygin <rider@altlinux.ru> 1:3.2.0-alt1
- 3.1.5 -> 3.2.0

* Thu Jun 16 2022 Anton Farygin <rider@altlinux.ru> 1:3.1.5-alt1
- 3.1.4 -> 3.1.5

* Fri Apr 15 2022 Anton Farygin <rider@altlinux.ru> 1:3.1.4-alt1
- 3.1.3 -> 3.1.4

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 1:3.1.3-alt1
- 3.1.2 -> 3.1.3
- built from upstream git

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 1:3.1.2-alt1
- 3.0.4 -> 3.1.2

* Tue Jul 06 2021 Anton Farygin <rider@altlinux.ru> 1:3.0.4
- update to 3.0.4
- mainline version number for package versioning

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.10-alt1
- updated to 2.8.0

* Fri Dec 21 2018 Anton Farygin <rider@altlinux.ru> 7.2.13-alt1.1
- updated to 2.6.1
- removed fullpath to module in config

* Tue Jan 30 2018 Vitaly Lipatov <lav@altlinux.ru> 7.1.12-alt0
- initial build xdebug 2.6.0 for ALT Sisyphus

