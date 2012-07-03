%define pear_name MDB2_Driver_pgsql

Name: pear-MDB2_Driver_pgsql
Version: 1.5.0b3
Release: alt2

Summary: pgsql MDB2 driver

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/MDB2_Driver_pgsql

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/MDB2_Driver_pgsql-%version.tar

BuildArchitectures: noarch

Requires: pear-core, php5-pgsql
BuildRequires: pear-core rpm-build-pear

Requires: pear-MDB2 >= 2.4.1, pear-core >= 1.4.0b1

%description
This is the PostgreSQL MDB2 driver.

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
%pear_testdir/MDB2_Driver_pgsql/
%pear_datadir/MDB2_Driver_pgsql/package_pgsql.xml
%pear_xmldir/%pear_name.xml

%changelog
* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.0b3-alt2
- add requires to php5-pgsql (ALT bug #17297)

* Mon Oct 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.0b3-alt1
- new version (1.5.0b3) import in git (ALT bug #23298)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Linux Sisyphus

