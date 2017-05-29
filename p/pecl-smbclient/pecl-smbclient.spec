%define php5_extension smbclient
%define pecl_name smbclient

Name: pecl-%pecl_name
Version: 0.9.0
Release: alt1.%php5_version.%php5_release

Summary: A PHP wrapper for libsmbclient

License: New BSD License
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Source: http://pecl.php.net/get/%pecl_name-%version.tar

BuildRequires:php5-devel libsmbclient-devel

BuildRequires(Pre): rpm-build-pecl

%description
smbclient is a PHP extension that uses Samba's libsmbclient library to provide
Samba related functions and 'smb' streams to PHP programs.

%prep
%setup -n %pecl_name-%version

%build
cd %pecl_name-%version
phpize
%pecl_configure '--with-smbclient'
%make_build

%install
%pecl_install
mkdir -p %buildroot%_docdir/%name-%version/

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release
