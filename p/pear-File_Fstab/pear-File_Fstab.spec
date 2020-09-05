%define pear_name File_Fstab

Name: pear-File_Fstab
Version: 2.0.3
Release: alt1

Summary: Read and write fstab files

License: PHP License v3.0
Group: Development/Other
Url: http://pear.php.net/package/File_Fstab

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_Fstab-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
File_Fstab is an easy-to-use package which can read & write UNIX fstab
files. It presents a pleasant object-oriented interface to the fstab.
Features:
* Supports blockdev, label, and UUID specification of mount device.
* Extendable to parse non-standard fstab formats by defining a new Entry
class for that format.
* Easily examine and set mount options for an entry.
* Stable, functional interface.
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
%pear_dir/File/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- initial build for ALT Linux Sisyphus

