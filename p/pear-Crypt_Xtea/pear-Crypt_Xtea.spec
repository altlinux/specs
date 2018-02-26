%define pear_name Crypt_Xtea

Name: pear-Crypt_Xtea
Version: 1.0
Release: alt3

Summary: A class that implements the Tiny Encryption Algorithm (TEA) (New Variant)

License: PHP 2.02
Group: Development/Other
Url: http://pear.php.net/package/Crypt_Xtea

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_Xtea-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
A class that implements the Tiny Encryption Algorithm (TEA) (New Variant).
    This class does not depend on mcrypt.
	Encryption is relatively fast, decryption relatively slow.
    Original code from http://vader.brad.ac.uk/tea/source.shtml#new_ansi

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

