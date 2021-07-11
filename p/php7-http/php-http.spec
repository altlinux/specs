%define php_extension http

Name: php%_php_suffix-%php_extension
Version: 3.2.4
Release: alt1.%_php_release_version

Summary: Extended HTTP Support

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/http

Source: php-%php_extension-%version.tar

BuildRequires(pre): rpm-build-php7-version
Requires: php%_php_suffix-propro php%_php_suffix-raphf

BuildRequires: php%_php_suffix php-devel = %php_version
BuildRequires: re2c zlib-devel libcurl-devel libbrotli-devel libicu-devel libidn2-devel libevent-devel libssl-devel
BuildRequires: php%_php_suffix-raphf-devel php%_php_suffix-propro-devel

%if "%_php_suffix" == "7"
Obsoletes: pecl-%php_extension < %EVR
Provides: pecl-%php_extension
%endif

%description
his HTTP extension aims to provide a convenient and powerful
set of functionality for one of PHPs major applications.

It eases handling of HTTP urls, dates, redirects, headers and
messages, provides means for negotiation of clients preferred
language and charset, as well as a convenient way to send any
arbitrary data with caching and resuming capabilities.

It provides powerful request functionality, if built with CURL
support. Parallel requests are available for PHP 5 and greater.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: php%_php_suffix-devel php%_php_suffix-raphf-devel php%_php_suffix-propro-devel

%description devel
Headers for developming with %name

%prep
%setup -n php-%php_extension-%version

%build
phpize
export LDFLAGS=-lphp-%_php_version
%configure --with-php-config=%_bindir/php-config \
  --with-raphf \
  --with-http \
  --with-http-zlib-dir=%{_prefix} \
  --with-http-libcurl-dir=%{_prefix} \
  --without-http-libidn-dir \
  --without-http-libidn2-dir \
  --without-http-libidnkit-dir \
  --without-http-libidnkit2-dir \
  --with-http-libicu-dir=%{_prefix} \
  --with-http-libevent-dir=%{_prefix} \
  --with-http-libbrotli-dir=%{_prefix}

%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
# create config
mkdir -p %buildroot%php_extconf/%php_extension
echo "extension=%php_extension.so" > %buildroot%php_extconf/%php_extension/config
cat <<EOF > %buildroot%php_extconf/%php_extension/params
file_ini=%php_extension.ini
exceptions=
EOF

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir

%files devel
%_includedir/php/*/*/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.4-alt1.7.4.16.alt1
- build 3.2.4 with php7

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 2.0.4-alt1.5.5.9.20140205-alt1
- new version

* Sun Apr 14 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.7.5-alt1.5.3.24.20130412.alt1
- Initial build for ALT Linux Sisyphus
