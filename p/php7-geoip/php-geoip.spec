# vim: set ft=spec: -*- rpm-spec -*-
%define php_extension geoip

Name: php%_php_suffix-%php_extension
Version: 1.1.1
Release: alt%php_version.%php_release

Summary: Map IP address to geographic places
License: PHP-3.01
Group: Development/Other

Url: http://pecl.php.net/package/%php_extension

# Source-url: http://pecl.php.net/get/%php_extension-%version.tgz
Source: php-%php_extension-%version.tar

BuildRequires(pre): rpm-build-php7-version
BuildRequires: php-devel = %php_version
BuildRequires: libGeoIP-devel

%description
This PHP extension allows you to find the location of an IP address -
City, State, Country, Longitude, Latitude, and other information as all,
such as ISP and connection type.
For more info, please visit Maxmind`s website.

%prep
%setup -n php-%php_extension-%version
mv %php_extension-%version/* ./

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
%php_extdir/

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Mon Mar 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt0
- new version (1.1.1) with rpmgs script

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt3
- Rebuild with php7-5.3.18.20121017-alt1
- cleanup spec - removed garbage from solo@

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- Rebuild with php7-devel-5.3.17.20120913-alt1

* Tue Apr 24 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.8-alt1
- Initial build for ALT Linux Sisyphus
