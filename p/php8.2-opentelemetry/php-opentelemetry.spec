%define		php_extension	opentelemetry
%define 	real_name	opentelemetry
%define		real_version	1.2.1

Name:	 	php%_php_suffix-%php_extension
Version:	%real_version
Release:	alt1.%_php_release_version

Summary:	OpenTelemetry auto-instrumentation support extension

License:	%asl
Group:		System/Servers
URL:		https://pecl.php.net/package/opentelemetry
VCS:		https://github.com/open-telemetry/opentelemetry-php-instrumentation

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh


BuildRequires(pre): rpm-build-php8.2-version
BuildRequires(pre): rpm-build-licenses
BuildRequires: php-devel = %php_version

BuildRequires: glibc-devel-static

%description
This is a PHP extension for OpenTelemetry, to enable auto-instrumentation.

It is based on zend_observer and allows:
- creating pre and post hook functions to arbitrary PHP functions and methods,
  which allows those methods to be wrapped with telemetry
- adding attributes to functions and methods to enable observers at runtime

In PHP 8.2+, internal/built-in PHP functions can also be observed.

%prep
%setup -c
%patch0 -p1

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/Apache-2.0 %_docdir/%name/LICENSE) LICENSE

%build
cd ext
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
cd ext
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%doc CODEOWNERS README.md
%doc --no-dereference LICENSE

%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%version-%release

* Sat Jan 10 2026 Nikolay A. Fetisov <naf@altlinux.org> 1.2.1-alt1
- Initial build for ALT Linux Sisyphus

