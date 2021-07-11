%define php_extension smbclient

Name: php%_php_suffix-%php_extension
Version: 1.0.6
Release: alt1.%_php_release_version
Summary: A PHP wrapper for libsmbclient

License: MIT
Group: Development/Other
Url: http://pecl.php.net/package/smbclient

Source: php-%php_extension-%version.tar

BuildRequires: php-devel = %php_version
BuildRequires: libsmbclient-devel

BuildRequires(Pre): rpm-build-php7-version

%if "%_php_suffix" == "7"
Obsoletes: pecl-%php_extension < %EVR
Provides: pecl-%php_extension
%endif


%description
smbclient is a PHP extension that uses Samba's libsmbclient library to provide
Samba related functions and 'smb' streams to PHP programs.

%prep
%setup -n php-%php_extension-%version

%build
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

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Fri Jul 09 2021 Anton Farygin <rider@altlinux.ru> 1.0.6
- update to 1.0.6

