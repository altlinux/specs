%define pear_name HTTP_Request2
Name: pear-%pear_name
Version: 0.5.2
Release: alt1

Summary: Provides an easy way to perform HTTP requests

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core
Requires: pear-Net_URL2 >= 0.2.0
Requires: pear-Net_Socket >= 1.0.9
Requires: php5-curl php5-fileinfo php5-openssl

BuildRequires: pear-core rpm-build-pear
BuildRequires: pear-Net_URL2 >= 0.2.0
BuildRequires: pear-Net_Socket >= 1.0.9
BuildRequires: php5-curl php5-fileinfo php5-openssl

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication, SSL, file uploads etc.

%prep
%setup -c -n %pear_name-%version

%build
%pear_build

%install
%pear_install_std


%post
%register_pear_module

%preun
%unregister_pear_module


%files
%pear_dir/HTTP/
%pear_xmldir/%pear_name.xml
%pear_docdir/%pear_name/
%pear_testdir/%pear_name/

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

