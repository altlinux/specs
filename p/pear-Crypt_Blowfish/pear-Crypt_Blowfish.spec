%define pear_name Crypt_Blowfish

Name: pear-Crypt_Blowfish
Version: 1.0.1
Release: alt3

Summary: Allows for quick two-way blowfish encryption without requiring the Mcrypt PHP extension

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Crypt_Blowfish

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_Blowfish-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package allows you to prefore two-way blowfish on the fly using only
PHP. This package does not require the Mcrypt PHP extension to work.

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
%pear_dir/Crypt
%pear_testdir/Crypt_Blowfish/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

