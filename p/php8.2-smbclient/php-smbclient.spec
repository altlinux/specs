%define php_extension smbclient

Name: php%_php_suffix-%php_extension
Version: 1.1.1
Release: alt1.%_php_release_version
Summary: A PHP wrapper for libsmbclient

License: MIT
Group: Development/Other
Url: http://pecl.php.net/package/smbclient

Source: php-%php_extension-%version.tar

BuildRequires: php-devel = %php_version
BuildRequires: libsmbclient-devel

BuildRequires(Pre): rpm-build-php8.2-version


%description
smbclient is a PHP extension that uses Samba's libsmbclient library to provide
Samba related functions and 'smb' streams to PHP programs.

%prep
%setup -n php-%php_extension-%version

%build
BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
phpize
%configure \
        --enable-%php_extension
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

%files
%php_extconf/%php_extension
%php_extdir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Wed Jan 10 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- update to 1.1.1

* Fri Jul 09 2021 Anton Farygin <rider@altlinux.ru> 1.0.6
- update to 1.0.6

