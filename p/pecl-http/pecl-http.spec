%define php5_extension http
%define pecl_name http

Name: pecl-%pecl_name
Version: 2.0.4
Release: alt1.%php5_version.%php5_release

Summary: Extended HTTP Support

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Source: http://pecl.php.net/get/%pecl_name-%version.tar

BuildPreReq: rpm-build-pecl
Requires: pecl-propro pecl-raphf

# Automatically added by buildreq on Wed Oct 27 2010
BuildRequires: gcc-c++ glibc-devel-static php5-devel re2c zlib-devel libcurl-devel pecl-raphf-devel pecl-propro-devel

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
Requires: php5-devel pecl-raphf-devel pecl-propro-devel

%description devel
Headers for developming with %name

%prep
%setup -n %pecl_name-%version

%build
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl_install
%pecl_install_doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%files devel
%_includedir/php/*/*/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 2.0.4-alt1.5.5.9.20140205-alt1
- new version

* Sun Apr 14 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.7.5-alt1.5.3.24.20130412.alt1
- Initial build for ALT Linux Sisyphus