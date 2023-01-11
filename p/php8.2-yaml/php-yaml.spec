%define php_extension yaml

Name: php%_php_suffix-%php_extension
Version: 2.2.2
Release: alt%php_version.%php_release
Summary: PHP5 YAML-1.1 parser and emitter
License: %mit
Group: System/Servers
Url: http://pecl.php.net/package/yaml
Source0: php-%php_extension-%version.tar
BuildRequires(pre): rpm-build-php8.2-version rpm-build-licenses
BuildRequires: php-devel = %php_version
BuildRequires: libyaml-devel

%description
YAML PHP extension provides support for YAML 1.1 (YAML Ain't Markup Language)
serialization using the LibYAML library.

%prep
%setup -n php-%php_extension-%version

%build
phpize
BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

%configure \
        --with-%php_extension \
        --with-libdir=%_lib \
	--enable-yaml \
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

* Thu Dec 09 2021 Anton Farygin <rider@altlinux.ru> 2.2.2-alt%php_version.%php_release
- built 2.2.2 for PHP 8.0 and PHP 7.4

* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.18.20121017-alt1
- Initial build for ALT Linux Sisyphus
