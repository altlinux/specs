%define pear_name DB_DataObject

Name: pear-DB_DataObject
Version: 1.8.10
Release: alt1

Summary: An SQL Builder, Object Interface to Database Tables

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/DB_DataObject

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB_DataObject-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-DB >= 1.7.0, pear-Date >= 1.4.3, pear-core >= 1.4.0b1

%description
DataObject performs 2 tasks:
  1. Builds SQL statements based on the objects vars and the builder
methods.
  2. acts as a datastore for a table row.
  The core class is designed to be extended for each of your tables so
that you put the
  data logic inside the data classes.
  included is a Generator to make your configuration files and your base
classes.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std
rm -rf %buildroot%_bindir/DB

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/DB/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jul 10 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.10-alt1
- new version 1.8.10 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- new version 1.8.8 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- initial build for ALT Linux Sisyphus

