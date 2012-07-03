%define pear_name Crypt_RC4

Name: pear-Crypt_RC4
Version: 1.0.2
Release: alt3

Summary: Encryption class for RC4 encryption

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Crypt_RC4

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_RC4-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
RC4 encryption class

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

