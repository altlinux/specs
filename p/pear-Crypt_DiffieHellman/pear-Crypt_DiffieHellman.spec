%define pear_name Crypt_DiffieHellman

Name: pear-Crypt_DiffieHellman
Version: 0.2.3
Release: alt1

Summary: Implementation of Diffie-Hellman Key Exchange cryptographic protocol for PHP5

License: New BSD License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.0b1

%description
Implementation of the Diffie-Hellman Key Exchange cryptographic protocol
in PHP5. Enables two parties without any prior knowledge of each other
establish a secure shared secret key across an insecure channel
of communication.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Crypt/DiffieHellman/
%pear_dir/Crypt/DiffieHellman.php
%pear_testdir/Crypt_DiffieHellman/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- initial build for ALT Linux Sisyphus

