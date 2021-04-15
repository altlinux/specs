%define php7_extension http
%define pecl_name http

Name: pecl-%pecl_name
Version: 3.2.4
Release: alt1.%php7_version.%php7_release

Summary: Extended HTTP Support

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

# Source-url: https://github.com/m6w6/ext-http/archive/refs/tags/RELEASE_3_2_4.tar.gz
Source: http://pecl.php.net/get/%pecl_name-%version.tar

BuildRequires(pre): rpm-build-pecl-php7
Requires: pecl-propro pecl-raphf

BuildRequires: php7 php7-devel re2c zlib-devel libcurl-devel libbrotli-devel libicu-devel libidn2-devel libevent-devel libssl-devel
BuildRequires: pecl-raphf-devel pecl-propro-devel

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
Requires: php7-devel pecl-raphf-devel pecl-propro-devel

%description devel
Headers for developming with %name

%prep
%setup -n %pecl_name-%version

%build
phpize
# TODO: %pecl7_configure
export LDFLAGS=-lphp-%_php7_version
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
%pecl7_install
%pecl7_install_doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%files devel
%_includedir/php/*/*/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.4-alt1.7.4.16.alt1
- build 3.2.4 with php7

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 2.0.4-alt1.5.5.9.20140205-alt1
- new version

* Sun Apr 14 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.7.5-alt1.5.3.24.20130412.alt1
- Initial build for ALT Linux Sisyphus
