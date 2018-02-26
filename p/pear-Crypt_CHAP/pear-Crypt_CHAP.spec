%define pear_name Crypt_CHAP

Name: pear-Crypt_CHAP
Version: 1.0.1
Release: alt3

Summary: Generating CHAP packets

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/Crypt_CHAP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_CHAP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package provides Classes for generating CHAP packets.
Currently these types of CHAP are supported:
* CHAP-MD5
* MS-CHAPv1
* MS-CHAPv2
For MS-CHAP the mhash and mcrypt extensions must be loaded.

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
%pear_testdir/Crypt_CHAP/
%pear_dir/Crypt
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

