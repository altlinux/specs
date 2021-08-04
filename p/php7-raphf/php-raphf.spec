%define php_extension raphf

Name: php%_php_suffix-%php_extension
Version: 2.0.1
Release: alt4.%_php_release_version

Summary:  Resource and persistent handles factory

License: BSD
Group: Development/Other
Url: http://pecl.php.net/package/%php_extension
# Source-url: http://pecl.php.net/get/%php_extension-%version.tgz
Source: php-%php_extension-%version.tar
BuildRequires(pre): rpm-build-php7-version
BuildRequires: php-devel = %php_version

%if "%_php_suffix" == "7"
Obsoletes: pecl-%php_extension < %EVR
Provides: pecl-%php_extension
%endif

%description
A reusable split-off of pecl_http's persistent handle and resource factory API.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: php-devel = %php_version
Requires: %name = %EVR

%description devel
Headers for developing with %name.

%prep
%setup -n php-%php_extension-%version
mv %php_extension-%version/* ./

%build
phpize
%configure \
        --enable-%php_extension
%php_make

%install
%makeinstall_std INSTALL_ROOT=%buildroot
# create config
mkdir -p %buildroot%php_extconf/%php_extension
echo "extension=%php_extension.so" > %buildroot%php_extconf/%php_extension/config
cat <<EOF > %buildroot%php_extconf/%php_extension/params
file_ini=01_%php_extension.ini
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

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- load firstly

* Thu Apr 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- build 2.0.1 for php7

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.org> 1.0.4-alt1.5.5.9.20140205-alt1
- Initial build for ALT Linux Sisyphus
