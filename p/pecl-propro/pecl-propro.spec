%define php7_extension propro

Name: pecl-%php7_extension
Version: 2.1.0
Release: alt2

Summary:  Property proxy

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/%php7_extension

# Source-url: http://pecl.php.net/get/%php7_extension-%version.tgz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-pecl-php7

BuildRequires: php7-devel

%description
A reusable split-off of pecl_http's property proxy API.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: php7-devel
Requires: %name = %EVR

%description devel
Headers for developing with %name.

%prep
%setup

%build
cd %php7_extension-%version
phpize
%pecl7_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl7_install
%pecl7_install_doc CREDITS

# load firstly
subst "s|file_ini=|file_ini=01_|" %buildroot%php7_extconf/%php7_extension/params

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

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- load firstly

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- build 2.1.0 for php7

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 1.0.4-alt1.5.5.9.20140205-alt1
- Initial build for ALT Linux Sisyphus
