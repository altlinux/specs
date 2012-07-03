%define pear_name MDB2_Driver_mysqli

Name: pear-MDB2_Driver_mysqli
Version: 1.4.1
Release: alt3

Summary: mysqli MDB2 driver

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/MDB2_Driver_mysqli

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/MDB2_Driver_mysqli-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-MDB2 >= 2.4.1, pear-core >= 1.4.0b1

%description
This is the MySQLi MDB2 driver.

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
%pear_dir/MDB2
%pear_testdir/MDB2_Driver_mysqli/
%pear_datadir/MDB2_Driver_mysqli/package_mysqli.xml
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Linux Sisyphus

