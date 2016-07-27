%define pear_name Crypt_CBC

Name: pear-Crypt_CBC
Version: 1.0.1
Release: alt1

Summary: A class to emulate Perl's Crypt::CBC module

License: PHP 2.02
Group: Development/Other
Url: http://pear.php.net/package/Crypt_CBC

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Crypt_CBC-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
A class to emulate Perl's Crypt::CBC module.

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
%pear_dir/Crypt/
%pear_docdir/Crypt_CBC/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus

