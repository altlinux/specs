%define php7_extension krb5
%define pecl_name krb5

Name: pecl-%pecl_name
Version: 1.1.4
Release: alt1.%php7_version.%php7_release

Summary: PHP module for authentication via GSSAPI

License: New BSD License
Group: Development/Other
Url: http://pecl.php.net/package/krb5

Source: http://pecl.php.net/get/%pecl_name-%version.tar

# Automatically added by buildreq on Mon Feb 27 2017
# optimized out: gnu-config libcom_err-devel perl php5-libs python-base

BuildRequires: php7-devel libkrb5-devel

BuildRequires(Pre): rpm-build-pecl-php7

%description
An interface for maintaining credential caches (KRB5CCache),
that can be used for authenticating against a kerberos5 realm
Bindings for nearly the complete GSSAPI (RFC2744)
The administrative interface (KADM5)
Support for HTTP Negotiate authentication via GSSAPI

%prep
%setup -n %pecl_name-%version

%build
phpize
%pecl7_configure '--with-krb5kadm'
%make_build

%install
%pecl7_install
%pecl7_install_doc CREDITS
rm -rf %buildroot%php7_includedir/

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release
