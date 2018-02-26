%define pear_name System_Mount

Name: pear-System_Mount
Version: 1.0.0
Release: alt3

Summary: Mount and unmount devices in fstab

License: PHP License v3.0
Group: Development/Other
Url: http://pear.php.net/package/System_Mount

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/System_Mount-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-File_Fstab >= 2.0.0beta1, pear-System_Command

%description
System_Mount provides a simple interface to deal with mounting and
unmounting devices listed in the system's fstab.

Features:
* Very compact, easy-to-read code, based on File_Fstab.
* Examines mount options to determine if a device can be mounted or not.
* Extremely easy to use.
* Fully documented with PHPDoc.

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
%pear_dir/System
%pear_dir/docs
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

