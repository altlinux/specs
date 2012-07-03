%define pear_name Crypt_RSA

Name: pear-Crypt_RSA
Version: 1.0.0
Release: alt3

Summary: Provides RSA-like key generation, encryption/decryption, signing and signature checking

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Crypt_RSA

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_RSA-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package allows you to use two-key strong cryptography like RSA with
arbitrary key length.
It uses one of the following extensions for math calculations:
 - PECL big_int extension ( http://pecl.php.net/packages/big_int ) version
greater than or equal to 1.0.3
 - PHP GMP extension ( http://php.net/gmp )
 - PHP BCMath extension ( http://php.net/manual/en/ref.bc.php ) for both
PHP4 and PHP5

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
%pear_testdir/Crypt_RSA/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

