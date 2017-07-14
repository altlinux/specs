%define php5_extension krb5
%define pecl_name krb5

Name: pecl-%pecl_name
Version: 1.1.2
Release: alt1.%php5_version.%php5_release

Summary: PHP module for authentication via GSSAPI

License: New BSD License
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Source: http://pecl.php.net/get/%pecl_name-%version.tar

# Automatically added by buildreq on Mon Feb 27 2017
# optimized out: gnu-config libcom_err-devel perl php5-libs python-base

BuildRequires:php5-devel libkrb5-devel

BuildRequires(Pre): rpm-build-pecl

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
%pecl_configure '--with-krb5kadm'
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

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release
