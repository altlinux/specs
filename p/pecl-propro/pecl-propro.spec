%define php5_extension propro

Name: pecl-%php5_extension
Version: 1.0.2
Release: alt1.%php5_version.%php5_release

Summary:  Property proxy

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/%php5_extension

Source: http://pecl.php.net/get/%name-%version.tar

BuildPreReq: rpm-build-pecl

# Automatically added by buildreq on Wed Oct 27 2010
BuildRequires: gcc-c++ glibc-devel-static php5-devel re2c zlib-devel libcurl-devel

%description
A reusable split-off of pecl_http's property proxy API.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: php5-devel

%description devel
Headers for developming with %name

%prep
%setup -n %name-%version

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

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 1.0.4-alt1.5.5.9.20140205-alt1
- Initial build for ALT Linux Sisyphus
