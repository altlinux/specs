%define pear_name Net_Curl

Name: pear-Net_Curl
Version: 1.2.5
Release: alt1

Summary: Net_Curl provides an OO interface to PHP's cURL extension

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Net_Curl

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Curl-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: php5-curl

%description
Provides an OO interface to PHP's curl extension

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Net/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- new version 1.2.5 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- initial build for ALT Linux Sisyphus

