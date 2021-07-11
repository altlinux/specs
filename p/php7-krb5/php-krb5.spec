%define php_extension krb5

Name: php%_php_suffix-%php_extension
Version: 1.1.4
Release: alt1.%_php_release_version

Summary: PHP module for authentication via GSSAPI

License: MIT
Group: Development/Other
Url: http://pecl.php.net/package/krb5

Source: php-%php_extension-%version.tar

BuildRequires(pre): rpm-build-php7-version
BuildRequires: php-devel = %php_version
BuildRequires: libkrb5-devel

%if "%_php_suffix" == "7"
Obsoletes: pecl-krb5
Provides: pecl-krb5
%endif

%description
An interface for maintaining credential caches (KRB5CCache),
that can be used for authenticating against a kerberos5 realm
Bindings for nearly the complete GSSAPI (RFC2744)
The administrative interface (KADM5)
Support for HTTP Negotiate authentication via GSSAPI

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
